"""Offline discovery and consent-gated private copy of user-provided UI sources.

Never executes, installs, archives, downloads, or publishes the selected source.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = Path('integrations/design-frameworks/code-xr-private.json')
EXCLUDED_DIRS = {'.git', 'node_modules', 'bower_components', 'vendor', 'dist', 'build',
                 '.next', '.nuxt', '.cache', '.venv', 'venv', '__pycache__', '.github',
                 '.claude', '.codex', '.cursor'}
ALLOWED_SUFFIXES = {'.js', '.jsx', '.ts', '.tsx', '.css', '.scss', '.sass', '.html',
                    '.json', '.md', '.txt', '.png', '.jpg', '.jpeg', '.gif', '.webp',
                    '.svg', '.ico', '.avif', '.woff', '.woff2', '.ttf', '.otf',
                    '.glb', '.fbx', '.hdr', '.usdc', '.mp4', '.webm'}
BLOCKED_NAMES = {'agents.md', 'claude.md', 'gemini.md', 'credentials.json',
                 'service-account.json', 'secrets.json', '.npmrc', '.yarnrc'}
SHA256 = re.compile(r'^[a-f0-9]{64}$')


class FrameworkError(ValueError):
    pass


def manifest() -> dict[str, Any]:
    roots = [SOURCE_ROOT, Path(sys.prefix), Path(sys.base_prefix)]
    if os.environ.get('INTERNET_WELL_ROOT'):
        roots.insert(0, Path(os.environ['INTERNET_WELL_ROOT']).expanduser().resolve())
    for root in roots:
        path = root / MANIFEST_REL
        if path.is_file():
            data = json.loads(path.read_text(encoding='utf-8'))
            if data.get('id') != 'code-xr-private' or not isinstance(data.get('frameworks'), list):
                raise FrameworkError('Invalid private framework catalogue.')
            return data
    raise FrameworkError('Private framework catalogue not found.')


def discover(query: str = '') -> list[dict[str, Any]]:
    return [x for x in manifest()['frameworks']
            if query.lower() in (x['id'] + ' ' + x['name'] + ' ' + x['category']).lower()]


def _entry(framework_id: str) -> dict[str, Any]:
    for item in discover():
        if item['id'] == framework_id:
            _relative(framework_id)
            return item
    raise FrameworkError('Unknown framework ID.')


def _relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or '\\' in value or ':' in value or path.is_absolute() or any(x in {'', '.', '..'} for x in value.split('/')):
        raise FrameworkError('Only contained relative paths are allowed.')
    return Path(*path.parts)


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _private(path: Path) -> Path:
    # Also reject symlinked path components, including an existing private root.
    absolute = path.expanduser().absolute()
    if any(p.is_symlink() for p in [absolute, *absolute.parents]):
        raise FrameworkError('Private roots must not use symbolic links.')
    result = absolute.resolve()
    if _inside(result, SOURCE_ROOT) or any((p / '.git').exists() for p in [result, *result.parents]):
        raise FrameworkError('Private files must remain outside repository working trees.')
    return result


def _home(value: Path | None = None) -> Path:
    return _private(value or Path.home() / '.internet-well' / 'private-frameworks')


def bind(source_root: Path, private_root: Path | None = None, approve: bool = False) -> dict[str, str]:
    if not approve:
        raise FrameworkError('Binding writes local state and requires --approve.')
    source = _private(source_root)
    home = _home(private_root)
    if not source.is_dir():
        raise FrameworkError('Source root is not a directory.')
    if _inside(source, home) or _inside(home, source):
        raise FrameworkError('Source root and private output root must not overlap.')
    home.mkdir(parents=True, exist_ok=True, mode=0o700)
    state = home / 'binding.json'
    if state.is_symlink():
        raise FrameworkError('Binding must not be a symbolic link.')
    payload = {'source_root': str(source), 'policy': 'private-source; no redistribution established'}
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, 'O_NOFOLLOW', 0)
    fd = os.open(state, flags, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        json.dump(payload, handle, indent=2)
        handle.write('\n')
    return {'status': 'bound', 'execution': 'not-performed'}


def _source(home: Path) -> Path:
    binding = home / 'binding.json'
    if binding.is_symlink():
        raise FrameworkError('Binding must not be a symbolic link.')
    try:
        source = _private(Path(json.loads(binding.read_text(encoding='utf-8'))['source_root']))
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        raise FrameworkError('Bind an existing private source root first.') from exc
    if not source.is_dir() or _inside(source, home) or _inside(home, source):
        raise FrameworkError('Invalid or overlapping private source root.')
    return source


def _reason(path: Path) -> str | None:
    if any(part.lower() in EXCLUDED_DIRS for part in path.parts):
        return 'dependency/generated/agent directory'
    if any(part.startswith('.') for part in path.parts):
        return 'hidden file or directory'
    name = path.name.lower()
    if name in BLOCKED_NAMES or name.startswith('.') or name.startswith('.env'):
        return 'secret/configuration/agent instruction file'
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        return 'unsupported or executable/archive file type'
    return None


def _read_regular(path: Path, root: Path) -> bytes:
    if path.is_symlink() or not _inside(path.resolve(), root):
        raise FrameworkError('Symbolic link or source path escape rejected.')
    flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0)
    fd = os.open(path, flags)
    with os.fdopen(fd, 'rb') as handle:
        if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
            raise FrameworkError('Only regular source files can be copied.')
        return handle.read()


def plan(framework_id: str, private_root: Path | None = None) -> dict[str, Any]:
    item = _entry(framework_id)
    home = _home(private_root)
    root = _source(home) / _relative(framework_id)
    if root.is_symlink() or not root.is_dir():
        raise FrameworkError('Framework source directory missing or symbolic.')
    files = []
    skipped = []
    seen_paths: set[str] = set()
    for package in item['package_roots']:
        package_path = root / _relative(package)
        if not package_path.exists():
            raise FrameworkError('Expected package root missing.')
        def fail_walk(error: OSError) -> None:
            raise FrameworkError('Unable to read all selected source directories.') from error

        for parent, dirs, names in os.walk(package_path, followlinks=False, onerror=fail_walk):
            parent_path = Path(parent)
            if parent_path.is_symlink() or not _inside(parent_path.resolve(), root.resolve()):
                raise FrameworkError('Source directory escape rejected.')
            for name in list(dirs):
                child = parent_path / name
                rel = child.relative_to(root)
                if child.is_symlink():
                    raise FrameworkError('Symbolic source directories are prohibited.')
                if _reason(rel / 'placeholder.txt'):
                    dirs.remove(name)
                    skipped.append({'path': rel.as_posix(), 'reason': 'excluded directory'})
            for name in sorted(names):
                path = parent_path / name
                rel = path.relative_to(root)
                if path.is_symlink():
                    raise FrameworkError('Symbolic source files are prohibited.')
                # Nested or repeated catalogue roots may reach this path again.
                # A source-relative path is copied at most once in a reviewed plan.
                if rel.as_posix() in seen_paths:
                    continue
                seen_paths.add(rel.as_posix())
                reason = _reason(rel)
                if reason:
                    skipped.append({'path': rel.as_posix(), 'reason': reason})
                    continue
                data = _read_regular(path, root.resolve())
                files.append({'path': rel.as_posix(), 'bytes': len(data),
                              'sha256': hashlib.sha256(data).hexdigest()})
    if not files:
        raise FrameworkError('No eligible source files found.')
    result = {'framework_id': framework_id, 'files': sorted(files, key=lambda x: x['path']),
              'skipped': sorted(skipped, key=lambda x: x['path']),
              'archive_sha256_reference': item['archive_sha256'],
              'archive_verified': False, 'production_approved': False,
              'redistribution': 'not-established', 'execution': 'not-performed'}
    result['plan_sha256'] = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()
    return result


def copy_source(framework_id: str, private_root: Path | None = None,
                approve: bool = False, plan_sha256: str = '') -> dict[str, Any]:
    if not approve:
        raise FrameworkError('Source copying requires --approve after reviewing a plan.')
    if not SHA256.fullmatch(plan_sha256):
        raise FrameworkError('Provide the reviewed --plan-sha256.')
    result = plan(framework_id, private_root)
    if result['plan_sha256'] != plan_sha256:
        raise FrameworkError('Source or plan changed. Review a fresh plan before copying.')
    home = _home(private_root)
    source = _source(home) / _relative(framework_id)
    destination = home / 'imports' / framework_id
    if destination.exists() or destination.is_symlink():
        raise FrameworkError('Destination already exists; overwriting is prohibited.')
    imports = home / 'imports'
    if imports.is_symlink():
        raise FrameworkError('Private import directory must not be symbolic.')
    # Verify all reads before creating output. Source content remains untrusted data.
    contents = []
    for row in result['files']:
        data = _read_regular(source / _relative(row['path']), source.resolve())
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise FrameworkError('Source changed during copy; no output written.')
        contents.append((row['path'], data))
    imports.mkdir(exist_ok=True, mode=0o700)
    destination.mkdir(mode=0o700)
    for relative, data in contents:
        target = destination / _relative(relative)
        target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with target.open('xb') as handle:
            handle.write(data)
        target.chmod(0o600)
    return {'framework_id': framework_id, 'status': 'copied-to-private-storage',
            'file_count': len(contents), 'plan_sha256': plan_sha256,
            'execution': 'not-performed', 'production_approved': False}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--private-root', type=Path, default=None,
                        help='Private local state/output directory outside all Git working trees')
    subs = parser.add_subparsers(dest='command', required=True)
    search = subs.add_parser('list')
    search.add_argument('query', nargs='?', default='')
    binding = subs.add_parser('bind')
    binding.add_argument('source_root', type=Path)
    binding.add_argument('--approve', action='store_true')
    planned = subs.add_parser('plan')
    planned.add_argument('framework_id')
    copied = subs.add_parser('copy')
    copied.add_argument('framework_id')
    copied.add_argument('--approve', action='store_true')
    copied.add_argument('--plan-sha256', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'list':
            result = discover(args.query)
        elif args.command == 'bind':
            result = bind(args.source_root, args.private_root, args.approve)
        elif args.command == 'plan':
            result = plan(args.framework_id, args.private_root)
        else:
            result = copy_source(args.framework_id, args.private_root, args.approve, args.plan_sha256)
        print(json.dumps(result, indent=2))
        return 0
    except (FrameworkError, OSError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())

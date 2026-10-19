import hashlib
import inspect
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from automation import private_design_frameworks as frameworks


class PrivateFrameworkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'
        self.home = self.base / 'private'
        self.item = frameworks.discover('01-dashboard-v12')[0]
        self.package = self.source / self.item['id'] / self.item['package_roots'][0]
        (self.package / 'src').mkdir(parents=True)
        (self.package / 'src' / 'App.jsx').write_text('export default function App() {return null;}')
        (self.package / 'package.json').write_text('{"scripts":{"postinstall":"do-not-run"}}')
        frameworks.bind(self.source, self.home, approve=True)

    def test_catalogue_is_complete_metadata_only_and_conditional(self):
        rows = frameworks.discover()
        self.assertEqual(len(rows), 76)
        self.assertEqual(len({x['id'] for x in rows}), 76)
        self.assertEqual(len(frameworks.discover('dashboard')), 11)
        for row in rows:
            self.assertEqual(row['availability'], 'user-provided-private-source')
            self.assertEqual(row['redistribution'], 'not-established')
            self.assertRegex(row['archive_sha256'], r'^[a-f0-9]{64}$')
            self.assertEqual(set(row), {'id', 'name', 'category', 'archive_sha256', 'package_roots',
                                        'availability', 'review_status', 'redistribution'})
            for root in row['package_roots']:
                self.assertFalse(Path(root).is_absolute())

    def test_plan_is_read_only_and_copy_requires_explicit_consent(self):
        result = frameworks.plan(self.item['id'], self.home)
        self.assertFalse((self.home / 'imports').exists())
        self.assertFalse(result['production_approved'])
        self.assertFalse(result['archive_verified'])
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.copy_source(self.item['id'], self.home, plan_sha256=result['plan_sha256'])
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.bind(self.source, self.home)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.copy_source(self.item['id'], self.home, approve=True)
        frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])
        copied = self.home / 'imports' / self.item['id'] / self.item['package_roots'][0] / 'src' / 'App.jsx'
        self.assertEqual(copied.read_bytes(), (self.package / 'src' / 'App.jsx').read_bytes())
        self.assertEqual(copied.stat().st_mode & 0o777, 0o600)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])

    def test_common_secrets_dependencies_instructions_and_archives_excluded(self):
        for name in ('node_modules/nested/package.json', 'dist/bundle.js', '.git/config', '.env',
                     'credentials.json', 'secrets.json', 'AGENTS.md', '.cursor/rules.json',
                     'payload.exe', 'nested.zip', 'install.sh', '.private/personal.json'):
            path = self.package / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('DO NOT COPY')
        result = frameworks.plan(self.item['id'], self.home)
        copied = [x['path'] for x in result['files']]
        self.assertEqual(len(copied), 2)
        frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])
        private_files = list((self.home / 'imports').rglob('*'))
        self.assertFalse(any(p.is_file() and 'DO NOT COPY' in p.read_text() for p in private_files))

    def test_overlapping_and_duplicate_package_roots_copy_each_file_once(self):
        nested = self.item['package_roots'][0] + '/src'
        entry = dict(self.item, package_roots=[nested, self.item['package_roots'][0], nested])
        with mock.patch.object(frameworks, '_entry', return_value=entry):
            result = frameworks.plan(self.item['id'], self.home)
            paths = [row['path'] for row in result['files']]
            self.assertEqual(len(paths), 2)
            self.assertEqual(len(paths), len(set(paths)))
            copied = frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])
        self.assertEqual(copied['file_count'], 2)
        destination = self.home / 'imports' / self.item['id']
        self.assertEqual(len([p for p in destination.rglob('*') if p.is_file()]), 2)

    def test_model_and_video_assets_are_copied_byte_for_byte_without_execution(self):
        media = {}
        for suffix in ('.glb', '.fbx', '.hdr', '.usdc', '.mp4', '.webm'):
            path = self.package / 'public' / ('asset' + suffix)
            path.parent.mkdir(exist_ok=True)
            media[path.relative_to(self.source / self.item['id'])] = b'private-media-fixture\x00' + suffix.encode()
            path.write_bytes(media[path.relative_to(self.source / self.item['id'])])
        with mock.patch('socket.socket', side_effect=AssertionError('network forbidden')), \
             mock.patch('subprocess.Popen', side_effect=AssertionError('execution forbidden')):
            result = frameworks.plan(self.item['id'], self.home)
            self.assertEqual(len(result['files']), 8)
            frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])
        for relative, expected in media.items():
            self.assertEqual((self.home / 'imports' / self.item['id'] / relative).read_bytes(), expected)

    def test_no_network_or_process_execution(self):
        # The adversarial script in package.json must remain inert data throughout.
        with mock.patch('socket.socket', side_effect=AssertionError('network forbidden')), \
             mock.patch('subprocess.Popen', side_effect=AssertionError('execution forbidden')):
            result = frameworks.plan(self.item['id'], self.home)
            frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])
        source = inspect.getsource(frameworks)
        self.assertNotIn('import subprocess', source)
        self.assertNotIn('import socket', source)
        self.assertNotIn('import requests', source)

    def test_changed_source_or_file_list_invalidates_review(self):
        result = frameworks.plan(self.item['id'], self.home)
        (self.package / 'src' / 'App.jsx').write_text('changed')
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])
        self.assertFalse((self.home / 'imports').exists())
        result = frameworks.plan(self.item['id'], self.home)
        (self.package / 'src' / 'extra.js').write_text('extra')
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])

    def test_traversal_and_repository_confinement(self):
        for bad in ('../escape', '/absolute', 'x/../../escape', 'x\\escape', 'C:/outside', 'C:foo', 'nested/C:foo'):
            with self.assertRaises(frameworks.FrameworkError):
                frameworks._relative(bad)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.bind(self.source, frameworks.SOURCE_ROOT / '.internet-well', True)
        repo = self.base / 'repo'
        (repo / '.git').mkdir(parents=True)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.bind(self.source, repo / 'private', True)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.bind(self.source, self.source / 'private', True)

    def test_symlinks_never_copied_or_used_for_private_state(self):
        (self.package / 'src' / 'escape.js').symlink_to(self.package / 'package.json')
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.plan(self.item['id'], self.home)
        (self.package / 'src' / 'escape.js').unlink()
        alias = self.base / 'alias'
        alias.symlink_to(self.home, target_is_directory=True)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.plan(self.item['id'], alias)
        (self.home / 'imports').symlink_to(self.base / 'escape', target_is_directory=True)
        result = frameworks.plan(self.item['id'], self.home)
        with self.assertRaises(frameworks.FrameworkError):
            frameworks.copy_source(self.item['id'], self.home, True, result['plan_sha256'])

    def test_package_and_ignore_policy(self):
        root = frameworks.SOURCE_ROOT
        for name in ('.internet-well', 'private-frameworks', 'private-framework-reports', 'purchased-design-sources'):
            self.assertIn(name + '/', (root / '.gitignore').read_text())
            self.assertIn('prune ' + name, (root / 'MANIFEST.in').read_text())
        config = (root / 'pyproject.toml').read_text()
        self.assertIn('"integrations/design-frameworks" = ["integrations/design-frameworks/code-xr-private.json"]', config)


if __name__ == '__main__':
    unittest.main()

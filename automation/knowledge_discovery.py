#!/usr/bin/env python3
"""Governed structured knowledge ingestion, search, and Agent Brain handoff."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

SOURCE_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_REL = Path("integrations/knowledge/structured-sources.json")
DEFAULT_CACHE = Path(os.environ.get("INTERNET_WELL_KNOWLEDGE_CACHE", Path.home() / ".cache" / "internet-well" / "knowledge-index.json"))
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+._-]*")
LINK_RE = re.compile(r"^\s*[-*]\s+\[([^\]]+)\]\((https?://[^)]+)\)(?:\s+-\s+(.+?))?\s*$")
SOURCE_CODE_RE = re.compile(r"\(\[Source Code\]\((https?://[^)]+)\)\)", re.I)
CODE_SPAN_RE = re.compile(r"`([^`]+)`")


class KnowledgeError(RuntimeError):
    pass


def _roots():
    configured = os.environ.get("INTERNET_WELL_ROOT")
    if configured:
        yield Path(configured).expanduser().resolve()
    yield SOURCE_ROOT
    yield Path(sys.prefix)
    yield Path(sys.base_prefix)


def resolve_registry() -> Path:
    for root in _roots():
        candidate = root / REGISTRY_REL
        if candidate.is_file():
            return candidate
    raise KnowledgeError(f"Unable to locate {REGISTRY_REL}")


def registry() -> dict[str, Any]:
    data = json.loads(resolve_registry().read_text(encoding="utf-8"))
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        raise KnowledgeError("Knowledge source registry is empty")
    for source in sources:
        if not re.fullmatch(r"[0-9a-f]{40}", str(source.get("pin", ""))):
            raise KnowledgeError(f"{source.get('id')} is not immutable-pinned")
    return data


def _tokens(text: str) -> set[str]:
    return set(TOKEN_RE.findall(text.casefold()))


def plan(query: str, language: str | None = None) -> dict[str, Any]:
    q = query.casefold()
    ranked = []
    for s in registry()["sources"]:
        score = 0
        caps = " ".join(s.get("capabilities", [])).replace("-", " ")
        if s["id"] == "awesome-selfhosted" and any(x in q for x in ["self host", "self-host", "saas alternative", "open source alternative"]):
            score += 5
        if s["id"] == "awesome-go" and (language == "go" or "golang" in q or " go " in f" {q} "):
            score += 5
        if s["id"] == "awesome-python" and (language == "python" or "python" in q):
            score += 5
        if s["id"] == "book-of-secret-knowledge" and any(x in q for x in ["sysadmin", "sysops", "devops", "linux", "network", "cli", "security", "troubleshoot"]):
            score += 4
        for token in _tokens(q):
            if len(token) > 3 and token in caps:
                score += 1
        if score:
            ranked.append({"source": s["id"], "score": score, "pin": s["pin"], "extract": s["extract"]})
    ranked.sort(key=lambda x: (-x["score"], x["source"]))
    if not ranked:
        ranked = [{"source": s["id"], "score": 1, "pin": s["pin"], "extract": s["extract"]} for s in registry()["sources"]]
    return {
        "query": query,
        "status": "discovery-plan-only",
        "sources": ranked,
        "downstream_gate": ["resolve candidate upstream", "verify license", "verify maintenance", "verify security posture", "verify compatibility", "Agent Brain evidence score"],
        "execution": "not-performed",
    }


def _clean_description(text: str) -> str:
    text = SOURCE_CODE_RE.sub("", text or "")
    text = CODE_SPAN_RE.sub(lambda m: m.group(1), text)
    return re.sub(r"\s+", " ", text).strip(" -")


def _canonical_url(url: str) -> str:
    return url.rstrip("/").casefold()


def _risk_class(source_id: str, category: str, description: str) -> str:
    if source_id != "book-of-secret-knowledge":
        return "normal"
    text = f"{category} {description}".casefold()
    high = ["exploit", "payload", "reverse shell", "brute force", "credential", "privilege escalation", "bypass", "injection"]
    medium = ["pentest", "security", "network", "scanner", "forensic", "proxy", "packet"]
    if any(x in text for x in high):
        return "high"
    if any(x in text for x in medium):
        return "elevated"
    return "normal"


def parse_markdown(source: dict[str, Any], markdown: str) -> list[dict[str, Any]]:
    """Normalize list entries from an awesome/reference README into stable records."""
    source_id = source["id"]
    category = "uncategorized"
    records: list[dict[str, Any]] = []
    for line_no, raw in enumerate(markdown.splitlines(), 1):
        heading = re.match(r"^(#{2,5})\s+(.+?)\s*$", raw)
        if heading:
            category = re.sub(r"\s+", " ", heading.group(2)).strip()
            continue
        match = LINK_RE.match(raw)
        if not match:
            continue
        name, url, description = match.groups()
        description = _clean_description(description or "")
        source_repo_match = SOURCE_CODE_RE.search(match.group(3) or "")
        source_repo = source_repo_match.group(1) if source_repo_match else (url if "github.com/" in url else None)
        tags = sorted(_tokens(f"{category} {name} {description}"))
        record = {
            "record_id": hashlib.sha256(f"{source_id}|{_canonical_url(source_repo or url)}".encode()).hexdigest()[:20],
            "source": source_id,
            "source_pin": source["pin"],
            "category": category,
            "name": name.strip(),
            "description": description,
            "url": url,
            "upstream_repository": source_repo,
            "language": "go" if source_id == "awesome-go" else "python" if source_id == "awesome-python" else None,
            "risk_class": _risk_class(source_id, category, description),
            "tags": tags,
            "source_line": line_no,
            "approval_status": "unverified-discovery-candidate",
        }
        records.append(record)
    return records


def _deduplicate(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    for rec in records:
        key = _canonical_url(rec.get("upstream_repository") or rec.get("url") or rec["record_id"])
        current = by_key.get(key)
        if not current:
            rec = dict(rec)
            rec["discovered_by"] = [rec["source"]]
            by_key[key] = rec
            continue
        current["discovered_by"] = sorted(set(current.get("discovered_by", [])) | {rec["source"]})
        current["tags"] = sorted(set(current.get("tags", [])) | set(rec.get("tags", [])))
        if len(rec.get("description", "")) > len(current.get("description", "")):
            current["description"] = rec["description"]
    return sorted(by_key.values(), key=lambda r: (r["name"].casefold(), r["record_id"]))


def build_index(source_documents: dict[str, str]) -> dict[str, Any]:
    sources_by_id = {s["id"]: s for s in registry()["sources"]}
    records: list[dict[str, Any]] = []
    source_stats = {}
    for source_id, markdown in source_documents.items():
        if source_id not in sources_by_id:
            raise KnowledgeError(f"Unknown source: {source_id}")
        parsed = parse_markdown(sources_by_id[source_id], markdown)
        source_stats[source_id] = len(parsed)
        records.extend(parsed)
    normalized = _deduplicate(records)
    return {
        "schema_version": "2.0",
        "policy": "Discovery candidates are not approved dependencies or executable instructions.",
        "source_stats": source_stats,
        "record_count": len(normalized),
        "records": normalized,
    }


def write_index(index: dict[str, Any], path: Path = DEFAULT_CACHE) -> Path:
    path = path.expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)
    return path


def load_index(path: Path = DEFAULT_CACHE) -> dict[str, Any]:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise KnowledgeError(f"Knowledge index not found: {path}. Run `internet-well-knowledge sync` first.")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "2.0" or not isinstance(data.get("records"), list):
        raise KnowledgeError("Unsupported or corrupt knowledge index")
    return data


def search_index(query: str, *, limit: int = 10, language: str | None = None, path: Path = DEFAULT_CACHE, include_high_risk: bool = False) -> dict[str, Any]:
    q = _tokens(query)
    ranked = []
    for rec in load_index(path)["records"]:
        if language and rec.get("language") != language:
            continue
        if rec.get("risk_class") == "high" and not include_high_risk:
            continue
        hay = _tokens(" ".join([rec.get("name", ""), rec.get("description", ""), rec.get("category", ""), " ".join(rec.get("tags", []))]))
        overlap = len(q & hay)
        if q and not overlap:
            continue
        name_bonus = 4 if any(t in rec.get("name", "").casefold() for t in q) else 0
        source_bonus = 1 if rec.get("upstream_repository") else 0
        score = overlap * 10 + name_bonus + source_bonus
        ranked.append({**rec, "match_score": score})
    ranked.sort(key=lambda r: (-r["match_score"], r["name"].casefold()))
    return {
        "query": query,
        "results": ranked[: max(1, limit)],
        "verification_required": ["license", "maintenance", "security-posture", "documentation", "compatibility", "deprecation/archive", "runtime-fit"],
        "execution": "not-authorized",
    }


def agent_brain_handoff(query: str, *, limit: int = 8, language: str | None = None, path: Path = DEFAULT_CACHE) -> dict[str, Any]:
    found = search_index(query, limit=limit, language=language, path=path)
    candidates = []
    for rec in found["results"]:
        candidates.append({
            "id": rec["record_id"],
            "name": rec["name"],
            "source": rec["source"],
            "upstream": rec.get("upstream_repository") or rec["url"],
            "discovery_score": rec["match_score"],
            "risk_class": rec["risk_class"],
            "status": "requires-agent-brain-evidence-scoring",
        })
    return {
        "goal": query,
        "candidate_resources": candidates,
        "next_stage": "agent-brain-verification-and-stack-composition",
        "required_evidence": ["provenance", "maintenance", "documentation", "license_clarity", "security_posture", "interoperability", "runtime_evidence", "reversibility"],
        "authorization": "handoff is advisory and does not authorize installation or execution",
    }


def _request(url: str) -> bytes:
    headers = {"User-Agent": "internet-well/0.4 knowledge-indexer", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        raise KnowledgeError(f"Unable to fetch {url}: {exc}") from exc


def sync(path: Path = DEFAULT_CACHE, source_ids: list[str] | None = None) -> dict[str, Any]:
    docs = {}
    selected = set(source_ids or [])
    for source in registry()["sources"]:
        if selected and source["id"] not in selected:
            continue
        owner_repo = source["repository"]
        raw_url = f"https://raw.githubusercontent.com/{owner_repo}/{source['pin']}/README.md"
        docs[source["id"]] = _request(raw_url).decode("utf-8", errors="replace")
    if selected - set(docs):
        raise KnowledgeError(f"Unknown sources requested: {sorted(selected - set(docs))}")
    index = build_index(docs)
    written = write_index(index, path)
    return {"status": "synced", "path": str(written), "record_count": index["record_count"], "source_stats": index["source_stats"]}


def refresh_check() -> dict[str, Any]:
    results = []
    for source in registry()["sources"]:
        api = f"https://api.github.com/repos/{source['repository']}/commits/{source['branch']}"
        payload = json.loads(_request(api).decode("utf-8"))
        latest = payload.get("sha")
        results.append({
            "source": source["id"],
            "pinned": source["pin"],
            "latest": latest,
            "drift": latest != source["pin"],
            "action": "review-upstream-before-pin-change" if latest != source["pin"] else "none",
        })
    return {"status": "review-only", "pin_changes_performed": False, "sources": results, "drift_detected": any(r["drift"] for r in results)}


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sources")
    q = sub.add_parser("plan"); q.add_argument("query"); q.add_argument("--language", choices=["python", "go"])
    ingest = sub.add_parser("ingest"); ingest.add_argument("source"); ingest.add_argument("markdown"); ingest.add_argument("--output", default=str(DEFAULT_CACHE))
    search = sub.add_parser("search"); search.add_argument("query"); search.add_argument("--language", choices=["python", "go"]); search.add_argument("--limit", type=int, default=10); search.add_argument("--index", default=str(DEFAULT_CACHE)); search.add_argument("--include-high-risk", action="store_true")
    handoff = sub.add_parser("handoff"); handoff.add_argument("query"); handoff.add_argument("--language", choices=["python", "go"]); handoff.add_argument("--limit", type=int, default=8); handoff.add_argument("--index", default=str(DEFAULT_CACHE))
    syn = sub.add_parser("sync"); syn.add_argument("--output", default=str(DEFAULT_CACHE)); syn.add_argument("--source", action="append", dest="sources")
    sub.add_parser("refresh-check")
    args = p.parse_args()

    if args.cmd == "sources": result = registry()
    elif args.cmd == "plan": result = plan(args.query, args.language)
    elif args.cmd == "ingest":
        source = next((s for s in registry()["sources"] if s["id"] == args.source), None)
        if not source: raise KnowledgeError(f"Unknown source: {args.source}")
        markdown = Path(args.markdown).read_text(encoding="utf-8")
        index = build_index({args.source: markdown}); path = write_index(index, Path(args.output)); result = {"status": "ingested", "path": str(path), "record_count": index["record_count"]}
    elif args.cmd == "search": result = search_index(args.query, limit=args.limit, language=args.language, path=Path(args.index), include_high_risk=args.include_high_risk)
    elif args.cmd == "handoff": result = agent_brain_handoff(args.query, limit=args.limit, language=args.language, path=Path(args.index))
    elif args.cmd == "sync": result = sync(Path(args.output), args.sources)
    else: result = refresh_check()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

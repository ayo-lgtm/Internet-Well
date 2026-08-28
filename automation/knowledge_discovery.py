#!/usr/bin/env python3
"""Governed discovery across curated technical knowledge sources."""
from __future__ import annotations
import argparse, json, os, re, sys
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]


def resolve_registry() -> Path:
    roots=[]
    configured=os.environ.get("INTERNET_WELL_ROOT")
    if configured: roots.append(Path(configured).expanduser().resolve())
    roots.extend([SOURCE_ROOT, Path(sys.prefix), Path(sys.base_prefix)])
    for root in roots:
        candidate=root / "integrations" / "knowledge" / "structured-sources.json"
        if candidate.is_file(): return candidate
    raise FileNotFoundError("Unable to locate integrations/knowledge/structured-sources.json")


def registry():
    data = json.loads(resolve_registry().read_text(encoding="utf-8"))
    for source in data["sources"]:
        if not re.fullmatch(r"[0-9a-f]{40}", source["pin"]):
            raise ValueError(f"{source['id']} is not immutable-pinned")
    return data


def plan(query: str, language: str | None = None):
    q = query.casefold(); sources = registry()["sources"]; ranked=[]
    for s in sources:
        score=0; caps=" ".join(s.get("capabilities", [])).replace("-", " ")
        if s["id"] == "awesome-selfhosted" and any(x in q for x in ["self host", "self-host", "saas alternative", "open source alternative"]): score += 5
        if s["id"] == "awesome-go" and (language == "go" or "golang" in q or " go " in f" {q} "): score += 5
        if s["id"] == "awesome-python" and (language == "python" or "python" in q): score += 5
        if s["id"] == "book-of-secret-knowledge" and any(x in q for x in ["sysadmin", "sysops", "devops", "linux", "network", "cli", "security", "troubleshoot"]): score += 4
        for token in set(re.findall(r"[a-z0-9]+", q)):
            if len(token) > 3 and token in caps: score += 1
        if score: ranked.append({"source":s["id"],"score":score,"pin":s["pin"],"extract":s["extract"]})
    ranked.sort(key=lambda x:(-x["score"],x["source"]))
    if not ranked: ranked=[{"source":s["id"],"score":1,"pin":s["pin"],"extract":s["extract"]} for s in sources]
    return {"query":query,"status":"discovery-plan-only","sources":ranked,"downstream_gate":["resolve candidate upstream","verify license","verify maintenance","verify security posture","verify compatibility","Agent Brain evidence score"],"execution":"not-performed"}


def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True); sub.add_parser("sources")
    q=sub.add_parser("plan"); q.add_argument("query"); q.add_argument("--language",choices=["python","go"])
    args=p.parse_args(); print(json.dumps(registry() if args.cmd=="sources" else plan(args.query,args.language),indent=2))

if __name__ == "__main__": main()

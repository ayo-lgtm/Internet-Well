#!/usr/bin/env python3
"""Generate evidence-backed upstream verification reports without silently changing pins."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from automation.agent_brain import BrainError, graph


def git_ls_remote(source: str, ref: str = "HEAD") -> dict[str, Any]:
    proc = subprocess.run(["git", "ls-remote", source, ref], text=True, capture_output=True, timeout=30, check=False)
    sha = None
    if proc.returncode == 0 and proc.stdout.strip():
        sha = proc.stdout.split()[0]
    return {"source": source, "ref": ref, "returncode": proc.returncode, "sha": sha, "stderr": proc.stderr[-2000:]}


def verify(network: bool = False) -> dict[str, Any]:
    items = []
    for node in graph()["nodes"]:
        source = node.get("source")
        pin = node.get("pin")
        row: dict[str, Any] = {
            "id": node.get("id"),
            "kind": node.get("kind"),
            "source": source,
            "current_pin": pin,
            "restrictions": node.get("restrictions", []),
            "status": "manual-review-required",
            "checks": [
                "upstream-exists",
                "pin-still-resolves",
                "license-unchanged",
                "security-advisories-reviewed",
                "release-notes-reviewed",
                "breaking-changes-reviewed",
                "better-alternatives-considered",
            ],
        }
        if network and isinstance(source, str) and source.startswith("https://github.com/"):
            head = git_ls_remote(source, "HEAD")
            row["network"] = head
            if head["returncode"] == 0:
                row["status"] = "reachable-review-needed"
                if pin and head.get("sha") and pin != head["sha"]:
                    row["upgrade_candidate"] = {"from": pin, "observed_head": head["sha"], "automatic_update": False}
            else:
                row["status"] = "unreachable-or-error"
        items.append(row)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "network_checked": network,
        "policy": "Internet-Well never silently updates immutable pins. Any observed upstream change becomes an upgrade candidate that requires provenance, license, security, compatibility, fixture, and rollback review.",
        "resources": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser(prog="internet-well-upstreams")
    parser.add_argument("--network", action="store_true", help="Use git ls-remote to check public GitHub sources.")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = verify(args.network)
        text = json.dumps(payload, indent=2, sort_keys=True)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text + "\n", encoding="utf-8")
        else:
            print(text)
        return 0
    except (BrainError, OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

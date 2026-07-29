#!/usr/bin/env python3
"""Internet-Well experimental project detector and resource selector.

No third-party dependencies. Python 3.9+.

Examples:
  python3 automation/founder_os_engine.py assess ../target-repo
  python3 automation/founder_os_engine.py select ../target-repo --goal "launch AI SaaS"
  python3 automation/founder_os_engine.py select ../target-repo --capability browser-testing --capability secret-detection

The engine treats registry records as validated knowledge and catalog entries as
research candidates. Candidate-only selections are always labeled unverified.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog" / "curated-repositories.json"
REGISTRY = ROOT / "registry"


@dataclass
class Signal:
    name: str
    evidence: str
    confidence: str = "high"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def file_names(project: Path) -> set[str]:
    names: set[str] = set()
    for path in project.rglob("*"):
        if any(part in {".git", "node_modules", ".next", "dist", "build", "vendor", ".venv"} for part in path.parts):
            continue
        if path.is_file():
            try:
                names.add(path.relative_to(project).as_posix())
            except ValueError:
                pass
    return names


def detect_project(project: Path) -> dict:
    if not project.exists() or not project.is_dir():
        raise ValueError(f"project directory not found: {project}")

    names = file_names(project)
    joined_names = "\n".join(sorted(names)).lower()
    package = read_text(project / "package.json").lower()
    pyproject = read_text(project / "pyproject.toml").lower()
    requirements = read_text(project / "requirements.txt").lower()
    docker = read_text(project / "docker-compose.yml").lower() + read_text(project / "compose.yml").lower()
    readme = read_text(project / "README.md").lower()
    corpus = "\n".join([package, pyproject, requirements, docker, readme, joined_names])

    stacks: list[Signal] = []
    hosting: list[Signal] = []
    product_types: list[Signal] = []
    risks: set[str] = set()
    capabilities: set[str] = {"unit-testing", "secret-detection", "dependency-scanning"}

    def add_stack(name: str, condition: bool, evidence: str) -> None:
        if condition:
            stacks.append(Signal(name, evidence))

    add_stack("nextjs", '"next"' in package or "next.config" in joined_names, "package.json or Next.js config")
    add_stack("react", '"react"' in package, "package.json dependency")
    add_stack("nodejs", bool(package), "package.json")
    add_stack("python", bool(pyproject or requirements or re.search(r"\.py$", joined_names, re.M)), "Python manifest or source files")
    add_stack("supabase", "supabase" in corpus or "supabase/" in joined_names, "Supabase dependency or directory")
    add_stack("docker", "dockerfile" in joined_names or bool(docker), "Dockerfile or Compose file")
    add_stack("cloudflare", "wrangler.toml" in joined_names or "cloudflare" in corpus, "Wrangler config or dependency")

    if "vercel.json" in names or "vercel" in corpus:
        hosting.append(Signal("vercel", "vercel.json or project metadata"))
    if "railway" in corpus:
        hosting.append(Signal("railway", "Railway metadata"))
    if ".github/workflows" in joined_names:
        hosting.append(Signal("github-actions", ".github/workflows"))
    if "aws" in corpus or "serverless.yml" in names or "template.yaml" in names:
        hosting.append(Signal("aws", "AWS dependency or deployment file"))

    ai_markers = ["openai", "anthropic", "gemini", "ollama", "langchain", "llm", "prompt", "embedding"]
    legal_markers = ["legal", "lawyer", "attorney", "case", "court", "claim", "immigration"]
    finance_markers = ["trading", "broker", "portfolio", "crypto", "payment", "stripe", "finance"]
    employment_markers = ["job", "resume", "career", "applicant", "employer"]
    health_markers = ["health", "medical", "patient", "diagnosis", "hipaa"]

    if any(m in corpus for m in ai_markers):
        product_types.append(Signal("ai-saas", "AI provider, model, prompt, or embedding markers"))
        risks.update({"ai-output", "prompt-injection", "provider-data-flow"})
        capabilities.update({"llm-evaluation", "ai-observability", "privacy-review"})
    if any(m in corpus for m in legal_markers):
        product_types.append(Signal("legal-tech", "legal-domain terms in repository"))
        risks.update({"legal-advice", "regulated-or-high-impact-output"})
        capabilities.update({"legal-review", "provenance", "abstention", "accessibility-testing"})
    if any(m in corpus for m in finance_markers):
        product_types.append(Signal("fintech-or-trading", "finance, payments, or trading terms"))
        risks.update({"financial-harm", "money-movement"})
        capabilities.update({"financial-review", "audit-logging", "authorization"})
    if any(m in corpus for m in employment_markers):
        product_types.append(Signal("employment-or-job-tech", "employment-domain terms"))
        risks.update({"employment-impact", "external-communications"})
        capabilities.update({"browser-testing", "privacy-review", "authorization"})
    if any(m in corpus for m in health_markers):
        product_types.append(Signal("healthcare", "health-domain terms"))
        risks.update({"health-harm", "regulated-data"})
        capabilities.update({"privacy-review", "human-review", "audit-logging"})

    if any(s.name in {"nextjs", "react"} for s in stacks):
        capabilities.update({"browser-testing", "accessibility-testing"})
    if any(s.name == "supabase" for s in stacks):
        capabilities.update({"authorization", "tenant-isolation", "backup", "database-migrations"})
    if any(s.name == "docker" for s in stacks):
        capabilities.update({"container-scanning", "sbom"})
    if hosting:
        capabilities.update({"monitoring", "incident-response", "rollback"})

    critical_files = {
        "package.json": (project / "package.json").exists(),
        "pyproject.toml": (project / "pyproject.toml").exists(),
        "requirements.txt": (project / "requirements.txt").exists(),
        "dockerfile": any(Path(n).name.lower() == "dockerfile" for n in names),
        "github_actions": any(n.startswith(".github/workflows/") for n in names),
        "tests": any(re.search(r"(^|/)(tests?|__tests__)(/|$)", n.lower()) for n in names),
    }

    risk_class = "high" if risks.intersection({"legal-advice", "financial-harm", "health-harm", "regulated-data", "money-movement"}) else ("moderate" if risks else "low")
    return {
        "project_path": str(project.resolve()),
        "product_types": [asdict(s) for s in product_types] or [asdict(Signal("general-software", "no specialized domain signal", "medium"))],
        "stacks": [asdict(s) for s in stacks],
        "hosting": [asdict(s) for s in hosting],
        "risk_class": risk_class,
        "risks": sorted(risks),
        "required_capabilities": sorted(capabilities),
        "evidence": critical_files,
        "limitations": [
            "Static repository inspection cannot prove runtime behavior.",
            "Missing product or jurisdiction context must be supplied by a human.",
            "High-risk conclusions require qualified human review."
        ]
    }


def registry_slugs() -> set[str]:
    slugs: set[str] = set()
    pattern = re.compile(r"^canonical_repo:\s*https://github\.com/([^\s]+)", re.M)
    for path in REGISTRY.glob("*/*.md"):
        match = pattern.search(read_text(path))
        if match:
            slugs.add(match.group(1).lower().removesuffix(".git"))
    return slugs


def load_catalog() -> list[dict]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    return list(data["repositories"])


def goal_capabilities(goal: str) -> set[str]:
    text = goal.lower()
    result: set[str] = set()
    rules = {
        "launch": {"browser-testing", "secret-detection", "dependency-scanning", "monitoring", "accessibility-testing", "incident-response", "backup"},
        "security": {"secret-detection", "dependency-scanning", "sast", "dast", "sbom"},
        "ai": {"llm-evaluation", "ai-observability", "red-teaming"},
        "agent": {"agent-orchestration", "mcp", "llm-evaluation", "authorization"},
        "legal": {"legal-review", "document-ingestion", "provenance", "abstention"},
        "trading": {"backtesting", "paper-trading", "portfolio-analysis", "audit-logging"},
        "privacy": {"privacy", "pii-detection", "license-compliance"},
        "supabase": {"authorization", "tenant-isolation", "postgres-backup", "database-migrations"},
        "next.js": {"browser-testing", "unit-testing", "authentication"},
        "nextjs": {"browser-testing", "unit-testing", "authentication"},
    }
    for marker, caps in rules.items():
        if marker in text:
            result.update(caps)
    return result


def score_candidate(repo: dict, required: set[str], validated: set[str]) -> tuple[int, list[str]]:
    repo_caps = set(repo.get("capabilities", []))
    matched = sorted(required.intersection(repo_caps))
    score = len(matched) * 10
    if repo.get("readiness") == "production":
        score += 4
    if repo.get("risk") == "low":
        score += 2
    if repo["slug"].lower() in validated:
        score += 8
    if repo.get("role") == "reference-implementation":
        score -= 2
    if str(repo.get("risk", "")).startswith("high"):
        score -= 3
    return score, matched


def select_resources(assessment: dict, goal: str, explicit_capabilities: Iterable[str], limit: int = 12) -> dict:
    required = set(assessment.get("required_capabilities", []))
    required.update(goal_capabilities(goal))
    required.update(explicit_capabilities)
    validated = registry_slugs()
    ranked = []
    for repo in load_catalog():
        score, matched = score_candidate(repo, required, validated)
        if score <= 0 or not matched:
            continue
        verified = repo["slug"].lower() in validated
        ranked.append({
            **repo,
            "matched_capabilities": matched,
            "selection_score": score,
            "evidence_status": "validated-registry" if verified else "research-candidate-unverified",
            "requires_human_review": str(repo.get("risk", "")).startswith("high") or assessment.get("risk_class") == "high"
        })
    ranked.sort(key=lambda x: (-x["selection_score"], x["name"].lower()))

    selected = []
    covered: set[str] = set()
    for repo in ranked:
        new_coverage = set(repo["matched_capabilities"]) - covered
        if not new_coverage:
            continue
        selected.append(repo)
        covered.update(repo["matched_capabilities"])
        if len(selected) >= limit:
            break

    return {
        "goal": goal,
        "risk_class": assessment.get("risk_class"),
        "required_capabilities": sorted(required),
        "covered_capabilities": sorted(covered),
        "uncovered_capabilities": sorted(required - covered),
        "selected_resources": selected,
        "selection_policy": "smallest-greedy-coverage-with-validated-registry-preference",
        "warnings": [
            "Research-candidate entries are not approved until promoted through the registry methodology.",
            "High-risk legal, financial, health, privacy, security, authentication, and production choices require human review.",
            "Selection does not authorize installation, deployment, purchases, account changes, communications, or live trading."
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    assess = sub.add_parser("assess")
    assess.add_argument("project", type=Path)
    select = sub.add_parser("select")
    select.add_argument("project", type=Path)
    select.add_argument("--goal", default="")
    select.add_argument("--capability", action="append", default=[])
    select.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()
    try:
        assessment = detect_project(args.project)
        if args.command == "assess":
            output = assessment
        else:
            output = {
                "assessment": assessment,
                "selection": select_resources(assessment, args.goal, args.capability, args.limit)
            }
        print(json.dumps(output, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

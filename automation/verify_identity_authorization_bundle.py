#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = ROOT / "evidence" / "intensive-verification" / "tranche-03.md"
BUNDLE = ROOT / "bundles" / "identity-authorization.md"

required_dossier = {
    "OpenFGA": "v1.15.1",
    "SpiceDB": "v1.51.1",
    "Keycloak": "26.6.2",
    "Ory Kratos": "v26.2.0",
    "Ory Hydra": "v26.2.0",
    "ZITADEL": "v4.15.0",
    "Better Auth": "v1.6.6",
    "Node Casbin": "v5.50.0",
}

required_bundle_terms = [
    "Separate authentication requirements from authorization requirements",
    "Database-native authorization",
    "deny-by-default",
    "cross-tenant access attempts",
    "authorization dependency timeout or outage",
    "Do not infer authorization from successful authentication",
]


def main() -> None:
    dossier = DOSSIER.read_text(encoding="utf-8")
    bundle = BUNDLE.read_text(encoding="utf-8")

    missing = []
    for project, pin in required_dossier.items():
        if project not in dossier or pin not in dossier:
            missing.append(f"{project} {pin}")

    for term in required_bundle_terms:
        if term not in bundle:
            missing.append(term)

    if "Auth.js | pending exact stable pin" not in dossier:
        missing.append("Auth.js must remain pending until exact stable pin verification")
    if "Supabase Auth | pending exact service/component pin" not in dossier:
        missing.append("Supabase Auth must remain pending until exact service pin verification")
    if "No candidate becomes Tier A through automation" not in dossier:
        missing.append("human-review Tier A prohibition")

    if missing:
        raise SystemExit("Identity/authorization verification gaps: " + "; ".join(missing))

    print("Identity and authorization evidence/bundle checks passed")


if __name__ == "__main__":
    main()

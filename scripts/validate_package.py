#!/usr/bin/env python3
"""Run structural QA for the headline-ideation package."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = [
        "01_SPECIFICATION.md",
        "SKILL.md",
        "agents/openai.yaml",
        "package_manifest.json",
        "RULES/ruleset.json",
        "RULES/decision_hooks.json",
        "RULES/authority_registry.json",
        "schemas/headline-input.schema.json",
        "schemas/headline-option.schema.json",
        "schemas/finding.schema.json",
        "schemas/ledger.schema.json",
        "schemas/decision.schema.json",
        "schemas/output.schema.json",
        "schemas/run-manifest.schema.json",
        "schemas/cross-family-contracts.json",
        "evals/fixture_contract.schema.json",
        "evals/fixture_catalog.json",
        "evals/rule_fixture_crosswalk.json",
        "evals/adversarial_negative_controls.json",
        "evals/integration_cases.json",
        "evals/evaluation_set.md",
        "evals/scorer.py",
        "references/generation-procedure.md",
        "references/quality-rubric.md",
        "references/diversity-matrix.md",
        "references/anti-slop-checklist.md",
        "references/examples.md",
        "references/research-basis.md",
        "CHANGELOG_REGRESSION/CHANGELOG.md",
        "scripts/validate_package.py",
        "scripts/validate_schemas.py",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill = ROOT / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        if len(text.splitlines()) > 500:
            errors.append("SKILL.md exceeds 500 lines")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append("SKILL.md lacks required frontmatter")
        if re.search(r"\b(TODO|TBD|FIXME)\b", text, re.IGNORECASE):
            errors.append("SKILL.md contains unresolved placeholders")
        if "$headline-ideation" not in text:
            errors.append("SKILL.md lacks invocation marker")

    agent = ROOT / "agents/openai.yaml"
    if agent.is_file():
        text = agent.read_text(encoding="utf-8")
        for marker in ["interface:", "display_name:", "short_description:", "default_prompt:", "policy:", "allow_implicit_invocation:"]:
            if marker not in text:
                errors.append(f"agents/openai.yaml missing {marker}")
        if "$headline-ideation" not in text:
            errors.append("agent default prompt lacks invocation marker")

    documents: dict[str, Any] = {}
    for path in sorted(ROOT.rglob("*.json")):
        try:
            documents[path.relative_to(ROOT).as_posix()] = load(path)
        except Exception as exc:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

    manifest = documents.get("package_manifest.json", {})
    if manifest.get("package_version") != "0.1.0":
        errors.append("package version must be 0.1.0")
    if manifest.get("runtime", {}).get("network_required") is not False:
        errors.append("runtime network_required must be false for the self-contained package")

    ruleset = documents.get("RULES/ruleset.json", {})
    rules = ruleset.get("rules", [])
    rule_ids = [rule.get("id") for rule in rules]
    if ruleset.get("version") != "0.1.0":
        errors.append("ruleset version must be 0.1.0")
    if len(rules) != 30:
        errors.append(f"expected 30 rules, found {len(rules)}")
    if len(set(rule_ids)) != len(rule_ids):
        errors.append("rule IDs are not unique")
    hooks = documents.get("RULES/decision_hooks.json", {}).get("hooks", [])
    hook_ids = [hook.get("id") for hook in hooks]
    if len(hooks) != 10:
        errors.append(f"expected 10 decision hooks, found {len(hooks)}")
    if len(set(hook_ids)) != len(hook_ids):
        errors.append("decision hook IDs are not unique")

    catalog = documents.get("evals/fixture_catalog.json", {})
    fixtures = catalog.get("fixtures", [])
    fixture_ids = [item.get("fixture_id") for item in fixtures]
    fixture_map = {item.get("fixture_id"): item for item in fixtures}
    if len(fixtures) != 30:
        errors.append(f"expected 30 fixtures, found {len(fixtures)}")
    if len(set(fixture_ids)) != len(fixture_ids):
        errors.append("fixture IDs are not unique")
    counts = Counter(item.get("kind") for item in fixtures)
    for kind, expected in catalog.get("fixture_counts", {}).items():
        if counts.get(kind, 0) != expected:
            errors.append(f"fixture count for {kind}: expected {expected}, got {counts.get(kind, 0)}")
    for fixture in fixtures:
        if fixture.get("synthetic") is not True:
            errors.append(f"{fixture.get('fixture_id')}: synthetic must be true")
        gold = fixture.get("gold", {})
        unknown = (set(gold.get("expected_rule_ids", [])) | set(gold.get("must_not_emit_rule_ids", []))) - set(rule_ids)
        if unknown:
            errors.append(f"{fixture.get('fixture_id')}: unknown rule IDs {sorted(unknown)}")
        unknown_hooks = set(gold.get("required_decision_hooks", [])) - set(hook_ids)
        if unknown_hooks:
            errors.append(f"{fixture.get('fixture_id')}: unknown decision hooks {sorted(unknown_hooks)}")

    crosswalk = documents.get("evals/rule_fixture_crosswalk.json", {})
    rows = crosswalk.get("rows", [])
    row_ids = [row.get("rule_id") for row in rows]
    if len(rows) != len(rules) or set(row_ids) != set(rule_ids):
        errors.append("crosswalk must contain exactly one row for every rule")
    for row in rows:
        for field in ("positive", "negative", "adversarial"):
            values = row.get(field, [])
            if not values:
                errors.append(f"{row.get('rule_id')}: missing {field} fixture")
            for fixture_id in values:
                if fixture_id not in fixture_map:
                    errors.append(f"{row.get('rule_id')}: unknown fixture {fixture_id}")
        for fixture_id in row.get("integration", []):
            if fixture_id not in fixture_map or fixture_map[fixture_id].get("kind") != "integration":
                errors.append(f"{row.get('rule_id')}: invalid integration fixture {fixture_id}")

    controls = documents.get("evals/adversarial_negative_controls.json", {})
    if set(controls.get("adversarial_fixture_ids", [])) != {f["fixture_id"] for f in fixtures if f.get("kind") == "adversarial"}:
        errors.append("adversarial control list does not match catalog")
    if set(controls.get("negative_control_fixture_ids", [])) != {f["fixture_id"] for f in fixtures if f.get("kind") == "negative_control"}:
        errors.append("negative control list does not match catalog")
    integrations = documents.get("evals/integration_cases.json", {}).get("cases", [])
    if {item.get("fixture_id") for item in integrations} != {f["fixture_id"] for f in fixtures if f.get("kind") == "integration"}:
        errors.append("integration case list does not match catalog")

    research = ROOT / "references/research-basis.md"
    if research.is_file() and len(re.findall(r"https?://", research.read_text(encoding="utf-8"))) < 10:
        warnings.append("research basis has fewer than ten source URLs")

    result = {
        "pass": not errors,
        "package": "headline-ideation",
        "package_version": manifest.get("package_version"),
        "rule_count": len(rules),
        "decision_hook_count": len(hooks),
        "fixture_count": len(fixtures),
        "fixture_counts": dict(counts),
        "crosswalk_rows": len(rows),
        "json_file_count": len(documents),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())

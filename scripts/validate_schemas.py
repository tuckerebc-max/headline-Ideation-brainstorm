#!/usr/bin/env python3
"""Validate JSON schema examples against the package's declared schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"
PAIRS = {
    "headline-input.example.json": "headline-input.schema.json",
    "headline-option.example.json": "headline-option.schema.json",
    "finding.example.json": "finding.schema.json",
    "ledger.example.json": "ledger.schema.json",
    "decision.example.json": "decision.schema.json",
    "output.example.json": "output.schema.json",
    "run-manifest.example.json": "run-manifest.schema.json",
}


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    registry = Registry()
    schemas: dict[str, dict] = {}
    for path in sorted(SCHEMAS.glob("*.schema.json")):
        document = read(path)
        schemas[path.name] = document
        registry = registry.with_resource(document["$id"], Resource.from_contents(document))

    errors: list[str] = []
    for example_name, schema_name in PAIRS.items():
        example_path = EXAMPLES / example_name
        if not example_path.is_file():
            errors.append(f"missing example: {example_name}")
            continue
        schema = schemas[schema_name]
        validator = Draft202012Validator(schema, registry=registry)
        for error in validator.iter_errors(read(example_path)):
            location = ".".join(str(item) for item in error.absolute_path)
            errors.append(f"{example_name} {location}: {error.message}")

    result = {"pass": not errors, "validated_examples": len(PAIRS), "errors": errors}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())

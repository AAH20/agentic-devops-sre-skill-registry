from __future__ import annotations

import json
import re
from pathlib import Path


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_CONTRACT = {"schema_version", "risk", "permissions", "mutation_policy", "required_outputs", "source_project"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}
    block = text.split("---\n", 2)[1]
    result = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def validate_skill(path: Path) -> list[str]:
    errors = []
    if not NAME.fullmatch(path.name) or len(path.name) > 63:
        errors.append("folder name must be lowercase kebab-case and under 64 characters")
    skill_file, contract_file = path / "SKILL.md", path / "contract.json"
    if not skill_file.exists():
        errors.append("missing SKILL.md")
    else:
        meta = parse_frontmatter(skill_file)
        if meta.get("name") != path.name:
            errors.append("frontmatter name must match folder")
        if len(meta.get("description", "")) < 40:
            errors.append("description is missing or not discriminating")
        if "TODO" in skill_file.read_text(encoding="utf-8"):
            errors.append("unfinished TODO in SKILL.md")
    if not contract_file.exists():
        errors.append("missing contract.json")
    else:
        try:
            contract = json.loads(contract_file.read_text(encoding="utf-8"))
            for field in sorted(REQUIRED_CONTRACT - contract.keys()):
                errors.append(f"contract missing {field}")
            if contract.get("mutation_policy") != "explicit-authorization-required":
                errors.append("mutation policy must preserve explicit authorization")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid contract JSON: {exc}")
    return errors


def catalog(root: Path) -> list[dict]:
    rows = []
    for path in sorted(item for item in root.iterdir() if item.is_dir()):
        metadata = parse_frontmatter(path / "SKILL.md") if (path / "SKILL.md").exists() else {}
        contract = json.loads((path / "contract.json").read_text()) if (path / "contract.json").exists() else {}
        rows.append({"name": path.name, "description": metadata.get("description"), "risk": contract.get("risk"), "source_project": contract.get("source_project"), "valid": not validate_skill(path)})
    return rows

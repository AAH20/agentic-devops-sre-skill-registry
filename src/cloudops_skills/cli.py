from __future__ import annotations

import argparse
import json
from pathlib import Path

from .registry import catalog, validate_skill
from .scoring import score


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and score reusable Agentic CloudOps skills")
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("path")
    listing = commands.add_parser("catalog")
    listing.add_argument("path", default="skills", nargs="?")
    scoring = commands.add_parser("score")
    scoring.add_argument("records")
    scoring.add_argument("--output")
    args = parser.parse_args()
    if args.command == "validate":
        errors = validate_skill(Path(args.path))
        print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
        raise SystemExit(0 if not errors else 2)
    if args.command == "catalog":
        print(json.dumps(catalog(Path(args.path)), indent=2))
        return
    result = score(json.loads(Path(args.records).read_text(encoding="utf-8")))
    content = json.dumps(result, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(content, encoding="utf-8")
    print(content, end="")


if __name__ == "__main__":
    main()

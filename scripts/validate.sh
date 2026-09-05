#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
PYTHONPATH=src python3 -m unittest discover -s tests -v
for skill in skills/*; do
  PYTHONPATH=src python3 -m cloudops_skills.cli validate "$skill"
done
PYTHONPATH=src python3 -m cloudops_skills.cli catalog skills >/tmp/cloudops-skill-catalog.json
PYTHONPATH=src python3 -m cloudops_skills.cli score evals/reference-results.json --output /tmp/cloudops-skill-scorecard.json
python3 -m json.tool /tmp/cloudops-skill-catalog.json >/dev/null
python3 -m json.tool /tmp/cloudops-skill-scorecard.json >/dev/null

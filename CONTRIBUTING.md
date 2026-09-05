# Contributing

Every new skill must:

1. Use lowercase kebab-case naming under 64 characters.
2. Include `SKILL.md` with matching `name` and a precise activation description.
3. Include `contract.json` declaring risk, minimal permissions, mutation policy, required outputs and source implementation.
4. Put substantial conditional material in linked references rather than bloating the entry point.
5. Preserve user scope and require authorization immediately before external mutation.
6. Provide meaningful evaluation cases and label all synthetic results.
7. Pass both the registry validator and the skill-creator quick validator.

Never commit credentials, customer evidence, private prompts, proprietary runbooks, unsanitized telemetry or model outputs without redistribution rights.

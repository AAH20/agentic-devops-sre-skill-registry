---
name: azure-private-link-diagnose
description: Diagnose Azure Private Endpoint, Private DNS, hybrid DNS, DNS Private Resolver, routing, NSG, and service-firewall failures from supplied evidence. Use for read-only Azure private-connectivity troubleshooting; do not use it to deploy or change resources.
---

# Diagnose Azure Private Link

Establish the failed layer and produce an evidence-backed diagnosis before proposing a change.

## Workflow

1. Confirm the affected FQDN, client network, expected private endpoint, port, and observation time.
2. Inspect only supplied evidence or collect more through read-only operations authorized by the user.
3. Check in order: endpoint state, expected private DNS zone, A record, source-VNet link, client DNS answer, hybrid forwarding, ruleset link, effective route, effective NSG rule, then service firewall.
4. Mark the result `INCOMPLETE` when a required layer is unobserved. Do not infer health from missing evidence.
5. Report every root cause with the observed value, expected condition, impact, confidence, and smallest reversible remediation.
6. Separate diagnosis from execution. Obtain authorization before any Azure, DNS, routing, NSG, or IaC mutation.

When constructing an evidence bundle or mapping service zones, read [references/evidence-contract.md](references/evidence-contract.md).

## Safety invariants

- Never request or expose credentials, tokens, connection strings, customer identifiers, or unsanitized tenant exports.
- Do not claim a live packet path was validated from configuration evidence alone.
- Treat generated Terraform/Bicep as review scaffolding until plan/what-if, peer review, approval, rollback, and post-change checks exist.
- Do not advise forwarding on-premises DNS directly to `168.63.129.16`; use an Azure-hosted forwarder or DNS Private Resolver inbound endpoint as appropriate.

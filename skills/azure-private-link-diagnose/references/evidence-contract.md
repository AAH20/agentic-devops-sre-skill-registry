# Evidence contract

Collect only the fields required to distinguish the failed layer:

- Endpoint: resource type, FQDN, connection state and private IP
- DNS: expected zone, observed answer/status, A record and VNet links
- Hybrid DNS: client origin, forwarders, resolver inbound IP and ruleset links
- Path: source VNet/subnet, expected and observed next hop
- Policy: effective NSG and service-firewall decisions
- Metadata: sanitized scenario identifier and observation time

Common private zones include `privatelink.blob.core.windows.net`, `privatelink.database.windows.net`, and `privatelink.vaultcore.azure.net`. Verify the service-specific zone using current Microsoft documentation rather than relying on this non-exhaustive list.

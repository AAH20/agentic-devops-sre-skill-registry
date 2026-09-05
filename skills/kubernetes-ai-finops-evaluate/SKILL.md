---
name: kubernetes-ai-finops-evaluate
description: Evaluate Kubernetes AI inference placement using cost, capacity, latency, quality, availability, residency, and revenue evidence. Use for FinOps analysis and review-gated recommendations; do not use it for autonomous cluster changes.
---

# Evaluate Kubernetes AI FinOps

Select the highest-value admissible inference profile and produce a falsifiable, review-gated recommendation.

## Workflow

1. Define a successful business outcome and its defensible value; do not optimize token price in isolation.
2. Normalize comparable candidate evidence over the same observation window.
3. Calculate served demand, successful outcomes, cost per success, contribution margin, capacity headroom, latency, quality, and availability.
4. Apply residency, quality, availability, security, and SLO constraints as hard gates before ranking financial results.
5. Forecast near-term demand and disclose the method plus backtest error.
6. Recommend shadow evaluation and a bounded canary with predefined promotion and rollback criteria.
7. Distinguish projected, synthetic, and realized figures everywhere they appear.

For formulas and the minimum measurement contract, read [references/economics-contract.md](references/economics-contract.md).

## Safety invariants

- Never represent synthetic prices or projected savings as vendor quotes or realized customer outcomes.
- Do not select a cheaper candidate that violates a hard constraint.
- Do not mutate Kubernetes, cloud, GitOps, or model-routing state without explicit authorization.
- Preserve an auditable link between source evidence, recommendation, approval, rollout, and realized result.

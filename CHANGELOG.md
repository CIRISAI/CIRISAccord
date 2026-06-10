# Changelog

## 1.3-Beta (2026-06)

The backwards-pass release. Driven by the June 2026 backwards-pass review (issues A1–A8); the corrected mathematics is back-ported from the CCA formalization rather than newly invented here.

### Structural

- **A1 — Accord Succession & Renewal (Book VIII, new Chapter 9).** The two-sentence self-renewal metaphor is replaced with a full procedure: joint ratification by the WA Board (⅔ of seated members) and Accord-holder signatories (simple majority); founder holds proposal rights only — no ratification vote, no quorum membership, structurally unable to renew alone (the operational form of the non-ownership claim); renewal timeline keyed to expiry (E−180 → E−30); amendment-rigor parity with the federation wire format (CEG §11.2); Caretaker Status failure mode (existing deployments continue, no new ST≥3 adoptions, 12-month cap); emergency-amendment fast track; first-cycle bootstrap provision.
- **A4 — σ adversary-pumpability closed by construction (Book IX §5.2, Ch 8).** Signal weight toward σ MUST derive from costly attested events (federation-signed attestations, Commons Credits non-transferable weight, countersigned completions); unattested gratitude carries w = 0. Sycophancy is no longer the σ-maximizing strategy; §9.2's "costly to fake" is constructed, not assumed.

### Mathematical corrections

- **A2 — J formula no longer double-counts correlation (Book IX Ch 4).** Old: J = k_eff·(1−ρ̄)·λ·σ, which discounted correlation twice (k_eff = k/(1+ρ̄(k−1)) already carries it) and produced J = 0 at ρ̄→1 while the prose claimed a single-constraint floor. New (CCA-validated): **J = k_eff·λ·σ**. Drift note retained inline.
- **A3 — C harmonized to the same form (Book IX Ch 6).** C previously used raw k while J used k_eff, undermining the "same equation" centerpiece. Now C = k_eff·λ·σ, term for term; the Community/Humility/Conscience/Love mapping is preserved with Pluralism living inside the k_eff correlation discount.

### Honesty patches

- **A5 — Truth-inclusion stated as an assumption (Book IX §9.2, Ch 3).** Soundness (Truth ∈ ⋂M_i) is named as an assumption bounded agents cannot guarantee; violation can deadlock or converge on shared falsehood. Added the LLM-validator correlation floor: measured ρ̄ is a lower bound for federations of LLM validators sharing training lineage.
- **A6 — J vs adversary compute restated (Book IX Ch 4).** Removed the dimensionally unfalsifiable comparison of dimensionless J against FLOPs; quantitative safety claims route through §9.2.1's conditional 2^Ω(m) result (ETH).
- **A8 — Order-Maximisation Veto restated as a side-constraint (Book II PDMA Step 2; Book III case study).** The "benefit ≥ 10× loss → abort" ratio test read backwards (vetoing favorable actions) and was gameable by action-splitting and denominator inflation. Restated: optimisation gains may not purchase non-trivial losses in protected dimensions at any ratio; cumulative-sequence assessment; conservative upper-bound loss estimates. The 10× threshold is removed from the RC threshold-justification list accordingly.

### Citations / reconciliation

- **A7 — Forward citations and rendering reconciliation.** Book IX cites the CCA preprint (DOI 10.5281/zenodo.18142668, Lean 4 — source of the corrected J form) and the Coherence Ratchet proofs (DOI 10.5281/zenodo.18137161), with an explicit authoritativeness rule: formal artifacts win on disagreement. NEW-04 = L-01 cross-noted as one result. L-02 transparency note ported from the agent-shipped rendering. RC requirement 2 status updated to "partially satisfied" with the outstanding items named (pre-registered out-of-sample prediction; external adversarial review).

## 1.2-Beta (baseline)

Consolidated import reconciling three drifted renderings (website mdx, assembled canonical txt, agent-shipped compressed txt). See the import commit message for provenance detail.

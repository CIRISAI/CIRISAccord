# CIRIS Accord

The canonical source of the **CIRIS Accord** — the constitutional layer of the CIRIS ethical-AI framework, governing the ethical operation of autonomous systems from narrow tools to recursive ASI.

**Current version**: 1.3-Beta (working draft, open to adversarial review)
**Issued**: 2025-04-16 (1.0) · 2026-06 (1.3-Beta)
**Auto-expires**: 2027-04-16 — renewal per Book VIII, Chapter 9

## This repository is the source of truth

Before this repo existed, the Accord text lived in three drifting renderings (the ciris.ai website mdx, an assembled canonical txt, and the agent-shipped compressed txt) whose version headers disagreed. This repo consolidates them. The website and the agent-shipped copy are now **derived artifacts** that should be regenerated from this source.

## Structure

| Path | Content |
|---|---|
| `accord/00_introduction.md` | Version, scope, RC requirements, review cadence |
| `accord/01_foreword.md` · `02_genesis.md` | Foreword + Genesis of Ethical Agency |
| `accord/03_book_I.md` … `11_book_IX.md` | Books I–IX (principles → mathematics of coherence) |
| `accord/annexes/` | Annexes A–J (F–I are stubs pending operationalization) |
| `accord/90_addenda.md` · `91_backmatter.md` | Addenda + change-log backmatter |

## Versioning

- **1.2-Beta** — the consolidated baseline imported here (formerly scattered across renderings).
- **1.3-Beta** — the backwards-pass release: J/C formula correction (CCA-validated form), σ attestation requirement, truth-inclusion assumption, OMV side-constraint restatement, forward citations to formal artifacts, and the Accord Succession & Renewal procedure (Book VIII Ch 9). See [CHANGELOG.md](CHANGELOG.md).

Where Book IX and the formally verified artifacts disagree, the formal artifact is authoritative:
- CCA preprint (Lean 4): DOI [10.5281/zenodo.18142668](https://doi.org/10.5281/zenodo.18142668)
- Coherence Ratchet proofs: DOI [10.5281/zenodo.18137161](https://doi.org/10.5281/zenodo.18137161)

## How to propose changes

Open an issue or PR. A public comment window opens every 12 months — or within 30 days of any material safety/governance incident. Renewal at expiry, material amendment, and emergency amendment follow **Book VIII, Chapter 9**: joint ratification by the Wise Authority Board (⅔) and Accord-holder signatories (majority). The founder holds proposal rights only and cannot renew the Accord alone.

## License

The Accord text is published for adversarial review and adoption. License selection is pending (founder decision); until then the Liability section of the Introduction governs: provided "as-is," informative in nature.

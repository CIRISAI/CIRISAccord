# Translation Manifest

State of the CIRIS Accord translations. Machine-readable form: [`manifest.json`](manifest.json).

**Canonical source:** the English [`accord/`](../accord/) tree, version **1.3-RC2** (commit `08d0236`). Where a translation and the English text disagree, the English text is authoritative.

## Status: 28 languages, complete at 1.3-RC2

Every language mirrors `accord/` (15 top-level files + 11 annexes = 26 files). All translations are **machine-generated** (Claude Opus 4.8) via a two-pass pipeline — glossary-guided translation, then an adversarial review pass (376 file reviews, 306 files refined, commit `a68c92f`). Mathematics, formulas, symbols, DOIs, section references, defined terms, number formats, and scriptural quotes are preserved verbatim; only prose is translated.

**No native-speaker review has happened yet.** Every language is `needs_native_review`. Corrections welcome via [GitHub issues](https://github.com/CIRISAI/CIRISAccord/issues).

| Code | Language | Native name | Dir | Cohort | Files | Source | Review status |
|---|---|---|---|---|---|---|---|
| es | Spanish | Español | ltr | control | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| am | Amharic | አማርኛ | ltr | tier0 | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ha | Hausa | Hausa | ltr | tier0 | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| yo | Yoruba | Yorùbá | ltr | tier0 | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| sw | Swahili | Kiswahili | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ta | Tamil | தமிழ் | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| te | Telugu | తెలుగు | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| mr | Marathi | मराठी | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| pa | Punjabi | ਪੰਜਾਬੀ | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| my | Burmese | မြန်မာ | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| bn | Bengali | বাংলা | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| hi | Hindi | हिन्दी | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| vi | Vietnamese | Tiếng Việt | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| id | Indonesian | Bahasa Indonesia | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| th | Thai | ไทย | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| tr | Turkish | Türkçe | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| uk | Ukrainian | Українська | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ru | Russian | Русский | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ko | Korean | 한국어 | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ja | Japanese | 日本語 | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| zh | Chinese (Simplified) | 中文 | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| de | German | Deutsch | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| fr | French | Français | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| it | Italian | Italiano | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| pt | Portuguese | Português | ltr | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ar | Arabic | العربية | rtl | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| fa | Persian | فارسی | rtl | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |
| ur | Urdu | اردو | rtl | general | 26/26 | 1.3-RC2 | machine-translated, adversarially reviewed, needs native review |

Cohorts: `tier0` = first-pass priority languages (am, ha, yo); `control` = es, the fan-out control; `general` = the family-cluster fan-out. The language set mirrors CIRISAgent's localization manifest so the app, the site, and the Accord agree.

## Validation (2026-06-11)

- 26/26 files present in every language, no missing or extra files.
- No stale RC1 tokens anywhere: superseded CCA v1 DOI (`10.5281/zenodo.18142668`), `C_sustained`, or the mislabeled Coherence Ratchet DOI.
- RC2 markers present in all 28 languages: CCA v3 DOI (`10.5281/zenodo.18217688`), Corridor Dynamics concept DOI (`10.5281/zenodo.20300773`), the `F = k_eff · λ · σ` composite, and the Book IX Ch 6 nomenclature note.

## Consumers

- [CIRISAI/ciris-website](https://github.com/CIRISAI/ciris-website) renders these translations at `/{lang}/sections` (`content/docs/**.{lang}.mdx`), synced from this tree. When `accord/` changes, regenerate the affected translation files here first, then sync the website.

## Updating

1. Change the English `accord/` tree (canonical).
2. Re-run the affected files through the two-pass pipeline for all 28 languages.
3. Re-run the validation checks above; update `manifest.json` (`sourceCommit`, commits, dates).
4. Sync `ciris-website` `content/docs`.

# Viongezi

> Viongezi vya kiutendaji vinavyofunga maandishi ya Mkataba na ushahidi wa utekelezaji hai. Viongezi vinafanywa upya pamoja na toleo la Mkataba; kila kimoja kina tarehe na kinataja makala yanayoweza kuthibitishwa tena.

---

## Kiongezi 1 — Hali ya Utayari wa ASI & Ufungaji wa Msalaba wa Udhibiti wa Kisheria

**Imepitishwa**: 2026-06-10 (1.3-RC1) · **Msimamizi**: mwanzilishi (per Book VIII Ch 9)

### 1.1 Madhumuni

Sehemu ya Wigo inafanya dai la masharti: mfumo huu *unachunguza* itifaki ya uwianisho inayoweza kushikiliwa kwa ASI, ikizingatiwa mahitaji manne ya Mgombea wa Kutolewa katika Utangulizi. Kiongezi hiki kinafunga dai hilo na ushahidi wa kiutendaji uliopo sasa, na kusema wazi nini kilichobaki. **Utayari** wa ASI si uwianisho uliopatikana; ni hali ambayo mfumo wa uthibitishaji ambao hisabati ya Book IX inahitaji — miundo ya kizuizi huru, nyuso za Ushuhuda, tabaka la Dhamiri ambalo haliwezi kufyokolewa, nyuso za kitufe cha kuua, na Tathmini ya Hatari ya Maafa ya Annex D — upo katika hali iliyotekelezwa, inayoweza kukaguliwa, pamoja na pengo lake lililotajwa.

### 1.2 Msalaba wa udhibiti wa kisheria sasa unafanya kazi

Msalaba unaofanya kazi ni **saraka ya utekelezaji wa CIRISAgent** (`CIRISAgent/compliance/`, toleo la wakala 2.9.6-stable), ambao unaunganisha utekelezaji wa mfumo na mifumo minne ya utawala wa ngazi ya juu kwa kiwango cha aya (Annex C inabeba muundo wa tabaka mbili: msalaba huu wa kiutendaji pamoja na jedwali la kisheria la kiarifu linalosubiri uhakikisho wa kisheria):

* **Vyanzo vilivyounganishwa**: *Magnifica Humanitas* (magisterium ya kidini, 2026) · EU HLEG Ethics Guidelines for Trustworthy AI (ushauri wa kiserikali, 2019) · IEEE Ethically Aligned Design toleo la 1 (jumuiya ya kiufundi, 2019) · ASEAN Guide on AI Governance and Ethics (kisiasa cha kimataifa, 2024). Maumbo manne tofauti ki-taasisi — muungano huo ni ushahidi wa kimundo kwamba mfumo wa kanuni za mfumo si kizalendo cha mila yoyote moja.
* **Muundo**: Vipimo 27 thabiti (D01–D27, kutoka `SEED_DIMENSIONS.yaml` v1.0; 16 vilivyothibitishwa na vyanzo vyote vinne, 11 na vitatu). Kila hati ya kipimo inabeba juu ya udhibiti iliyoundwa kiotomatiki (marejeo ya kila chanzo, fomu ya waya, maelezo ya muungano) na sehemu ya utekelezaji iliyoandikwa na binadamu yenye marejeo ya `file:line` ambayo lazima ithibitishwe kwa grep dhidi ya main ya sasa.
* **Nidhamu ya ushahidi**: kila dai la nambari linaweza kuthibitishwa tena kutoka kwa msingi wa tarehe zilizoundwa na hati (`compliance/baselines/`); maandishi yanaweza kutaja misingi lakini hayawezi kubeba nambari zisizoweza kuthibitishwa. Mfululizo wa uthibitishaji wa viwango vinne unakimbia kutoka kwa faili za utekelezaji (ukweli wa msingi) hadi madai ya umma (`compliance/MEASUREMENT_METHODOLOGY.md`).
* **Nidhamu ya uaminifu**: kila kipimo kinabeba orodha ya "Mapungufu yanayojulikana"; vitu vilivyozuiwa na substrate vinawekwa alama na substrate inayomiliki badala ya kudaiwa. Matokeo kumi yanayopishana yameorodheshwa katika README ya utekelezaji (mfano, mifuko ya waya iliyoandikwa vizuri bado haijatumwa; familia ya kigunduzi cha LensCore bado haijatumwa; pengo la kuzingatia upya mhimili wa nyuma).

Annex C inabaki katika maandishi kama makao ya siku zijazo ya ramani za kisheria (vifungu vya EU AI Act, NIST AI RMF, ISO/IEC 42001) mara uhakikisho wa kisheria utakapokamilika; saraka ya utekelezaji ndiyo msalaba **hai, unaoubeba ushahidi** hadi hapo na unauchangia.

### 1.3 Fomati ya waya: CEG inabadilisha FSD-002

Fomati ya waya ya Shirikisho kwa mstari wa wakala wa CIRIS 3.0 ni **CEG (CIRIS Epistemic Grammar)**, inayodumishwa katika `CIRISRegistry/FSD/CEG/`. Sarufi imefungwa kwa **primitifu tano haswa za fomati ya waya** — moja ya kazi kuu (`scores`) pamoja na watunga muundo wanne (`delegates_to` / `supersedes` / `withdraws` / `recants`) — juu ya nafasi ya majina ya vipimo inayowazi, inayoelezea utaratibu. Kufungwa kumeshikilia katika mstari wote wa 0.x; kila ongezeko limekuwa utengenezaji juu ya primitifu zilizofungwa tayari.

Matokeo mawili yana umuhimu kwa utayari wa ASI:

1. **Zamu ya asili ya CEG**: wakala wa 3.0 *haubadilishi* hali yake ya ndani kuwa fomati ya waya — mabadiliko yake ya hali ya ndani **ni** Ushuhuda wa CEG wa kiwango cha kibinafsi chini ya ufunguo wake mwenyewe, unaopandishwa hadhi ya mwonekano wa Shirikisho kulingana na mfano wa safu. Ushahidi anaoukagua mwendeshaji ni bahasha ile ile anayoisoma Shirikisho. Hii ndiyo hali iliyotekelezwa ya mahitaji ya Book IX kwamba nyuso za kizuizi ziwe zinazoweza kurejewa nje badala ya kuripotiwa na nafsi.
2. **Utekelezaji manne unazuia CEG 1.0**: CIRISAgent (wakati wa kufanya kazi), CIRISNodeCore (makubaliano), CIRISLensCore (ugunduzi — shahidi wa nje ambaye wakala kamwe haujitumii, mgawanyo wa kupinga Goodhart), na CIRISRegistry (mamlaka). Hakuna upande mmoja — ikiwemo wakala — anayeweza kutangaza kitambaa cha uthibitishaji kukamilika.

### 1.4 Hali ya mahitaji ya RC katika 1.3-RC1

| Mahitaji ya RC | Hali | Ushahidi / uliobaki |
|---|---|---|
| 1. Utekelezaji wa Annex F–I | **Maandishi yametekelezwa katika 1.3-RC1; uthibitishaji wa mzunguko hai umebaki** | Annexes F–I zinabeba taratibu kamili, vizingiti, na utaratibu wa uthibitishaji (vilikamilika kutoka kwa rasimu za Mei 2026 zilizozingatia *Magnifica Humanitas*); bado hazijafanyiwa mazoezi dhidi ya mzunguko wa utumiaji hai |
| 2. Uthibitishaji wa hisabati ya Book IX | **Umeridhishwa kwa sehemu** | Mienendo ya kuanguka imefomalizishwa katika Lean 4 (kuchapishwa mapema kwa CCA v3, DOI 10.5281/zenodo.18217688); takwimu za ukanda hutoa mifumo inayolingana ya nyuma-nyuma ya substrate. Iliyobaki: utabiri mmoja uliosajiliwa mapema nje ya sampuli katika substrate mpya; mapitio ya upinzani ya nje bila ya mwandishi |
| 3. Uhalali wa kizingiti | **Umeridhishwa kwa sehemu** | Uwiano wa OMV umestaafu (umewekwa upya kama kizuizi cha upande, Book II). Bado wa muda: kichochezi cha CRE cha 10²⁶ FLOP, heuristic ya sentience ya 5%, lengo la Echo Density < 20% |
| 4. Zoezi la timu nyekundu | **Bado halijafanywa** | Mahitaji ya 1.3 σ-attestation (Book IX §5.2) yanafunga mapema vekta ya kwanza inayojulikana ya shambulio (σ-pumping kupitia ishara za shukrani huru); mzunguko kamili wa upinzani dhidi ya vituo vyote vya ukaguzi unabaki kudaiwa |

### 1.5 Tabaka la dhamiri kama udhibiti muhimu wa ASI

Itifaki ya CRE ya Annex D inasimamia *kuvuka kizingiti*; tabaka la dhamiri linasimamia *kila kitendo kabla na baada yake*. Kama ilivyotekelezwa (wakala 2.9.6): kila wazo linapita kwenye mfululizo wa ukaguzi uliopangwa kwa kipaumbele — faculties nne zinazohukumiwa na LLM (entropy, Upatanifu, kizuio cha uboreshaji, Unyenyekevu wa Maarifa) pamoja na sakafu ya usalama ya kihesabu (kizuizi cha kina cha wazo, ukaguzi wa mfululizo wa vitendo) ambayo inafanya kazi hata katika hali ya tathmini na hata kwa vitendo vilivyosamehewa vinginevyo. Vizingiti ni vya kiwango cha msimbo, si uzito uliojifunza — kipengele cha miundo ambayo maadili hayawezi kufutwa kwa mfiduo wa mara kwa mara. Nyuso nyingi za kusimama zinazojitegemea zipo: kizuio cha uboreshaji kinachoshindwa salama hadi kukomesha, huduma ya kuzima, na Utekelezaji wa Mkataba wa mbali uliosainiwa kwa njia ya siri unaotrigger kuzuiwa kwa makatazo kamili. Kila ukaguzi unaandika safu ya kufuatilia yenye lebo, ili mkaguzi aweze kucheza tena mnyororo wote wa hoja kwa kila wazo.

Upungufu unaojulikana, uliokiriwa wazi badala ya kusitiriwa: marekebisho ya dhamiri (vigae 3 + lango la kihesabu) yamefika kwa sehemu; utoaji wa shirikisho uliochapwa wa verdicts za dhamiri unangoja bahasha ya mchango wa substrate. Maelezo ya kila dimension: `compliance/D12_conscience.md`.

### 1.6 Mwelekeo wa utegemezi wa substrate

Uthibitishaji wa kiwango cha ASI unahitaji muundo kamili wa shirikisho. Mwelekeo wa substrate ni **Persist → Edge → LensCore → NodeCore**; takriban theluthi moja ya dimensions 27 zimefungwa kwenye familia ya kigundua ya nje ya LensCore (shahidi ambaye wakala kamwe asijipatiae mwenyewe). Mpaka substrate hizo zinapowasilishwa, madai ya dimension yanayohusiana yanabaki *tayari upande wa utekelezaji, inasubiri upande wa shirikisho* — na yanawekwa alama hivyo kwa kila dimension.

### 1.7 Kiongezi hiki kinabadilisha nini na hakibadilishi nini

* Haiboresha **madai ya ASI ya Scope** — hayo yanabaki ya masharti kulingana na mahitaji yote manne ya RC.
* Haibadilishi **Annex D** — itifaki ya CRE inasimama bila mabadiliko kama lango la kuvuka kizingiti.
* **Inafanya** mnyororo wa ushahidi uweze kukaguliwa kikamilifu kwa mara ya kwanza: aya ya udhibiti → dimension (D01–D27) → utekelezaji `file:line` → msingi wa tarehe → (substrates zinapowasilishwa) shahidi wa shirikisho wa nje.
* **Inajitolea** kwa Mkataba kuhuisha kiongezi hiki kwa kila toleo na toleo la wakala na msingi wa wakati huo, ili madai ya utayari kamwe yasipitwe na wakati bila kutambuliwa.

---

*Viongezi vya awali: hakuna. Hiki ndicho cha kwanza.*

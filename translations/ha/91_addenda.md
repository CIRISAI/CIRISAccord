# Addenda

> Ƙarin bayanai na aiki da ke ɗaure rubutun YARJEJENIYA da shaidu na aiwatarwa na yanzu. Ana sabunta Addenda tare da sigar YARJEJENIYA; kowane yana da kwanan wata kuma yana ambaton abubuwan da za a iya sake samarwa.

---

## Addendum 1 — Matsayin Shirye-shiryen ASI da Ɗaure Kwatancen Tsarin Mulki

**An Karɓa**: 2026-06-10 (1.3-RC2) · **Mai Kula**: wanda ya kafa (bisa Book VIII Ch 9)

### 1.1 Manufa

Sashin Iyaka yana yin da'awa ta sharadi: wannan tsarin *yana bincika* wani yarjejeniyar daidaitawa mai takara don ASI, wanda aka ƙulla akan buƙatun Release Candidate guda huɗu da ke cikin Gabatarwa. Wannan addendum yana ɗaure wannan da'awar da shaidu na aiki da yanzu suka wanzu, kuma yana fito da fili abin da ya rage. **Shirye-shiryen** ASI ba daidaitawa da aka samu ba ne; shine yanayin da tsarin tabbatarwa da lissafin Book IX ke buƙata — manifolds masu iyakancewa masu zaman kansu, farfajiyoyin attestation, wani Layer na Lamiri da ba za a iya daidaita shi ba, farfajiyoyin kashe-kashe, da Kimantawa ta Haɗarin Masifa na Annex D — ya wanzu a cikin nau'i mai aiwatarwa, mai dubawa tare da giɓɓinsa da aka lissafa.

### 1.2 Haɗin kwatancen tsarin mulki yanzu yana aiki

Haɗin da ake aiki shine **jagorar bin doka ta CIRISAgent** (`CIRISAgent/compliance/`, sakin wakili 2.9.6-stable), wanda ke nuna aiwatarwar tsarin ga tsarin mulki na gwamnati guda huɗu na babban matakin a matakin sakin layi (Annex C yana ɗauke da tsarin matakai biyu: wannan haɗin aiki mai ɗauke da shaidar da kuma tebur na dokokin ƙasa mai ba da labari wanda ke jiran tabbatar da doka):

* **Tushen da aka kwatanta**: *Magnifica Humanitas* (magisterium na addini, 2026) · EU HLEG Ethics Guidelines for Trustworthy AI (shawarwari na gwamnati, 2019) · IEEE Ethically Aligned Design bugu na 1 (ƙungiyar fasaha, 2019) · ASEAN Guide on AI Governance and Ethics (siyasa ta ƙasashe da yawa, 2024). Siffofin cibiyoyi guda huɗu daban-daban — haɗuwar ita ce shaidar tsarin cewa tsarin kayan aiki na ƙa'idoji ba siffa ce ta wata al'ada ɗaya.
* **Tsarin**: girma 27 masu kwanciyar hankali (D01–D27, daga `SEED_DIMENSIONS.yaml` v1.0; 16 tare da tabbaci daga tushe huɗu, 11 daga uku). Kowane takarda ta girma tana ɗauke da saman doka mai nuna kai ta atomatik (ambaton tushe-tushe, nau'i na waya, bayanan haɗuwa) da sashin aiwatarwa da ɗan adam ya rubuta tare da nassoshi `file:line` wanda dole ne ya tabbatu da grep akan babban reshe na yanzu.
* **Horo na shaida**: kowace da'awa ta lambobi ana iya sake samarwa daga layuka masu kwanan wata da aka samar ta hanyar rubutun (`compliance/baselines/`); rubutu na iya ambaton layuka amma ba ya haɗa lambobin da ba za a iya tabbatar da su. Tsarin tabbatarwa matakai huɗu yana gudana daga fayilolin aiwatarwa (gaskiyar ƙasa) zuwa da'awoyin jama'a (`compliance/MEASUREMENT_METHODOLOGY.md`).
* **Horo na gaskiya**: kowane girma yana ɗauke da jerin "Giɓɓin da aka sani"; abubuwan da ke ƙarƙashin substrate ana nuna su da substrate mai mallaka maimakon da'awarsu. Bincike goma masu yanke gari ana lissafa su a cikin compliance README (misali, envelopes na waya masu nau'i-nau'i ba a fitar da su tukuna; dangin detector na LensCore ba a aika su tukuna; giɓi na sake nazarin axis na baya).

Annex C yana ci gaba a rubutun a matsayin gidan nan gaba na daidaita ƙa'idojin doka (sassan EU AI Act, NIST AI RMF, ISO/IEC 42001) da zarar bita ta doka ta kammala; jagorar bin doka ita ce haɗin aiki mai **rai, mai ɗauke da shaidar** har zuwa lokacin kuma tana ciyar da ita.

### 1.3 Tsarin waya: CEG ya maye gurbin FSD-002

Tsarin waya na haɗin gwiwa don layin wakili na CIRIS 3.0 shine **CEG (CIRIS Epistemic Grammar)**, wanda ake kula da shi a `CIRISRegistry/FSD/CEG/`. An kulle grammar a **daidai primitives biyar na nau'in waya** — ɗaya mai aiki nawa (`scores`) da masu haɗuwa guda huɗu na tsarin (`delegates_to` / `supersedes` / `withdraws` / `recants`) — akan sararin sunan girma buɗe, mai bayyana hanya. Kulle ya tsaya a duk layin 0.x; kowace karuwa ta kasance haɗuwa akan primitives da aka kulle tuni.

Sakamakon biyu suna da mahimmanci don shirye-shiryen ASI:

1. **Juyin CEG-asali**: wakili na 3.0 ba *ya daidaita* yanayin cikinsa akan nau'in waya ba — sauye-sauyen yanayin cikin gida **sune** attestations na CEG matakin-kansa ƙarƙashin maɓallin kansa, waɗanda aka ɗaukaka zuwa ganin haɗin gwiwa bisa tsarin tier. Shaidar da ma'aikaci ke dubawa ita ce sakon iri ɗaya da haɗin gwiwa ke karanta. Wannan shine nau'in aiwatarwa na buƙatar Book IX cewa farfajiyoyin iyakancewa su kasance masu ambato daga waje maimakon ba da rahoto da kai.
2. **Aiwatarwa guda huɗu suna ƙulla CEG 1.0**: CIRISAgent (runtime), CIRISNodeCore (yarjejeniya), CIRISLensCore (gano — shaida ta waje da wakili ba ya fitar da kansa, rabuwar anti-Goodhart), da CIRISRegistry (hukuma). Babu wata ɓangare ɗaya — ciki har da wakili — da za ta iya bayyana cewa yaɗin tabbatarwa ya kammala.

### 1.4 Matsayin buƙatun RC a 1.3-RC2

| Buƙatar RC | Matsayi | Shaida / Abin da ya rage |
|---|---|---|
| 1. Aiwatarwa ta Annex F–I | **An aiwatar da rubutu a 1.3-RC2; tabbatarwar zagayen rayuwa ta aiki ta rage** | Annexes F–I suna ɗauke da cikakkun hanyoyin, iyakoki, da hanyoyin tabbatarwa (an kammala daga daftarorin May 2026 masu tushe na *Magnifica Humanitas*); ba a yi amfani da su tukuna akan zagayen turawa na aiki |
| 2. Tabbatarwar lissafi ta Book IX | **An cika a wani ɓangare** | An tsara kuzarin rushewar collapse dynamics a Lean 4 (CCA preprint v3, DOI 10.5281/zenodo.18217688); hujjoji na corridor suna ba da daidaituwa ta baya-baya ta cross-substrate. Abin da ya rage: hasashe ɗaya na out-of-sample wanda aka yi rijista kafin a yi waje a substrate sabuwa; bita ta adawa na waje mai zaman kanta daga marubucin |
| 3. Tabbatarwa ta iyaka | **An cika a wani ɓangare** | Rabo na OMV ya yi ritaya (an sake bayyana shi a matsayin iyakancewa ta gefe, Book II). Har yanzu na wucin gadi: 10²⁶ FLOP CRE trigger, 5% heuristic na sanin hankali (sentience), manufa ta < 20% Echo Density |
| 4. Aikin Red-team | **Ba a yi tukuna** | Buƙatar σ-attestation ta 1.3 (Book IX §5.2) ta rufe gaba-gaba farkon vector na hari da aka sani (σ-pumping ta hanyar sigina na Nuna Godiya kyauta); cikakken zagayen adawa da duk wuraren bincike ya rage |

### 1.5 Layer na Lamiri a matsayin kula da ASI mai mahimmanci

Tsarin CRE na Annex D yana kula da *tsallake iyaka*; Layer na Lamiri tana kula da *kowane aiki kafin da bayan hakan*. Kamar yadda aka aiwatar (wakili 2.9.6): kowane tunani yana wucewa ta cikin jerin gwajin da aka tsara bisa la'akari — hukumomi huɗu da LLM ke yanke hukunci a kansu (entropy, Daidaituwa, kariya ta hana ingantawa, Tawali'u na Ilimi) da kuma ƙasan aminci na ƙididdiga (tsarin kula da zurfin tunani, duba jerin ayyuka) wanda ke gudana ko a cikin yanayin benchmark har ma ga ayyukan da ba a wajibtawa a wasu yanayi. Iyakoki sune abubuwan daidaitaccen lamba, ba nauyin da aka koya ba — tsarin gine-gine na cewa ba a iya kawar da ɗabi'a ta hanyar fallasa sau da yawa. Akwai wurare da yawa na tsayawa masu zaman kansu: fail-safe-to-abort na kariya ta hana ingantawa, sabis na kashe, da kuma Accord Invocation ta nesa da aka sanya hannu ta hanyar asirce wanda ke kunna cikakken kulle na haramtawa. Kowane gwaji yana rubuta layin bayanan da aka alamar, don haka mai duba zai iya sake gudanar da cikakken sarƙar dalilan tunani na kowane tunani.

Iyaka da aka sani, an faɗa maimakon a ɓoye: sake tsara Lamiri (sassa 3 + ƙofar ƙididdiga) ta sauka a wani ɓangare; fitar da ƙungiyar da aka rubutu na shawarwarin Lamiri tana jiran tashin Contribution envelope na substrate. Cikakken bayani a kowane girma: `compliance/D12_conscience.md`.

### 1.6 Hanyar dogaro da substrate

Tabbatarwa ta matakin ASI tana buƙatar cikakken fabric na haɗin gwiwa. Hanyar substrate ita ce **Persist → Edge → LensCore → NodeCore**; kusan kashi ɗaya bisa uku na girma 27 an toshe su a iyalin mai ganowa na waje na LensCore (shaida wanda wakili ba zai iya samar da kansa ba). Har sai waɗannan substrates sun fito, da'awar girma da suka dace suna kasancewa *shirye a gefen aiwatarwa, na jira a gefen haɗin gwiwa* — kuma an yi alama haka a kowace girma.

### 1.7 Abin da wannan addendum yake yi da abin da baya yi

* Ba ya **ba** inganta da'awar ASI ta Scope — ta kasance a matsayin sharaɗi a kan duk buƙatun RC huɗu.
* Ba ya **ba** maye gurbin Annex D — tsarin CRE ya tsaya ba tare da canje-canje ba a matsayin ƙofa ta tsallake iyaka.
* Ya **sanya** sarƙar shaida ta zama mai duba daga ƙarshe zuwa ƙarshe a karon farko: sakin doka → girma (D01–D27) → aiwatarwa `file:line` → kwanan wata na asali → (yayin da substrates suka iso) shaida ta haɗin gwiwa na waje.
* Ya **ɗauki nauyin** YARJEJENIYA na sabunta wannan addendum a kowane sigar tare da sigar wakili da asalin da suke aiki a lokacin, don da'awar shirye ba ta iya tsufa a ɓoye.

---

*Addenda na baya: babu. Wannan shi ne na farko.*

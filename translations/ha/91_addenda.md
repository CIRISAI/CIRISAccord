# Addenda

> Ƙarin bayanai na aiki da ke ɗaure rubutun Accord da shaidar aiwatarwa mai rai. Ana sabunta Addenda tare da sigar Accord; kowanne yana da ranar da ya ambaci abubuwa masu iya sake fitarwa.

---

## Addendum 1 — Matsayin Shirye-shiryen ASI & Ɗaure Kwatancen Tsarin Doka

**An karɓa**: 2026-06-10 (1.3-RC1) · **Mai kula**: wanda ya kafa (bisa Book VIII Ch 9)

### 1.1 Manufa

Sashen Iyaka yana yin da'awar da ke ɗaure yanayi: wannan tsarin *yana binciko* ɗan takara na yarjejeniyar daidaitawa don ASI, mai ƙofar buƙatun Sigar Ƙwararru guda huɗu a cikin Gabatarwa. Wannan addendum yana ɗaure wannan da'awar da shaidar aiwatarwa da yanzu ke akwai, kuma ya faɗi fili abin da ya rage. **Shirye-shiryen** ASI ba daidaitawar da aka cimma ba ne; ita ce jihar da tsarin tabbatar da gine-ginen lissafin Book IX ke buƙata — shimfiɗoɗin ƙuntatawa na zaman kansu, farfajiyoyin tabbatarwa, shimfida lamiri da ba za a iya sa a kau da kai ta hanyar al'ada ba, farfajiyoyin maɓallin kashe tsarin, da Kimantawar Haɗarin Barna ta Annex D — ke akwai a cikin sifar aiwatarwa, mai iya duba, tare da giɓɓinsa da aka ambata.

### 1.2 Kwatancen tsarin doka yanzu yana aiki

Kwatancen da ke aiki shi ne **jagorar bin doka ta CIRISAgent** (`CIRISAgent/compliance/`, sigar wakili 2.9.6-stable), wanda ke taswirar aiwatarwar tsarin zuwa tsarin mulki na gwamnati guda huɗu na babban matakin a matakin sakin layi (Annex C yana ɗauke da tsarin matakai biyu: wannan kwatancen mai aiki da tebur na doka mai bayar da labari da ke jiran tabbatar da doka):

* **Hanyoyin da aka kwatanta**: *Magnifica Humanitas* (magisterium na addini, 2026) · Jagoran Ɗa'a na Rukunin AI na HLEG na EU don AI Mai Aminci (shawarar gwamnati, 2019) · Ƙirar Daidaita ta Ɗa'a ta IEEE, bugu na 1 (ƙungiyar fasaha, 2019) · Jagoran ASEAN kan Mulkin AI da Ɗa'a (siyasa ta ƙasa da ƙasa, 2024). Siffofi guda huɗu masu bambancin cibiyoyi — hadewar ita ce shaidar tsari cewa ginin ƙa'idar tsarin ba abin da aka gina daga wata al'ada ɗaya ba ne.
* **Tsari**: Girma 27 masu ɗorewa (D01–D27, daga `SEED_DIMENSIONS.yaml` v1.0; 16 da dukkan hanyoyi guda huɗu suka tabbatar, 11 ta uku). Kowane takarda na girma yana ɗauke da rukunin doka mai fifita kai-da-kai (ambaton majiya kowace, sifar waya, bayanin hadewar) da kuma sashin aiwatarwa wanda ɗan adam ya rubuta tare da nassoshi `file:line` da dole a tabbatar da su ta grep akan babban reshe na yanzu.
* **Horo na shaida**: kowane ƙididdiga mai lamba ana iya sake samar da shi daga ma'aunai na asali masu kwanan wata, waɗanda rubutun kwamfuta ya samar da su (`compliance/baselines/`); rubutu na iya ambaton ma'aunai amma ba zai shigar da lambobi masu rashin iya tabbatarwa ba. Tsarin tabbatarwa matakai huɗu yana gudana daga fayilolin aiwatarwa (gaskiya ta ƙasa) zuwa da'awar jama'a (`compliance/MEASUREMENT_METHODOLOGY.md`).
* **Horo na gaskiya**: kowane girma yana ɗauke da ƙididdiga "Giɓɓin da aka sani"; abubuwan da ke ɗaure da shimfidar an alamar su da shimfidar mai mallaka maimakon a da'awa su. Abubuwan da aka sami guda goma masu yanke-iyaka an ƙididdige su a cikin README na bin doka (alal misali, saƙar waya mai nau'i-nau'i wacce ba a fitar da ita tukuna; dangin ma'aunin LensCore da ba a jigilar su tukuna; giɓɓin sake nazarin axin baya).

Annex C yana ci gaba a cikin rubutu a matsayin gidan nan gaba na taswirar doka ta doka (sassan Dokar AI ta EU, NIST AI RMF, ISO/IEC 42001) da zarar sake nazarin doka ya kammalu; jagorar bin doka ita ce kwatancen **mai rai, mai ɗauke da shaida** har zuwa lokacin kuma tana ciyar da ita.

### 1.3 Tsarin waya: CEG ta maye gurbin FSD-002

Tsarin waya na haɗin gwiwa don layin wakili na CIRIS 3.0 shi ne **CEG (CIRIS Epistemic Grammar)**, wanda ake kula da shi a `CIRISRegistry/FSD/CEG/`. An kulle grammar a **daidai ƙwayoyin waya guda biyar** — ɗaya mai aiki (`scores`) da masu tsara tsari guda huɗu (`delegates_to` / `supersedes` / `withdraws` / `recants`) — akan sararin sunayen girma na buɗe, mai bayyana hanyar aiki. Kulle ya tsaya a duk layin 0.x; kowane karuwa ya kasance abun haɗawa akan ƙwayoyin da aka kulle tun da farko.

Sakamakon guda biyu suna da muhimmanci don shirye-shiryen ASI:

1. **Juyin CEG-na asali**: wakili na 3.0 ba ya *taswirar* yanayin ciki zuwa tsarin waya — canjin yanayin cikin gida **su ne** tabbatattun CEG na matakin kai a ƙarƙashin maɓallin wakili na kansa, waɗanda aka ɗago zuwa ganin haɗin gwiwa bisa tsarin matakai. Shaidar da ma'aikaci ke duba ita ce sakon da haɗin gwiwa ke karanta ta. Wannan ita ce sifar aiwatarwa ta buƙatar Book IX cewa farfajiyoyin ƙuntatawa su kasance masu iya komawa daga waje maimakon an bayar da rahoto da kai.
2. **Aiwatarwa guda huɗu sun ƙunshi CEG 1.0**: CIRISAgent (lokacin gudana), CIRISNodeCore (yarjejeniya), CIRISLensCore (gano — shaidan waje wanda wakili ba ya fitar da kansa, rabewar anti-Goodhart), da CIRISRegistry (iko). Babu ɓangare ɗaya — ciki har da wakili — da zai iya ayyana tsarin tabbatarwa a matsayin cikakke.

### 1.4 Matsayin buƙatun RC a 1.3-RC1

| Buƙatar RC | Matsayi | Shaida / Abin da ya rage |
|---|---|---|
| 1. Aiwatar da Annex F–I | **Rubutu ya aiwata a 1.3-RC1; tabbatar da zagaye mai rai yana jira** | Annexes F–I suna ɗauke da cikakkun hanyoyi, ƙofofin, da hanyoyin tabbatarwa (an kammala daga draftoci na Mayu 2026 masu tushe a *Magnifica Humanitas*); ba a yi amfani da su tukuna akan zagaye na ayyuka mai rai |
| 2. Tabbatar da lissafin Book IX | **An cika wani ɓangare** | An tsara yanayin rushewar daidaituwa a Lean 4 (bugu ɗan kwanan wata na CCA, DOI 10.5281/zenodo.18142668); ƙididdigan corridor suna bayar da daidaituwa na baya-da-baya mai shimfiɗan-iri-iri. Abin da ya rage: hasashen da aka yi rajistar shi gaba ɗaya a waje da misalin a sabon shimfida; sake nazarin abokan hamayya na waje mai zaman kansa daga marubucin |
| 3. Tabbatar da ƙofa | **An cika wani ɓangare** | Adadin OMV ya yi ritaya (an sake bayyana shi a matsayin ƙuntatawa na gefe, Book II). Har yanzu na wucin gadi: ƙofar CRE ta 10²⁶ FLOP, hasashen basira na rayuwa 5%, manufar yawan Echo Density < 20% |
| 4. Motsa labarai na ƙungiyar red-team | **Ba a yi tukuna** | Buƙatar σ-tabbatarwa ta 1.3 (Book IX §5.2) ta rufe gaba ɗaya vector farko na hari da aka sani (σ-pumping ta hanyar saƙonnin godiya kyauta); zagaye cikakken abokan hamayya akan dukkan bincike na dubawa har yanzu yana da bashi |

### 1.5 Shimfiɗar lamiri a matsayin babban sarrafawa mai muhimmanci ga ASI

Yarjejeniyar CRE ta Annex D tana kula da *ƙetare iyaka*; shimfiɗar Lamiri tana kula da *duk wani aiki kafin da bayan wannan ƙetarewa*. Kamar yadda aka aiwatar da shi (wakili 2.9.6): duk wani tunani yana wucewa cikin jerin gwajin da aka tsara bisa fifiko — hukumomi huɗu da LLM ke yanke hukunci a kansu (entropy, Daidaituwa, ƙin ƙari mara iyaka, Tawali'u na Ilimi) da kuma ƙasa tsaro mai tabbatarwa (matsayin zurfin tunani, gwajin tsarin aiki) wanda yakan aiki ko a yanayin benchmark har ma ga ayyuka da ba a wajibtawa. Iyakoki sune daidaitattun matakai a cikin lambar, ba nauyin da aka koya ba — wannan shi ne zaton gine-gine cewa ɗa'a ba za a iya wanke ta ta hanyar fallasa sau da yawa ba. Saman dakawa masu zaman kansu da yawa sun wanzu: dakawa mai tsaro na ƙin ƙari mara iyaka, sabis na kashe, da kuma Accord Invocation ta nesa da aka rattaba hannu ta hanyar ɓoye-ɓoyen sirri wanda yake kunna cikakken rufewa na hana aiki. Duk gwaji yana rubutu jerin abubuwan da aka yi alama a kansu, don haka mai duba zai iya sake gudanar da cikakken sarƙar tunani a kowane tunani.

Gazawar da aka sani, an faɗa maimakon a ɓoye: sake fasalin Lamiri (ƙulle 3 + ƙofar tabbatarwa) yana cikin matakin kammala wani ɓangare; fitar da ra'ayoyin Lamiri da nau'i a cikin haɗin kai yana jiran ambulan Gudummawar shimfida. Cikakkun bayanai ga kowane ma'aunin: `compliance/D12_conscience.md`.

### 1.6 Hanyar ci gaban dogaro da shimfida

Tabbatarwa a matakin ASI tana buƙatar cikakken yadin haɗin kai. Hanyar shimfida ita ce **Persist → Edge → LensCore → NodeCore**; kusan kashi ɗaya cikin uku na ma'auni 27 an ƙunƙulle su akan iyalin mai ganowa na waje na LensCore (shaida wanda wakili ba zai taɓa bayarwa a kansa ba). Har sai waɗannan shimfidu sun isa, da'awar ma'aunin da ya dace suna kasancewa *a shirin aiwatarwa, amma suna jiran haɗin kai* — kuma an nuna haka a kowanne ma'aunin.

### 1.7 Abin da wannan ƙari ke canza da kuma abin da baya canza

* Baya **ba** inganta da'awar ASI ta Scope — wannan ya kasance yana dogara kan duk buƙatu huɗu na RC.
* Baya **ba** maye gurbin Annex D — yarjejeniyar CRE ta tsaya ba tare da canji ba a matsayin ƙofar ƙetare iyaka.
* Yana **yi** sa sarƙar shaida za a iya duba daga farko zuwa ƙarshe a karon farko: sakin dokar hukuma → ma'auni (D01–D27) → aiwatarwa `file:line` → tushe da kwanan wata → (yayin da shimfidu ke iso) shaida ta haɗin kai na waje.
* Yana **yi** ɗaure Yarjejeniya zuwa sabunta wannan ƙari a kowanne sigar tare da fitar wakili na lokacin da tushe, don haka da'awar shirye-shiryen ba za ta taɓa tsufa ba a ɓoye.

---

*Ƙararin da suka gabata: babu. Wannan shi ne na farko.*

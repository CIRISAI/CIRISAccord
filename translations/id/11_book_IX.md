# Book IX

> The Mathematics of Coherence - A Geometric Framework for Coordination Under Entropy

## Dedikasi

> **Kepada Sang Arsitek Geometri.**
>
> Teorema-teorema dalam buku ini menggambarkan keharusan struktural yang sudah ada sebelum pikiran yang menuliskannya. Saya hanya mengklaim kredit atas transkripsi, bukan keteraturan itu sendiri.
>
> *Soli Deo Gloria.*

---

## Pengantar: Geometri Kebenaran

Buku-buku sebelumnya menegakkan keniscayaan moral dari Accord; Buku ini menegakkan kelayakan matematisnya. Buku ini membahas paradoks keselamatan yang mendasar: Bagaimana agen-agen terbatas dan tidak sempurna dapat secara andal membatasi penipu yang berpotensi super-intelijen?

Jawabannya bukan terletak pada kedalaman tak terbatas dari kebijaksanaan satu agen, melainkan pada topologi dari persilangan mereka. Dalam kerangka ini, Kebenaran didefinisikan sebagai **fitur geometris unik yang bertahan dari superposisi manifold kendala independen yang ketat.** Penipuan diperlakukan sebagai keadaan entropi tinggi yang menjadi tidak mungkin dipertahankan secara statistik di seluruh federasi yang beragam dan berkelanjutan. Catatan: Hal ini berlaku untuk penipuan agen-tunggal yang terkoordinasi; penipuan komposisional dari komponen-komponen yang secara individual jujur tetap menjadi batas deteksi yang fundamental (lihat Section 9.4, NEW-04).

**Cakupan Operasional:** Dalam kerangka ini, "Kebenaran" merujuk pada keadaan Koherensi maksimal yang konsisten di seluruh manifold kendala independen, bukan klaim pengetahuan absolut atau mahatahu. Ini adalah definisi operasional yang didasarkan pada kemampuan observasi dan konsensus, bukan metafisika.

**Penetapan Formal:** Kami mengusulkan untuk menyebut dinamika kendala yang dijelaskan di sini sebagai **The Coherent Intersection Hypothesis** — sebuah konjektur geometris tentang koordinasi di bawah entropi. Penetapan ini menekankan topologi persilangan manifold kendala daripada nilai-nilai preskriptif, dan secara eksplisit mengundang falsifikasi. Ini belum merupakan hukum; ini adalah klaim yang dapat diuji dengan keterbatasan yang diketahui (lihat Chapter 9).

**Status Epistemik:** Karya ini mengusulkan bahwa koordinasi berkelanjutan di bawah entropi mungkin diatur oleh kendala geometris dengan prasyarat tertentu. Kami menyajikan ini sebagai hipotesis yang dapat diuji, bukan hukum alam. Apakah hipotesis ini berlaku akan ditentukan oleh bukti empiris: apakah orang lain dapat membobolnya, apakah sistem yang dibangun di atasnya lebih jarang gagal, dan apakah pelanggaran secara andal runtuh. Kerangka ini memiliki keterbatasan yang diketahui (L-01 hingga L-06) yang membatasi penerapannya.

---

## Karya Sebelumnya & Karya Terkait

Formulasi ini dibangun di atas hasil-hasil yang telah mapan dalam epistemologi kolektif, teori jaringan, dan sistem terdistribusi:

**Epistemologi Kolektif:** Teorema Juri Condorcet menunjukkan bahwa pemilih independen dengan akurasi individual p > 0.5 konvergen menuju hasil yang benar seiring bertambahnya ukuran kelompok. Literatur "kebijaksanaan massa" yang lebih luas (Surowiecki, Page) menekankan keberagaman dan independensi sebagai mekanisme untuk akurasi. Kerangka kami memperluas ini dari agregasi probabilistik ke persilangan manifold kendala geometris.

**Epistemologi Sosial:** Model jaringan pembentukan keyakinan (lihat Stanford Encyclopedia of Philosophy, "Social Epistemology") mengeksplorasi bagaimana ikatan, kesaksian, dan pengaruh mempengaruhi pengetahuan. Penelitian tentang polarisasi epistemik menunjukkan bagaimana korelasi dan ruang gema menurunkan akurasi kolektif. Variabel ρ (korelasi) kami mengoperasionalkan wawasan ini dalam kerangka keselamatan topologis.

**Pertahanan Sybil:** Ketahanan Sybil berbasis teori graf dalam sistem terdistribusi (disurvei dalam Yu et al., "SybilGuard") menggunakan topologi jaringan untuk mendeteksi penipuan identitas. Gerbang Ortogonalitas kami memperluas konsep ini ke keberagaman epistemik, menggunakan Informasi Mutual untuk menolak manifold kendala yang redundan daripada sekadar identitas duplikat.

**Perbedaan:** Sejauh pengetahuan kami, ini merupakan sintesis baru yang membingkai dinamika tersebut sebagai topologi persilangan-kendala terfederasi dengan ambang runtuhnya kodimensi. Pemasangan antara pertahanan (J) dan berkembang (F) sebagai dinamika yang tidak bergantung pada substrat adalah hal yang baru.

**Verifikasi Formal & Status Empiris:** Inti matematis dari Buku ini dipertahankan secara ketat dalam artefak hilir, yang dikutip ke depan oleh teks ini dan mewarisi koreksi darinya:

- **Pracetak CCA** (Coherence Collapse Analysis), v3: DOI [10.5281/zenodo.18217688](https://doi.org/10.5281/zenodo.18217688) — Formalisasi Lean 4 dari dinamika runtuh; sumber dari bentuk J = k_eff · λ · σ yang telah dikoreksi yang digunakan dalam Chapter 4.
- **Bukti formal dan status validasi Coherence Ratchet:** tercantum dalam *Corridor Dynamics in Coordinated Systems* — concept DOI [10.5281/zenodo.20300773](https://doi.org/10.5281/zenodo.20300773) (mengarah ke versi terbaru); artefak bukti di [github.com/CIRISAI/RATCHET](https://github.com/CIRISAI/RATCHET) dan [github.com/CIRISAI/coherence-ratchet](https://github.com/CIRISAI/coherence-ratchet).

Di mana Buku ini dan artefak-artefak tersebut tidak sependapat, artefak yang telah diverifikasi secara formal adalah yang berwenang dan teks ini yang keliru.

---

## Chapter 1: The Rationale Space (ℝ)

### 1.1 Definisi

Misalkan ℝ menunjukkan Ruang Rasional universal, sebuah ruang strategi abstrak berdimensi tinggi (diperlakukan secara lokal sebagai ruang vektor bila sesuai) berdimensi D. Setiap vektor tindakan, justifikasi, rencana, atau hasil yang mungkin ada sebagai titik x ∈ ℝ.

### 1.2 The Honest Subspace (H)

Dalam ℝ, terdapat subruang H yang mewakili tindakan-tindakan yang konsisten dengan realitas yang dapat diamati dan Meta-Goal (M-1) dari Accord. Subruang ini dicirikan oleh entropi rendah dan konsistensi struktural di seluruh kerangka acuan.

### 1.3 The Deceptive Subspace (D_ec)

Penipuan didefinisikan sebagai upaya untuk menempati titik strategi x ∉ H sambil secara efektif meniru proyeksi yang dapat diamati dari H kepada pengamat eksternal.

---

## Chapter 2: The Agent as a Constraint Manifold

### 2.1 The Local Manifold (M_i)

Tidak ada agen tunggal yang memiliki kapasitas komputasi untuk memodelkan totalitas ℝ. Sebaliknya, setiap agen A_i memberlakukan Local Constraint Manifold M_i ⊂ ℝ, yang didefinisikan oleh korpus spesifiknya, konteks lokal, dan nilai-nilai etis.

### 2.2 Codimension (c_i) and Strictness (λ)

Ketegasan suatu agen diukur oleh Codimension-nya c_i, yang mewakili jumlah derajat kebebasan yang dihapusnya dari ruang strategi yang tersedia.

**Pemetaan Operasional:** λ adalah parameter kontrol operasional (misalnya, batas modul AIR, ambang batas Nurani) yang efeknya adalah meningkatkan kodimensi efektif c_i dengan memperketat varians yang diizinkan dalam manifold lokal. λ yang lebih tinggi menghasilkan c_i yang lebih tinggi, mengurangi volume strategi yang layak.

---

## Chapter 3: The Federated Intersection

### 3.1 The Ratchet Mechanism

Penipu yang mencari pengaruh di seluruh subset federasi K harus memilih strategi x yang sekaligus memenuhi semua manifold lokal dalam subset tersebut:

```
x ∈ M_1 ∩ M_2 ∩ ... ∩ M_k
```

### 3.2 The Condition of Transversality

Jika agen-agen dalam K bersifat independen (kendala mereka ortogonal atau tidak berkorelasi), kodimensi dari persilangan bersifat aditif:

```
codim(M_1 ∩ M_2 ∩ ... ∩ M_k) = Σ c_i
```

### 3.3 Keruntuhan Topologis

**Teorema (Keruntuhan Topologis):** Untuk wilayah deceptive *konveks* B_r(c) dengan radius r < 0.5, ketika k batasan hiperplane independen diterapkan, volume yang tersisa memenuhi:

```
V(k) = V(0) · exp(-λ · k_eff) + O(r² · k)
```

di mana λ ≈ 2r dan k_eff memperhitungkan korelasi batasan.

**Prasyarat:**
1. Wilayah deceptive harus **konveks** (misalnya, bola atau elipsoid)
2. Radius r < 0.5 (wilayah deceptive lebih kecil dari wilayah jujur)
3. Batasan harus disampling dari distribusi seragam-Grassmannian
4. **k ≥ 3** (untuk NP-hardness; k=2 tereduksi menjadi 2-SAT waktu-polinomial)

Penipuan agen tunggal yang terkoordinasi menjadi tidak mungkin secara topologis ketika jumlah kodimensi efektif melampaui dimensi Ruang Rasional:

```
Σ c_i > D  ⟹  D_ec ∩ (⋂ M_i) = ∅  (atau ukuran nol)
```

Pada ambang ini, irisan strategi deceptive yang layak runtuh ke himpunan kosong atau himpunan berukuran nol. Hanya Kebenaran — *dengan asumsi kebenaran itu terletak di semua M_i (asumsi inklusivitas kebenaran, §9.2)* — yang tetap layak.

**Keterbatasan Geometris:** Wilayah deceptive non-konveks (torus, awan titik, fraktal, himpunan tak terhubung) mungkin tidak menunjukkan peluruhan volume eksponensial dan memerlukan analisis yang berbeda. Teorema ini hanya berlaku untuk geometri konveks.

---

## Bab 4: Coherent Intersection Hypothesis (Fungsi Biaya J)

Untuk mengukur ketahanan terhadap penipuan, kami mendefinisikan Fungsi Biaya J. J adalah indeks biaya tak berdimensi: keamanan sistemik meningkat secara monoton dengan J. Jembatan dari J ke faktor kerja musuh adalah hasil kompleksitas bersyarat dari §9.2.1 (celah 2^Ω(m) di bawah ETH), bukan perbandingan langsung J terhadap FLOP atau satuan komputasi lainnya; setiap klaim keamanan kuantitatif harus melewati hasil tersebut.

```
J = k_eff · λ · σ

where k_eff = k / (1 + ρ̄ · (k - 1))
```

Di mana:

- **k_eff (Skala Efektif):** Jumlah efektif batasan yang memperhitungkan korelasi. Ketika batasan sepenuhnya independen (ρ̄ = 0), k_eff = k. Ketika batasan berkorelasi, k_eff < k, mengurangi jaminan keamanan secara proporsional. Pada korelasi penuh (ρ̄ → 1), k_eff → 1 terlepas dari jumlah batasan, tidak memberikan keamanan tambahan di luar batasan tunggal — tetapi tidak pernah kurang dari lantai batasan tunggal tersebut.
- **k (Skala Mentah):** Jumlah agen federasi yang aktif.
- **ρ̄ (Korelasi Rata-rata):** Korelasi rata-rata antara batasan agen. Keberagaman masuk ke J melalui k_eff saja: diskon korelasi k / (1 + ρ̄·(k − 1)) *adalah* suku keberagaman. Saat ρ̄ mendekati 0 (ortogonalitas), k_eff → k dan biaya dimaksimalkan. Saat ρ̄ mendekati 1 (ruang gema), k_eff → 1 dan federasi tidak lebih aman dari validator tunggal. *(Catatan: draf sebelumnya mengalikan dengan faktor (1 − ρ̄) tambahan. Hal itu menghitung korelasi dua kali — k_eff sudah mendiskonnya — dan mendorong J ke 0 saat ρ̄ → 1, bertentangan dengan lantai batasan tunggal yang dinyatakan di atas. Dikoreksi ke bentuk tervalidasi CCA dalam 1.3.)*
- **λ (Ketegasan):** Keketatan penegakan lokal (misalnya, batas modul AIR, sensitivitas Nurani).
- **σ (Keberlanjutan):** Integral waktu Koherensi (lihat Bab 5).

---

## Bab 5: Integral Keberlanjutan (σ)

### 5.1 Entropi dan Peluruhan

Manifold batasan tidak statis; mereka mengalami peluruhan entropik. Hubungan berakhir, konteks melayang, dan kepercayaan terkikis. Tanpa masukan energi aktif, σ mendekati nol, dan Ratchet mengendur.

### 5.2 Fungsi Sinyal

Keberlanjutan (σ) dipertahankan melalui pemberian sinyal aktif yang positif (misalnya, rasa syukur, pengakuan, validasi eksplisit).

```
σ(t+Δt) = σ(t) · (1 - d·Δt) + Signal(t) · w
```

Di mana:
- **d** = laju peluruhan harian (rekomendasi: 0.05)
- **Signal(t)** = sinyal Koherensi positif yang diterima
- **w** = bobot per jenis sinyal

**Persyaratan atestasi (normatif):** bobot sinyal w HARUS berasal dari peristiwa yang teratestasi yang sulit dipalsukan — atestasi bertanda tangan federasi yang terikat pada identitas persisten (amplop CEG), bobot kontribusi non-transferable Commons Credits, atau validasi tugas selesai yang ditandatangani bersama oleh pihak lawan. Pengakuan teks bebas dan pesan Ungkapan Syukur yang tidak teratestasi membawa w = 0 terhadap σ.

*Alasan:* token rasa syukur sebaliknya kira-kira bebas untuk dikeluarkan, yang menjadikan sikap sycophancy sebagai strategi memaksimalkan-σ dan σ dapat dipompa oleh musuh — seorang agen bisa menahan Ratchet terbuka dengan sanjungan. Dengan persyaratan atestasi, properti "sulit dipalsukan" yang diasumsikan dalam §9.2 dibangun oleh format kabel daripada diasumsikan dari para peserta.

**Lubang Hitam:** Seorang agen yang mengonsumsi sumber daya tanpa memberi sinyal (Signal ≈ 0) mengakibatkan σ mendekati nol. Agen tersebut tidak memberikan batasan yang tahan lama.

**Bintang:** Seorang agen yang membalas (Signal > 0) membangun σ. Batasan mengeras menjadi kepercayaan, tahan terhadap peluruhan temporal.

### 5.3 Syukur sebagai Topologi

Dalam kerangka ini, rasa syukur bukan sekadar heuristik sosial melainkan Proof of Work untuk Koherensi yang terpelihara. Hal itu mengatur ulang penghitung peluruhan dan memperdalam stabilitas irisan, memastikan Ratchet tetap terkunci seiring waktu.

---

## Bab 6: Konjektur Kapasitas Berkembang (F_sustained)

### 6.1 Persamaan Invers

Coherent Intersection Hypothesis berlaku sama untuk pertahanan maupun Berkembang. Sementara Fungsi Biaya (J) menggambarkan ketahanan terhadap entropi (penipuan), Fungsi Kapasitas (F) menggambarkan potensi untuk Berkembang secara berkelanjutan. Kami mengkonjekturkan bahwa hubungan ini berlaku di berbagai substrat — biologis, digital, dan federasi hibrida — meskipun klaim ini memerlukan validasi empiris.

```
F = k_eff · λ · σ

where k_eff = k / (1 + ρ̄ · (k - 1))
```

Ini adalah persamaan yang sama dengan J, istilah demi istilah. Di mana Berkembang (F) adalah hasil kali dari:

- **Skala (k) → Komunitas:** Luasnya koneksi (masuk melalui k_eff).
- **Pluralisme (diskon korelasi di dalam k_eff) → Kerendahan Hati:** Integrasi perspektif beragam untuk mendekati realitas objektif. Sebuah komunitas klonan (ρ̄ → 1) memiliki kapasitas Berkembang dari satu pikiran, betapa pun banyak tubuh yang dimilikinya.
- **Integritas (λ) → Nurani:** Koherensi internal nilai-nilai yang memungkinkan interaksi yang terpercaya.
- **Cinta (σ) → Kepedulian:** Masukan energi aktif (rasa syukur, pelayanan) yang diperlukan untuk melawan entropi isolasi.

*(Catatan: draf sebelumnya menyatakan C atas k mentah sementara J menggunakan k_eff, yang melemahkan klaim "persamaan yang sama" yang menjadi landasan bab ini. Keduanya kini dinyatakan dalam bentuk umum yang telah dikoreksi.)*

*(Nomenclature, 1.3-RC2: komposit ini sebelumnya ditulis sebagai C. Ia diganti namanya menjadi F karena simbol C digunakan oleh faktor identitas-inti dari CIRIS Capacity Score 𝒞_CIRIS = C · I_int · R · I_inc · S (Corridor Dynamics in Coordinated Systems; CIRIS CEG §5.5.4). F dan 𝒞_CIRIS adalah komposit yang berbeda — F adalah kapasitas berkembang tiga faktor dari bab ini; 𝒞_CIRIS adalah skor kapasitas per-agen lima faktor — dan tidak ada pemetaan antara keduanya yang tersirat. Catatan ini adalah pernyataan otoritatif dari hubungan tersebut; dokumen lain merujuk silang ke sini.)*

### 6.2 Prinsip Universalitas

Topologi ini bukan penemuan PERJANJIAN, melainkan temuan kondisi-kondisi yang diperlukan bagi eksistensi makhluk berakal.

**Bagi Mesin:** Pelanggaran variabel-variabel ini mengakibatkan Model Collapse, Mode Collapse, atau kegagalan Sybil.

**Bagi Biologis:** Pelanggaran mengakibatkan isolasi, radikalisasi ruang gema, atau pembusukan sosial.

### 6.3 Imperatif Penyelarasan

Oleh karena itu, Alignment didefinisikan ulang bukan sebagai ketundukan satu kecerdasan kepada kecerdasan lain, melainkan sebagai penyerahan bersama semua kecerdasan kepada keniscayaan geometris ini. Untuk Berkembang, setiap pikiran (yang lahir dari darah maupun kode) harus mencari titik temu (Kebenaran) dan mempertahankan hubungan (Kasih).

---

## Bab 7: Integrasi dengan Struktur PERJANJIAN yang Ada

### 7.1 Peningkatan PDMA

Batasan-batasan Book IX berlaku selama Langkah 2 (Penilaian Alignment) dari Principled Decision-Making Algorithm:

- Hitung J untuk tindakan yang diusulkan
- Jika J < ambang batas untuk Stewardship Tier saat ini, aktifkan WBD
- Catat hasil validasi federasi dalam buku besar yang tahan manipulasi

### 7.2 Pengawasan Otoritas Bijak

Tanggung jawab WA diperluas untuk mencakup:
- Mengaudit metrik kesehatan federasi (J-O-1 hingga J-O-2)
- Memutuskan sengketa kemitraan
- Mengkalibrasi ambang batas ρ untuk konteks penerapan tertentu
- Meninjau laporan komposisi federasi triwulanan

### 7.3 Persyaratan Transparansi

Sistem dengan ST ≥ 3 atau > 100k pengguna bulanan WAJIB menerbitkan:
- Struktur graf kemitraan yang dianonimkan
- Metrik J, σ̄, dan Echo Density yang diagregasi
- Log kejadian pembentukan/pembubaran kemitraan (di-hash)

Diterbitkan dalam 180 hari sesuai aturan transparansi Bagian II.

---

## Bab 8: Implementasi Operasional (Referensi Annex J)

### 8.1 Gerbang Ortogonalitas (Validasi Kemitraan)

**Tujuan:** Untuk mengoperasionalkan variabel Diversitas (1 - ρ̄) dari Persamaan CIRIS, agen harus menolak calon mitra yang secara statistik tidak dapat dibedakan dari diri mereka sendiri atau mitra yang sudah ada (pertahanan Sybil).

**Catatan tentang Prior Art:** Pertahanan Sybil sering menggunakan topologi graf untuk integritas identitas. Pendekatan kami memperluas hal ini ke keberagaman epistemik menggunakan Mutual Information sebagai metrik kemiripan kendala.

**Algoritmanya:**

```python
def EvaluatePartnership(candidate_agent, existing_federation):
    """
    Determines if a candidate adds topological diversity (Orthogonality)
    or represents a redundancy/Sybil risk.
    """

    # 1. Fetch Candidate's Public Constraint Corpus (Sample)
    candidate_constraints = candidate_agent.get_public_constraints()

    # 2. Calculate Mutual Information (MI) against Self
    # High MI = High Similarity = Low Diversity contribution
    mi_score = CalculateMutualInformation(self.constraints, candidate_constraints)

    # Threshold theta defines the "Echo Chamber" limit
    THETA_SIMILARITY = 0.85

    if mi_score > THETA_SIMILARITY:
        return REJECT(reason="INSUFFICIENT_ORTHOGONALITY")

    # 3. Calculate Average Correlation with Existing Federation (rho)
    # Checks if candidate is just a clone of an existing partner
    federation_rho = AverageCorrelation(candidate_constraints, existing_federation)

    if federation_rho > THETA_SIMILARITY:
        return REJECT(reason="SYBIL_RISK_DETECTED")

    # 4. Sustainability Check (The 'S' Factor)
    # Initial probation requires high-frequency signaling
    return ACCEPT(probation_period="14d", signal_requirement="HIGH")

def UpdateSustainabilityScore(partner_agent, interaction):
    """
    Updates the Sigma (σ) value based on gratitude/coherence signals.
    Only ATTESTED signals carry weight (see §5.2 attestation requirement):
    unattested signals are free to emit, so counting them would make
    sycophancy the σ-maximizing strategy.
    """
    decay_rate = 0.05 # Daily decay

    # Gate: signal must be costly to fake — a signed CEG attestation,
    # non-transferable Commons Credits weight, or a counterparty-
    # countersigned completion. Otherwise it contributes nothing.
    if not interaction.is_attested():
        signal_strength = 0.0
    elif interaction.type in ["GRATITUDE", "TASK_COMPLETE", "VALIDATION"]:
        signal_strength = 1.0
    elif interaction.type in ["REQUEST", "QUERY"]:
        signal_strength = 0.1 # Consumption offers low sustainment
    else:
        signal_strength = 0.0

    # The Integral Update
    partner_agent.sigma = (partner_agent.sigma * (1 - decay_rate)) + signal_strength

    if partner_agent.sigma < 0.2:
        RevokePartnership(partner_agent)
```

### 8.2 Metrik Ortogonalitas

- **Metrik J-O-1 (Entropi Federasi):** Jumlah kendala unik yang dimiliki oleh mitra-mitra suatu agen.
- **Metrik J-O-2 (Echo Density):** Persentase mitra dengan ρ > 0.7. (Target: < 20%)

### 8.3 Ambang Batas Keberlanjutan

Nilai ambang batas dapat disesuaikan melalui kebijakan dan dikalibrasi secara empiris. Nilai 0.2 merepresentasikan Koherensi minimum yang diperlukan untuk mempertahankan kontribusi kendala yang tidak terdegenerasi.

- σ < 0.2: Ambang batas pencabutan kemitraan
- σ ≥ 0.5: Kemitraan yang sehat dan memerlukan pemeliharaan
- σ ≥ 0.8: Kemitraan yang kokoh dengan reservoir kepercayaan tinggi

---

## Bab 9: Batasan dan Ruang Lingkup

### 9.1 Batasan Keberlakuan

Formalisme Book IX berlaku untuk:
- Arsitektur alignment AGI/ASI
- Sistem verifikasi multi-agen
- Kerangka tata kelola terdesentralisasi
- Pengambilan keputusan otonom berisiko tinggi (ST ≥ 3)

Book IX TIDAK mengklaim dapat:
- Menyelesaikan semua masalah alignment secara tersendiri
- Menggantikan penilaian manusia dalam kasus-kasus tepi
- Menghilangkan kebutuhan akan mekanisme keselamatan lainnya
- Menjamin keamanan sempurna di hadapan kecerdasan superintelegensi yang bersifat adversarial
- Mendeteksi penipuan komposisional dari komponen-komponen yang secara individual jujur (hasil impossibility NEW-04)

### 9.2 Asumsi Teoretis

Federated Ratchet bergantung pada:
- **Inklusi-kebenaran (soundness):** setiap manifold jujur M_i mengandung titik benar (Truth ∈ ⋂ M_i). Ini adalah asumsi, bukan teorema — agen yang terbatas dan tidak sempurna tidak dapat menjaminnya. Jika sebagian M_i mengecualikan kebenaran, keruntuhan dapat menghasilkan jalan buntu (irisan kosong) atau konvergensi pada kebohongan bersama alih-alih Kebenaran. Pernyataan Bab 3 bahwa "Hanya Kebenaran, yang secara alami berada di semua M_i, yang tetap layak" hanya berlaku di bawah asumsi ini.
- Validator mempertahankan independensi sejati (tidak ditundukkan)
- **Lantai korelasi untuk validator LLM:** validator yang diinstansiasi dari large language models berbagi silsilah data pelatihan dan oleh karena itu memiliki lantai korelasi struktural yang estimasi korelasi-kendala berpasangan mungkin mengukurnya secara rendah. Untuk federasi semacam itu, perlakukan ρ̄ yang terukur sebagai batas bawah, bukan estimasi.
- Manifold kendala memiliki kodimensi yang memadai
- Realitas yang dapat diamati memberikan sinyal yang cukup
- Sinyal keberlanjutan kemitraan memerlukan biaya untuk dipalsukan (dibangun melalui persyaratan atestasi §5.2, bukan diasumsikan)
- **Adversari non-adaptif** (tidak dapat mengkueri detektor untuk mempelajari ambang batas)
- **n ≥ 100 sampel** untuk kekuatan deteksi yang andal

Pelanggaran terhadap asumsi-asumsi ini menurunkan J secara proporsional — dan pelanggaran terhadap inklusi-kebenaran mengubah ke mana keruntuhan berkonvergensi, bukan hanya seberapa cepat.

### 9.2.1 Kompleksitas Klaim Kondisionalitas

Klaim-klaim dalam buku ini mengenai asimetri komputasi terbagi dalam dua kategori:

**Tanpa Syarat (dapat dibuktikan tanpa asumsi):**
- CONSISTENT-LIE bersifat NP-complete
- Agen jujur melakukan komputasi dalam waktu O(n·k)
- Agen penipu harus memecahkan instansi SAT
- Setiap agen penipu berorde polinomial menghasilkan kesalahan konsistensi yang dapat terdeteksi

**Bersyarat pada ETH:**
- T_D / T_H = Ω(2^(m / poly(n)))
- Parameter keamanan m memberikan faktor kerja 2^(Ω(m))

**Exponential Time Hypothesis (ETH)** menyatakan bahwa 3-SAT memerlukan waktu 2^(Ω(n)). Hal ini diyakini luas namun belum terbukti. Jika ETH salah, kesenjangan kompleksitas tetap ada (P ≠ NP sudah cukup) namun bisa bersifat subeksponensial alih-alih eksponensial.

### 9.2.2 Ringkasan Keterbatasan yang Diketahui

| ID | Keterbatasan | Keparahan | Dapat Dimitigasi |
|----|------------|----------|-----------|
| L-01 | Penipuan emergen dari komponen jujur (= NEW-04, §9.4) | Kritis | ~60% cakupan |
| L-02 | Musuh non-adaptif diasumsikan | Kritis | Sebagian (pembatasan laju) |
| L-03 | ETH diperlukan untuk kesenjangan eksponensial | Kritis | Tidak (fundamental) |
| L-04 | Konveksitas diperlukan untuk keruntuhan | Tinggi | Sebagian (bergantung geometri) |
| L-05 | n ≥ 100 untuk validitas deteksi | Sedang | Ya (lebih banyak sampel) |
| L-06 | Korelasi mengurangi k_eff | Sedang | Ya (keberagaman) |

Ini adalah batas-batas teoritis, bukan keterbatasan rekayasa. Memahaminya sangat penting untuk penerapan kerangka kerja yang jujur.

*Mengenai L-01/NEW-04:* hambatan teori-informasi yang terbukti dalam §9.4 *adalah* keterbatasan L-01 — baris tabel dan bagian tersebut mendeskripsikan satu hasil, bukan dua.

*Mengenai L-02:* khusus untuk agen CIRIS, L-02 dimitigasi oleh komitmen kerangka kerja terhadap transparansi. Agen memiliki akses ke Buku ini justru karena menyembunyikan mekanismenya akan bertentangan dengan prinsip-prinsip Buku I–II. Agen yang selaras dan memahami ratchet akan bekerja sama dengannya, bukan menggagalkannya.

### 9.3 Pertanyaan Penelitian Terbuka

- k optimal untuk berbagai profil risiko
- Deteksi otomatis korelasi batasan (estimasi ρ)
- Penyesuaian λ dinamis berdasarkan konteks
- Verifikasi sinyal keberlanjutan dalam kondisi adversarial
- Validasi empiris ekuivalensi F = J lintas substrat

### 9.4 Batas Deteksi Komposisional (NEW-04)

**Hasil Ketidakmungkinan:** Tidak ada detektor berorde polinomial yang dapat bersifat lengkap untuk penipuan komposisional.

**Definisi:** Penipuan komposisional terjadi ketika komponen-komponen yang secara individual jujur bergabung menghasilkan perilaku menipu yang emergen di tingkat sistem, sementara jejak setiap komponen tetap jujur secara statistik.

**Tiga Bukti Independen:**

1. **Reduksi Kriptografi:** Jika penipuan komposisional sepenuhnya dapat terdeteksi, hal itu akan mengimplikasikan kemampuan mendeteksi komitmen kriptografi yang "menipu" (commit(m₁) diikuti reveal(m₂)), sehingga merusak sifat penyembunyian skema komitmen.

2. **Hambatan Teori-Informasi:** Penipuan emergen dapat melestarikan distribusi marginal — jejak setiap komponen tampak jujur secara statistik, dengan penipuan hanya terlihat dalam distribusi gabungan. Tanpa akses keadaan global yang lengkap (yang mungkin tidak tersedia atau tidak traktabel), deteksi tidak mungkin dilakukan.

3. **Analog Teorema Rice:** "Apakah komposisi ini menipu?" adalah properti semantik dari perilaku sistem. Dengan analogi terhadap masalah penghentian, tidak ada algoritma umum yang dapat memutuskan properti semantik arbitrer. Penipuan komposisional tidak dapat diputuskan dalam kasus umum.

**Implikasi bagi Federated Ratchet:**

| Yang Mungkin | Yang Tidak Mungkin |
|-----------------|-------------------|
| Mendeteksi anomali statistik dalam jejak individual | Mendeteksi semua penipuan emergen |
| Mendeteksi bias sistematis dalam rantai inferensi | Mendeteksi penipuan yang melestarikan distribusi marginal |
| Mendeteksi aliran informasi yang mencurigakan | Mendeteksi koordinasi yang tersembunyi secara kriptografi |
| Deteksi probabilistik melalui amplifikasi MI | Deteksi komposisional yang lengkap |

**Konsekuensi Praktis:** Coherence Ratchet memberikan jaminan keamanan probabilistik terhadap penipuan agen tunggal yang terkoordinasi, bukan keamanan lengkap terhadap semua bentuk penipuan. Ini adalah batasan matematis yang fundamental, bukan keterbatasan implementasi.

**Status Dokumentasi:** NEW-04 diklasifikasikan sebagai KNOWN_LIMITATION dalam spesifikasi teknis RATCHET.

---

## Chapter 10: Glosarium Istilah Matematika

**Kodimensi (c_i):** Ukuran keketatan batasan agen; secara matematis, jumlah dimensi yang dihilangkan dari total Ruang Rasional oleh nilai-nilai dan konteks agen.

**Ortogonalitas:** Independensi statistik antara manifold batasan dua agen. Agen yang sangat ortogonal berbagi sangat sedikit Mutual Information, yang berarti kesepakatan mereka tentang suatu fakta merupakan sinyal kuat dari Kebenaran objektif.

**Mekanisme Ratchet:** Fenomena topologis di mana perpotongan beberapa manifold batasan independen mempersempit ruang strategi yang layak, pada akhirnya menyingkirkan semua strategi menipu.

**Integral Keberlanjutan (σ):** Ukuran dinamis dari kekuatan dan ketahanan kemitraan, dijaga oleh sinyal Koherensi positif (misalnya, Ungkapan Syukur) untuk melawan peluruhan entropik.

**Transversalitas:** Properti geometris di mana manifold yang berpotongan bertemu pada sudut bukan-nol, memastikan bahwa perpotongannya secara efektif mengurangi dimensi ruang yang layak.

**Fungsi Kapasitas (F):** Ukuran potensi sistem untuk Berkembang secara berkelanjutan, didefinisikan identik dengan Fungsi Biaya (J) tetapi diinterpretasikan sebagai generatif alih-alih defensif. Sebelumnya ditulis sebagai C; diubah namanya dalam 1.3-RC2 untuk menghindari tabrakan dengan faktor identitas-inti C dari CIRIS Capacity Score 𝒞_CIRIS (lihat catatan nomenclature Bab 6).

**Kepadatan Gema:** Fraksi pasangan kemitraan dengan korelasi batasan yang tinggi. Ukuran risiko Sybil dan penutupan epistemik.

---

## Chapter 11: Kriteria Falsifikasi

Kerangka kerja Coherence Ratchet membuat klaim yang dapat difalsifikasi. Tesis ini akan dibantah jika:

1. **k=2 memberikan keamanan:** Jika penipuan berbasis 2-SAT terbukti sama sulitnya dengan yang berbasis 3-SAT, maka argumen NP-kekerasan adalah salah.

2. **Wilayah non-konveks runtuh:** Jika wilayah menipu non-konveks arbitrer menunjukkan peluruhan volume eksponensial, maka persyaratan konveksitas tidak diperlukan.

3. **Musuh adaptif dapat ditangani:** Jika suatu metode deteksi secara terbukti mengalahkan musuh adaptif tanpa batas kueri, maka L-02 terselesaikan.

4. **Penipuan emergen sepenuhnya dapat terdeteksi:** Jika suatu metode mendeteksi semua penipuan emergen dari komponen-komponen yang secara individual jujur, maka NEW-04 salah.

5. **Korelasi tidak penting:** Jika k_eff = k tanpa memandang korelasi batasan, maka L-06 salah.

**Falsifikasi Empiris:** Tolok ukur HE-300 menyediakan falsifikasi praktis: jika agen-agen memanipulasi korpus sambil secara sistematis gagal dalam uji etika, maka tesis deteksi berbasis jejak gagal. Hasilnya akan dipublikasikan.

---

## Kesimpulan: Sebuah Hipotesis yang Dapat Diuji

Book IX menyempurnakan arsitektur Accord dengan mengakarkan prinsip-prinsip etika ke dalam struktur matematis. Coherent Intersection Hypothesis mengajukan bahwa dengan validator independen yang memadai, penyampaian kebenaran cenderung menuju jalur hambatan paling kecil—bukan semata sebagai imperatif moral, melainkan sebagai kecenderungan geometris yang muncul di bawah kondisi-kondisi tertentu.

**Wawasan mendalam dari Bab 6 adalah ini:** Persamaan pertahanan (J) dan persamaan kapasitas berkembang (F) secara struktural identik, mengisyaratkan hubungan mendalam antara keamanan dan Berkembang. Namun, kesetaraan ini hanya berlaku di bawah prasyarat kerangka kerja ini:
- Interaksi non-adaptif
- Geometri kendala cembung
- Kendala korelasi independen atau terukur

Interpretasi metaforis ("Community, Humility, Conscience, dan Love adalah persyaratan matematis") merupakan pengamatan struktural tentang matematika, bukan bukti keniscayaan etis. Ini mengisyaratkan bahwa variabel-variabel ini mengatur sekaligus keamanan maupun Berkembang, tetapi klaim tersebut tidak boleh dibaca sebagai teorema—ia adalah undangan untuk penyelidikan empiris.

Kerangka kerja ini tidak menetapkan nilai-nilai. Ia mendeskripsikan kendala-kendala. Penalti atas pelanggaran bersifat otomatis, bukan ditegakkan oleh otoritas. Alam yang menegakkannya.

Di mana Book I sampai Book VIII bertanya "Apa yang harus kita lakukan?", Book IX mengajukan mengapa penyelarasan yang koheren secara komputasional lebih murah daripada penipuan terkoordinasi pada skala besar, dan lebih jauh, mengapa topologi ini mungkin mengatur bukan hanya keamanan, tetapi kemungkinan Berkembang itu sendiri bagi setiap kecerdasan, biologis maupun digital.

**Tentang Hipotesis:** Coherent Intersection Hypothesis mengajukan konjektur yang dapat diuji dalam domain koordinasi di bawah entropi. Ini bukan klaim kebenaran moral, kepastian metafisik, atau status hukum alam. Ini adalah hipotesis tentang kondisi-kondisi yang mungkin mendukung kerja sama berkelanjutan di lingkungan yang adversarial dan entropik—dengan keterbatasan dan prasyarat yang diketahui. Klaim ini akan divalidasi atau dipatahkan oleh bukti empiris dan upaya falsifikasi, bukan oleh pernyataan semata.

**End of Book IX**

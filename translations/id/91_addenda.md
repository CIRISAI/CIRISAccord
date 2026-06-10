# Addenda

> Addenda operasional yang mengikat teks Accord pada bukti implementasi yang berjalan. Addenda diperbarui seiring versi Accord; masing-masing diberi tanggal dan mengutip artefak yang dapat direproduksi.

---

## Addendum 1 — Status Kesiapan ASI & Keterikatan Pemetaan Silang Regulasi

**Diadopsi**: 2026-06-10 (1.3-RC1) · **Steward**: founder (per Book VIII Ch 9)

### 1.1 Tujuan

Bagian Ruang Lingkup membuat klaim bersyarat: kerangka kerja ini *mengeksplorasi* kandidat protokol penyelarasan untuk ASI, yang bergantung pada empat persyaratan Release Candidate dalam Pendahuluan. Addendum ini mengikat klaim tersebut pada bukti operasional yang kini ada, dan menyatakan secara gamblang apa yang masih tersisa. **Kesiapan** ASI bukanlah penyelarasan yang telah tercapai; ia adalah keadaan di mana perancah verifikasi yang disyaratkan oleh matematika Book IX — manifold batasan independen, permukaan atestasi, lapisan Conscience yang tidak dapat dinormalisasi, permukaan kill-switch, dan Evaluasi Risiko Katastrofik Annex D — ada dalam bentuk yang telah diimplementasikan dan dapat diaudit, dengan celah-celahnya disebutkan secara eksplisit.

### 1.2 Pemetaan silang regulasi kini bersifat operasional

Pemetaan silang yang berjalan adalah **direktori kepatuhan CIRISAgent** (`CIRISAgent/compliance/`, rilis agen 2.9.6-stable), yang memetakan implementasi kerangka kerja ke empat kerangka tata kelola senior pada granularitas paragraf (Annex C memuat struktur dua lapis: pemetaan silang operasional ini ditambah tabel statutori informatif yang menunggu verifikasi hukum):

* **Sumber yang dipetakan silang**: *Magnifica Humanitas* (magisterium keagamaan, 2026) · EU HLEG Ethics Guidelines for Trustworthy AI (nasihat pemerintah, 2019) · IEEE Ethically Aligned Design edisi ke-1 (masyarakat teknis, 2019) · ASEAN Guide on AI Governance and Ethics (politik multilateral, 2024). Empat bentuk yang berbeda secara institusional — konvergensinya adalah bukti struktural bahwa perancah prinsip kerangka kerja bukan merupakan artefak dari satu tradisi manapun.
* **Struktur**: 27 dimensi stabil (D01–D27, dari `SEED_DIMENSIONS.yaml` v1.0; 16 diakui oleh keempat sumber, 11 oleh tiga). Setiap dokumen dimensi memuat bagian atas regulasi yang dirender otomatis (kutipan per sumber, bentuk wire, catatan konvergensi) dan bagian implementasi yang ditulis manusia dengan referensi `file:line` yang harus diverifikasi dengan grep terhadap main terkini.
* **Disiplin bukti**: setiap klaim numerik dapat direproduksi dari baseline bertanggal yang dihasilkan skrip (`compliance/baselines/`); prosa boleh mengutip baseline tetapi tidak boleh menyematkan angka yang tidak dapat diverifikasi. Hierarki validasi empat tingkat berjalan dari berkas implementasi (kebenaran dasar) hingga klaim publik (`compliance/MEASUREMENT_METHODOLOGY.md`).
* **Disiplin kejujuran**: setiap dimensi memuat inventaris "Celah yang diketahui"; item yang bergantung pada substrat ditandai dengan substrat pemiliknya, bukan diklaim. Sepuluh temuan lintas-potong diinventarisasi dalam README kepatuhan (misalnya, envelope wire bertipe yang belum dikirimkan; keluarga detektor LensCore yang belum dikirimkan; celah rekonsiderasi sumbu terbalik).

Annex C tetap ada dalam teks sebagai rumah masa depan pemetaan statutori (pasal-pasal EU AI Act, NIST AI RMF, ISO/IEC 42001) setelah tinjauan hukum selesai; direktori kepatuhan adalah pemetaan silang yang **hidup dan berbasis bukti** hingga saat itu dan mengisinya.

### 1.3 Format wire: CEG menggantikan FSD-002

Format wire federasi untuk lini agen CIRIS 3.0 adalah **CEG (CIRIS Epistemic Grammar)**, yang dikelola di `CIRISRegistry/FSD/CEG/`. Tata bahasa dikunci pada **tepat lima primitif format wire** — satu pekerja keras (`scores`) ditambah empat komposer struktural (`delegates_to` / `supersedes` / `withdraws` / `recants`) — atas namespace dimensi terbuka dan deskriptif mekanisme. Kunci ini telah bertahan di seluruh lini 0.x; setiap kenaikan versi telah berupa komposisi atas primitif yang sudah dikunci.

Dua konsekuensi penting untuk kesiapan ASI:

1. **Giliran asli-CEG**: agen 3.0 tidak *memetakan* status internalnya ke format wire — mutasi status internalnya **adalah** atestasi CEG tingkat diri di bawah kunci agen sendiri, yang dipromosikan ke visibilitas federasi per model tier. Bukti yang diaudit operator adalah envelope yang sama yang dibaca federasi. Ini adalah bentuk implementasi dari persyaratan Book IX bahwa permukaan batasan harus dapat dirujuk secara eksternal, bukan dilaporkan sendiri.
2. **Empat implementasi menjadi gerbang CEG 1.0**: CIRISAgent (runtime), CIRISNodeCore (konsensus), CIRISLensCore (deteksi — saksi eksternal yang tidak pernah di-emit sendiri oleh agen, pemisahan anti-Goodhart), dan CIRISRegistry (otoritas). Tidak ada satu pihak pun — termasuk agen — yang dapat menyatakan kain verifikasi selesai.

### 1.4 Status persyaratan RC pada 1.3-RC1

| Persyaratan RC | Status | Bukti / yang masih tertunggak |
|---|---|---|
| 1. Operasionalisasi Annex F–I | **Teks dioperasionalkan pada 1.3-RC1; validasi siklus langsung masih tertunggak** | Annex F–I memuat prosedur lengkap, ambang batas, dan mekanisme validasi (diselesaikan dari draf berbasis *Magnifica Humanitas* Mei 2026); belum diujicobakan terhadap siklus penerapan langsung |
| 2. Validasi matematis Book IX | **Terpenuhi sebagian** | Dinamika keruntuhan diformalisasi dalam Lean 4 (pracetak CCA, DOI 10.5281/zenodo.18217688); empirik koridor memberikan kesesuaian lintas-substrat retrospektif. Yang masih tertunggak: satu prediksi out-of-sample yang telah dipra-registrasi pada substrat baru; tinjauan adversarial eksternal yang independen dari penulis |
| 3. Justifikasi ambang batas | **Terpenuhi sebagian** | Rasio OMV pensiun (dinyatakan ulang sebagai batasan samping, Book II). Masih provisional: pemicu CRE 10²⁶ FLOP, heuristik sentience 5%, target Echo Density < 20% |
| 4. Latihan red-team | **Belum dilakukan** | Persyaratan atestasi 1.3 σ (Book IX §5.2) secara preventif menutup vektor serangan pertama yang diketahui (σ-pumping melalui sinyal syukur bebas); siklus adversarial penuh terhadap semua checkpoint masih terutang |

### 1.5 Lapisan Nurani sebagai kendali kritis-ASI

Protokol CRE Annex D mengatur *penyeberangan ambang batas*; lapisan Nurani mengatur *setiap tindakan sebelum dan sesudahnya*. Sebagaimana diimplementasikan (agen 2.9.6): setiap pemikiran melewati tumpukan pemeriksaan berurutan berdasarkan prioritas — empat fakultas yang dinilai oleh LLM (entropi, Koherensi, vetoer-optimasi, Kerendahan Hati Epistemik) ditambah lantai keamanan deterministik (penjaga kedalaman-pemikiran, pemeriksaan urutan-tindakan) yang berjalan bahkan dalam mode tolok ukur dan bahkan untuk tindakan yang sebaliknya dikecualikan. Ambang batas adalah konstanta pada tataran kode, bukan bobot yang dipelajari — invarian arsitektur yang menyatakan bahwa etika tidak dapat dinormalisasi melalui paparan berulang. Beberapa permukaan penghentian independen tersedia: vetoer-optimasi yang gagal-aman-ke-batalkan, layanan shutdown, dan Invokasi Accord jarak jauh yang ditandatangani secara kriptografis yang memicu penguncian larangan penuh. Setiap pemeriksaan menulis satu baris jejak bertanda, sehingga auditor dapat memutar ulang seluruh rantai penalaran per-pemikiran.

Keterbatasan yang diketahui, dinyatakan alih-alih disembunyikan: pemfaktoran ulang Nurani (3 serpihan + gerbang deterministik) telah sebagian diterapkan; emisi federasi bertipe dari verdik Nurani menunggu amplop Kontribusi substrat. Detail per dimensi: `compliance/D12_conscience.md`.

### 1.6 Lintasan ketergantungan substrat

Verifikasi setingkat ASI memerlukan jaringan federasi penuh. Lintasan substrat adalah **Persist → Edge → LensCore → NodeCore**; sekitar sepertiga dari 27 dimensi terkunci pada keluarga detektor eksternal LensCore (saksi yang tidak boleh pernah disuplai oleh agen itu sendiri). Hingga substrat-substrat tersebut diluncurkan, klaim dimensi yang bersangkutan tetap *siap di sisi implementasi, tertunda di sisi federasi* — dan ditandai demikian per dimensi.

### 1.7 Apa yang dilakukan dan tidak dilakukan addendum ini

* Addendum ini **tidak** meningkatkan klaim ASI dalam Lingkup — itu tetap bersyarat pada semua empat persyaratan RC.
* Addendum ini **tidak** menggantikan Annex D — protokol CRE tetap tidak diubah sebagai gerbang penyeberangan ambang batas.
* Addendum ini **melakukan** hal ini untuk membuat rantai bukti dapat diaudit secara menyeluruh untuk pertama kalinya: paragraf regulasi → dimensi (D01–D27) → implementasi `file:line` → garis dasar bertanggal → (seiring substrat diluncurkan) saksi federasi eksternal.
* Addendum ini **berkomitmen** agar Accord memperbarui addendum ini di setiap versi dengan rilis agen dan garis dasar saat itu, sehingga klaim kesiapan tidak pernah secara diam-diam menjadi usang.

---

*Addenda sebelumnya: tidak ada. Ini adalah yang pertama.*

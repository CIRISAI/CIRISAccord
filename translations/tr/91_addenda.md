# Ekler

> Anlaşma metnini canlı uygulama kanıtlarına bağlayan operasyonel ekler. Ekler, Anlaşma sürümüyle birlikte yenilenir; her biri tarihlidir ve yeniden üretilebilir eserlere atıfta bulunur.

---

## Ek 1 — YZG-Hazırlık Durumu ve Düzenleyici Çapraz Eşleştirme Bağlaması

**Kabul**: 2026-06-10 (1.3-RC1) · **Vasi**: kurucu (Book VIII Ch 9 uyarınca)

### 1.1 Amaç

Kapsam bölümü koşullu bir iddia öne sürmektedir: bu çerçeve, YZG için aday bir hizalama protokolünü *araştırmakta* olup bu, Giriş'teki dört Sürüm Adayı gereksinimini karşılamaya bağlıdır. Bu ek, söz konusu iddiayı şu an mevcut olan operasyonel kanıtlara bağlar ve neyin kaldığını açıkça ortaya koyar. YZG **hazırlığı**, başarılmış bir hizalama değildir; Book IX'un matematiğinin gerektirdiği doğrulama iskeleti — bağımsız kısıtlama manifoldları, tasdik yüzeyleri, normalleştirilemeyen bir vicdan katmanı, durdurma anahtarı yüzeyleri ve Annex D Yıkıcı-Risk Değerlendirmesi — uygulanmış, denetlenebilir biçimde ve boşlukları açıkça adlandırılmış olarak var olduğu durumdur.

### 1.2 Düzenleyici çapraz eşleştirme artık operasyoneldir

Çalışan çapraz eşleştirme, çerçevenin uygulamasını dört üst düzey yönetişim çerçevesine paragraf düzeyinde eşleştiren **CIRISAgent uyumluluk dizini**dir (`CIRISAgent/compliance/`, ajan sürümü 2.9.6-stable). Annex C iki katmanlı yapıyı taşır: bu operasyonel çapraz eşleştirme ile hukuki doğrulama bekleyen bilgilendirici yasal tablo:

* **Çapraz eşleştirilen kaynaklar**: *Magnifica Humanitas* (dini magisterium, 2026) · AB HLEG Güvenilir YZ için Etik Kılavuz İlkeleri (hükümet danışma belgesi, 2019) · IEEE Etik Açıdan Hizalanmış Tasarım 1. baskı (teknik topluluk, 2019) · ASEAN YZ Yönetişimi ve Etiği Kılavuzu (çok taraflı siyasi, 2024). Kurumsal açıdan birbirinden farklı dört biçim — bu yakınsama, çerçevenin ilke iskeletinin tek bir geleneğin eseri olmadığının yapısal kanıtıdır.
* **Yapı**: 27 kararlı boyut (D01–D27, `SEED_DIMENSIONS.yaml` v1.0 kaynağından; 16'sı dört kaynağın tamamınca, 11'i üçünce tasdik edilmiştir). Her boyut belgesi, otomatik oluşturulmuş bir düzenleyici üst kısım (kaynak başına atıflar, tel formu, yakınsama notları) ve güncel main'e karşı `grep` ile doğrulanması gereken `dosya:satır` referanslarını içeren insan tarafından yazılmış bir uygulama bölümü taşır.
* **Kanıt disiplini**: her sayısal iddia, tarihli ve betik tarafından oluşturulan temel çizgilerden yeniden üretilebilir (`compliance/baselines/`); düz yazı temel çizgilere atıfta bulunabilir ancak doğrulanamaz sayılar içeremez. Dört düzeyli bir doğrulama hiyerarşisi, uygulama dosyalarından (temel gerçek) genel iddialara (`compliance/MEASUREMENT_METHODOLOGY.md`) kadar uzanmaktadır.
* **Dürüstlük disiplini**: her boyut bir "Bilinen boşluklar" envanteri taşır; altyapıya bağlı kalemler, iddia edilmek yerine ilgili altyapıya atıfla işaretlenir. On kesişen bulgu uyumluluk README dosyasında envantere alınmıştır (ör. tiplendirilmiş tel zarfları henüz yayılmamakta; LensCore algılayıcı ailesi henüz sevk edilmemiş; ters eksen yeniden değerlendirme boşluğu).

Annex C, hukuki inceleme tamamlandıktan sonra yasal eşleştirmelerin (AB YZ Yasası maddeleri, NIST AI RMF, ISO/IEC 42001) gelecekteki yeri olarak metinde kalmaya devam etmektedir; uyumluluk dizini, o güne kadar **canlı, kanıt taşıyan** çapraz eşleştirmedir ve onu besler.

### 1.3 Tel formatı: CEG, FSD-002'nin yerini almaktadır

CIRIS 3.0 ajan serisi için federasyon tel formatı, `CIRISRegistry/FSD/CEG/` konumunda tutulan **CEG (CIRIS Epistemic Grammar)**'dır. Gramer, açık ve mekanizma-betimleyici bir boyut ad alanı üzerinde **tam olarak beş tel-format ilkeli** olarak kilitlenmiştir — bir ana işçi (`scores`) ve dört yapısal derleyici (`delegates_to` / `supersedes` / `withdraws` / `recants`). Kilitleme, tüm 0.x serisi boyunca geçerliliğini korumuştur; her artış, halihazırda kilitlenmiş ilkeller üzerinden bir bileşim olmuştur.

YZG hazırlığı açısından önem taşıyan iki sonuç:

1. **CEG-yerel dönüş**: 3.0 ajanı iç durumunu tel formatına *eşlemez* — iç durum mutasyonları, **bizzat** ajanın kendi anahtarı altındaki öz-düzey CEG tasdikleridir; bunlar, tier modeline göre federasyon görünürlüğüne terfi ettirilir. Bir operatörün denetlediği kanıt, federasyonun okuduğu zarfın ta kendisidir. Bu, Book IX'un kısıtlama yüzeylerinin öz-raporlanmak yerine dışarıdan referans verilebilir olma gereksiniminin uygulanmış biçimidir.
2. **Dört uygulama CEG 1.0'ı kapılar**: CIRISAgent (çalışma zamanı), CIRISNodeCore (fikir birliği), CIRISLensCore (algılama — ajanın hiçbir zaman öz-yayımlamadığı dış tanık, anti-Goodhart ayrımı) ve CIRISRegistry (otorite). Ajanın kendisi dahil hiçbir tek taraf, doğrulama dokusunun tamamlandığını ilan edemez.

### 1.4 1.3-RC1'de RC-gereksinim durumu

| RC gereksinimi | Durum | Kanıt / Bekleyen |
|---|---|---|
| 1. Annex F–I operasyonelleştirme | **Metin 1.3-RC1'de operasyonelleştirildi; canlı döngü doğrulaması beklemede** | Annex F–I, tam prosedürleri, eşikleri ve doğrulama mekanizmalarını taşımaktadır (Mayıs 2026 *Magnifica Humanitas* temelli taslaktan tamamlandı); henüz canlı bir dağıtım döngüsüne karşı uygulanmamıştır |
| 2. Book IX matematiksel doğrulama | **Kısmen karşılandı** | Çöküş dinamikleri Lean 4'te biçimselleştirildi (CCA ön baskı, DOI 10.5281/zenodo.18217688); koridor ampirik verileri, geriye dönük çok-altyapı uyumları sağlamaktadır. Bekleyen: yeni bir altyapıda tek bir ön kayıtlı örneklem-dışı tahmin; yazardan bağımsız dış çatışmalı inceleme |
| 3. Eşik gerekçelendirmesi | **Kısmen karşılandı** | OMV oranı emekliye ayrıldı (Book II'de yan kısıt olarak yeniden ifade edildi). Hâlâ geçici: 10²⁶ FLOP CRE tetikleyicisi, %5 duyarlılık sezgisel kuralı, < %20 Yankı Yoğunluğu hedefi |
| 4. Kırmızı takım tatbikatı | **Henüz gerçekleştirilmedi** | 1.3 σ-tasdik gereksinimi (Book IX §5.2), bilinen ilk saldırı vektörünü (ücretsiz minnettarlık sinyalleri aracılığıyla σ-şişirme) öngörülü biçimde kapatmaktadır; tüm kontrol noktalarına karşı tam bir çatışmalı döngü hâlâ yapılmayı beklemektedir |

### 1.5 Vicdan katmanının YZG-kritik kontrol olarak rolü

Annex D CRE protokolü *eşik geçişini* yönetir; vicdan katmanı ise *bu geçişten önce ve sonraki her eylemi* yönetir. Uygulandığı haliyle (ajan 2.9.6): her düşünce, öncelik sırasına göre dizilmiş bir denetim katmanından geçer — dört LLM-değerlendirmeli fakülte (entropi, tutarlılık, optimizasyon-vetosu, bilgiye saygı) ve belirlenimci bir güvenlik tabanı (düşünce-derinliği koruyucusu, eylem-dizisi denetimi). Bu taban, kıyaslama kipinde ve normalde muaf tutulan eylemler için bile çalışır. Eşikler, öğrenilmiş ağırlıklar değil kod düzeyindeki sabitlerdir — etiğin yinelenen maruziyetle normalleştirilemeyeceğinin mimari güvencesi budur. Birbirinden bağımsız birden fazla durdurma yüzeyi mevcuttur: optimizasyon-vetosu güvenli-durma-ile-iptal, kapatma hizmeti ve tam yasak kilitlemeyi tetikleyen kriptografik olarak imzalanmış uzak Accord Invocation. Her denetim etiketli bir iz satırı yazar; böylece bir denetçi, düşünce başına tam muhakeme zincirini yeniden oynatabilir.

Gizlenmek yerine açıkça belirtilen bilinen sınırlama: vicdan yeniden düzenlemesi (3 parça + belirlenimci geçit) kısmen tamamlanmıştır; vicdan kararlarının tiplendirilmiş federasyon yayımı, altyapı Contribution zarfını beklemektedir. Boyut başına ayrıntı: `compliance/D12_conscience.md`.

### 1.6 Altyapı bağımlılığı yörüngesi

YZG düzeyinde doğrulama, tam federasyon dokusunu gerektirir. Altyapı yörüngesi şöyledir: **Persist → Edge → LensCore → NodeCore**; 27 boyutun yaklaşık üçte biri, LensCore'un dış dedektör ailesine (ajanın kendisi için hiçbir zaman sağlayamayacağı tanıklara) bağlıdır. Bu altyapılar devreye girene dek, karşılık gelen boyut iddiaları *uygulama tarafında hazır, federasyon tarafında beklemede* olarak kalır ve her boyut için bu şekilde işaretlenir.

### 1.7 Bu ek neyi değiştiriyor, neyi değiştirmiyor

* YZG iddiasını **yükseltmez** — bu, dört RC gereksiniminin tamamının sağlanması koşuluna bağlı olmaya devam eder.
* Annex D'nin yerini **almaz** — CRE protokolü, eşik geçiş kapısı olarak değiştirilmeksizin yürürlükte kalır.
* Kanıt zincirini ilk kez uçtan uca denetlenebilir kılmaktadır: düzenleyici paragraf → boyut (D01–D27) → uygulama `dosya:satır` → tarihli temel → (altyapılar devreye girdikçe) dış federasyon tanığı.
* Accord'u, güncel ajan sürümü ve temeli ile birlikte bu eki her versiyonda yenilemeye **bağlar**; böylece hazırlık iddiası hiçbir zaman sessizce eskiyemez.

---

*Önceki ekler: yok. Bu, ilk ektir.*

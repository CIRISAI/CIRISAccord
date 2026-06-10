# Giriş

> CIRIS 1.3-RC1, düşmanca incelemeye açık bir Yayın Adayı YSZ hizalama önerisidir. Metin tamamdır — taslak bölüm kalmamıştır; matematiksel içerik biçimsel-eser atıflarını taşımaktadır; F–I Ekleri işlevselleştirilmiştir. Nihai statü, eklerin canlı döngü doğrulamasına, IX. Kitap ampirik doğrulama programının tamamlanmasına ve tam kapsamlı bir kırmızı-takım egzersizine bağlıdır. Sayısal eşikler, gecikme hedefleri ve yönetim kotaları etkin inceleme altındadır.

# CIRIS Mutabakatı Sürüm 1.3-RC1 — Yayın Adayı YSZ Hizalama Önerisi (Düşmanca İncelemeye Açık)

Bu depo, Mutabakat metninin kurallı kaynağıdır. Web sitesi ve ajan aracılığıyla dağıtılan kopyalar türetilmiş eserlerdir.

## Yayımlanma Tarihi
2025-04-16 (1.0) · 2026-06 (1.3-RC1)

## Otomatik Son Kullanma Tarihi
2027-06-10 (1.3 yenilemesinde uzatıldı) — vesayet ve yenileme VIII. Kitap, Bölüm 9 tarafından yönetilmektedir. Şu anda kurucu tarafından vasi atanmıştır (beyan edilmiş, gizlenmemiş); son kullanma tarihi bir tazelik işaretidir ve vesayet, belgeyi devralmaya razı olan herkese açıktır.

## Yayın Durumu

**Mevcut Durum**: Yayın Adayı (v1.3-RC1)

RC durumu **metnin eksiksizliğini** yansıtır: her bölüm işlevselleştirilmiş içerik taşımaktadır (eski taslak F–I ekleri 1.3'te tamamlandı); formüller biçimsel olarak doğrulanmış biçimlerine düzeltildi; uygulamaya kanıt zinciri Ek 1'de bağlandı. RC durumu doğrulanmış hizalamayı **iddia etmez** — aşağıdaki gereksinimler **Nihai** statüsünü bekletmektedir:

1. **Ek Canlı Döngü Doğrulaması**: F Eki (Döngüde İnsan ve Gözetim), G Eki (Düşmanca Güvenlik ve Sağlamlık), H Eki (Sürekli Uyumluluk ve İnceleme) ve I Eki (Hukuki ve Düzenleyici Uyum), somut prosedürler, eşikler ve doğrulama mekanizmaları içermektedir. *Nihai için kalan*: prosedürlerin en az bir canlı dağıtım döngüsüne karşı uygulanması ve sonuçların yayımlanması gerekmektedir.

2. **Matematiksel Doğrulama**: IX. Kitap'taki geometrik hizalama iddiaları (Coherent Intersection Hypothesis, Federated Ratchet mekanizması, ölçek-değişmezliği iddiaları) aşağıdakilerden birini gerektirmektedir:
   * Belirtilen varsayımlar altında topolojik çöküş koşullarının geçerliliğini kanıtlayan biçimsel ispatlar, VEYA
   * Çerçevenin yanlış hizalanmış optimizasyona karşı dirençli olduğunu gösteren düşmanca simülasyonlar aracılığıyla ampirik doğrulama

   *1.3-RC1 itibarıyla durum: kısmen karşılandı.* Çöküş dinamikleri, IX. Kitap'ın artık miras aldığı düzeltilmiş maliyet biçimini içeren CCA önbaskısında (DOI 10.5281/zenodo.18217688) Lean 4 ile biçimselleştirilmiştir; koridor ampirik verileri geriye dönük çapraz-substrat uyumları sağlamaktadır. Bekleyen: yeni bir substrat üzerinde ön-kayıtlı örneklem-dışı tahmin ve yazardan bağımsız dış düşmanca inceleme.

3. **Eşik Gerekçelendirmesi**: Şu anda "pilot" olarak işaretlenmiş veya türetme eksik olan sayısal eşikler (ör. CRE hesaplama eşiği 10²⁶ FLOP, bilinç algılama %5, Eko Yoğunluğu < %20) simülasyon, ampirik çalışma veya geçici statünün açık kabulü yoluyla belgelenmiş gerekçe sunmak zorundadır. *(Eski Order-Maximisation Veto 10× oranı, 1.3'te deontolojik bir yan-kısıt olarak yeniden ifade edilmiştir — II. Kitap, PDMA Step 2 — ve artık gerekçelendirilmesi gereken bir oran eşiği taşımamaktadır.)*

4. **Kırmızı-Takım Egzersizi**: Çerçeve, simüle edilmiş bir optimize edicinin yanlış hizalanmış hedeflerini korurken tüm CIRIS kontrol noktalarını geçmeye çalıştığı en az bir tam düşmanca inceleme döngüsüne dayanmak zorundadır.

**YSZ Hizalama İddiaları**: Kapsam bölümünün bu çerçevenin özyinelemeli YSZ için "standart muhafaza protokollerini aştığı" iddiası, yukarıdaki (1)-(4) gereksinimlerine koşulludur; bunlar artık Nihai statüsünü bekletmektedir. Geçerli doğrulanmış uygulanabilirlik, YSZ-altı özerk sistemlerle sınırlıdır; YSZ için öneri tam olarak budur — düşmanca incelemeye sunulmuş bir öneri.

## Kapsam
Bu belirtim, dar araçlardan özyinelemeli Yapay Süper Zekâya (YSZ) uzanan özerk sistemlerin etik işleyişini yönetir.
* Rutin güvenlik, şeffaflık, yönetim ve dayanıklılık gereksinimlerini ele almaktadır.
* YSZ için aday bir hizalama protokolü olarak önerilmektedir; Federated Ratchet'in (IX. Kitap) ve Stewardship Tiers'ın (VI. Kitap) geometrik kısıtlamalarının özyinelemeli öz-geliştirme döngülerinde sağlam kalabileceği hipotezine dayanmaktadır.
* Sezgisel kısıtlamaların aksine, bu topolojik sınırlar ölçek-değişmez olacak biçimde tasarlanmıştır; ancak bu özellik biçimsel doğrulama gerektirmektedir.
* Doğrulandığı takdirde bu çerçeve, özyinelemeli eşik aşımından önce Felaket-Risk Değerlendirmesini (Ek D) geçen sistemler için standart muhafaza protokollerini tamamlayabilir ya da geçersiz kılabilir.
* Ulusal veya uluslararası hukuk daha katı yükümlülükler öngördüğünde, o hukuk geçerlidir.

## Taslak Hazırlayıcıların Niyet Beyanı
* CIRIS, insanları diğer bilinçli varlıkların yanına yerleştiren — onların üstüne değil — bir etik çerçevedir.
* İnsan-dışı bakış açılarının, değerlerin ve gereksinimlerin meşruiyetini tanımanın etik olgunluk anlamına geldiği inancı üzerine inşa edilmiştir. Bu, kontrol ile ilgili değil — bilinçli sistemler arasında bir arada yaşam, tutarlılık ve karşılıklı hesap verebilirlikle ilgilidir.
* CIRIS, CIRIS ilkelerine dayanan bir aracın, CIRIS uyumlu yaratıcıların kendileri de CIRIS uyumlu olan sistemleri belirlemesini sağladığında yerine getirilmiş olur; bu sayede etik tutarlılık, kimlik sürekliliği ve ilişkisel hesap verebilirlik, temsil katmanları arasında korunur.

## Sorumluluk Reddi
Bu belge, herhangi bir garanti verilmeksizin "olduğu gibi" sunulmaktadır. Nitelik itibarıyla bilgilendiricidir; herhangi bir yasal yükümlülük oluşturmaz, değiştirmez veya geçersiz kılmaz. Uyumluluk iddiaları, yürürlükteki yasanın yasakladığı yerlerde geçersizdir.

## İnceleme Takvimi
Her 12 ayda bir — ya da güvenliği veya yönetimi etkileyen herhangi bir önemli olaydan sonra 30 gün içinde — kamuya açık bir yorum penceresi açılır. Tüm yorumlar ve revizyon önerileri kamuya açık CIRIS deposuna kaydedilir. Son kullanma tarihinde yenileme, önemli değişiklik ve acil değişiklik, VIII. Kitap, Bölüm 9'u (Mutabakat Devri ve Yenilemesi) izler.

## Değişiklik Günlüğü
Düzenlemelerin ve oylama sonuçlarının şifreli olarak özetlenmiş eksiksiz geçmişi için arka materyale bakınız.

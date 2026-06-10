# Rumus-Rumus

> Semua rumus matematika eksplisit yang didefinisikan dalam spesifikasi CIRIS Accord 1.3-RC1.

## 1. Skor Pengaruh Pencipta (CIS)

```math
CIS = CW + IW
```

(Book VI §3 STEP A)

---

## 2. Tingkat Pengelolaan (ST)

```math
ST = ⌈(CIS × RM) / 7⌉
```

di mana ⌈ ⌉ melambangkan fungsi plafon (ceiling function).
(Book VI §3 STEP C)

---

## 3. Pengaruh Struktural (SI)

```math
SI = CW + OA + log(1 + DWP)
```

(Annex E §2.3)

---

## 4. Kepentingan Koherensi (CS)

```math
CS = RH_weighted + AC_weighted + SDA_bonus
```

(Annex E §3.3)

---

## 5. Bobot Pemungutan Suara

```math
VotingWeight(agent) = f(SI(agent), CS(agent))
```

(Annex E §4)

---

## 6. Fungsi Pertahanan (J)

```math
J = k_eff · λ · σ

k_eff = k / (1 + ρ̄ · (k − 1))
```

(Book IX Ch 4 — bentuk yang telah divalidasi oleh CCA; keragaman masuk melalui k_eff saja. Draf-draf sebelumnya memuat faktor tambahan (1 − ρ̄), yang menghitung korelasi secara ganda; lihat catatan drift Book IX Ch 4.)

---

## 7. Kapasitas Berkembang (F)

```math
F = k_eff · λ · σ
```

(Book IX Ch 6 — identik dengan suku J suku demi suku; dimaknai sebagai generatif, bukan defensif. Sebelumnya ditulis C; diganti nama menjadi F dalam 1.3-RC2 untuk menghindari tabrakan dengan faktor identitas-inti C dari Skor Kapasitas CIRIS 𝒞_CIRIS — lihat catatan nomenklatur Book IX Ch 6, yang merupakan pernyataan otoritatif mengenai hubungan tersebut.)

---

## 8. Integral Keberlanjutan (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

di mana d adalah laju peluruhan harian (disarankan 0.05) dan w HARUS diturunkan dari peristiwa yang telah dibuktikan dan sulit dipalsukan; sinyal yang tidak dibuktikan membawa w = 0.
(Book IX §5.2)

---

## 9. Keruntuhan Topologis (peluruhan volume)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

untuk wilayah menipu (deceptive region) cembung berradius r < 0.5 di bawah kendala seragam Grassmannian, λ ≈ 2r.
(Book IX Ch 3 — lihat prasyarat yang dinyatakan.)

---

## Order‑Maximisation Veto (kendala samping, bukan rumus)

Per versi 1.3, OMV (Book II §II Step 2) adalah kendala samping deontologis, bukan pertidaksamaan rasio: manfaat optimisasi, seberapa pun besarnya, tidak boleh diperoleh melalui kerugian yang diprediksi secara non-trivial dalam otonomi, keadilan, keanekaragaman hayati, atau keragaman preferensi. Versi-versi sebelumnya mengungkapkan hal ini sebagai pertidaksamaan "manfaat ≥ 10 × kerugian → batalkan"; pembacaan tersebut ditinggalkan karena membalik niat yang sesungguhnya (memveto perdagangan yang menguntungkan) dan dapat dimanipulasi melalui pemecahan tindakan dan inflasi penyebut.

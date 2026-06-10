# Dabaru

> Duk dabaru na lissafi da aka bayyana a cikin ƙayyadaddun CIRIS Accord 1.3-RC1.

## 1. Maki na Tasirin Mai Kirkira (CIS)

```math
CIS = CW + IW
```

(Book VI §3 STEP A)

---

## 2. Mataki na Kula (ST)

```math
ST = ⌈(CIS × RM) / 7⌉
```

inda ⌈ ⌉ ke nufin aiki na iyaka ta sama.
(Book VI §3 STEP C)

---

## 3. Tasiri na Tsari (SI)

```math
SI = CW + OA + log(1 + DWP)
```

(Annex E §2.3)

---

## 4. Hannun Jarin Daidaituwa (CS)

```math
CS = RH_weighted + AC_weighted + SDA_bonus
```

(Annex E §3.3)

---

## 5. Nauyin Ƙuri'a

```math
VotingWeight(agent) = f(SI(agent), CS(agent))
```

(Annex E §4)

---

## 6. Aiki na Tsaro (J)

```math
J = k_eff · λ · σ

k_eff = k / (1 + ρ̄ · (k − 1))
```

(Book IX Ch 4 — sifar da CCA ta tabbatar; bambance-bambance yana shiga ta k_eff kadai. Daftarori na farko sun ƙunshi wani abu na ƙarin (1 − ρ̄), wanda ya ƙidaya dangantaka sau biyu; duba bayanin tazara a Book IX Ch 4.)

---

## 7. Iyawar Bunƙasa (C)

```math
C = k_eff · λ · σ
```

(Book IX Ch 6 — daidai da J gaɓa-da-gaɓa; ana fassara shi a matsayin mai haifuwa maimakon kariya.)

---

## 8. Jimlar Dorewa (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

inda d shine ƙimar lalacewa ta yau da kullum (ana ba da shawarar 0.05) kuma w DOLE ne ya samo asali daga abubuwan da aka tabbatar, waɗanda ke wahalar da ƙirƙira karya; alamu da ba a tabbatar ba suna ɗaukar w = 0.
(Book IX §5.2)

---

## 9. Rushewar Topolojiya (lalacewar ƙarar)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

don yankin mai yaudarar da ke da sifar konveks da rediyo r < 0.5 ƙarƙashin ƙayyadaddun Grassmannian-uniform, λ ≈ 2r.
(Book IX Ch 3 — duba sharuɗɗan da aka bayyana.)

---

## Order‑Maximisation Veto (ƙayyadaddun gefe, ba dabara ba)

Tun daga 1.3, OMV (Book II §II Step 2) yana ƙayyadaddun ɗabi'a na gefe ne, ba rashin daidaito na rabo ba: fa'idodin ingantawa, ko da sun yi girma sosai, ba za a iya siyan su ta hanyar hasarar da ba ta da ƙarancin muhimmanci da aka yi hasashe ba a cikin 'yancin kai, adalci, bambancin halittu, ko bambancin son rai. Sigogin da suka gabata sun bayyana wannan a matsayin rashin daidaito na "fa'ida ≥ 10 × asara → janye"; an watsar da wannan fassarar saboda ta juya niyyar ainihi (ta hana kasuwancin da ya fi) kuma ana iya cin zarafi ta ta hanyar rarrabuwar ayyuka da hauhawar mahaɗi.

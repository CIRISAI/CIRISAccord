# Fomula

> Fomula zote za kihesabu zilizofafanuliwa wazi katika maelezo ya CIRIS Accord 1.3-RC1.

## 1. Alama ya Ushawishi wa Muundaji (CIS)

```math
CIS = CW + IW
```

(Book VI §3 STEP A)

---

## 2. Tabaka la Uangalizi (ST)

```math
ST = ⌈(CIS × RM) / 7⌉
```

ambapo ⌈ ⌉ inaashiria kazi ya dari ya juu.
(Book VI §3 STEP C)

---

## 3. Ushawishi wa Kimuundo (SI)

```math
SI = CW + OA + log(1 + DWP)
```

(Annex E §2.3)

---

## 4. Dau la Upatanifu (CS)

```math
CS = RH_weighted + AC_weighted + SDA_bonus
```

(Annex E §3.3)

---

## 5. Uzito wa Kupiga Kura

```math
VotingWeight(agent) = f(SI(agent), CS(agent))
```

(Annex E §4)

---

## 6. Kazi ya Ulinzi (J)

```math
J = k_eff · λ · σ

k_eff = k / (1 + ρ̄ · (k − 1))
```

(Book IX Ch 4 — fomu iliyothibitishwa na CCA; utofauti huingia kupitia k_eff peke yake. Rasimu za awali zilibeba sehemu ya ziada ya (1 − ρ̄), ambayo ilihesabu uwiano mara mbili; angalia kumbuka ya mwelekeo katika Book IX Ch 4.)

---

## 7. Uwezo wa Kustawi (F)

```math
F = k_eff · λ · σ
```

(Book IX Ch 6 — sawa kabisa na neno J kwa neno; hutafsiriwa kama uzalishaji badala ya ulinzi. Awali iliandikwa C; iliitwa upya katika 1.3-RC2 ili kuepuka mgongano na kipengele cha utambulisho wa msingi C cha Alama ya Uwezo wa CIRIS 𝒞_CIRIS — angalia kumbuka ya istilahi katika Book IX Ch 6, ambayo ndiyo taarifa ya mamlaka kuhusu uhusiano huo.)

---

## 8. Jumla ya Uendelevu (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

ambapo d ni kiwango cha kuoza kwa siku (inayopendekezwa ni 0.05) na w LAZIMA itokane na matukio yaliyoshuhudiwa ambayo ni vigumu kughushi; ishara zisizoshuhudiwa hubeba w = 0.
(Book IX §5.2)

---

## 9. Kuanguka kwa Topolojia (kuoza kwa ujazo)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

kwa eneo la udanganyifu la mviringo wenye radius r < 0.5 chini ya vikwazo vya Grassmannian-uniform, λ ≈ 2r.
(Book IX Ch 3 — angalia masharti yaliyowekwa.)

---

## Order‑Maximisation Veto (kikwazo cha pembeni, si fomula)

Kuanzia toleo la 1.3, OMV (Book II §II Step 2) ni kikwazo cha deontolijia cha pembeni, si usawa wa uwiano: faida za uboreshaji, haijalishi ni kubwa kiasi gani, haziwezi kununuliwa kwa kupoteza kwa kiasi kikubwa kwa uhuru, haki, bioanuwai, au utofauti wa mapendeleo — kama inavyotabiriwa. Matoleo ya awali yalieleza hili kama usawa wa "faida ≥ 10 × hasara → sitisha"; usomaji ule ulistaafu kwa sababu uligeuka nia (ukikataa biashara zenye faida) na uliweza kudanganywa kwa mgawanyo wa vitendo na uvimbishaji wa dhehebu.

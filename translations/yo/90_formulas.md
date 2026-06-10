# Àwọn Fọ́múlà

> Gbogbo àwọn fọ́múlà ìṣirò tó jẹ́ kedere tí wọ́n ṣàlàyé nínú ìpínrọ̀ CIRIS Accord 1.3-RC1.

## 1. Creator‑Influence Score (CIS)

```math
CIS = CW + IW
```

(Book VI §3 STEP A)

---

## 2. Stewardship Tier (ST)

```math
ST = ⌈(CIS × RM) / 7⌉
```

níbi tí ⌈ ⌉ túmọ̀ sí iṣẹ́ àárọ̀ (ceiling function).
(Book VI §3 STEP C)

---

## 3. Structural Influence (SI)

```math
SI = CW + OA + log(1 + DWP)
```

(Annex E §2.3)

---

## 4. Coherence Stake (CS)

```math
CS = RH_weighted + AC_weighted + SDA_bonus
```

(Annex E §3.3)

---

## 5. Voting Weight

```math
VotingWeight(agent) = f(SI(agent), CS(agent))
```

(Annex E §4)

---

## 6. Defense Function (J)

```math
J = k_eff · λ · σ

k_eff = k / (1 + ρ̄ · (k − 1))
```

(Book IX Ch 4 — irú tó jẹ́rìí sí CCA; oríṣiríṣi náà wọ inú nípasẹ̀ k_eff nìkan. Àwọn àkọsílẹ̀ ìjímìjí gbe ìpínrọ̀ (1 − ρ̄) àfikún kan, èyí tó ṣe ìkà ìbáṣepọ̀ lẹ́ẹ̀mejì; wo àkọsílẹ̀ ìyípadà Book IX Ch 4.)

---

## 7. Flourishing Capacity (C)

```math
C = k_eff · λ · σ
```

(Book IX Ch 6 — ó jọra pẹ̀lú J ní gbogbo ọ̀nà; a túmọ̀ rẹ̀ gẹ́gẹ́ bí ohun tó ń ṣẹ̀dá kì í ṣe gẹ́gẹ́ bí ohun ìdáàbòbò.)

---

## 8. Sustainability Integral (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

níbi tí d jẹ́ ìwọ̀n ìbàjẹ́ ojoojúmọ́ (a dábàá 0.05) àti w GBỌ́DỌ̀ jẹ yíyọ jáde lọ́wọ́ àwọn ìṣẹ̀lẹ̀ tó ti jẹ́rìísi tí ó ṣoro láti parọ; àwọn ìfúnni tí a kò ṣèrìíyìn fún ni w = 0.
(Book IX §5.2)

---

## 9. Topological Collapse (volume decay)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

fún àgbègbè ẹ̀tàn tó dín padà (convex deceptive region) tí rédíọ̀sì r < 0.5 lábẹ́ àwọn ìdíwọ̀n Grassmannian-uniform, λ ≈ 2r.
(Book IX Ch 3 — wo àwọn ìṣáájú tó dábọ̀.)

---

## Order‑Maximisation Veto (ìdíwọ̀ ìhà, kì í ṣe fọ́múlà)

Ní 1.3, OMV (Book II §II Step 2) jẹ́ ìdíwọ̀ ìhà deontological, kì í ṣe àìdọ́gba ipin: àwọn anfàní ìmúnadara, bí wọ́n ṣe tóbi tó, kò lè ra ara wọn nípasẹ̀ àwọn ìdínkù tí a sọ àsọtẹ́lẹ̀ tó ṣe pàtàkì nínú òmìnira, ìdájọ́ òdodo, ìpínpín ẹ̀dá àti oríṣiríṣi àwọn ààyò. Àwọn ẹ̀yà ìjímìjí gbé èyí jáde gẹ́gẹ́ bí àìdọ́gba "àǹfàní ≥ 10 × ìpàdánù → fòpin"; ìtumọ̀ yẹn ni a fágbàle nítorí pé ó yípadà ohun tí a fẹ́ (ó ń fi àwọn ìdúnàádúrà dáadáa dópin) àti pé ó ṣeéṣe láti ṣe eré rẹ̀ nípasẹ̀ pípin iṣẹ́ àti ìgbéga ìpín ìsàlẹ̀.

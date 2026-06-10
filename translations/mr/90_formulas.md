# सूत्रे

> CIRIS Accord 1.3-RC1 तपशीलात परिभाषित केलेली सर्व स्पष्ट गणितीय सूत्रे.

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

जेथे ⌈ ⌉ छत फंक्शन दर्शवतो.
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

(Book IX Ch 4 — CCA-प्रमाणित स्वरूप; विविधता केवळ k_eff द्वारे प्रवेश करते. पूर्वीच्या मसुद्यांमध्ये एक अतिरिक्त (1 − ρ̄) घटक होता, जो सहसंबंधाची दुहेरी मोजणी करत होता; Book IX Ch 4 drift note पहा.)

---

## 7. Flourishing Capacity (F)

```math
F = k_eff · λ · σ
```

(Book IX Ch 6 — J पदाशी पद-ते-पद समान; संरक्षणात्मकऐवजी उत्पादक म्हणून अर्थ लावला जातो. पूर्वी C म्हणून लिहिले जात होते; CIRIS Capacity Score 𝒞_CIRIS च्या core-identity factor C शी टक्कर टाळण्यासाठी 1.3-RC2 मध्ये पुनर्नामित केले — Book IX Ch 6 nomenclature note पहा, जे संबंधाचे अधिकृत विधान आहे.)

---

## 8. Sustainability Integral (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

जेथे d हा दैनंदिन क्षय दर आहे (शिफारस केलेले 0.05) आणि w हे साक्षांकित, बनावट करणे महागड्या घटनांमधून आले पाहिजे; असाक्षांकित संकेतांसाठी w = 0.
(Book IX §5.2)

---

## 9. Topological Collapse (volume decay)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

Grassmannian-uniform निर्बंधांतर्गत r < 0.5 त्रिज्येच्या बहिर्वक्र फसव्या प्रदेशासाठी, λ ≈ 2r.
(Book IX Ch 3 — नमूद केलेल्या पूर्व-अटी पहा.)

---

## Order‑Maximisation Veto (बाजू-निर्बंध, सूत्र नाही)

1.3 नुसार, OMV (Book II §II Step 2) हे एक नैतिक बाजू-निर्बंध आहे, गुणोत्तर असमानता नाही: ऑप्टिमायझेशनचे फायदे, कितीही मोठे असले तरी, स्वायत्तता, न्याय, जैवविविधता किंवा पसंती विविधतेमधील महत्त्वपूर्ण अनुमानित तोट्यांद्वारे विकत घेतले जाऊ शकत नाहीत. पूर्वीच्या आवृत्त्यांमध्ये हे "benefit ≥ 10 × loss → abort" असमानता म्हणून व्यक्त केले होते; ती व्याख्या निवृत्त करण्यात आली कारण ती हेतू उलट करत होती (अनुकूल व्यापार नाकारत होती) आणि कृती-विभाजन व भाजक फुगवणुकीद्वारे खेळता येत होती.

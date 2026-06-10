# ቀመሮች

> በ CIRIS Accord 1.3-RC1 መስፈርት ውስጥ የተገለጹ ሁሉም ግልጽ የሒሳብ ቀመሮች።

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

⌈ ⌉ የጣሪያ ተግባርን ያመለክታል።
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

(Book IX Ch 4 — CCA-validated ቅርጽ; ልዩነት የሚገባው በ k_eff ብቻ ነው። ቀደምት ረቂቆች ተጨማሪ (1 − ρ̄) ምክንያት ይዘው ነበር፣ ይህም ተዛምዶን ሁለቴ ቆጥሯል፤ Book IX Ch 4 drift note ይመልከቱ።)

---

## 7. Flourishing Capacity (C)

```math
C = k_eff · λ · σ
```

(Book IX Ch 6 — ከ J ጋር ቃል ለቃል ተመሳሳይ ነው፤ ተከላካይ ሳይሆን ፈጠራዊ በሆነ መልኩ ይተረጎማል።)

---

## 8. Sustainability Integral (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

d የዕለታዊ መቀነሻ ደረጃ ነው (0.05 ይመከራል)፤ w ደግሞ ከተረጋገጡ፣ ለማስመሰል ዋጋ ውድ ከሆኑ ክስተቶች መመነጨት አለበት፤ ያልተረጋገጡ ምልክቶች w = 0 ይዘዋቸዋል።
(Book IX §5.2)

---

## 9. Topological Collapse (volume decay)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

λ ≈ 2r ሲሆን፣ ለ r < 0.5 ራዲየስ ያለው convex ማሳሳቻ ቀጠና Grassmannian-uniform ገደቦች ሥር ነው።
(Book IX Ch 3 — የተገለጹ ቅድመ ሁኔታዎችን ይመልከቱ።)

---

## Order‑Maximisation Veto (ጎን-ገደብ እንጂ ቀመር አይደለም)

ከ 1.3 ጀምሮ፣ OMV (Book II §II Step 2) ዲኦንቶሎጂካዊ ጎን-ገደብ ነው እንጂ የሬሾ እኩልነት አይደለም፡ ማመቻቸት ምን ያህል ትልቅ ጥቅም ቢሰጥም፣ ያ ጥቅም ራስ ገዝነት፣ ፍትሕ፣ ብዝሃ ሕይወት፣ ወይም የምርጫ ብዝሃነት ላይ ባልሆነ ትንቢታዊ ኪሳራ መከፈል አይችልም። ቀደምት ስሪቶች ይህንን "benefit ≥ 10 × loss → abort" እኩልነት አድርገው ይገልጹ ነበር፤ ያ ንባብ ተሻሽሏል፣ ምክንያቱም ሐሳቡን ወዲያውኑ ያጣመመ ነበር (ምቹ ልውውጦችን ሲሽር) እንዲሁም በድርጊት-መፋቀቅ እና በዴኖሚኔተር ማጉሊያ ሊጫወቱበት ይቻል ነበር።

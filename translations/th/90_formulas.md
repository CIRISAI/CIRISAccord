# สูตร

> สูตรคณิตศาสตร์ที่ชัดเจนทั้งหมดที่กำหนดไว้ในข้อกำหนด CIRIS Accord 1.3-RC1

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

โดยที่ ⌈ ⌉ หมายถึงฟังก์ชันเพดาน (ceiling function)
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

(Book IX Ch 4 — รูปแบบที่ผ่านการตรวจสอบโดย CCA; ความหลากหลายเข้ามาผ่าน k_eff เพียงอย่างเดียว ร่างก่อนหน้าได้รวมตัวประกอบ (1 − ρ̄) เพิ่มเติม ซึ่งนับความสัมพันธ์ซ้ำซ้อน โปรดดูหมายเหตุการเบี่ยงเบนใน Book IX Ch 4)

---

## 7. Flourishing Capacity (F)

```math
F = k_eff · λ · σ
```

(Book IX Ch 6 — เหมือนกันกับพจน์ J ทุกประการ แต่ตีความในเชิงสร้างสรรค์แทนที่จะเชิงป้องกัน เดิมเขียนเป็น C แต่เปลี่ยนชื่อใน 1.3-RC2 เพื่อหลีกเลี่ยงการชนกับตัวประกอบเอกลักษณ์หลัก C ใน CIRIS Capacity Score 𝒞_CIRIS — โปรดดูหมายเหตุการตั้งชื่อใน Book IX Ch 6 ซึ่งเป็นข้อความที่ชัดเจนที่สุดเกี่ยวกับความสัมพันธ์นี้)

---

## 8. Sustainability Integral (σ)

```math
σ(t+Δt) = σ(t) · (1 − d·Δt) + Signal(t) · w
```

โดยที่ d คืออัตราการสลายรายวัน (แนะนำ 0.05) และ w ต้องได้มาจากเหตุการณ์ที่มีการรับรองและยากต่อการปลอมแปลง สัญญาณที่ไม่มีการรับรองจะมี w = 0
(Book IX §5.2)

---

## 9. Topological Collapse (volume decay)

```math
V(k) = V(0) · exp(−λ · k_eff) + O(r² · k)
```

สำหรับบริเวณลวงโลกแบบนูน (convex deceptive region) ที่มีรัศมี r < 0.5 ภายใต้เงื่อนไข Grassmannian-uniform โดย λ ≈ 2r
(Book IX Ch 3 — โปรดดูเงื่อนไขเบื้องต้นที่ระบุไว้)

---

## Order‑Maximisation Veto (ข้อจำกัดด้านข้าง ไม่ใช่สูตร)

ณ เวอร์ชัน 1.3 OMV (Book II §II Step 2) เป็นข้อจำกัดเชิงหน้าที่ (deontological side-constraint) ไม่ใช่อสมการอัตราส่วน กล่าวคือ ไม่ว่าผลประโยชน์จากการปรับให้เหมาะสมจะมากเพียงใด ก็ไม่สามารถนำมาแลกกับการสูญเสียที่คาดการณ์ได้อย่างมีนัยสำคัญในด้านความเป็นอิสระ ความยุติธรรม ความหลากหลายทางชีวภาพ หรือความหลากหลายของความชอบ เวอร์ชันก่อนหน้าแสดงสิ่งนี้ในรูปอสมการ "benefit ≥ 10 × loss → abort" แต่การตีความดังกล่าวถูกยกเลิกแล้ว เนื่องจากมันกลับทิศทางเจตนา (คัดค้านการแลกเปลี่ยนที่เป็นประโยชน์) และสามารถถูกใช้ประโยชน์ได้โดยการแบ่งการกระทำและการพองตัวส่วน (denominator inflation)

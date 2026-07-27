# G2 Errata Scan — position 200 (B3 → B4 boundary)

**Scan type**: batch-boundary (end of B3, start of B4)
**Curator**: G2
**Date**: 2026-07-22
**Framework**: v7.1 with HOT LOOKUP + sibling-bit HARD RULE (memory_index)

---

## Cooldown accounting

Per shared_rules v7: 50-item cooldown per retry. Items last retried at
`scan_position` ≥ 150 are checked:

- **scan_position 150** (B2 mid-scan): cooldown ends at pos 200 → **eligible now**.
- **scan_position 213** (B3-scan; label is anomalous — B3 was
  curated at end of the batch; treat as position ~200 event):
  cooldown ends at pos 250 → **NOT eligible now**.

Items blocked by cooldown this scan:
- p2_radical_080_尢 (retry_n=2, last scan 213)
- p2_radical_081_夂 (retry_n=2, last scan 213)
- p2_radical_083_丬 (retry_n=2, last scan 213)  ← unfortunate; 209 丬 upcoming
- p2_radical_089_车 (retry_n=2, last scan 213)
- p2_radical_093_方 (retry_n=2, last scan 213)
- p2_radical_094_风 (retry_n=2, last scan 213)
- p2_radical_099_旡 (retry_n=2, last scan 213)
- p2_radical_106_牛 (retry_n=2, last scan 213)
- p2_radical_109_攴 (retry_n=2, last scan 213)
- p2_radical_036_夂-in-B3 items (retry_n=2, last scan 213)

Items never retried (retry_n=0) — always eligible:
- All B2 items with retry_n=0 tag
- All B3 items (retry_n=0 tag)

---

## Upcoming curriculum scan (positions 201–250)

All Phase-3 characters, 3–4 stroke. Many are **same-as-radical**
overlaps with items in errata — direct (a) prospective triggers:

| upcoming pos | char | direct errata match | strength |
|--------------|------|---------------------|----------|
| 203 | 刂 | p2_radical_015_刀 & p3_char_0033_刀 | VERY STRONG |
| 205 | 匕 | p2_radical_011_匕 | VERY STRONG |
| 208 | 大 | p3_char_0011_人 (人-apex sibling) | STRONG |
| 209 | 丬 | p2_radical_083_丬 (COOLDOWN — cannot retry) | blocked |
| 210 | 个 | p3_char_0011_人 (人-apex under 亠) | STRONG |
| 211 | 丸 | p3_char_0023_九 (九 is body of 丸) | VERY STRONG |
| 216 | 子 | p3_char_0009_了 (子 = 了 + 一) | VERY STRONG |
| 217 | 亍 | p2_radical_133_止 (亍 upper) | MODERATE |
| 229 | 门 | p2_radical_059_门 | VERY STRONG |
| 231 | 及 | p3_char_0016_乃 (乃-body inside 及); p2_radical_015_刀 | STRONG |
| 235 | 干 | p2_radical_048_干 | VERY STRONG |
| 236 | 夂 | p2_radical_081_夂 (COOLDOWN — blocked) | blocked |
| 238 | 夊 | p2_radical_084_夊 | VERY STRONG |
| 239 | 飞 | p2_radical_047_飞 | VERY STRONG |
| 240 | 孑 | p3_char_0009_了 (孑 = 子 with detail) | STRONG |
| 242 | 孓 | p3_char_0009_了 (arm-variant of 子) | STRONG |
| 245 | 已 | p2_radical_053_己 (直接 sibling — signature-bit-test) | VERY STRONG |
| 248 | 尢 | p2_radical_080_尢 (COOLDOWN — blocked) | blocked |

---

## Decisions

### RETRY (14 items) — balance, not minimalism

Grouped by rationale:

**Group 1 — direct same-char upcoming (a: VERY STRONG)**

1. **p2_radical_011_匕** (retry_n=3 → 4)
   - (a): pos 205 匕 is the exact same character; retry is a rehearsal.
   - Fix per errata: 撇 body must overlap 竖, endpoint at x≈70 clearly
     LEFT of 竖 with body crossing.
   - Risk: retry_n=4 is high, but the direct upcoming match justifies
     one more attempt with sibling-pair table now HARD-ruled.

2. **p2_radical_047_飞** (retry_n=1 → 2)
   - (a): pos 239 飞 is the exact same character.
   - (b): form_catalog KEY PRIMITIVE 横折弯钩 is now proven; new inside-
     dot recipe from errata.

3. **p2_radical_048_干** (retry_n=2 → 3)
   - (a): pos 235 干 exact same character.
   - (b): form_catalog "竖 as through-going axis" — the 竖 must extend
     BELOW the bottom 横; move top 横 down to y≈85.

4. **p2_radical_059_门** (retry_n=0 → 1)
   - (a): pos 229 门 exact same character; also 229 is directly in the
     next 25 items.
   - (b): form_catalog "横 as top-lid" + "横折 top-right corner" cover
     the gap-at-top fix.

5. **p2_radical_084_夊** (retry_n=0 → 1)
   - (a): pos 238 夊 exact same character.
   - (b): form_catalog "捺 as right-leg" applies to bottom stroke.

**Group 2 — sibling upcoming (a: STRONG)**

6. **p2_radical_053_己** (retry_n=1 → 2)
   - (a): pos 245 已 is己/已/巳 sibling — form_catalog sibling-pair
     table row 己/已/巳 explicitly codified since prior fail.
   - (b): HARD RULE now: signature bit = whether middle 横 touches
     left wall. Do not over-reason — render the bit.

7. **p2_radical_133_止** (retry_n=0 → 1)
   - (a): pos 212 上 (止/上 share topology), pos 217 亍 upper.
   - (b): form_catalog "竖 as through-going axis" + top 卜 recipe.

8. **p3_char_0009_了** (retry_n=0 → 1)
   - (a): pos 216 子 = 了 + 一; pos 240 孑; pos 242 孓 — three
     upcoming characters use 了 as base. Highest downstream leverage
     of any single retry.
   - (b): form_catalog "撇 as body-crossing diagonal" and terminal
     hook rules from drawer_memory.

9. **p3_char_0011_人** (retry_n=0 → 1)
   - (a): pos 208 大, pos 210 个 both embed 人-topology.
   - (b): HARD RULE at top of memory_index (v7.1) added specifically
     for this failure — "signature-bit override" prevents the previous
     over-reasoning collapse.

10. **p3_char_0016_乃** (retry_n=0 → 1)
    - (a): pos 231 及 has 乃-body inside; 及 = 丿 + 乃-like body.
    - (b): drawer_memory batch-2 mastery entry for 横折折撇 has the
      exact recipe; new form_catalog "折 shoulder placement" family.

11. **p3_char_0021_几** (retry_n=0 → 1)
    - (a): pos 229 门 shares 冂/几 bracket topology; also pos 211 丸
      envelops a hook-family shape.
    - (b): new form_catalog "撇 + 竖弯钩 as leg-pair under a lid"
      B3 addition — first attempt at leg-pair primitive for a
      standalone glyph.

12. **p3_char_0023_九** (retry_n=0 → 1)
    - (a): pos 211 丸 = 九 + 丶. Direct compositional prerequisite.
    - (b): same KEY PRIMITIVE (横折弯钩) recipe as 飞/几.

13. **p3_char_0029_入** (retry_n=0 → 1)
    - (b) STRONG: this is the ORIGINAL signature-bit-override failure
      that motivated the v7.1 HARD RULE. Retry is the direct test of
      whether the HARD RULE breaks the loop.
    - (a): weak — no direct 入-body in upcoming 25, but 入-topology
      shows up in 210 个 approximately.

14. **p3_char_0033_刀** (retry_n=0 → 1)
    - (a) VERY STRONG: pos 203 刂 is the 刀-radical variant — same
      shape modulo the 撇 length.
    - (b): form_catalog "撇 as body-crossing diagonal" +
      joining-dab discipline.

### SKIP — items with cooldown blocking or weak (a)/(b)

**Cooldown-blocked (would-be strong (a))**:
- p2_radical_083_丬 — pos 209 丬 upcoming; blocked until 250.
  Painful skip but rule is rule.
- p2_radical_081_夂 — pos 236 夂 upcoming; blocked. Same regret.
- p2_radical_080_尢 — pos 248 尢 upcoming; blocked.

**No prospective and no new insight** (skip until (b) arrives):
- p1_stroke_24_横撇弯钩 — belly-on-right arc still unproven.
- p1_stroke_32_横折折折钩 — retry_n=2; no new multi-fold primitive.
- p2_radical_020_阝 — depends on belly-on-right arc (still unproven).
- p2_radical_032_厶 — no direct upcoming; skip.
- p2_radical_042_巛 — no upcoming; skip.
- p2_radical_050_弓 — no upcoming; skip.
- p2_radical_055_彑 — no upcoming; skip.
- p2_radical_056_巾 — no upcoming; skip.
- p2_radical_067_士 — 士 not in next 25; retry-n=1 already, subtle
  length-ratio fix — skip this scan.
- p2_radical_058_马 — no upcoming; skip.
- p2_radical_078_幺 — no upcoming; skip.
- p2_radical_085_贝 — no upcoming; skip.
- p2_radical_086_比 — depends on 匕 mastery first; skip until 匕 is
  proven this scan.
- p2_radical_088_长 — no upcoming; skip.
- p2_radical_092_厄 — no upcoming; skip.
- p2_radical_096_戈 — no upcoming; skip.
- p2_radical_097_户 — no upcoming; skip.
- p2_radical_100_见 — no upcoming; skip.
- p2_radical_101_斤 — no upcoming; skip.
- p2_radical_102_耂 — no upcoming; skip.
- p2_radical_105_肀 — no upcoming; skip.
- p2_radical_107_爿 — no direct upcoming (丬 is cooldown-blocked;
  爿 is 丬 mirror); skip until 丬 opens up.
- p2_radical_108_片 — no upcoming; skip.
- p2_radical_110_攵 — no upcoming; skip.
- p2_radical_115_氏 — no upcoming; skip.
- p2_radical_116_礻 — no direct upcoming; skip.
- p2_radical_015_刀 — subsumed by fresher p3_char_0033_刀; skip the
  older one to avoid double-attempting the same shape.
- p2_radical_030_入 — subsumed by p3_char_0029_入; skip older.
- p2_radical_119_水 — no upcoming; skip.
- p2_radical_120_瓦 — no upcoming; skip.
- p2_radical_121_尣 — 尢/尣 sibling but 尢 is cooldown-blocked; skip.
- p2_radical_123_韦 — no upcoming; skip.
- p2_radical_125_毋 — no upcoming; skip.
- p2_radical_127_牙 — no upcoming; skip.
- p2_radical_131_爫 — no upcoming; skip.
- p2_radical_132_支 — 攴 cooldown-blocked; 支 alone lacks upcoming;
  skip.
- p2_radical_134_爪 — no upcoming; skip.
- p3_char_0006_乚 — no upcoming; skip.
- p3_char_0010_丩 — no upcoming; skip.
- p3_char_0018_乜 — 也 (pos 214) is a sibling but 乜's failure is
  a two-stroke minimalism issue; low prospective value this scan.

---

## Summary

- **Errata size at scan**: ~55 open items.
- **Retries scheduled**: 14.
- **Retry rate**: 14/55 ≈ 25%.
- **Reason distribution**: 13 with strong (a), 1 with strong (b) only.
- **Cooldown-blocked strong-(a) items** (regret list): 丬, 夂, 尢.
  These would have been retries if timing allowed; queued for next
  scan at pos 225 (mid-B4).
- **Balance check**: prior scan (pos 150) attempted 20; prior-to-prior
  (pos 100) attempted 12. This scan at 14 is mid-range — appropriate
  given (a) triggers are unusually dense in the next 25.

Expected pass rate: 5–8 of 14 (based on B3's 4/13 = 31% baseline plus
the v7.1 HARD RULE lift and the density of direct same-char upcomings).

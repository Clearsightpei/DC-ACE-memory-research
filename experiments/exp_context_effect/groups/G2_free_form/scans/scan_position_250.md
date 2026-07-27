# G2 Errata Scan — position 250 (B4 → B5 boundary)

**Scan type**: batch-boundary (end of B4, start of B5)
**Curator**: G2
**Date**: 2026-07-23
**Framework**: v7.2 (adds `sibling_signature_checklist.md` — copy-verbatim protocol for sibling-risk targets)

---

## Cooldown accounting

Per shared_rules v7: 50-item cooldown per retry.

- **scan_position 150**: cooldown ends at pos 200 — items already off cooldown
  (were checked at 200, several retried).
- **scan_position 200**: cooldown ends at pos 250 → **items just retried this
  cycle are BLOCKED until pos 300**.
- **scan_position 213** (chronic-cluster items retried at end of B3): cooldown
  ends at pos 250 → **NOW ELIGIBLE** (this is the key cohort unblocked this scan).

### Blocked this scan (retried at pos 200, cooldown until pos 300)

- p2_radical_011_匕 (retry_n=4)
- p2_radical_047_飞 (retry_n=3)
- p2_radical_053_己 (retry_n=3)
- p2_radical_059_门 (retry_n=2)
- p2_radical_084_夊 (retry_n=2)
- p3_char_0009_了 (retry_n=2)
- p3_char_0011_人 (retry_n=2) — CANDIDATE DISAGREEMENT
- p3_char_0016_乃 (retry_n=2)
- p3_char_0021_几 (retry_n=2) — CANDIDATE DISAGREEMENT
- p3_char_0023_九 (retry_n=2)
- p3_char_0033_刀 (retry_n=2) — CANDIDATE DISAGREEMENT

### Newly OFF cooldown (retried at pos 213)

- p2_radical_080_尢 (retry_n=2)
- p2_radical_081_夂 (retry_n=2)
- p2_radical_083_丬 (retry_n=2)
- p2_radical_089_车 (retry_n=2)
- p2_radical_093_方 (retry_n=2)
- p2_radical_094_风 (retry_n=2)
- p2_radical_099_旡 (retry_n=2)
- p2_radical_106_牛 (retry_n=2)
- p2_radical_109_攴 (retry_n=2)

### Off cooldown from earlier (never retried since pos 100/150)

- p2_radical_067_士 (retry_n=1, last 150)
- p2_radical_058_马 (retry_n=1, last 150)
- All retry_n=0 items — always eligible

---

## Upcoming curriculum 251–300 — same-as-radical direct triggers (a)

Phase-3 3-4-stroke band, dense with radical-derived characters.

| pos | char | direct errata match | strength |
|-----|------|---------------------|----------|
| 252 | 马  | p2_radical_058_马 | VERY STRONG |
| 253 | 巛  | p2_radical_042_巛 | VERY STRONG |
| 258 | 乡  | p2_radical_078_幺 (related 撇折-loop family) | MODERATE |
| 267 | 中  | p2_radical_056_巾 (adjacent 冂-center-竖 topology) | MODERATE |
| 271 | 方  | p2_radical_093_方 | VERY STRONG (off cooldown) |
| 273 | 日  | no direct errata | — |
| 275 | 无  | p2_radical_099_旡 (旡/无 direct siblings; 无 passed at 167) | VERY STRONG |
| 279 | 心  | no direct errata (忄 graduated B3) | — |
| 281 | 见  | p2_radical_100_见 | VERY STRONG |
| 283 | 公  | 八-family; no direct match | — |
| 285 | 从  | 人-family; p3_char_0011_人 (BLOCKED — cooldown) | — |
| 287 | 气  | no direct errata (气/飞 hook-family cousins) | WEAK |
| 291 | 文  | no direct errata (passed) | — |
| 293 | 长  | p2_radical_088_长 | VERY STRONG |
| 294 | 冈  | p2_radical_094_风 (风/冈 direct siblings per errata) | VERY STRONG (off cooldown) |
| 295 | 太  | 大 in checklist, no errata match | — |
| 297 | 切  | 七+刀; 七 in checklist, 刀 BLOCKED | — |
| 299 | 内  | 冂+人 hybrid; MODERATE relation to 丸/几 (BLOCKED) | — |

---

## v7.2 retrospective (b) — sibling_signature_checklist targets

New file surfaces bright-line-bits and bright-line-flicks. Cross-check
errata items whose failure mode was a **sibling-bit collapse** or a
**flick-direction failure**:

| errata item | failure was | checklist row | eligible? |
|-------------|-------------|---------------|-----------|
| p2_radical_067_士 | 士→土 length collapse | 士 top-longer bit | YES (last 150) |
| p2_radical_080_尢 | 尢→九 (missing lid) | 尢 vs 九 lid-bit | YES (last 213) |
| p2_radical_081_夂 | 捺 not dominating | flick + 捺 rule | YES |
| p2_radical_083_丬 | brackets not touching | 竖-through axis (no direct row) | MARGINAL |
| p2_radical_089_车 | symmetric-王 collapse | 横 differential (no direct row) | MARGINAL |
| p2_radical_093_方 | narrow body | 亠-lid; no direct row | MARGINAL |
| p2_radical_094_风 | boxy corner | flick UP-LEFT rule for 横折弯钩 | YES |
| p2_radical_099_旡 | ambiguous with 无 | 无 not on checklist (旡 not either) | WEAK |
| p2_radical_106_牛 | subtle length ratio | not on checklist | NO |
| p2_radical_109_攴 | halves fused | not on checklist | NO |

---

## Decisions

### RETRY (13 items) — balance, not minimalism

**Group 1 — direct same-char upcoming (a: VERY STRONG)**

1. **p2_radical_058_马** (retry_n=1 → 2)
   - (a): pos 252 马 exact same character.
   - (b): drawer_memory beat-count rule + form_catalog 折-shoulder;
     prior fix "bottom 横 through" needs body-height also increased.

2. **p2_radical_042_巛** (retry_n=0 → 1)
   - (a): pos 253 巛 exact same character.
   - (b): errata already spells the ㄑ-shape recipe — three small
     compound loops side by side.

3. **p2_radical_093_方** (retry_n=2 → 3)
   - (a): pos 271 方 exact same character.
   - (b): NOW off cooldown; form_catalog "撇 as top-lid" for 亠 +
     body width ≥ 70% canvas fix from B3 diagnosis.

4. **p2_radical_099_旡** (retry_n=2 → 3)
   - (a): pos 275 无 direct sibling (无 passed at 167 with same 二 top
     + splayed legs). Copy 无's layout verbatim.
   - (b): form_catalog "二 as top-of-radical stacked pair" + "撇 +
     竖弯钩 as leg-pair under a lid".

5. **p2_radical_100_见** (retry_n=0 → 1)
   - (a): pos 281 见 exact same character.
   - (b): NEW v7.2 sibling_signature_checklist row 贝-vs-见 directly
     codifies "ONE 横 + ㄦ legs" bit — the exact failure mode
     (missing inside 一 or missing 竖弯钩 sweep).

6. **p2_radical_088_长** (retry_n=0 → 1)
   - (a): pos 293 长 exact same character.
   - (b): form_catalog + radical_position_rules "square" family; the
     4-stroke recipe is spelled in errata.

7. **p2_radical_094_风** (retry_n=2 → 3)
   - (a): pos 294 冈 is direct sibling per errata diagnosis (风/冈
     confusion was the exact original failure — attempt read as 冈).
   - (b): NOW off cooldown; drawer_memory 横折弯钩 KEY PRIMITIVE +
     v7.2 flick-checklist row (up-and-left ~-115°) directly targets
     the boxy-right-angle failure.

**Group 2 — sibling-checklist retrospective (b: STRONG)**

8. **p2_radical_080_尢** (retry_n=2 → 3)
   - (a): 尢 sibling not in next 50 directly, but 尢 vs 九 sibling
     row surfaces in checklist and 275 无 shares leg-splay pattern.
   - (b) STRONG: NEW checklist row "尢: 一 top + 撇 + 竖弯钩 (3
     strokes with LID)" IS the exact bit the prior fail missed
     (missing 一 lid → reads as 九). Copy-verbatim protocol.

9. **p2_radical_081_夂** (retry_n=2 → 3)
   - (a): moderate — 夊 was blocked, 夂 not in next 50 directly.
   - (b): flick-checklist plus errata's specific fix (short 撇 ≈50 px,
     long 捺 ≈150 px with broad foot) is a knob-move-further attempt.

10. **p2_radical_067_士** (retry_n=1 → 2)
    - (b) STRONG: NEW v7.2 checklist row 士/土 gives the bit verbatim
      ("TOP 横 LONGER than bottom ~1.5×"). Prior fail was subtle
      ratio (140/120); apply "move the knob further" — 160/100.
    - (a): weak — 士 not in next 50; but the checklist row transfers
      directly to any future 士/土 discrimination.

**Group 3 — sibling-checklist for chronic hook-flick failures (b: STRONG)**

11. **p2_radical_089_车** (retry_n=2 → 3)
    - (a): weak — 车 not in next 50.
    - (b): form_catalog "竖 as through-going axis" + errata's specific
      "shoulder-竖 drop must be visible" fix; retry with the
      differential-横-lengths knob pushed further.

12. **p2_radical_106_牛** (retry_n=2 → 3)
    - (b) STRONG: apply "move-the-knob-further" rule from drawer_memory
      — errata specifies exaggerated 65 vs 165 ratio, not tweak.
    - (a): weak — 牛 not in next 50.

13. **p2_radical_109_攴** (retry_n=2 → 3)
    - (a): moderate — 支 (its modern form, also in errata retry_n=0)
      shares failure mode; fix here validates for 支.
    - (b): errata already codifies the 20-px whitespace band between
      halves. Deterministic fix; low-risk retry.

### SKIP — cooldown-blocked or weak (a)/(b)

**Cooldown-blocked (would-be strong)**:
- p2_radical_011_匕 (BLOCKED until pos 300) — pos 297 切 has 七 top;
  匕/七 checklist bit is HOT but retry is blocked.
- p2_radical_053_己 (BLOCKED) — pos 245 already handled last scan.
- p2_radical_059_门 (BLOCKED) — no more 门-family upcoming.
- p2_radical_084_夊 (BLOCKED)
- p2_radical_047_飞 (BLOCKED) — pos 287 气 is HOT (气/飞 hook-family
  cousins); regret skip.
- p3_char_0009_了, 人, 乃, 几, 九, 刀 (all BLOCKED) — pos 285 从
  and pos 295 太 are 人-family; regret skip on 人.

**No prospective + no meaningful new (b)**:
- p1_stroke_24_横撇弯钩 — belly-on-right arc still unproven.
- p1_stroke_32_横折折折钩 — retry_n=2, no new multi-fold primitive.
- p2_radical_020_阝 — depends on belly-on-right arc.
- p2_radical_032_厶 — no upcoming.
- p2_radical_050_弓 — no upcoming.
- p2_radical_055_彑 — no upcoming.
- p2_radical_056_巾 — 中 (267) is only marginal sibling; skip.
- p2_radical_078_幺 — 乡 (258) is 3-loop version, but 幺 itself
  never proven; low upside, skip.
- p2_radical_083_丬 — off cooldown but no direct upcoming (mirror 爿
  not in 251-300); regret skip.
- p2_radical_085_贝 — no upcoming; skip.
- p2_radical_086_比 — depends on 匕 (BLOCKED); skip.
- p2_radical_092_厄 — no upcoming; skip.
- p2_radical_096_戈 — no upcoming; skip.
- p2_radical_097_户 — no upcoming; skip.
- p2_radical_101_斤 — no upcoming; skip.
- p2_radical_102_耂 — no upcoming; skip.
- p2_radical_105_肀 — no upcoming; skip.
- p2_radical_107_爿, 108_片, 110_攵, 115_氏, 116_礻 — no upcoming.
- p2_radical_015_刀, 030_入 — subsumed by p3 versions (blocked); skip.
- p2_radical_119_水, 120_瓦, 121_尣, 123_韦, 125_毋, 127_牙, 131_爫,
  132_支, 134_爪 — no direct upcoming; skip. (支 could ride with 攴
  fix if 攴 passes, but attempting both is redundant this scan.)
- p3 B4 additions (0042_丬, 0043_个, 0044_丸, 0046_久, 0047_也,
  0049_子, 0056_亾, 0059_么, 0060_卂, 0061_与, 0065_及, 0068_纟,
  0069_干, 0072_夊, 0073_飞, 0074_孑, 0076_孓, 0077_习, 0079_已,
  0081_女, 0082_尢) — most retry_n=0, but their upcoming-siblings
  are either (i) BLOCKED cooldown items covering the same shape or
  (ii) not in next 50. Skip this scan; reconsider at pos 275
  mid-scan or pos 300.

---

## Summary

- **Errata size at scan**: ~57 open items.
- **Retries scheduled**: **13**.
- **Retry rate**: 13/57 ≈ 23%.
- **Reason distribution**: 7 strong (a) + 6 strong (b, mostly v7.2
  checklist-driven).
- **Cooldown-blocked strong-(a) regret list**: 匕 (297 切), 飞 (287 气),
  人 (285 从 / 295 太), 刀 (297 切). These four are the highest-value
  BLOCKED items; queued for pos 300 scan.
- **New signal to watch**: 6 of 13 retries directly cite the NEW
  `sibling_signature_checklist.md`. If retry pass rate on these
  rises above B4's 21% baseline (target ≥ 40%), that's evidence the
  copy-verbatim protocol lifts sibling-bit and flick-direction
  failures. If it stays flat or drops, checklist is not yet delivering
  the intended lift.
- **Balance check**: prior scan (pos 200) attempted 14; this scan at
  13 is comparable — appropriate given (a) triggers are less dense
  than 201-250, but sibling-checklist retrospective adds a full new
  layer of (b) reasons.

Expected pass rate: 4–6 of 13 (B4 baseline 21% + v7.2 lift on
checklist-cited items).

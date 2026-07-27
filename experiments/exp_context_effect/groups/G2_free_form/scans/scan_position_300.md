# G2 Errata Scan — position 300 (B5 → B6 boundary)

**Scan type**: batch-boundary (end of B5, start of B6)
**Curator**: G2
**Date**: 2026-07-24
**Framework**: v7.3 (adds `composition_rules.md` and `frozen_cohort.md`
— per evolution.md pos 326)

---

## B5 self-evolution follow-through — files landed at this scan

1. **`frozen_cohort.md`** CREATED — 7 items formally frozen:
   马, 尢, 夂, 车, 风, 旡, 牛. They are REMOVED from the retry
   scan cohort and do not count against retry-pass-rate denominators.
2. **`composition_rules.md`** CREATED — 5 composition families (亻+X,
   人-lid+X, 冂+interior, 亠+X, 阝+X). B6 hypothesis: compound-char
   main-pass rate ≥ 60% if drawers cite it.

**B5 hard commitment (per prompt + evolution.md pos 326)**: if B6
misses EITHER retry ≥30% OR compound-char main ≥60%, the next
postmortem MUST retire the retry mechanism (Option 3) or accept
the ceiling (Option 4). No more additive interventions.

---

## Cooldown accounting

Per shared_rules v7: 50-item cooldown per retry (measured from attempt
position, not scan_position).

### Blocked this scan (attempted during B5, cooldown until pos 350)

Items retried during B5 (scan_position=250 in retry_log, attempts
executed at positions 251–300):

- p2_radical_042_巛 (retry_n=2, failed B5)
- p2_radical_100_见 (retry_n=2, failed B5)
- p2_radical_088_长 (retry_n=2, failed B5)

Plus all FROZEN items (excluded permanently from cohort).

### Newly OFF cooldown (retried during B4 at scan 200, cooldown
expired at pos 250; not retried in B5)

- p2_radical_011_匕 (retry_n=4)
- p2_radical_047_飞 (retry_n=3)
- p2_radical_053_己 (retry_n=3)
- p2_radical_059_门 (retry_n=2)
- p2_radical_084_夊 (retry_n=2)
- p3_char_0009_了 (retry_n=2)
- p3_char_0011_人 (retry_n=2)
- p3_char_0016_乃 (retry_n=2)
- p3_char_0021_几 (retry_n=2)
- p3_char_0023_九 (retry_n=2)
- p3_char_0033_刀 (retry_n=2)

### Off cooldown from earlier (never retried since 150/200)

- All retry_n=0 items in errata — always eligible.
- p1_stroke_24_横撇弯钩 (still blocked by "belly-on-right arc unproven"
  memo — internal skip rule, not cooldown).

### FROZEN (never eligible)

- p2_radical_058_马, _080_尢, _081_夂, _089_车, _094_风, _099_旡,
  _106_牛. See frozen_cohort.md.

---

## Upcoming curriculum 301–350 — same-as-radical direct triggers (a)

Phase-3 3-4-stroke band (with a few 5-stroke) — many characters
overlap with radicals in errata.

| pos | char | direct errata match | strength |
|-----|------|---------------------|----------|
| 301 | 化  | p2_radical_028_人 (graduated) + 匕 body | MODERATE (via 匕) |
| 302 | 刅  | p3_char_0033_刀 + 刂 variant | STRONG |
| 303 | 比  | p2_radical_086_比 + p2_radical_011_匕 (匕+匕) | VERY STRONG |
| 304 | 刈  | 刂 variant; no direct 乂 in errata | WEAK |
| 305 | 水  | p2_radical_119_水 | VERY STRONG |
| 306 | 礻  | p2_radical_116_礻 | VERY STRONG |
| 307 | 反  | 厂 (graduated B1) + 又 | MODERATE |
| 308 | 办  | 力-family; 力 graduated B2 | WEAK |
| 309 | 区  | 匚 bracket + 乂 body | MODERATE |
| 310 | 勻  | 勹 body + interior 二 | MODERATE (勹 in form_catalog only) |
| 311 | 风  | FROZEN (p2_094) — main attempt only, no retry | — |
| 312 | 勿  | 勹 + interior 撇×3; no direct errata | WEAK |
| 313 | 队  | p2_radical_020_阝 + 人 body | VERY STRONG |
| 314 | 卅  | 卄-family; no direct errata | WEAK |
| 315 | 书  | complex; no direct errata | WEAK |
| 316 | 升  | 卄-like + 撇; no direct errata | WEAK |
| 317 | 引  | p2_radical_050_弓 + 竖 | VERY STRONG |
| 318 | 卞  | 卜 top + 一; 卜-adjacent | WEAK |
| 319 | 元  | 二 top + 儿-legs (form_catalog covers) | WEAK (form ok) |
| 320 | 卬  | rare; no direct errata | WEAK |
| 321 | 他  | 亻 + 也; 亻 graduated, 也 in errata | MODERATE (also composition_rules 亻+X) |
| 322 | 必  | 心 + 撇; 心 in form_catalog | MODERATE |
| 323 | 们  | 亻 + 门; both in errata (门 blocked earlier) | MODERATE |
| 324 | 甲  | 田-based, form_catalog has 曰 entry | WEAK |
| 325 | 出  | 山 stacked pair; no direct errata | WEAK |
| 326 | 申  | 田 + 竖; form_catalog | WEAK |
| 327 | 可  | 一 + 口 + 亅; form_catalog | WEAK |
| 328 | 甴  | rare; no direct errata | — |
| 329 | 生  | 牛-adjacent (frozen); different topology | WEAK |
| 330 | 丱  | rare; no direct errata | — |
| 331 | 对  | 又 + 寸-like; no direct | WEAK |
| 332 | 乍  | complex 一+丨 combo; no direct | WEAK |
| 333 | 去  | 土 + 厶; form_catalog | WEAK |
| 334 | 乎  | 4-stroke complex; no direct | WEAK |
| 335 | 用  | 冂 + interior 三; composition_rules 冂 family | MODERATE |
| 336 | 疋  | 5-stroke; no direct | WEAK |
| 337 | 发  | 又-body + complex; no direct | WEAK |
| 338 | 疒  | 广-family + 冫; no direct | WEAK |
| 339 | 只  | 口 + 八; form_catalog | WEAK |
| 340 | 仔  | 亻 + 子 (子 in errata) | MODERATE (composition_rules 亻+X) |
| 341 | 主  | 亠-adjacent + 王 (graduated) | WEAK |
| 342 | 仕  | 亻 + 士 (graduated B5) | MODERATE (composition_rules 亻+X) |
| 343 | 平  | 干-adjacent (干 graduated B4) | MODERATE |
| 344 | 仗  | 亻 + 丈; 亻 graduated | MODERATE (composition_rules 亻+X) |
| 345 | 外  | 夕 + 卜; form_catalog | WEAK |
| 346 | 付  | 亻 + 寸; 亻 graduated | MODERATE (composition_rules 亻+X) |
| 347 | 打  | 扌 + 丁; form_catalog | WEAK |
| 348 | 仝  | 人-lid + 工 | MODERATE (composition_rules 人-lid+X) |
| 349 | 正  | 一 + 止 (止 graduated B4) | MODERATE |
| 350 | 仞  | 亻 + 刃 | MODERATE (composition_rules 亻+X) |

---

## Retrospective (b) — new leverage from B5

Two new files landed this position:
- **`composition_rules.md`** — targets 亻+X, 人-lid+X, 冂+interior,
  亠+X, 阝+X compounds. Directly addresses B5 main-fail cluster
  (仇, 仑, 仓, 内, 內, 亢, 分).
- **`frozen_cohort.md`** — removes 7 items from retry cohort denominator.

Errata items whose failure mode is now addressed by composition_rules:

| errata item | family in composition_rules | eligible? |
|-------------|------------------------------|-----------|
| p3_char_0111_仇 (B5 main-fail, retry_n=0) | 亻+X (nine body) | YES |
| p3_char_0117_仑 (B5 main-fail, retry_n=0) | 人-lid+X | YES |
| p3_char_0119_仓 (B5 main-fail, retry_n=0) | 人-lid+X | YES |
| p3_char_0103_亢 (B5 main-fail, retry_n=0) | 亠+X | YES (but no B6 亢/亠 sibling) |
| p3_char_0110_分 (B5 main-fail, retry_n=0) | 八+刀 (not covered) | MARGINAL |
| p3_char_0121_內 (B5 main-fail, retry_n=0) | 冂+interior | YES (335 用 shares family) |
| p3_char_0132_内 (B5 main-fail, retry_n=0) | 冂+interior | YES (335 用) |

---

## Decisions

### RETRY (11 items) — balance, not minimalism

**Group 1 — direct same-char upcoming (a: VERY STRONG)**

1. **p2_radical_086_比** (retry_n=0 → 1)
   - (a) VERY STRONG: pos 303 比 exact same character.
   - (b) 比 = 匕+匕 side-by-side; sibling_signature_checklist 匕 row
     applied twice + form_catalog "撇 as body-crossing diagonal" for
     each 匕 body.

2. **p2_radical_119_水** (retry_n=0 → 1)
   - (a) VERY STRONG: pos 305 水 exact same character.
   - (b) form_catalog 亅 (through-竖) + 撇/捺 leg-pair; 4-stroke
     water recipe with central 亅 dominant.

3. **p2_radical_116_礻** (retry_n=0 → 1)
   - (a) VERY STRONG: pos 306 礻 exact same character.
   - (b) 礻 = 丶 + 一 + 亅 + 撇 + 丶 (5-stroke show-radical); form_catalog
     'top-lid 丶' + 'through-going 亅' cover the recipe.

4. **p2_radical_050_弓** (retry_n=0 → 1)
   - (a) VERY STRONG: pos 317 引 = 弓 + 竖 (direct compositional
     prerequisite).
   - (b) form_catalog folder-family (横折折折钩 is 弓's spine) + 3-fold
     zigzag body; drawer_memory beat-count rule applies.

5. **p2_radical_020_阝** (retry_n=0 → 1)
   - (a) VERY STRONG: pos 313 队 = 阝 + 人 (direct); pos 313 is the
     earliest 阝-compound in P3.
   - (b) **NEW composition_rules.md 阝+X family** first-test; if
     阝 lands here, 队 becomes an easy composition. Belly-on-right
     arc still an internal risk but form_catalog + composition_rules
     give a fresh recipe.

**Group 2 — direct upcoming via compositional prerequisite (a: STRONG)**

6. **p2_radical_011_匕** (retry_n=4 → 5)
   - (a) VERY STRONG: pos 303 比 = 匕+匕. Chart-level: 匕 has
     failed 4× but the 比 upcoming makes this the highest-leverage
     retry — passing 匕 nets both 匕 AND 比.
   - (b) sibling_signature_checklist 匕 row copy-verbatim protocol
     (top stroke is a 撇, terminal hook flicks UP-and-LEFT). Prior
     fail mode: hook flick DOWN. This is a copy-verbatim discipline
     test; if it fails again on the exact same file the drawer just
     wrote, that IS the retrieval ceiling.
   - Note: 匕 is NOT in frozen_cohort.md despite retry_n=4 — it has
     a bright, specific bit remaining to try (the copy-verbatim
     protocol was only introduced at v7.2 pos 277 and 匕 was
     BLOCKED for its next available retry at pos 250).

7. **p3_char_0033_刀** (retry_n=2 → 3)
   - (a) STRONG: pos 302 刅 has 刀-shape core; pos 304 刈 has 刂.
   - (b) form_catalog "撇 as body-crossing diagonal" + candidate-
     disagreement note from B4 (curator read PASS last time);
     tighten body-crossing signature (撇 tip clearly ABOVE 横 by 20+px).

**Group 3 — retrospective (b: STRONG) via NEW composition_rules.md**

8. **p3_char_0111_仇** (retry_n=0 → 1)
   - (b) STRONG: 亻+X family (composition_rules new file) — 仇 was
     a B5 main-fail with the exact 亻-scaling issue this file
     addresses. First composition_rules transfer test.
   - (a) STRONG: pos 340 仔 / 342 仕 / 344 仗 / 346 付 / 348 仝
     / 350 仞 are ALL 亻+X — 仇 landing validates the composition
     rule for the ~7 亻+X items in B6.

9. **p3_char_0117_仑** (retry_n=0 → 1)
   - (b) STRONG: 人-lid+X family (composition_rules) + sibling_signature_
     checklist 匕 row for the body.
   - (a) MODERATE: pos 348 仝 is 人-lid+工 — same family. 仑 landing
     lifts 仝.

10. **p3_char_0011_人** (retry_n=2 → 3)
    - (a) MODERATE: pos 348 仝 has 人-lid; several B6 chars use
      人-topology.
    - (b) NEW composition_rules 人-lid+X family gives new fresh
      framing; sibling_signature_checklist 人/入 row still hot.
      Prior fail was CANDIDATE DISAGREEMENT (curator read PASS).
      One more attempt then decide whether to freeze.

**Group 4 — retrospective (b) for 冂+interior upcoming**

11. **p3_char_0132_内** (retry_n=0 → 1)
    - (b) STRONG: 冂+interior family (composition_rules) — 内 was
      a B5 main-fail with interior-人 not captured inside 冂.
    - (a) MODERATE: pos 335 用 is 冂+interior — 内 landing lifts 用.
    - Note: NOT retrying 內 (Japanese-traditional 內) simultaneously;
      one 冂+interior test is enough this scan.

### SKIP — cooldown-blocked, frozen, or weak (a)/(b)

**Cooldown-blocked (attempted during B5)**:
- p2_radical_042_巛 (BLOCKED until pos 350) — no B6 巛 anyway.
- p2_radical_100_见 (BLOCKED) — no B6 见 anyway.
- p2_radical_088_长 (BLOCKED) — no B6 长 anyway.

**FROZEN (frozen_cohort.md)**:
- p2_radical_058_马, _080_尢, _081_夂, _089_车, _094_风, _099_旡,
  _106_牛. Excluded permanently unless unfrozen by evidence.

**Off cooldown but weak (a)/(b)**:
- p2_radical_047_飞 (retry_n=3) — no B6 飞/几 sibling; 4th retry
  without new leverage; skip.
- p2_radical_053_己 (retry_n=3) — no B6 己/巳 sibling; skip.
- p2_radical_059_门 (retry_n=2) — no B6 门-family; skip.
- p2_radical_084_夊 (retry_n=2) — no B6 夊/夂 (dad frozen); skip.
- p3_char_0009_了 (retry_n=2) — no B6 了/子/孑; skip.
- p3_char_0016_乃 (retry_n=2) — no B6 乃/及; skip.
- p3_char_0021_几 (retry_n=2) — no B6 几/门; skip.
- p3_char_0023_九 (retry_n=2) — no B6 九/丸; skip.
- p1_stroke_24_横撇弯钩 — belly-on-right arc still unproven; skip
  (阝 retry above will test the primitive).
- p1_stroke_32_横折折折钩 — retry_n=2; 弓 retry above will exercise
  the same 3-fold family; skip solo retry.

**Other errata items with no B6 trigger + no new (b) leverage**:
- p2_radical_078_幺, _085_贝, _083_丬, _092_厄, _096_戈, _097_户,
  _101_斤, _102_耂, _105_肀, _107_爿, _108_片, _110_攵, _115_氏,
  _121_尣, _123_韦, _125_毋, _127_牙, _131_爫, _132_支, _134_爪 —
  no direct upcoming; skip.
- Various B4/B5 P3 fails (0042_丬, 0043_个, 0044_丸, 0046_久, 0047_也,
  0049_子, 0056_亾, 0059_么, 0060_卂, 0061_与, 0065_及, 0068_纟,
  0069_干, 0072_夊, 0073_飞, 0074_孑, 0076_孓, 0077_习, 0079_已,
  0081_女, 0082_尢 (frozen adjacent), 0085_马 (frozen), 0086_巛
  (blocked), 0090_幺, 0097_乌, 0099_予, 0102_天, 0103_亢, 0104_方,
  0108_无, 0110_分, 0114_见 (blocked), 0116_公, 0118_从, 0119_仓,
  0120_气, 0121_內, 0122_五, 0123_兮, 0125_円, 0126_长 (blocked),
  0130_切, 0131_冗, 0133_冘) — most retry_n=0, mostly no upcoming
  sibling in B6 or covered by other retries in this scan; skip.
- Exception noted: 0119_仓 is a strong 人-lid+X candidate, but
  0117_仑 (retry #9 above) is a nearly-identical composition test
  and testing both would double-count the composition_rules signal.
  Skip 0119 this scan; if 0117_仑 passes, promote 0119_仓 at pos 325
  mid-scan.

---

## Summary

- **Errata size at scan**: ~63 open items (post-B5 additions),
  MINUS 7 frozen = 56 active.
- **Retries scheduled**: **11**.
- **Retry rate**: 11/56 ≈ 20% (down from B4-B5's ~23%, but the
  denominator is now de-noised of frozen items and the numerator
  is higher-quality).
- **Reason distribution**: 7 strong (a) with direct upcoming char,
  4 (b/hybrid) with composition_rules or sibling_signature_checklist
  new leverage.
- **First composition_rules test**: 4 of 11 retries directly test
  the new file (阝, 仇, 仑, 内 — 亻+X, 人-lid+X, 冂+interior,
  阝+X). If ≥50% pass, composition_rules is validated as
  transferable; if <25%, treat as another additive-not-effective
  intervention per B5 commitment.
- **Cohort de-noising**: this is the first scan where FROZEN items
  are excluded from the retry pool. The retry-pass-rate metric is
  now measured on genuinely eligible items only.
- **Balance check**: prior scans (200, 250) attempted 13-14 each;
  this scan at 11 reflects (i) 7 items moved to freeze, (ii) less
  dense (a) trigger overlap in B6 than in B5 (B5 had many direct
  same-char P3 items; B6 has fewer). Consciously not padding with
  weak (b) retries — B5 commitment forbids more additive noise.
- **Watch for accidental unfreeze**: pos 311 风 draws as B6 main;
  if it PASSes on main attempt, unfreeze p2_radical_094_风 in
  evolution.md.

**Expected pass rate**: 4–5 of 11 (target ≥30% per B5 commitment;
if <30%, next postmortem MUST retire retry or accept ceiling).
**Compound-char main watch**: pos 301, 313, 321, 323, 335, 340,
342, 344, 346, 348, 350 — 11 compound-char items testing
composition_rules; target ≥6 PASS.

---

## Retry list (for retry_log.jsonl append)

```
p2_radical_086_比      retry_n=0→1
p2_radical_119_水      retry_n=0→1
p2_radical_116_礻      retry_n=0→1
p2_radical_050_弓      retry_n=0→1
p2_radical_020_阝      retry_n=0→1
p2_radical_011_匕      retry_n=4→5
p3_char_0033_刀        retry_n=2→3
p3_char_0111_仇        retry_n=0→1
p3_char_0117_仑        retry_n=0→1
p3_char_0011_人        retry_n=2→3
p3_char_0132_内        retry_n=0→1
```

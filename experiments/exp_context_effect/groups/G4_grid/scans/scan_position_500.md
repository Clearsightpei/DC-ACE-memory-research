# Scan @ position 500 — B9 curator retry queue for B10

**Batch summary (B9)**:
- Mains (50): **10 A + 10 PASS + 30 FAIL = 40% success (20 A+PASS/50)**;
  10 A verdicts is a landmark — first double-digit A count in G4.
- Retries (16): **1 A + 4 PASS + 11 FAIL = 5/16 = 31% recovery**.
  Huge jump from B7/B8 combined 0/22. v10 trajectory-view + v11
  pass_index appear to be the recovery mechanism.
- BANK_DEVIATION channel (v13): 0/66 usage — no drawer invoked the
  new channel this batch.
- Chronic-import rate on chronic-component mains (~5 candidates:
  两/甸/丽/甹/冱-family via 冂/勹/丿): **0/5**. Third negative
  batch in a row (B7=0, B8=0, B9=0). Mechanism is dead.

## A-verdict items (10 mains + 1 retry)

| item | Char | Recipe |
|------|------|--------|
| p3_char_0287_光 | 光 | 6 strokes MMH-verbatim; inline dians + hand-shaped 竖弯钩; explicit N-joint declaration |
| p3_char_0291_这 | 这 | 7 strokes MMH-verbatim; 文 top-right + 辶 bottom-left inline; s3+s4 P-weld at ('C', 0.841, 0.97) |
| p3_char_0293_来 | 来 | 7 strokes; uses `heng/shu/pie/na` primitives per MMH |
| p3_char_0300_乱 | 乱 | 7 strokes; 舌 left + 乚 right hook; MMH-verbatim |
| p3_char_0305_还 | 还 | 7 strokes; `chuo_walk.py` bank primitive imported + hand 不-like top |
| p3_char_0310_伯 | 伯 | 7 strokes; 亻 inline (MMH placement rejects ren_side default) + hand 白 |
| p3_char_0313_位 | 位 | 7 strokes; imports `pie`, `shu` primitives; 立 = dot+heng+dot+dot+heng inline |
| p3_char_0320_伾 | 伾 | 7 strokes; 亻 inline (MMH placement rejects ren_side default) + hand 丕 |
| p3_char_0324_但 | 但 | 7 strokes; MMH-literal fallback via `_anchor + fat_line` |
| p3_char_0330_佉 | 佉 | 7 strokes; imports `pie/shu/heng/pie_zhe/dian`; 亻+土+厶 decomposition |
| p3_char_0234_亚__retry_1 | 亚 | retry v13: replicated passing main approach |

## The A-recipe (what pushed these to reference-quality)

Common pattern across all 11 A verdicts:

1. **Explicit decomposition comment at top** naming sub-radicals + stroke count
   ("`# 佉 = 亻 + 土 + 厶, 7 strokes`") — every A had this.
2. **MMH-verbatim anchor use** — no tuning, no "clever mirror math",
   no over-clever quad_bezier control-point deviation.
3. **SELF_CHECK block** with explicit `stroke_count_ok`, `joint_class_mismatches`
   fields — every A had this.
4. **Base primitives (`_anchor + fat_line`) or single-cell bank primitives
   (`pie/shu/heng/na/dian`) — NOT the compound bank primitives**
   (ren_side/mian/etc). When drawer's read of MMH placement disagrees
   with the compound primitive's default anchors, drawer inlines with
   MMH anchors rather than override the primitive. This is a departure
   from the v6/v7 bank-mandate philosophy — but it produces A verdicts.
5. **N-joint discipline**: A items explicitly declare joints as N-class
   (natural gap, ~15-25 px) and leave the gap. Novices try to weld;
   A-drawers leave the gap.

Compare to PASS items (10 mains): all follow points 1-3 but often
skip point 4 (some import compound primitives that work). Compare
to FAIL items (30 mains): most miss BOTH point 1 (no decomposition
comment) AND point 4 (over-invest in compound primitives that don't
match MMH placement).

This has been added to `drawer_memory.md` as the "A-recipe" section.

## Retry recovery analysis (5 PASS + 1 A / 16)

| item | Recovery mechanism |
|------|-------------------|
| 亚 (A) | Trajectory-diff showed main already PASSed; replicated same approach unchanged |
| 如 (PASS) | Trajectory-diff caught MMH-literal collapsed X-crossing; nv primitive w/ x-scaled overrides + kou for right half |
| 次 (PASS) | Trajectory-diff surfaced 冫 placement bug; hand-derived 欠 with pie/heng-zhe/na |
| 处 (PASS) | CROSS_ANCHOR = BL(0.942, 0.154) shared by s2 bend + s3 mid; from `drawer_memory.md` v9 X-cross snippet |
| 凹 (PASS) | 5-stroke plan applied literally; heng-zhe corners aligned |

All 5 recoveries used the **v10 TRAJECTORY DIFF block** in the code
header. This has been the highest-yield mechanism since v9's
introduction (which gave B7r 2 PASSes). v10+v11 combined seems to
lift retry pass rate from ~10% baseline to ~30%.

## The 7 canonical primitives that never got hand-written

Position 400 queued 长/夂/夊/水/礻/无/气 canonical primitives. Position
450 confirmed the files were never written. Position 500 decision:

**UNFREEZE none this batch.** The BANK_DEVIATION channel (v13) is
too fresh to demonstrate an alternative mechanism — 0/66 usage
this batch means we cannot yet claim it opens a new path for these
items. And hand-writing 7 primitives during a diagnostic-heavy pass
would not be honest work; another delivery-failure repeat would
poison the record. If a future curator has explicit budget for the
7 files AND updates `drawer_memory.md` mandatory-imports section AND
the dispatcher pre-checks for those imports, then unfreeze.

Marker unchanged: TERMINAL_FROZEN.

## Retry queue for B10 (positions 501-550)

### Category A — TERMINAL_FROZEN (still frozen)

Same 7 items as position 450: 长/夂/夊/水/礻/无/气. Not re-queued.

### Category B — B9 main FAILs with clear next-fix ideas (v13 retry)

| item_id | Char | Fix idea | Rationale |
|---------|------|----------|-----------|
| p3_char_0303_进 | 进 | import `chuo_walk.py` | mastered walk primitive exists |
| p3_char_0329_运 | 运 | import `chuo_walk.py` | same |
| p3_char_0298_丽 | 丽 | MANDATORY `chronic/jiong_frame` × 2 | chronic exists; test if retry drawer finally imports |
| p3_char_0309_两 | 两 | MANDATORY `chronic/jiong_frame` | same |
| p3_char_0321_把 | 把 | import `shou_side.py` + hand 巴 | mastered primitive |
| p3_char_0318_伽 | 伽 | import `ren_side` + `li` + `kou` | 3 mastered primitives |
| p3_char_0297_你 | 你 | import `ren_side`; hand 尔 | mastered primitive |
| p3_char_0325_状 | 状 | X-cross snippet on 犬 pie+na apex | drawer_memory X-cross recipe |
| p3_char_0296_串 | 串 | enforce s1 shu at C→BC; 2 口 centered | placement rule |
| p3_char_0311_身 | 身 | MMH-verbatim; ensure s7 pie tail to BR | placement rule |

**Category B size**: 10 items.

### Category C — B9 retry saturations (retry_n=2, near cutoff)

| item_id | Char | retry_n | Decision |
|---------|------|---------|----------|
| p3_char_0236_亥 | 亥 | 1 (was 1) | RETRY with hard CROSS_ANCHOR spec |
| p3_char_0238_亦 | 亦 | 1 | RETRY with hard CROSS_ANCHOR spec |
| p3_char_0193_癶 | 癶 | 2 | RETRY final; if FAIL at retry_n=3 → TERMINAL_FROZEN |
| p3_char_0213_処 | 処 | 2 | RETRY final; same rule |
| p3_char_0228_乩 | 乩 | 2 | RETRY final; same rule |
| p3_char_0233_那 | 那 | 2 | RETRY final; same rule |

**Category C size**: 6 items.

### Category D — Skip / need new primitive first

- 军 (needs `che.py` for 车 — not in bank)
- 好, 她 (need `zi.py` fully-mastered; `nv` exists)
- 267_西 (frame closure — no mechanism)
- 240_仰 (needs 卬 primitive)
- 龹, 甹 (rare compound chars — no clear next fix)

Skipped this batch — deferred.

### Category E — Missing primitives (Teacher hand-write recommendations)

Same as position 450, still not delivered:
- `fu_left.py` (阝-left)
- `yan_side.py` (讠)
- `zou_zhi.py` (辶) — though `chuo_walk.py` already covers most 辶 needs
- **NEW at position 500**: `chuang_sick.py` for 疒 (needed by 疔/疖/病/疗 family)
- **NEW**: `shui_side.py` for 氵 (needed by 没/汉/河 family)

---

## Total B10 retry queue length

- Category A: 0 (7 frozen; not re-queued)
- Category B (B9 main FAILs, cool-down till pos 550): 10
- Category C (B9 retry saturations, executable now): 6
- Category D: 0 executable
- Category E: 5 primitive promotions (Teacher-only, not retries)

**Executable B10 retry queue**: 10 (Cat B) + 6 (Cat C) = **16 items**.

## Predictions for B10

- B10 mains pass rate: 40-50% (item pool continues 亻/心/宀-family;
  A-recipe now documented in `drawer_memory.md` — may lift A count).
- B10 retries: expected ~30-40% pass (same mechanism as B9 v10+v11+v13).
- Chronic-import rate on chronic-component mains: predict 0-10% again.
  Recommend: retire the chronic-mandatory mechanism from
  `drawer_memory.md` and replace with a dispatcher-side hard fail
  when a chronic-component target's generated.py lacks the import.
- BANK_DEVIATION channel: predict 0-5% usage until a drawer sees a
  worked example in `drawer_memory.md`.

## Structural notes carried into B10

- No new primitives added by curator this batch (0 promotions).
- No prunes (deferred again — awaits post-B9 usage data).
- No memory-file restructure (v8 slim + v9/v10/v11/v13 addenda active).
- v13 BANK_DEVIATION channel remains available but underutilized.
- **New in drawer_memory.md**: A-recipe section documenting the pattern
  that produced 11 A verdicts.

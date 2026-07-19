# G2 错题集 (Wrong-Answer Notebook)

Failed items awaiting retry. Format: item_id · target · batch of first failure ·
diagnosis (curator, from vision — no human text feedback exists).

**Batch-3 update**: 5 items GRADUATED (撇点, 横折弯, 竖弯钩, 横折折, 丿) — all
PASSed on retry and removed from this notebook. 2 items FAILED retry again
(横折折折钩, 乛) — diagnosis updated below with retry note. 8 NEW items added
from the batch-3 main curriculum (all 2画 radicals).

**Batch-4 update**: 2 more GRADUATED (八, 冂 — both retry PASSed) and REMOVED.
6 retry FAILs incremented (乛 retry_n→2, 厂 retry_n→1, 横折折折钩 retry_n→2, 匕
retry_n→1, 冖 retry_n→1, 人 retry_n→1, 丷 retry_n→1). 13 NEW items added from
batch-4 main curriculum. Errata net change: -2 (八, 冂 graduated) + 13 (new
fails) = +11. Total open errata items now = 20 (was 11).

**Batch-5 update**: 1 GRADUATED (亻 — retry PASSed) and REMOVED. 4 retry FAILs
incremented (屮 retry_n→1, 干 retry_n→1, 廴 retry_n→1, 讠 retry_n→1). 11 NEW
items added from batch-5 main curriculum (弓, 广, 己, 彑, 马, 门, 宀, 女, 犭,
尸, 士). All new items tagged `initial_batch: 5`. Errata net change: -1 (亻) +
11 (new) = +10. Total open errata items now = 30 (was 20).

**IMPORTANT — BATCH 6 ONE-TIME ERRATA REFRESH**: per shared_rules "One-time
errata refresh", the Drawer will attempt EVERY item currently in this errata
in batch 6, using the new "bank is supplementary, never mandatory" framing.
Items tagged `initial_batch: 5` are the newest under the current-rules regime
and should show early signal about whether new principles help.

Retry counter is tracked per item as `retry_n`.

---

## p1_stroke_24_横撇弯钩   (batch 2, retry_n=0)

**Attempt file**: `attempts/p1_stroke_24_横撇弯钩/01_横撇弯钩.png`

**Diagnosis (curator, vision-based)**:

Overall shape reads as a numeral **"3"**, not a right-ear-radical hook.
Two specific errors:

1. The 弯 arc sweeps DOWN-and-RIGHT then curls RIGHT-and-DOWN — belly
   on the lower side, opening to the upper-right. Correct 横撇弯钩
   (as in 阝-right / 及) has belly on the RIGHT with the arc opening
   to the left, so the tail can hook back UP-and-LEFT into the interior
   of the character.
2. The terminal 钩 flick reads as DOWN-and-RIGHT, not the intended
   up-and-left; likely a collision-with-arc issue.

**Root cause**: arc-parameterization confusion — belly on wrong side.

**Fix for retry** (still not proven, do NOT retry until belly-on-right
primitive is validated on another PASS):
- Belly-on-right arc: `x = cx - R*sin(t*pi/2), y = cy + R*(1 - cos(t*pi/2))`
  starting from the 撇 tip.
- Terminal 钩 flicks UP-and-LEFT (~-135° in image coords) from arc's
  bottom endpoint.

**Retry eligibility**: SKIPPED in batch 3 (log reason: primitive not
yet proven). Reconsider after any batch that proves belly-on-right
arcs on a different item.

---

## p1_stroke_32_横折折折钩   (batch 2, retry_n=2, retry FAILED batch 3 AND batch 4)

**Batch-4 retry FAIL update**: attempted again at scan #2. Applied the
"1.5-2× further" rule — pushed terminal 竖 further left (~30 px lean)
and made hook 40 px. But the render (see `retry_attempts/.../01_横折折折钩.png`)
STILL fails: the terminal 竖 now leans correctly but the retrograde
middle 横 became too short (~25 px), making the whole zigzag look
cramped in the upper half of the canvas. The 乃-swoop needs BOTH long
verticals AND a wide overall footprint — moving one knob at a time is
not enough. Also the hook still reads as a right-angle nub rather than
a swept flick.

**Fix for next retry (retry_n=2)**: rebuild from scratch with the whole
shape scaled to fill 250 px vertical extent. Middle 横 length must be
~50 px (not 25); terminal 竖 length ~120 px with 25 px lean; hook 50 px
at -145°. Do not tweak — restart.

**Original diagnosis retained (still applicable):**

**Attempt file (retry)**: `retry_attempts/p1_stroke_32_横折折折钩/01_横折折折钩.png`

**Diagnosis of retry FAIL (curator, vision-based)**:

Retry applied the segment-length hierarchy rule (retrograde middle 横
shortened to ~35 px, terminal 竖 extended to ~90 px). Beat count is
right. But visually the glyph STILL reads as a squarish zigzag, not
the tall/swept 乃-shape. Two remaining defects:

1. **Terminal 竖 lean is too weak.** The final 竖 drops nearly vertically;
   canonical 乃/及 has the terminal 竖 clearly LEANING LEFT (starts at
   roughly the middle 横's left endpoint, descends and drifts further
   left), so the whole bottom-hook profile swings to the lower-left.
2. **Hook flick is too small and near-horizontal.** Reads as a small
   right-angle nub. Needs to be ~30-40 px long, angled -140° to -150°
   (a diagonal up-and-left sweep), tapered to a sharp tip.

**Fix for next retry**:
- Move terminal 竖's END point ~20-30 px LEFT of its start (strong lean).
- Increase hook length to ~35 px, angle -145°, taper r=6→1.
- Consider also making the top 横 slightly longer than currently used
  (the 横 dominance sets up the "tall swept" balance).

**Retry eligibility**: after batch-4 boundary (item #80) at earliest.

---

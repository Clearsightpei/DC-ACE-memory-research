# Cycle 10 — Task brief (火/习/也 repair + 钩 family drill)

Carry the three c9 failures (火, 习, 也) with explicit composition
fixes already in `drawer_memory.md`. Introduce three new chars that
drill the 横折钩 / 横折弯钩 / 竖弯钩 family more thoroughly: 力, 巴,
已.

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND
`calligraphy_rubric.total >= 7` (no 0).

## Repair targets (carry-overs)

1. **火** — apex is shared (good). **New fix:** the two 点 must HUG
   the apex (their tails nearly touch the apex point). Belly of each
   点 sits just up-and-outward from the apex. NOT floating high
   above with a gap. Also: 撇 head heavier (match the 捺 head
   weight).
2. **习** — c9's 提 was too short / disconnected. **Fix:** 提 must
   be a substantial rising flick (~60–70% the width of the 横折
   above) with its weighted base touching/close-to the bottom-left
   corner of the 横折. Tucked-in 点 at upper-left interior.
3. **也** — c9's three strokes were fragmented. **Fix:** 也 is a
   unified shape, not three separated fragments.
   - 横折钩 (stroke 1) is the top-left assembly.
   - middle shu (stroke 2) sits CLOSE to the right of 横折钩's
     vertical portion (do NOT center it independently).
   - 竖弯钩 (stroke 3) wraps around the others — sweeps down from
     upper-right area, curls right along the bottom, hooks up-right.
     Its bottom portion forms the FLOOR; other strokes sit ABOVE.

## New compositions

4. **力 (2 strokes):**
   - 横折钩 (compound: top heng → 90° turn → shu descending → small
     钩 at the bottom-left). The character's "frame".
   - 撇 (long, head at the top-right area, sweeping down through the
     interior and out to the lower-left).
5. **巴 (4 strokes):**
   - top short heng (top of the upper frame),
   - 横折 (right edge + top, forming a small frame at the top right),
   - middle heng (across the frame),
   - 竖弯钩 (long bottom — comes down from the frame's lower-left
     corner, curls right along the bottom, hooks up-right).
   Top half = small frame; bottom half = 竖弯钩 sweep.
6. **已 (3 strokes):**
   - top 横折钩 (heng → corner → short shu → small 钩 at the bottom),
     all in the upper portion,
   - middle heng (short, inside the frame),
   - bottom 竖弯钩 (sweep from inside the frame down, curling right
     along the bottom, hooking up-right — like 也 / 巴's signature
     stroke).

## Calligraphic detail

All strokes use the mastered Bézier-with-per-sample-pensize approach.
For 钩 family strokes, the corner before the 钩 must be a clear
顿笔 thickening; the 钩 itself is a short snappy tail-arm (~15–20%
of main length) tapering to a fine point.

Save each PNG as `attempts/cycle_10/<idx>_<char>.png`.

Your only inputs are `drawer_memory.md` and this brief.

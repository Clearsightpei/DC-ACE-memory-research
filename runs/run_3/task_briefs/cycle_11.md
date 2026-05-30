# Cycle 11 — Task brief (last-pass repairs + frame-with-hooks)

This is the final pass on 火 (if OCR fails again, retire as OCR-wall),
and a focused repair of 也, 力, 巴 with the explicit composition
prescriptions from `drawer_memory.md`. Two new chars (月, 见) drill
the frame-with-interior-hooks family.

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND
`calligraphy_rubric.total >= 7` (no 0).

## Repair targets (carry-overs)

1. **火** — final attempt. Two 点 must literally HUG the apex
   (tails almost touching the apex point); 撇 head heavier; aim for
   maximum-distinguishable from 八.
2. **也** — three strokes occupy the SAME bounding rectangle, NOT
   side-by-side. The 竖弯钩 forms a wrap-around floor + right wall;
   the 横折钩 hangs from upper-left into that wall; the middle shu
   drops straight through the middle with its foot LANDING on the
   bottom curl of the 竖弯钩.
3. **力** — the 撇 must PASS THROUGH the interior of the 横折钩's
   frame. Start 撇 head at top of the frame (near the heng's middle),
   sweep down-left out through the frame and beyond.
4. **巴** — two-level frame. Top portion is a small CLOSED
   rectangle with a middle heng dividing it. Below that, the 竖弯钩
   extends. Make the upper level clearly closed and double-decked.

## New compositions

5. **月 (4 strokes):**
   - 撇 (left side — long, head at top, sweeps down-left as a gentle
     curve, NOT a full diagonal),
   - 横折钩 (right side — heng across top → corner → long shu
     descending → small 钩 at bottom-left),
   - middle heng (inside, upper),
   - middle heng (inside, lower).
   Looks like a tall rectangle frame with two interior heng. The
   left side is a 撇 (curved), the right side is a 横折钩.
6. **见 (4 strokes):**
   - 竖 (left side, short),
   - 横折 (right side — heng + descending shu),
   - middle heng (inside),
   - 撇 + 竖弯钩 as the bottom legs: actually 见 has 4 strokes total —
     the top is a small frame (3 strokes: shu, 横折, middle heng or
     just 2 strokes for the frame), then a 撇 + 竖弯钩 below.
   Practically: a small "目-like" frame on top with two diagonal
   strokes (撇 left, 竖弯钩 right with hook) on the bottom forming
   the "feet" of the character.

## Calligraphic detail

Brushed sweep, compound primitives with corner 顿笔. The 钩 family
is now well-verified — apply liberally.

Save each PNG as `attempts/cycle_11/<idx>_<char>.png`.

Your only inputs are `drawer_memory.md` and this brief.

# Cycle 15 — Task brief (5 carry-overs + 小)

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND rubric ≥ 7
(no 0). Hard no-skip active.

## Carry-overs (5)

1. **也 (6 attempts).** Re-think: **let 竖弯钩 BE the dominant
   frame** that sweeps from upper area → down → right → hook UP-right.
   Put the other 2 strokes INSIDE that wraparound: 横折钩 in the
   upper-left corner of the area; middle shu drops straight down
   inside. Tighter bounding box so they overlap into one body.
2. **巴 (5 attempts).** Try a SQUARER aspect ratio (frame width
   approximately equal to total height). c14 was too tall (had
   strong 已-prior).
3. **见 (3 attempts).** Smaller, clearly-closed top frame; shorter
   distinct 撇 leg sweeping down-LEFT; 竖弯钩 as the right edge of
   the frame extended downward.
4. **天 (2 attempts).** Straighter 捺 diagonal (less curve so it
   doesn't read as 竖弯钩). Strong horizontal flat-tail at the
   bottom-right.
5. **了 (1 attempt).** Bottom stroke clearly CURVED: sweep right
   then hooking left at bottom (NOT a straight vertical-with-hook
   like 丁).

## New (1)

6. **小 (3 strokes):**
   - center 竖钩 (vertical line through the middle with small hook
     at the bottom-left),
   - left 点 (left of the center, tilted; head at upper-left, tail
     toward the center),
   - right 点 (right of the center, mirror of left).
   The two 点 flank the central 竖钩. Compact, centered.

## Calligraphic detail

Standard. Save each PNG as `attempts/cycle_15/<idx>_<char>.png`.
Only inputs: `drawer_memory.md` + this brief.

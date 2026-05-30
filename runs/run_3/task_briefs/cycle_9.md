# Cycle 9 — Task brief (frame family + 钩 family)

This batch carries 火 (apex-sharing fix) and introduces five new
chars covering: pure frame (口), tall frame (日), and the 钩
("hook") family of compound strokes (子, 习, 也). 大 and 入 are
retired under documented OCR-wall status — do not attempt them this
cycle.

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND
`calligraphy_rubric.total >= 7` (no 0).

## Repair target (carry-over)

1. **火 — apex-share fix.** Last cycle drew the 撇 and 捺 with a
   small GAP at the top so the bottom read as 八. **Fix:** 撇 and
   捺 must share a SINGLE apex near the top center (think of it
   like 大 / 个 — one apex). Then the two 点 sit close to either
   side of that apex (left 点 just upper-left, right 点 just
   upper-right of the apex), NOT floating high above with a big
   gap.

## New compositions

2. **口 (3 strokes):** pure rectangular frame.
   - left shu (left edge),
   - 横折 (top + right edge — one compound stroke turning 90° at
     upper-right corner),
   - bottom heng (closes the frame).
   No center shu — distinct from 中. Shorter and squarer than 中's
   frame.

3. **子 (3 strokes):** the 子 family.
   - 横撇 (compound: short heng top → 90° turn → 撇 tail down-left),
     the head of the character.
   - 竖钩 (compound: vertical shu descending → small 钩 turn at the
     bottom, hooking up-and-leftward briefly). This is the LONG
     center stroke, going from below the 横撇 down through the rest
     of the character.
   - middle heng across the character at the waist.

4. **习 (3 strokes):**
   - 横折 (top + descending right portion — short),
   - 点 (top-left, a small dot),
   - 提 (a flick / rising stroke at the bottom).
   Looks like a small "习" shape — frame-like top with a flick
   underneath.

5. **也 (3 strokes):** the 也 family with two new compound strokes.
   - 横折钩 (compound: top heng → turn → short shu → small 钩
     hook at bottom). The character's top-left "L" shape.
   - shu (vertical, second stroke, slight separation from the first
     stroke).
   - 竖弯钩 (compound: shu descending → bottom curl rightward →
     final upward 钩 flick). The signature stroke of 也, sweeping
     from top through the bottom and ending with a hook up-right.

6. **日 (4 strokes):** tall narrow 口 with a middle heng.
   - left shu,
   - 横折 (top + right edge),
   - middle heng (inside the frame, horizontal),
   - bottom heng (closes the frame).

## Calligraphic details

Brushed sweep on every stroke. Compound strokes get the 顿笔 thick-
ening at each turn (横折, 横撇 patterns already verified; 竖钩 and
横折钩 are new — apply the same one-continuous-brushed-path
treatment with a corner Gaussian bump at each turn).

The 钩 family: at the END of a 钩 stroke, the brush makes a small
quick flick (usually up-and-back). Treat as a brief tail-arm coming
off the main stroke's end, with its own taper to a fine point. The
钩 is short and snappy, not a long extra stroke.

Save each PNG as `attempts/cycle_9/<idx>_<char>.png`.

Your only inputs are `drawer_memory.md` and this brief.

# Cycle 9 — 3 tasks: 八 / 人 / 入

## Hard gate (4 components)
- OCR is_correct AND `ocr_margin >= 0.3`
- `visual_score > 0.8`
- Judge panel (3 fresh-context subagents) **unanimous YES**

## Why this slate

The run_4 false-positive class. 人 and 入 were never properly drawn in run_5 — c5's PIL attempts (with disk-blob apexes, messy 撇/捺 crossings) were promoted falsely and then revoked. Now using the run_4 turtle 撇/捺 primitives, which are mastered with proper brushwork.

## Tasks

1. 八 → `attempts/cycle_9/01_八.png`, GT `ground_truths/cycle_9/01_八.png`. 撇 and 捺 with a VISIBLE GAP at the top (the silhouette opens like an upside-down V with an explicit horizontal slot).
2. 人 → `attempts/cycle_9/02_人.png`, GT `ground_truths/cycle_9/02_人.png`. 撇 and 捺 SHARE the apex at top.
3. 入 → `attempts/cycle_9/03_入.png`, GT `ground_truths/cycle_9/03_入.png`. 捺 is dominant (long sweep from upper-left, with kick); 撇 attaches BELOW the 捺's apex as a shorter secondary stroke.

## Use the carried-over run_4 primitives (turtle)

```python
import sys, os
SB = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from pie import draw as draw_pie   # head (+150,+200) → tail (-180,-180), scale=1
from na  import draw as draw_na    # head (-150,+200) → kick tip (+240,-172), scale=1
```

Both take `(t, ox, oy, scale)`. Translate/scale them to match the MMH GT centerlines.

## Approach

Read each GT. Note where the 撇's head/tail and 捺's head/tail/kick land in pixel coords. Convert to turtle math-coords (canvas 800×600, origin center, y-up). Compute `(ox, oy, scale)` for each call.

## Renderer

`turtle.Turtle` + `getcanvas().postscript()` → PIL save. **No subprocess.** Use `t.reset()` between tasks (same pattern that worked in c8).

## Self-preview budget

Max 2 iterations per task. Check each PNG: is the structural distinction visible?
- 八: gap between heads
- 人: shared apex
- 入: 捺-dominant + 撇 attached below

Don't promote in your head — that's the panel's job. Your job is to render clearly.

## Output

`attempts/cycle_9/generated.py`, 3 PNG outputs.

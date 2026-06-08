# Cycle 18 — 八 (ba, eight)

Phase 3 two-phase.

## Prereqs: 撇 (c3), 捺 (c4).

## What 八 is
Two separated strokes — 撇 on left, 捺 on right. Heads near each other at upper-middle but NOT TOUCHING (clear gap). Both sweep downward and outward.

## Skeleton from GT (approximate — Drawer adjusts during self-preview if needed)
- 撇: head (-30, +75) → tail (-100, -110). Short.
- 捺 main: head (+50, +100) → kick base (+150, -110). Kick: → (+200, -100).

Gap between heads at top: ~80 px.

## Brushwork composition

Compose c3 撇 and c4 捺 with translate+scale. The canonical strokes are larger than 八's — use scale ~0.55. The Drawer must find ox/oy that puts each head in the right position.

Suggested starting values:
```python
from pie import draw as draw_pie
from na import draw as draw_na
draw_pie(t, ox=-115, oy=-25, scale=0.55)   # tune ox to put 撇 head near (-30, +75)
draw_na(t, ox=130, oy=-20, scale=0.55)     # tune ox to put 捺 head near (+50, +100)
```

Self-preview: render, view, check head positions vs targets. Iterate.

Eval gt+ocr+vision. On mastery → success_bank/code/ba.py.

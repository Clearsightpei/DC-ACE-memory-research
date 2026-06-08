# Cycle 23 — 力 (li, power/strength)

Phase 3 two-phase.

## What 力 is
横折钩 (the L-with-hook frame) + 撇 (cuts through the heng from upper-middle down-left).

## Skeleton
- 横折钩: heng (-90, +95) → corner (+85, +95), shu down to (+85, -130), hook → (+30, -90).
- 撇: head (0, +120) above heng → tail (-130, -150).

## Brushwork composition
```python
from heng_zhe_gou import draw as draw_heng_zhe_gou
from pie import draw as draw_pie
draw_heng_zhe_gou(t, ox=-15, oy=-25, scale=0.95)
draw_pie(t, ox=-90, oy=-10, scale=0.6)
```

heng_zhe_gou canonical heng (-100,+120) → corner (+100,+120). At scale 0.95, ox=-15, oy=-25 → heng (-110,+89)→(+80,+89). Matches.

Eval gt+ocr+vision. On mastery → success_bank/code/li.py.

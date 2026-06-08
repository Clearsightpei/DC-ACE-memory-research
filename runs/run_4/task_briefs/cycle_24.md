# Cycle 24 — 万 (wan, ten thousand)

Phase 3 two-phase.

## What 万 is
3 strokes:
1. Top heng (long).
2. 横折钩 hanging from heng's right side (frame).
3. 撇 cutting through heng from upper-middle down-left.

Key distinguishing feature from 力: 万 has the EXTRA top heng above the 横折钩+撇 structure.

## Skeleton from GT
- Heng: (-130, +100) → (+170, +100).
- 横折钩 (right frame): corner at top-right ~(+170, +90), drops to (+150, -130), hook left → (+90, -110).
- 撇: head (+30, +130) ABOVE the heng → tail (-130, -130).

## Brushwork composition
```python
from heng import draw as draw_heng
from heng_zhe_gou import draw as draw_heng_zhe_gou
from pie import draw as draw_pie
draw_heng(t, ox=20, oy=+100, scale=0.75)               # top heng
draw_heng_zhe_gou(t, ox=70, oy=-25, scale=0.5)         # smaller 横折钩 hanging right
draw_pie(t, ox=-105, oy=-20, scale=0.7)                # 撇 head above heng
```

Self-preview: iterate if 撇 head is not visibly above heng (this is the 万 vs 力 distinguisher).

Eval gt+ocr+vision. On mastery → success_bank/code/wan.py.

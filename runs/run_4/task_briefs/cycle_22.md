# Cycle 22 — 又 (you)

Phase 3 two-phase.

## What 又 is
横撇 (top) + 捺 (bottom-right sweep). The 捺 starts BELOW the 横撇 corner and crosses through the 撇's path.

## Skeleton from GT
- 横撇 heng: (-100, +120) → (+50, +120). Then 折 + 撇 tail to (-100, -150).
- 捺: head (-30, +30), kick base (+150, -130), kick tip (+200, -120).

## Brushwork composition
```python
from heng_pie import draw as draw_heng_pie  # mastered c11
from na import draw as draw_na
draw_heng_pie(t, ox=20, oy=20, scale=0.9)
draw_na(t, ox=80, oy=-110, scale=0.70)
```

heng_pie's canonical heng spans (-100,+100)→(+30,+100); at scale 0.9 with ox=20,oy=20 → roughly (-70,+110)→(+47,+110). Close to target.

Eval gt+ocr+vision. On mastery → success_bank/code/you.py.

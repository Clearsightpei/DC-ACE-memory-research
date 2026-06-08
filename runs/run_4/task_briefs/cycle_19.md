# Cycle 19 — 人 (ren, person)

Phase 3 two-phase.

## What 人 is
撇 + 捺 with shared apex (both heads at the SAME point). This is the key difference from 八 (which has a gap). 人 = strokes meet at top.

## Skeleton from GT
- 撇: head at apex (+30, +100) → tail (-100, -130). 
- 捺 main: head at apex (+30, +100) → kick base (+150, -120).
- 捺 kick: → (+200, -110).

The apex is the SAME for both strokes.

## Brushwork composition
```python
draw_pie(t, ox=-52, oy=-10, scale=0.55)   # 撇 head → (+30, +100)
draw_na(t, ox=112, oy=-10, scale=0.55)    # 捺 head → (+30, +100)
```

Note: at scale 0.55, pie head (+150,+200) becomes (82.5,+110). +ox=-52 → (30.5, 110). +oy=-10 → (30.5, 100). Same for 捺.

Eval gt+ocr+vision. On mastery → success_bank/code/ren.py.

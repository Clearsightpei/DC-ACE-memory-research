# Cycle 20 — 入 (ru, enter)

Phase 3 two-phase.

## What 入 is
Same general shape as 人 (撇 + 捺 diverging from upper area), but with the **捺 dominant** (longer/extends further right) and the **撇 attached partway down** the 捺 — not at the apex. This is the key 人/入 distinction. Run_3 c12 mastered 入 with this asymmetry.

## Skeleton from GT
- 捺 (dominant, drawn first): head (0, +130) → kick base (+170, -120). Kick → (+220, -110).
- 撇 (shorter, attached to 捺): head (+15, +120) → tail (-150, -80). The 撇 starts ON the 捺's upper portion.

## Brushwork composition
```python
draw_na(t, ox=97, oy=0, scale=0.65)        # 捺 dominant, head at (~0, +130)
draw_pie(t, ox=-52, oy=30, scale=0.45)     # 撇 shorter, head at (~15, +120)
```

The brief difference vs 人: 捺 is BIGGER (0.65 vs 0.50) and 撇 is SMALLER (0.45 vs 0.70).

Eval gt+ocr+vision. On mastery → success_bank/code/ru.py.

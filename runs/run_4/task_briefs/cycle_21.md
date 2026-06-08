# Cycle 21 — 大 (da, big)

Phase 3 two-phase.

## What 大 is
heng + 撇 + 捺. The 撇 and 捺 have apex ABOVE the heng; the heng cuts horizontally THROUGH both limbs ~30-40% down from the apex. Limbs extend wider than heng.

## Skeleton from GT
- Heng: (-130, +40) → (+130, +40). ~260 px.
- 撇: head (+15, +130) → tail (-200, -120).
- 捺 main: head (+15, +130) → kick base (+220, -90). Kick: → (+260, -75).

## Brushwork composition
```python
draw_heng(t, ox=0, oy=+40, scale=0.65)
draw_pie(t, ox=-82, oy=-10, scale=0.72)   # 撇 sweeps wide
draw_na(t, ox=110, oy=+20, scale=0.62)    # 捺 sweeps wide with kick
```

Apex (撇 head + 捺 head) should land near (+15, +130). Limb tails extend WELL BEYOND heng's endpoints (±200 vs ±130 for heng).

Eval gt+ocr+vision. On mastery → success_bank/code/da.py.

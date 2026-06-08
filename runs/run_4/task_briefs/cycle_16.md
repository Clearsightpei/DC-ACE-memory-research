# Cycle 16 — 三 (san, three)

Phase 3 two-phase.

## Prereqs: 横, 一, 二.

## What 三 is
Three stacked hengs: SHORT-MEDIUM-LONG (top to bottom). The bottom is the longest.

## Skeleton from GT
- Top heng:     (-90, +90)  → (+50, +90).   ~140 px.
- Middle heng:  (-100, -10) → (+50, -10).   ~150 px.
- Bottom heng:  (-130, -120) → (+150, -120). ~280 px.
- Vertical gaps: ~100, ~110.

## Brushwork composition
```python
draw_heng(t, ox=-20, oy=+90, scale=0.35)    # top
draw_heng(t, ox=-25, oy=-10, scale=0.38)    # middle (slightly longer)
draw_heng(t, ox=+10, oy=-120, scale=0.70)   # bottom (longest)
```

Eval gt+ocr+vision. On mastery → success_bank/code/san.py.

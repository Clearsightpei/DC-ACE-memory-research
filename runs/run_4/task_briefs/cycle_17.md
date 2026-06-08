# Cycle 17 — 十 (shi, ten)

Phase 3 two-phase.

## What 十 is
Horizontal heng + vertical shu intersecting at center. Shu slightly above center (shu extends more BELOW heng than above).

## Skeleton from GT
- Heng: (-150, +20) → (+150, +20). ~300 px horizontal.
- Shu: (+15, +160) → (+15, -180). ~340 px vertical. Crosses heng near top (heng at +20, shu's top is +160 → 140 above heng; bottom at -180 → 200 below heng).

## Brushwork composition
```python
draw_heng(t, ox=0, oy=+20, scale=0.75)
draw_shu(t, ox=+15, oy=-10, scale=0.85)   # shu has its own y-extents — translate so center≈-10 to match
```

For shu, note canonical (0,+200)→(0,-200) becomes (+15,+200*0.85=+170)→(+15,-170) after scale=0.85, then +oy=-10 → (+15,+160)→(+15,-180). Matches GT.

Eval gt+ocr+vision. On mastery → success_bank/code/shi.py.

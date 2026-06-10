# Cycle 18 — 玉 / 末 / 未

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Rationale

All three are 1-stroke extensions of MASTERED characters in the Success Bank:
- **玉** = 王 + 点 (dot below the bottom heng's right side)
- **末** = 木 + heng above (long heng on top)
- **未** = 木 + heng above (SHORT heng on top, like 末 but the top heng is shorter than 木's heng)

Since 主 = 王 + 点 cleared visual 0.86 (c13), extending 王 with another 点 (玉) should clear. Since 木 cleared visual 0.85 (c14), adding a heng on top should keep visual above 0.8.

## Tasks

1. **玉** (5 strokes): reuse `wang.py` then add a 点 at the bottom-right (around the bottom heng's right portion).
2. **末** (5 strokes): reuse `mu.py` and add a LONG heng above 木's heng.
3. **未** (5 strokes): reuse `mu.py` and add a SHORT heng above 木's heng. The defining distinction from 末 is the top heng's length.

## Reuse
```python
from wang import draw as draw_wang
from mu   import draw as draw_mu
from heng import draw as draw_heng
from dian import draw as draw_dian
```

## Approach
- Measure GTs. Calculate where the extra stroke goes relative to the mastered character's position.
- For 玉: 王 ends at oy ≈ -158 (bottom heng). Add 点 at ~(60, -180) area.
- For 末/未: 木 has its top heng at ~oy=13. Add a NEW heng at oy ≈ +100 above. For 末 use scale ~0.85; for 未 use scale ~0.55.

## Renderer
turtle + postscript, no subprocess.

## Output
`attempts/cycle_18/generated.py` + 3 PNGs (CHINESE filenames).

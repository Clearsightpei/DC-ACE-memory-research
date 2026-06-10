# Cycle 19 — 五 / 六 / 九

Hard gate: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Slate rationale — numerics

Build the foundation 1-9 character set. Already done: 一, 二, 三, 八, 十 (one missing: 四, 五, 六, 七 carries, 九 here).

- **五** (4 strokes): heng + 竖 (going down-left as a slant or 撇) + heng + 横折钩? Standard: heng + 竖 + 横 + 横折 + 横... actually 五 = 一/丨/弓-like. MMH stroke order: heng + shu + heng_zhe + heng. 4 strokes.
- **六** (4 strokes): 点 + heng + 撇 (lower-left) + 点 (lower-right). Has a 撇 — diagonals are risky for visual gate, but 六's 撇 is short.
- **九** (2 strokes): 撇 + 横折弯钩 (a complex compound stroke). The 撇 from upper-right going down-left, then 横折弯钩 sweeping.

## Reuse
- heng, shu, pie, na, dian, heng_zhe, heng_zhe_wan_gou (or heng_zhe_gou)

## Approach
Same measure-and-place. For 六's 撇/点 try scales ~0.35-0.45 (small, like 木 c14 that cleared visual 0.85).

## Output
`attempts/cycle_19/generated.py` + 3 PNGs (CHINESE filenames: 01_五.png, 02_六.png, 03_九.png).

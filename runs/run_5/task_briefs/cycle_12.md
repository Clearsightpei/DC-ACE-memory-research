# Cycle 12 — 上 / 下 / 七

Hard gate (4): OCR is_correct + margin ≥ 0.3 + visual > 0.8 + panel unanimous YES.

## Tasks

1. **上** (shàng, 3 strokes): short 竖 + short 横 (right of 竖) + long bottom 横. Stroke order: 竖 → 横 → 横.
2. **下** (xià, 3 strokes): long top 横 + short 竖 (under 横, off-center toward left of midpoint) + short 点 to the right of the 竖.
3. **七** (qī, 2 strokes): 横 with a hooked tail (or 横+斜钩) — at the simplest, 横 + 竖弯钩 reading. In MMH it's heng (with slight leftward 撇 tail) + 竖弯钩 (vertical-curve-hook).

## Reuse

- `success_bank/code/heng.py` — 横
- `success_bank/code/shu.py` — 竖
- `success_bank/code/dian.py` — 点
- `success_bank/code/shu_wan_gou.py` — 竖弯钩 (for 七's curve+hook)
- Optionally `er.py`/`san.py` for stacked-横 pieces

## Renderer

Same turtle + postscript pattern. NO subprocess. `t.reset()` between tasks.

## Approach

Measure GT pixel coords for each stroke (use PIL+numpy on the GT — `tools/` is quarantined but you can run measurement in `attempts/cycle_12/`). Convert `tx=px-400, ty=300-py`. Choose (ox, oy, scale) for each call so centerlines align.

## Self-preview

Max 2 iterations. Check structural distinguishers:
- 上's bottom 横 is the LONGEST stroke; the small 横 attaches to the right of the 竖.
- 下's 横 is the TOP stroke; the 竖 hangs DOWN from it, with a 点 to its right.
- 七's hook curves up-right at the bottom.

## Output

`attempts/cycle_12/generated.py` + 3 PNGs.

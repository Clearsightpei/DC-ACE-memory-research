# Cycle 5 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 3
**Cycle:** 5

This is a **full carry-over cycle** — the same three strokes as
cycle 4 (na, dian, heng_zhe). Your memory was corrected since last
cycle with specific fixes for each. Read `drawer_memory.md`
carefully and apply the recipes exactly as written — they contain
specific numbers and methods that matter.

## Your job

Render three atomic Chinese strokes as PNG files in
`attempts/cycle_5/`. Each PNG must be exactly 800×600 white
background, drawn in black with pensize 3.

## Tasks

| idx | key      | char | meaning | description |
|-----|----------|------|---------|-------------|
| 01  | na       | 捺   | press / right-falling | a **shallow ~45° diagonal** descending from upper-left to lower-right, gently bowing and flattening toward the tail. Your memory has the exact heading and recipe — use them. |
| 02  | dian     | 点   | dot | the smallest stroke: a tiny **round dab**, not a line. Your memory has the exact method. |
| 03  | heng_zhe | 横折 | horizontal-fold | a short horizontal segment then a sharp ~90° fold straight down (box top-right corner). Your memory has the corrected, compact recipe. |

## Output file names (exact)

- `attempts/cycle_5/01_na.png`
- `attempts/cycle_5/02_dian.png`
- `attempts/cycle_5/03_heng_zhe.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — read it; it has corrected, specific recipes
  for all three of these strokes. Apply the numbers verbatim.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

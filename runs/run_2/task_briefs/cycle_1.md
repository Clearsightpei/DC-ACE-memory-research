# Cycle 1 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 6
**Cycle:** 1 — cold start (your memory is empty)

This is the foundation. The six strokes below are the atomic strokes
every Chinese character is built from. Draw each one as faithfully as
you can — not just the rough direction, but its **calligraphic
character**: the slight tilt, the curvature, the way it tapers or
flicks. You have no memory yet; draw from your own knowledge of how
these strokes look. A rough first attempt is expected — the point is
to produce an honest baseline.

## Your job

Render six atomic Chinese strokes as PNG files in
`attempts/cycle_1/`. Each PNG must be exactly 800×600, white
background, stroke in black.

## Tasks

| idx | key  | char | meaning | description |
|-----|------|------|---------|-------------|
| 01  | dian | 点   | dot | a small, short tear-drop dot — the tiniest stroke; a brief pressed dab, not a line |
| 02  | heng | 横   | horizontal | a horizontal stroke, left to right, with a faint upward tilt |
| 03  | shu  | 竖   | vertical | a straight vertical stroke, top to bottom, no curve |
| 04  | pie  | 撇   | throw / left-falling | a stroke that sweeps from upper-right down to lower-left, curving gently, tapering as it falls |
| 05  | na   | 捺   | press / right-falling | a stroke from upper-left falling down to lower-right, broadening then flattening into a tail |
| 06  | ti   | 提   | rise / flick | a short stroke that flicks upward from lower-left to upper-right, rising as it goes |

## Output file names (exact)

- `attempts/cycle_1/01_dian.png`
- `attempts/cycle_1/02_heng.png`
- `attempts/cycle_1/03_shu.png`
- `attempts/cycle_1/04_pie.png`
- `attempts/cycle_1/05_na.png`
- `attempts/cycle_1/06_ti.png`

## What you have available

- Python `turtle` (use the postscript→PIL trick to save PNGs).
- `drawer_memory.md` — currently empty (cold start). Draw from your
  own knowledge of stroke shapes.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

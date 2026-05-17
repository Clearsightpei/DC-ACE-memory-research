# Cycle 3 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 3
**Cycle:** 3

heng and shu are solved and have left the rotation. This cycle
**carries over pie** (still failing — your memory has a specific
fix to apply) and **introduces two new atomic strokes**: na and ti.
Read `drawer_memory.md` carefully before drawing — it has an exact
recipe-in-progress for pie.

## Your job

Render three atomic Chinese strokes as PNG files in
`attempts/cycle_3/`. Each PNG must be exactly 800×600 white
background, the stroke drawn in black with pensize 3.

## Tasks

| idx | key | char | meaning | description |
|-----|-----|------|---------|-------------|
| 01  | pie | 撇   | throw / left-falling sweep | a curved stroke that begins near the upper-right and sweeps down-and-to-the-left, ending in the lower-left; bulges convex toward the right. Your memory has a specific rotation/step fix for this — apply it. |
| 02  | na  | 捺   | press / right-falling | a stroke that starts near the upper-left and falls down-and-to-the-right, gradually broadening; roughly the mirror of pie, ending toward the lower-right with a flattening tail |
| 03  | ti  | 提   | rise / upward-flick | a short stroke that starts at the lower-left and flicks up-and-to-the-right, ending higher than it began; straight, rising diagonally |

## Output file names (exact)

- `attempts/cycle_3/01_pie.png`
- `attempts/cycle_3/02_na.png`
- `attempts/cycle_3/03_ti.png`

## What you have available

- Python `turtle` (use the postscript→PIL trick to save PNGs).
- `drawer_memory.md` at the run root — read it; it has working
  recipes for canvas conventions and a pie fix to apply.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

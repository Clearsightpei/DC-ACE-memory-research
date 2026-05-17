# Cycle 2 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 3
**Cycle:** 2

This is a **carry-over cycle** — the same three strokes as last
cycle. The Curator updated your memory based on what went wrong;
your memory now contains diagnostic notes. Read `drawer_memory.md`
carefully before drawing.

## Your job

Render three atomic Chinese strokes as PNG files in
`attempts/cycle_2/`. Each PNG must be exactly 800×600 white
background, the stroke drawn in black with pensize 3.

## Tasks

| idx | key  | char | meaning    | description                                                 |
|-----|------|------|------------|-------------------------------------------------------------|
| 01  | heng | 横   | horizontal | a horizontal stroke moving left-to-right with a faint upward tilt; one of the most common strokes in Chinese writing |
| 02  | shu  | 竖   | vertical   | a vertical stroke moving top-to-bottom; perfectly straight, no taper or curve |
| 03  | pie  | 撇   | throw / left-falling sweep | a curved stroke that begins near the upper-right and sweeps down-and-to-the-left, ending in the lower-left direction; bulges convex toward the right |

## Output file names (exact)

- `attempts/cycle_2/01_heng.png`
- `attempts/cycle_2/02_shu.png`
- `attempts/cycle_2/03_pie.png`

## What you have available

- Python `turtle` (use the postscript→PIL trick to save PNGs).
- `drawer_memory.md` at the run root — **has been updated since last
  cycle** with diagnostic notes from the Curator. Read it.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

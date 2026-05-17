# Cycle 1 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 3
**Cycle:** 1

## Your job

Render three atomic Chinese strokes as PNG files in
`attempts/cycle_1/`. Each PNG must be exactly 800×600 white background,
the stroke drawn in black with pensize 3, centered roughly at the
canvas origin (0,0).

## Tasks

| idx | key  | char | meaning    | description                                                 |
|-----|------|------|------------|-------------------------------------------------------------|
| 01  | heng | 横   | horizontal | a horizontal stroke moving left-to-right with a faint upward tilt; one of the most common strokes in Chinese writing |
| 02  | shu  | 竖   | vertical   | a vertical stroke moving top-to-bottom; perfectly straight, no taper or curve |
| 03  | pie  | 撇   | throw / left-falling sweep | a curved stroke that begins near the upper-right and sweeps down-and-to-the-left, ending in the lower-left direction; bulges convex toward the right |

## Output file names (exact)

- `attempts/cycle_1/01_heng.png`
- `attempts/cycle_1/02_shu.png`
- `attempts/cycle_1/03_pie.png`

## What you have available

- Python `turtle` (use the postscript→PIL trick to save PNGs — your
  `drawer_memory.md` may have notes, or you may need to figure it out)
- `drawer_memory.md` at the run root (currently empty — this is the
  first cycle, your cold start)
- No other inputs. Do not look at the ground-truth PNGs in
  `ground_truths/` — they are the answer key and you must NOT read them.
- Do not read `tools/` — it contains the canonical implementation.

Render from the textual descriptions above + any general knowledge you
have about how Chinese strokes look. A bad first attempt is fine and
expected — the Curator will use the results to seed memory for cycle 2.

# Cycle 2 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 6
**Cycle:** 2

Carry-over cycle. heng and shu were mastered last cycle and have
retired. The four strokes that fell below the fidelity gate are back
— your memory now has a specific diagnosis and recipe for each. The
two weakest (na, ti) appear twice so you get extra practice; draw
each independently.

**Read `drawer_memory.md` carefully first.** The single biggest
lesson: last cycle's strokes were drawn FAR too large and too heavy
(big filled brush shapes). The ground truths are **small (~70 px;
点 only ~17 px) and thin (a plain pensize-3 line, no fill, no taper
blobs)**. Apply the per-stroke recipes in memory.

## Your job

Render six atomic Chinese strokes as PNGs in `attempts/cycle_2/`.
Each PNG 800×600, white background, black, **pensize 3, no fill**.

## Tasks

| idx | key  | char | meaning | description |
|-----|------|------|---------|-------------|
| 01  | dian | 点   | dot | a tiny (~15–18 px) round pressed dab — NOT a long stroke |
| 02  | pie  | 撇   | throw / left-falling | short (~70 px) gentle arc from upper-right sweeping down-left, thin |
| 03  | na   | 捺   | press / right-falling | short (~70 px) shallow descent upper-left → lower-right, gentle bow flattening to a tail, thin |
| 04  | ti   | 提   | rise / flick | short (~70 px) straight thin rising line, lower-left → upper-right (~30–40°), no start blob |
| 05  | na   | 捺   | press / right-falling | (second attempt — same as idx 03) |
| 06  | ti   | 提   | rise / flick | (second attempt — same as idx 04) |

## Output file names (exact)

- `attempts/cycle_2/01_dian.png`
- `attempts/cycle_2/02_pie.png`
- `attempts/cycle_2/03_na.png`
- `attempts/cycle_2/04_ti.png`
- `attempts/cycle_2/05_na.png`
- `attempts/cycle_2/06_ti.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — has the "small + thin, no blob" rule and a
  specific recipe per stroke. Apply them.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

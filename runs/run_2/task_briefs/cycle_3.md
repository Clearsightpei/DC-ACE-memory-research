# Cycle 3 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 6
**Cycle:** 3

Carry-over cycle. Four of the six atomic strokes (heng, shu, pie,
ti) are mastered and retired. Two remain: **dian** and **na** — your
memory has a corrected, specific recipe for each (read it carefully:
dian must be a round `t.dot`, NOT a line; na's curve must bow the
*other* way — concave-up, using `t.right` from a steeper start).

idx 01–04 drill dian and na (two independent attempts each).
idx 05–06 re-draw pie and ti (already-mastered) as a stability
check — use their mastered recipes from memory verbatim.

## Your job

Render six atomic strokes as PNGs in `attempts/cycle_3/`. Each PNG
800×600, white, black, **pensize 3, no fill** (except dian uses
`t.dot`).

## Tasks

| idx | key  | char | meaning | description |
|-----|------|------|---------|-------------|
| 01  | dian | 点   | dot | tiny round dab — use `t.dot(~11)` at origin, NOT a line |
| 02  | na   | 捺   | press / right-falling | short ~74 px, concave-UP valley (steeper at top, flatten to tail), curve clockwise (`t.right`) |
| 03  | dian | 点   | dot | (second attempt — same as idx 01) |
| 04  | na   | 捺   | press / right-falling | (second attempt — same as idx 02) |
| 05  | pie  | 撇   | throw / left-falling | mastered recipe — reuse verbatim from memory |
| 06  | ti   | 提   | rise / flick | mastered recipe — reuse verbatim from memory |

## Output file names (exact)

- `attempts/cycle_3/01_dian.png`
- `attempts/cycle_3/02_na.png`
- `attempts/cycle_3/03_dian.png`
- `attempts/cycle_3/04_na.png`
- `attempts/cycle_3/05_pie.png`
- `attempts/cycle_3/06_ti.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — has mastered recipes (heng/shu/pie/ti) and
  corrected recipes for dian (`t.dot`) and na (concave-up,
  `t.right`, steeper start). Apply verbatim.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

# Cycle 1 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 6
**Cycle:** 1 — cold start (your memory is empty)
**Judged by:** the Claude-vision **calligraphy rubric** (reference-free
— there is NO ground truth this cycle). You are scored on brush
quality, not on matching any template.

Draw the six foundational atomic strokes. They are judged on:
**顿笔** (a pause/weight at the start, any turn, and the end),
**弧度** (natural, specific curvature — not a robotic line),
**粗细 / taper** (the stroke should vary in width like a brush — thin
to thick to thin, not a uniform pen line), and **proportion** (correct
length / slant / balance for that stroke). Draw them as a calligrapher
would — with brush character. Do your honest best from your own
knowledge; a rough first attempt is the expected baseline.

## Your job

Render six atomic Chinese strokes as PNGs in `attempts/cycle_1/`.
Each PNG 800×600, white background, black ink.

## Tasks

| idx | key  | char | meaning | description |
|-----|------|------|---------|-------------|
| 01  | dian | 点   | dot | a small pressed tear-drop dot — brief, weighted, not a thin line |
| 02  | heng | 横   | horizontal | left→right, slight upward tilt, weighted start & a 顿笔 at the end |
| 03  | shu  | 竖   | vertical | top→bottom, strong straight spine, weighted entry |
| 04  | pie  | 撇   | throw / left-falling | upper-right → lower-left, curving, tapering to a fine point |
| 05  | na   | 捺   | press / right-falling | upper-left → lower-right, broadening, then a flattened pressed tail |
| 06  | ti   | 提   | rise / flick | lower-left → upper-right, rising and flicking to a sharp point |

## Output file names (exact)

- `attempts/cycle_1/01_dian.png` … `06_ti.png` (idx_key.png)

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs). You may vary
  `pensize` along a stroke to create taper/weight.
- `drawer_memory.md` — empty (cold start). Draw from your own
  knowledge of how brushed strokes look.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

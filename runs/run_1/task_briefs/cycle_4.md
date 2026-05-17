# Cycle 4 — Task Brief

**Phase:** 1 (atomic strokes)
**Batch size:** 3
**Cycle:** 4

pie and ti are solved and retired. This cycle **carries over na**
(still failing — your memory has a specific shallow-bow fix to
apply) and **introduces two new strokes**: dian and heng_zhe. Read
`drawer_memory.md` carefully — it explicitly warns not to reuse
pie's deep curve for na.

## Your job

Render three atomic Chinese strokes as PNG files in
`attempts/cycle_4/`. Each PNG must be exactly 800×600 white
background, the stroke drawn in black with pensize 3.

## Tasks

| idx | key      | char | meaning | description |
|-----|----------|------|---------|-------------|
| 01  | na       | 捺   | press / right-falling | starts upper-left, falls down-and-to-the-right; a **shallow, nearly-straight diagonal that gently bows and flattens toward the tail** — NOT a deep curve. Your memory has the exact fix; apply it. |
| 02  | dian     | 点   | dot | a very short stroke — a small tear-drop/dot, drawn top-to-bottom-right, only ~15–20px long; the smallest stroke |
| 03  | heng_zhe | 横折 | horizontal-fold | a compound stroke: a horizontal segment moving left-to-right, then a sharp ~90° turn folding straight downward (like the top-right corner of a box: go right, then turn the corner and go down) |

## Output file names (exact)

- `attempts/cycle_4/01_na.png`
- `attempts/cycle_4/02_dian.png`
- `attempts/cycle_4/03_heng_zhe.png`

## What you have available

- Python `turtle` (use the postscript→PIL trick to save PNGs).
- `drawer_memory.md` at the run root — read it; it has working
  canvas conventions and an exact na fix (shallow ~20° bow, NOT
  pie's 60°).
- No other inputs. Do not look at `ground_truths/` or `tools/`.

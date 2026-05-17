# Cycle 10 — Task Brief

**Phase:** 2 (simple characters)
**Batch size:** 3
**Cycle:** 10

One carry-over (天) to verify a specific memory fix, plus two new
characters that reuse the enclosed-box structure (口) which is now
working.

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_10/`. 800×600 white, black, thicker pen per memory.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 天        | tiān   | "sky"   | two stacked horizontal bars on top (upper shorter), then below them the **人 shape** — a left-falling pie and right-falling na that **share a single top apex and splay outward without crossing**. Your memory has a specific fix for this (the bottom must be 人, not a crossed 乂). Apply it. |
| 02  | 中        | zhōng  | "middle/center" | an enclosed box/rectangle with a single long vertical stroke passing straight down through its centre, extending above and below the box |
| 03  | 日        | rì     | "sun/day" | an enclosed box/rectangle divided by one horizontal bar across its middle (like a box with a line through the centre, tall rather than wide) |

## Scale, placement & pen guidance

- Characters **large and centered**: ~300–360 px across, centered
  near canvas middle (0,0).
- **Thicker pen (pensize ~9–12)**, horizontals near-flat.

## Output file names (exact)

- `attempts/cycle_10/01_天.png`
- `attempts/cycle_10/02_中.png`
- `attempts/cycle_10/03_日.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — stroke recipes + Phase-2 structural rules,
  including the 天/元 "shared-apex, no crossing" fix and a working
  enclosed-box (口) approach. Apply them.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

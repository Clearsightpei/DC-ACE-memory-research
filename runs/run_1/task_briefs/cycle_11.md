# Cycle 11 — Task Brief

**Phase:** 2 (simple characters)
**Batch size:** 3
**Cycle:** 11

One carry-over (天) to verify a corrected memory theory, plus two
new characters built from heng + shu (both long-solved).

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_11/`. 800×600 white, black, thicker pen per memory.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 天        | tiān   | "sky"   | Your memory has a CORRECTED structural theory for this character (it was wrong before — read memory lesson #6 carefully). Build it as memory now specifies, reusing a confirmed sub-character recipe. |
| 02  | 王        | wáng   | "king"  | three horizontal strokes (top, middle shorter, bottom) with a single vertical stroke connecting through the centres of all three — like 三 with a vertical spine |
| 03  | 土        | tǔ     | "earth/soil" | a horizontal crossed by a vertical (like 十), then a longer horizontal across the bottom; the bottom bar is the widest |

## Scale, placement & pen guidance

- Characters **large and centered**: ~300–360 px across, centered
  near canvas middle (0,0).
- **Thicker pen (pensize ~9–12)**, horizontals near-flat.

## Output file names (exact)

- `attempts/cycle_11/01_天.png`
- `attempts/cycle_11/02_王.png`
- `attempts/cycle_11/03_土.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — stroke recipes + Phase-2 structural rules.
  Lesson #6 has the corrected 天 theory (it = a short heng on top
  + the confirmed 大 recipe, pie/na piercing the bar — NOT 二+人).
  Apply it exactly.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

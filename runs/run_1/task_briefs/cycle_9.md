# Cycle 9 — Task Brief

**Phase:** 2 (simple characters)
**Batch size:** 3
**Cycle:** 9

Continuing Phase 2. No carry-overs — last cycle was 3/3. These
three push on structural composition (the current frontier).

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_9/`. Each PNG: 800×600 white background, black,
thicker pen per your Phase-2 memory guidance.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 天        | tiān   | "sky/heaven" | two horizontal strokes stacked on top (the upper one shorter), then a left-falling pie and a right-falling na hanging below the lower bar — like 大 but with an extra bar ON TOP and the pie/na NOT rising above the top bar. Mind your memory's stacking-order rule: this is the case 大 must NOT look like. |
| 02  | 本        | běn    | "root/origin" | the character 木 (a heng crossed by a vertical shu, with a pie and na branching down-outward from the crossing) plus one extra short horizontal stroke near the bottom of the vertical |
| 03  | 口        | kǒu    | "mouth"  | a closed rectangle/box: a vertical down the left, a horizontal-then-fold across the top and down the right, and a horizontal closing the bottom — three strokes forming an enclosed square |

## Scale, placement & pen guidance

- Characters **large and centered**: ~300–360 px across, centered
  near canvas middle (0,0).
- **Thicker pen (pensize ~9–12)**, horizontals near-flat.

## Output file names (exact)

- `attempts/cycle_9/01_天.png`
- `attempts/cycle_9/02_本.png`
- `attempts/cycle_9/03_口.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — stroke recipes + Phase-2 structural rules
  (esp. the vertical-stacking-order rule). Apply it.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

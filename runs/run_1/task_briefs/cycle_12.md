# Cycle 12 — Task Brief

**Phase:** 3 (complex characters) — **PHASE TRANSITION**
**Batch size:** 3
**Cycle:** 12

You are moving from simple characters to **multi-radical
characters**. Every character this cycle is built entirely from
sub-characters the experiment has already solved (木, 十, 口). The
new skill is **arranging two known sub-characters into one glyph**
(side-by-side, stacked, or one enclosing the other).

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_12/`. 800×600 white, black, thicker pen per memory.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 林        | lín    | "forest" | two copies of 木 (tree) placed **side by side**, left and right; the left 木 slightly narrower, both about the same height |
| 02  | 古        | gǔ     | "ancient" | 十 (a cross) stacked **on top of** 口 (a box); the 十 sits above, the 口 directly below it |
| 03  | 困        | kùn    | "trapped" | a 口 (box) **enclosing** a 木 (tree) — the box is large and the 木 sits entirely inside it |

## Scale, placement & pen guidance

- Whole character **large and centered**: ~320–380 px across,
  centered near canvas middle (0,0). Each sub-character is scaled
  DOWN so the two together fill that footprint (each radical is
  roughly half-size of a standalone character).
- **Thicker pen (pensize ~9–12)**, horizontals near-flat.
- Reuse your confirmed sub-character recipes (木, 十, 口) — just
  position and scale them.

## Output file names (exact)

- `attempts/cycle_12/01_林.png`
- `attempts/cycle_12/02_古.png`
- `attempts/cycle_12/03_困.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — confirmed recipes for 木, 十, 口 and the
  Phase-2 structural rules. Compose, scale, position.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

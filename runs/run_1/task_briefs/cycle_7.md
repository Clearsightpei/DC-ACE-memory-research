# Cycle 7 — Task Brief

**Phase:** 2 (simple characters)
**Batch size:** 3
**Cycle:** 7

Continuing Phase 2. One carry-over (一) to test a specific memory
hypothesis, plus two new characters that are compositions of
strokes the experiment already has working recipes for.

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_7/`. Each PNG: 800×600 white background, black.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 一        | yī     | "one"   | a single horizontal stroke. Your memory has a specific hypothesis to test here (about pen thickness and flatness) — apply it. |
| 02  | 大        | dà     | "big"   | a horizontal stroke (heng) near the top, then a left-falling pie and a right-falling na crossing it like outstretched arms and legs |
| 03  | 木        | mù     | "tree/wood" | a horizontal (heng) crossed by a vertical (shu); then a pie and a na branching downward-outward from where they cross |

## Scale, placement & pen guidance

- Characters drawn **large and centered**: ~300–360 px across,
  centered near canvas middle (0,0).
- **Use a thicker pen for Phase-2 characters** (pensize ~6–10) —
  real glyphs are bold, and your memory notes this aids
  recognition. For 一 specifically, keep it **near-flat (≈0° tilt,
  not slanted)** and **bold**.

## Output file names (exact)

- `attempts/cycle_7/01_一.png`
- `attempts/cycle_7/02_大.png`
- `attempts/cycle_7/03_木.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — has working stroke recipes and a Phase-2
  section with composition + pen-thickness guidance. Apply it.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

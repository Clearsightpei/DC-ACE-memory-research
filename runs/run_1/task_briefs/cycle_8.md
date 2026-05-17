# Cycle 8 — Task Brief

**Phase:** 2 (simple characters)
**Batch size:** 3
**Cycle:** 8

Continuing Phase 2. One carry-over (大) to test a specific memory
fix, plus two new characters that are pure compositions of strokes
the experiment already has working recipes for.

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_8/`. Each PNG: 800×600 white background, black,
thicker pen per your Phase-2 memory guidance.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 大        | dà     | "big"   | a horizontal stroke (heng) with a left-falling pie and a right-falling na crossing it. **Your memory has a specific structural fix for this** (about which stroke is topmost) — apply it carefully. |
| 02  | 八        | bā     | "eight" | two separate splaying strokes: a left-falling pie on the left and a right-falling na on the right, NOT touching at the top — like two legs spread apart |
| 03  | 三        | sān    | "three" | three horizontal strokes (heng) stacked: a shorter one on top, a short middle one, and a longer one at the bottom |

## Scale, placement & pen guidance

- Characters drawn **large and centered**: ~300–360 px across,
  centered near canvas middle (0,0).
- Use a **thicker pen (pensize ~9–12)** — confirmed in memory to
  aid recognition. Keep horizontals near-flat.

## Output file names (exact)

- `attempts/cycle_8/01_大.png`
- `attempts/cycle_8/02_八.png`
- `attempts/cycle_8/03_三.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — working stroke recipes + a Phase-2 section
  including a 大-vs-天 structural fix. Apply it.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

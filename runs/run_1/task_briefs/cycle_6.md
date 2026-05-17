# Cycle 6 — Task Brief

**Phase:** 2 (simple characters) — **PHASE TRANSITION**
**Batch size:** 3
**Cycle:** 6

You have moved from atomic strokes to **whole characters**. The
three characters this cycle are each composed of strokes the
experiment already has working recipes for in your memory (heng,
shu, pie, na). Compose them.

Now the judge also runs OCR — a correctly-formed character can be
*recognized*, which is the real target in Phase 2 (`is_correct`).

## Your job

Render three Chinese characters as PNG files in
`attempts/cycle_6/`. Each PNG must be exactly 800×600 white
background, drawn in black with pensize 3.

## Tasks

| idx | character | pinyin | meaning | composition hint |
|-----|-----------|--------|---------|------------------|
| 01  | 一        | yī     | "one"   | a single horizontal stroke (heng), drawn large and centered |
| 02  | 十        | shí    | "ten"   | a horizontal stroke crossed by a vertical stroke through its middle (heng + shu, like a plus sign) |
| 03  | 人        | rén    | "person" | two strokes meeting at a top apex: a left-falling pie and a right-falling na splaying outward like legs |

## Scale & placement guidance

These characters should be drawn **large and centered** — roughly
**300–380 px across**, centered near the canvas middle (0,0 in
turtle coords). A character drawn too small will not be recognized.
This is bigger than the lone strokes you may have recipes for in
memory — scale the stroke recipes up accordingly.

## Output file names (exact)

- `attempts/cycle_6/01_一.png`
- `attempts/cycle_6/02_十.png`
- `attempts/cycle_6/03_人.png`

## What you have available

- Python `turtle` (postscript→PIL trick to save PNGs).
- `drawer_memory.md` — has working stroke recipes (heng, shu, pie,
  na) and canvas conventions. Compose and scale them up.
- No other inputs. Do not look at `ground_truths/` or `tools/`.

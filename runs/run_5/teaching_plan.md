# Teaching Plan — run_5

## Mission

Teach the Drawer to produce Chinese characters that, to a human eye,
are unambiguously the target character. Quality over quantity.

## Architecture context

- Drawer is a fresh subagent that **sees the GT PNG** and mimics it
  visually. 3 tasks per cycle.
- `tools/` is quarantined during the Drawer's turn. The Drawer
  cannot read parameter libraries.
- Curator's promotion gate is **strict Claude-vision identity
  check**: only promote if the attempt is unambiguously the target
  character with no plausible alternate reading.
- OCR / visual_score are logged but never sufficient. They produced
  the run_4 false positives.

## Phases

| Phase | What's taught | GT source | Eval |
|------|---------------|-----------|------|
| 1 | 1-stroke and very-simple characters (1–3 strokes) | `tools/make_char_gt.py` (MMH skeletons) | vision+ocr+gt |
| 2 | Simple characters (3–6 strokes), single-component | `tools/make_char_gt.py` | vision+ocr+gt |
| 3 | Compound characters (6–10 strokes), reuse Success Bank components | `tools/make_char_gt.py` | vision+ocr+gt |
| 4 | Complex characters (10+ strokes) | `tools/make_char_gt.py` | vision+ocr+gt |

**Atomic stroke GTs** (`tools/make_stroke_gt.py`) are NOT used in
run_5 — the hand-coded strokes are too thin to be a mimic target
(run_2 lesson). The Drawer learns brushwork from Principle Bank
§1.0 + observing skeleton GTs.

## Mastery rule

A focus is mastered when the Curator says the attempt PNG is
unambiguously the target character (vision identity) AND rubric ≥ 7
with no criterion at 0. A focus is NOT mastered just because OCR
landed on the right token.

A non-mastered focus carries over to the next cycle's slate.

## Curriculum (provisional, revised as the run evolves)

- **Cycles 1–2 (Phase 1)**: 一 二 三 十 八 入 (start with single-stroke
  and 2-stroke characters where the GT is unambiguous).
- **Cycles 3–5 (Phase 2 entry)**: simple 3-6 stroke characters with
  novel composition rules — 人 大 木 ...

Phase progression is judged by Curator promotion rate. If a phase's
slate produces < 1/3 promotion, hold the phase and pick different
characters within it; do not advance.

## Notes

- Teacher's mastery audit (cycle N-1) must be done by opening both
  PNGs in Claude vision. Do not rely on judge_results numbers alone.
- Carry-over is the default for any ambiguous case.

# Teaching plan

## Current phase

**Phase 3 — complex (multi-radical) characters** (entered cycle 12).
Rationale: Phase 2 (cycles 6–11) well-evidenced the full thesis —
emergent memory transfers, composes up to 5 strokes, generalizes to
new structures (enclosures), and *self-corrects* (the 天 wrong→
falsify→correct→confirm arc across c9–c11, made visible by the
mandatory carry-over rule). Two 3/3 cycles (c8, c11), 14 solved
characters. The next untested skill is arranging known
sub-characters into one glyph; Phase-3 entry uses only solved
radicals (木/十/口) to isolate arrangement from new-stroke learning.

### Phase 2 — simple characters (cycles 6–11, completed)

Entered cycle 6. Rationale for that transition: by cycle 5,
Phase-1 lone-stroke phase-correlation was
near its noise floor (visually-better drawings scored *lower*), and
the experiment's core question — does memory emerge and transfer? —
was already answered yes (shu/pie/ti solved from memory; faithful
verbatim transfer, including of a wrong number, documented). Further
lone-stroke drilling had low information value. Phase 2 gives the
metric more structure and unlocks the OCR `is_correct` target.

Phase-2 entry batch deliberately uses only characters that are pure
compositions of already-solved strokes (一, 十, 人) to isolate the
*composition* skill from new-stroke learning.

### Phase 1 — atomic strokes (cycles 1–5, completed)

Cold start with a memoryless fresh subagent, by design. heng/shu/
pie/ti reached passing/solved; na/dian/heng_zhe never passed but
their failure became a finding about metric noise rather than a
learning gap.

## Pacing principle (provisional)

- **3 tasks per cycle**, always (subject to revision based on what
  emerges).
- Cycle 1: introduce the three most foundational atomic strokes —
  横, 竖, 撇. These are present in nearly every Chinese character.
  If the Drawer can produce *recognizable* versions of these from
  textual description alone, the experiment has a viable starting
  point.
- After cycle 1, decisions about pacing depend on what the Curator
  observes.

## Carry-over rule (Phase 1)

- A stroke whose `visual_score < 0.7` carries over to next cycle.
  (Threshold loose at first because the Drawer is blind to the GT.)
- If a stroke passes once, it leaves the rotation.

## How I will use Curator feedback

`cycle_summary.md` is the primary input. The Curator tells me what
*kind* of mistake the Drawer made; my job is to design next cycle's
batch to either drill that mistake or introduce something new.

## Open questions

- How much does the Drawer's "general knowledge of Chinese strokes"
  carry it through cycle 1 without memory? That's the first
  observable.
- Is the visual_score threshold sane in the GT-blind regime? It may
  need to be lower than the previous run's 0.9.

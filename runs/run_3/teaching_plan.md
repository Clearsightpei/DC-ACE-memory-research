<!--
Teacher-owned. Pedagogy + long-term curriculum + mastery checklist.
Written from scratch on cycle 1, revised freely thereafter. Do not
edit outside /cycle's Teacher phase.
-->

# Teaching plan — run_3 (tool-orchestrator era)

## Ultimate goal

Teach the Drawer to draw the best **characters** possible. Strokes are
taught only because they make characters better. I (Teacher) choose
which evaluation tool judges each cycle (`judge.eval`).

## Why this run exists

`runs/run_2/POSTMORTEM.md`: the hand-coded stroke GTs were weaker
calligraphy than the model's own strokes, so GT-matching judging
*degraded* quality. Fix: **strokes are judged by the reference-free
Claude-vision rubric, not the weak stroke GT.** Characters keep the
trustworthy graphics.txt GT plus vision + OCR.

## Rubric calibration (recorded cycle 1 — justifies the 7/10 gate)

Scored run_1's crude-but-OCR-correct characters with the 5-criterion
rubric (0–2 each, /10):
- run_1 c12 林 → 4/10 (dunbi 0, hudu 1, taper 0, proportion 2,
  overall 1) — recognizable, mechanically thin, no 顿笔/taper.
- run_1 c6 人 → 3/10 (dunbi 0, hudu 1, taper 0, proportion 1,
  overall 1).
Crude-but-correct clusters at **3–4/10**, cleanly below the **7/10**
mastery gate. Gate retained at total ≥ 7 with no criterion == 0.

## Curriculum (long-term)

| Phase | What | Stroke band | Pool source | Default eval |
|-------|------|-------------|-------------|--------------|
| 1 | Atomic strokes | — | the 6 atomics, then compounds | `vision`
| 2 | Simple characters | 1–4 | `list_chars.py --min 1 --max 4` | `gt+ocr+vision` |
| 3 | Complex characters | 5–18 | `list_chars.py --min 5 --max 18` | `gt+ocr+vision` |

Advance when ≳80% of introduced items in a phase are mastered
post-reflection (soft, Teacher-judged; documented per advance).
Mastered: strokes → vision rubric ≥7/10, no 0 criterion,
post-reflection; characters → OCR is_correct AND rubric ≥7/10. GT
`visual_score` for characters tracked for regression only.

## Stroke-mastery checklist

| item | phase | signal | best post-reflection | mastered? |
|------|-------|--------|----------------------|-----------|
| dian | 1 | vision | 10/10 (c2) | **yes** |
| heng | 1 | vision | 9/10 (c2)  | **yes** |
| shu  | 1 | vision | 9/10 (c2)  | **yes** |
| pie  | 1 | vision | 10/10 (c2) | **yes** |
| na   | 1 | vision | 10/10 (c2) | **yes** |
| ti   | 1 | vision | 10/10 (c2) | **yes** |

(Updated each cycle from the calligraphy_rubric / Curator reflection.)

## Phase advance — cycle 2 → cycle 3 rationale

All 6 atomic strokes mastered post-reflection (c2 avg 9.67/10,
no criterion == 0). 6/6 = 100% mastered ≫ 80% gate. Advance to
**Phase 2** (simple characters, 1–4 strokes) starting cycle 3.
Phase-2 starter pool chosen to exercise every atomic primitive:
一 (heng), 二 (2 heng), 三 (3 heng), 十 (heng+shu), 人 (撇+捺),
八 (撇+捺 with gap). New gate: `is_correct == true` AND
rubric ≥ 7. GT `visual_score` for regression only.

## Open questions

- Cold start under vision-only judging: how rich are the Drawer's
  strokes when there is *no* GT to regress toward? (run_2's lesson
  predicts they start better than the old stroke GT.)
- Which atomic strokes are hardest to get 顿笔/弧度/taper on.

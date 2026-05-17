<!--
Append-only history. Teacher adds one block per cycle. Do not edit
prior entries.
-->

## Cycle 1 — 2026-05-15

- **Phase:** 1
- **Batch:** [heng, shu, pie]
- **Why this batch:** Cold start. The Drawer is a fresh subagent that
  cannot see the GTs and has no memory file content. Picked the three
  most foundational atomic strokes — every Chinese character uses
  these. If the Drawer's general knowledge can produce even rough
  versions, the experiment has signal to work with. If it fails
  entirely, Curator's notes seed cycle 2.
- **Cycle summary from last cycle:** (none; this is the first cycle of
  a fresh run after the pilot's reset)

## Cycle 2 — 2026-05-15

- **Phase:** 1
- **Batch:** [heng, shu, pie]  ← same as cycle 1, deliberately
- **Why this batch:** All three carry over (every cycle-1 visual_score
  was < 0.7). The Curator wrote explicit diagnostic notes in
  drawer_memory.md (scale guidance: ~70 pixels; pie direction
  correction: sweep DOWN-LEFT not UP-RIGHT). Repeating the exact same
  batch is the cleanest experiment: did memory transfer? If scores
  jump significantly, the Curator's memory contribution is the cause.
  If they don't, the memory format isn't working.
- **Cycle summary from last cycle:** "0/3 passed visual (avg 0.25).
  Scale 4× too large; pie reversed. Memory now has scale guidance
  and direction correction. Recommend repeat batch as memory-transfer
  test."
  → Following the recommendation verbatim.

## Cycle 3 — 2026-05-16

- **Phase:** 1
- **Batch:** [pie, na, ti]
- **Why this batch:** heng (0.74) and shu (1.00) passed in cycle 2
  and leave the rotation per the carry-over rule. pie carries over
  (0.40 < 0.7) and the Curator codified a specific fix (more total
  rotation ~60°, ~60 steps). Introducing na and ti — the two
  remaining foundational single-direction strokes — tests whether
  the Drawer's general knowledge + canvas conventions in memory
  generalize to *new* strokes it has never attempted, while pie
  tests whether a targeted memory fix lands.
- **Cycle summary from last cycle:** "2/3 pass; avg visual 0.25→0.71
  from memory alone. heng/shu solved. pie curve too shallow; memory
  now specifies ~60° rotation. Recommend carry pie + add na, ti."
  → Followed verbatim.

## Cycle 4 — 2026-05-16

- **Phase:** 1
- **Batch:** [na, dian, heng_zhe]
- **Why this batch:** pie (1.00) and ti (0.95) passed cycle 3 and
  retire per the carry-over rule. na carries over (0.22 < 0.7) with
  a specific Curator fix (shallow ~20° bow, flattening tail — do NOT
  reuse pie's 60°). Introducing dian (the smallest atomic stroke, a
  scale-extreme test) and heng_zhe (the first *compound* stroke — a
  horizontal then a folded vertical), which probes whether the
  Drawer can compose two known primitives (heng + shu, both solved)
  into one connected stroke.
- **Cycle summary from last cycle:** "2/3 pass; pie solved 0.40→1.00
  via exact memory fix; ti passed first try; na failed by reusing
  pie's curvature. Recommend carry na, retire pie/ti, add dian +
  heng_zhe." → Followed verbatim.

## Cycle 5 — 2026-05-16

- **Phase:** 1
- **Batch:** [na, dian, heng_zhe]  ← full carry-over of cycle 4
- **Why this batch:** All three failed cycle 4 (<0.7). The Curator
  identified that each failure was a *specific number/method* error,
  not a conceptual one, and corrected memory: na heading 285°→325°,
  dian should use t.dot() not a line, heng_zhe segments shortened &
  recentered. Repeating the exact batch is the cleanest test of
  whether corrected numeric memory now lands (mirrors the c2 and c3
  memory-transfer tests). No new strokes — isolate the variable.
- **Cycle summary from last cycle:** "0/3; a wrong number in memory
  transfers as faithfully as a right one. Corrected na heading, dian
  method, heng_zhe scale. Carry all three." → Followed verbatim.

## Cycle 6 — 2026-05-16

- **Phase:** 2  ← **PHASE TRANSITION from 1**
- **Batch:** [一, 十, 人]
- **Why this batch:** The Curator's cycle-5 summary showed Phase-1
  lone-stroke phase-correlation is near its noise floor (visually
  better drawings scored lower) and the memory-emergence signal is
  already well-demonstrated (shu/pie/ti solved; faithful verbatim
  transfer proven; "a wrong number transfers as faithfully as a
  right one" documented). Continuing to drill noisy lone strokes
  has low information value. Advancing to Phase 2: simple characters
  give phase correlation more structure to lock onto AND unlock the
  OCR `is_correct` signal (a real recognizability target, less
  noisy than thin-stroke correlation). Chose the three simplest
  characters that are pure compositions of already-solved strokes —
  一 (heng), 十 (heng+shu), 人 (pie+na) — so this cycle isolates the
  *composition* skill, not new stroke learning.
- **Cycle summary from last cycle:** "0/3; phase-correlation noisy/
  non-monotonic at stroke scale; memory transfer works; recommend
  Phase 2 or retiring noisy carry-overs." → Followed (Phase 2).

## Cycle 7 — 2026-05-16

- **Phase:** 2
- **Batch:** [一, 大, 木]
- **Why this batch:** Stay in Phase 2 (cycle 6 proved composition
  from memorized strokes works: 十/人 recognized first try). Carry
  over 一 ONCE to test the Curator's specific hypothesis that a
  bolder, flatter pen makes the featureless single stroke OCR-
  recognizable — a clean falsifiable test of a memory entry. Add 大
  (heng+pie+na) and 木 (heng+shu+pie+na): both are pure compositions
  of solved strokes but more complex than c6's, probing whether the
  composition skill scales to 3–4 stroke characters.
- **Cycle summary from last cycle:** "2/3 correct; composition
  works; 一 is an OCR blind spot; recommend more multi-stroke chars
  + optional bold-pen retry of 一." → Followed.

## Cycle 8 — 2026-05-16

- Phase: 2
- Batch: [大, 八, 三]
- Carry-overs: 大 (carried from cycle 7, where it OCR'd as 天 @ 0.39).
  Testing the Curator's c7 reflection: "in 大 the pie must rise ABOVE
  the heng; vertical stacking order determines identity for crossing
  characters." 一 and 木 retired — both passed cleanly on the cycle
  *after* their Curator reflections (一 bold+flat fix confirmed
  0.63; 木 @ 1.00), satisfying the new retire-only-after-confirmed
  -reflection rule.
- Why this batch: New mandatory carry-over rule forces 大 back until
  it cleanly passes post-reflection. Filled remaining slots with 八
  (pure pie+na, no crossing — isolates whether the splay shape
  alone is recognizable) and 三 (three heng — probes the earlier
  "featureless horizontal" concern at a multi-stroke scale, and
  whether stacked-heng spacing is learnable). Both are pure
  compositions of solved strokes.

## Cycle 9 — 2026-05-16

- Phase: 2
- Batch: [天, 本, 口]
- Carry-overs: none. Cycle 8 was 3/3 with all reflections confirmed
  (大 stacking fix verified @1.00); 大/八/三 retired cleanly per the
  retire-only-after-confirmed-reflection rule.
- Why this batch: Structural composition is the current frontier
  (stroke shape is solved). 天 directly stress-tests the confirmed
  stacking-order rule from the *opposite* side — it is the shape 大
  must NOT become, so it checks the rule is understood as a
  contrast, not memorized for one character. 本 builds on the
  already-perfect 木 (木 + one bottom heng) — tests incremental
  composition. 口 introduces a genuinely new structure: an enclosed
  box (corners/folds), unseen so far. Expect 口 to be the likely
  failure that seeds the next reflection.

## Cycle 10 — 2026-05-16

- Phase: 2
- Batch: [天, 中, 日]
- Carry-overs: 天 (carried from cycle 9, OCR'd 元 @ 0.61). Testing
  the Curator's c9 reflection: "天's bottom is the 人 shape — pie+na
  share one apex and splay, never cross; a crossing reads as 儿/乂".
  本/口 retired (clean first-try passes, no prior failure).
- Why this batch: Mandatory carry-over forces 天 back to verify the
  apex-vs-crossing reflection (a clean falsifiable test, parallel
  to the confirmed 大-stacking case). Filled remaining slots by
  *reusing the newly-working 口 enclosure*: 中 (口 + a vertical
  piercing it) and 日 (口 + a middle bar). This tests whether the
  enclosure primitive composes with other strokes the way the
  line/splay primitives already do.

## Cycle 11 — 2026-05-16

- Phase: 2
- Batch: [天, 王, 土]
- Carry-overs: 天 (carried from cycles 9 AND 10 — failed both as 元).
  Testing the CORRECTED c10 reflection: "天 = short heng on top +
  the confirmed 大 recipe (pie/na pierce the lower heng), NOT 二+人".
  The c9 theory was applied faithfully in c10 yet still failed,
  which falsified it; this is the second, corrected hypothesis.
  中/日 retired (clean first-try passes).
- Why this batch: Mandatory carry-over keeps 天 in until it passes
  post-reflection — and this is now a test of a *corrected* theory,
  the most informative kind (does the second hypothesis hold?).
  王 and 土 are new but built only from heng+shu (both solved since
  cycle 2); they keep the batch productive and probe stacked-bar +
  spine compositions without introducing new strokes.

## Cycle 12 — 2026-05-16

- Phase: 3  ← **PHASE TRANSITION from 2**
- Batch: [林, 古, 困]
- Carry-overs: none. Cycle 11 was 3/3 with 天's corrected reflection
  confirmed @1.00; 天/王/土 retired cleanly per the
  retire-only-after-confirmed-reflection rule.
- Why this batch: The Curator's c11 summary judged the Phase-2
  thesis (emergent memory transfers, composes, AND self-corrects)
  well-evidenced — two 3/3 cycles, a completed wrong→falsify→
  correct→confirm arc, 14 solved characters. Advancing to Phase 3
  (multi-radical characters). To isolate the NEW skill — arranging
  two known sub-characters into one glyph — every character here is
  built only from already-solved sub-characters: 林 = 木+木 (side by
  side), 古 = 十 over 口 (stacked), 困 = 口 enclosing 木 (nesting).
  This tests the three canonical radical arrangements without any
  new strokes or sub-characters.

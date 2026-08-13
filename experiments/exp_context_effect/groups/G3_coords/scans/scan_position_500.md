# Errata scan @ position 500 (B9 end / B10 start) — G3 curator

**Regime**: v10 trajectory-view retry prompt (first full B9 test).
Result on retry channel: 0/4 PASS (仔, 平, 矢, 失 all FAILed). v10
did not earn its keep as a distinct retrieval lever from v9 — the
HIGH-confidence bet (仔, predicted to graduate by surfacing zi_char
past-PASS) failed. Two of the four TERMINAL_FROZEN this scan.

**v11 introduced pass_index.md** — every past PASS with PNG paths,
available to curators for reflection. Confirms 224 total G3 successes
through B9. Used this scan to inspect PASSed 亻+bank-right compositions
(kang_char, zhong_char, dui_char, tong_same) as templates for the B10
retrieval-leak candidates.

**v12 verdict live from B9**: G3 0 A's vs G4 11 A's on identical items;
G3 28% vs G4 40% PASS. Code-format ceiling now diagnosed and named in
drawer_memory.md B9 addition. **The gap is structural to G3's memory
unit (PIL line primitives vs G4's 米字格 + P/T/N/S joint grammar) and
cannot be closed by prompt or retrieval improvements alone.** Going
forward, judge G3 by PASS rate on its winnable composition families
(identity-alias, envelope+interior, 亻+bank-right); do NOT chase A
verdicts on cursive/X-crossing/mirror-splay families where the format
ceiling holds.

**v13 introduced BANK_DEVIATION channel** — drawers may inline a fresh
sub-component when a bank primitive doesn't fit, provided they add a
`BANK_DEVIATION:` comment block at the top of `generated.py` naming
what/why/fresh_component. Curator promotes reusable fresh sub-elements
as NEW bank variants.

**BANK_DEVIATION scan on B9 PASSes**: 0/14 attempts contain a
BANK_DEVIATION block. Drawers are inlining freely (per v8 posture) but
not annotating the deviation. Either (a) the v13 signal did not reach
drawers via the prompt build, or (b) drawers don't consider their
inlined sub-components "deviations from a specific bank primitive"
since they never called the primitive to begin with. Recommend the
head curator check the drawer prompt build for v13 language.

**Cooldown-50 rule**: no item may be retried within 50 curriculum items
of its last retry. Items retried at position 450 (B9r: 仔, 平, 矢, 失)
are cooldown until position 500 — B10 (501–550) is the earliest
eligible re-window for the 2 that didn't TERMINAL_FREEZE (矢, 失).

## Retry candidates for B10 (positions 501–550)

### (a) Composition-retrieval leaks from B9 mains (HIGHEST PRIORITY)

Five B9 fails had ALL PARTS BANK-MASTERED but the drawer inlined
fresh instead of composing bank calls. Under v10 trajectory-view,
seeing past PASS PNGs of the constituent bank primitives should
surface the identity-alias recipe.

- **p3_char_0295_时** (retry_0 → retry_1) — HIGH: 日 (bank ri) + 寸
  (bank cun). Trajectory should surface p3_char_0225_日 PASS PNG and
  p2_radical_045_寸 PASS. Explicit instruction: call `ri.draw_ri(t, ox=-40, scale=0.55)`
  + `cun.draw_cun(t, ox=+40, scale=0.55)`.
- **p3_char_0296_串** (retry_0 → retry_1) — MEDIUM: bank kou ×2 +
  central shu. Prior attempt used scale 0.42 (too small). Explicit
  instruction: kou at scale 0.55, stacked with clear central shu
  protruding above top box and well below bottom box.
- **p3_char_0304_疖** (retry_0 → retry_1) — MEDIUM: bank ne_sick (疒)
  + bank jie_radical (卩). Explicit instruction: call jie_radical for
  right. B7 v9 疒-graduation trajectory should surface.
- **p3_char_0306_亨** (retry_0 → retry_1) — MEDIUM: bank tou_char +
  bank kou + bank liao. Stack proportions: tou 30/300 top, kou middle
  band (small ~0.4 scale), liao bottom (~0.45 scale).
- **p3_char_0315_声** (retry_0 → retry_1) — LOW-MEDIUM: bank shi_male
  + bank shi_radical. Prior attempt cramped 尸 hook. Explicit
  instruction: 士 top ~30% of canvas, 尸 bottom ~60%.

### (b) Retrospective — items now more likely to pass under v10

- **p3_char_0197_矢** (retry_2 → retry_3) — LOW-MEDIUM: X-crossing.
  v10 didn't move it in B9. Format ceiling likely. If B10 fails,
  TERMINAL_FREEZE.
- **p3_char_0216_失** (retry_2 → retry_3) — LOW: same as 矢. If B10
  fails, TERMINAL_FREEZE.

### (c) Prospective — prereqs for 501–550

Item pool 501–550 continues 亻-family + starts 佥/侃-cluster (7-8 stroke
compounds). Expected fail modes:
- Continued sub-radical gate (匕/也/夂 TERMINAL block ~10 items).
- New: 木-left compounds (林-type) — 木 bank works but composition needs
  care.
- New: 女-left compounds (女 has bank? — check INDEX; if not,
  add to sub-radical wishlist).

## Freeze / skip

- **p3_char_0173_仔** — TERMINAL_FREEZE this scan. HIGH-confidence v10
  bet failed; format ceiling on 亻+子.
- **p3_char_0176_平** — TERMINAL_FREEZE this scan. Per scan_450 explicit
  policy after v10 fail.
- **p2_radical_011_匕** — TERMINAL_FROZEN (scan_450). Do NOT schedule.
- **p2_radical_028_人, p2_radical_030_入** — TERMINAL_FROZEN. Not
  schedulable.
- **p3_char_0154_他, p3_char_0134_化** — blocked on 也/匕. Deferred
  indefinitely.
- Cursive family (刀/弓/己/马/长/见/巛/幺/书/引/必/发/乎) — format
  ceiling. Do not schedule.
- 44 of 45 B9 mains left in errata are single-shot format-ceiling fails
  or sub-radical-gate fails. Only the 5 composition-retrieval-leak
  candidates + 2 X-crossing retros get B10 slots.

## Retry queue for B10 (in dispatch order — max 7 slots)

1. p3_char_0295_时 (retry_0 → retry_1) — HIGHEST: pure bank-composition
   retrieval test. Explicit call instructions.
2. p3_char_0296_串 (retry_0 → retry_1) — HIGH: bank kou ×2 with corrected
   scale.
3. p3_char_0304_疖 (retry_0 → retry_1) — MEDIUM: bank ne_sick +
   jie_radical.
4. p3_char_0306_亨 (retry_0 → retry_1) — MEDIUM: 3-bank stack with
   proportion guidance.
5. p3_char_0315_声 (retry_0 → retry_1) — MEDIUM: 2-bank stack with
   proportion guidance.
6. p3_char_0197_矢 (retry_2 → retry_3) — LOW-MEDIUM: last-shot X-cross;
   TERMINAL_FREEZE if fail.
7. p3_char_0216_失 (retry_2 → retry_3) — LOW: last-shot X-cross;
   TERMINAL_FREEZE if fail.

## Measurement plan for B10 retry channel

- **Primary metric**: composition-retrieval leak recovery.
  Goal: ≥ 3 of 5 leak-candidates (295_时, 296_串, 304_疖, 306_亨,
  315_声) PASS under v10 trajectory-view + explicit bank-call
  instructions.
  - If ≥ 3 pass → retrieval leak is the primary lever, not format
    ceiling. Codify explicit-call retry recipe in drawer_memory.md.
  - If ≤ 1 passes → even explicit instructions don't overcome the
    drawer's inline-preference habit. Deeper prompt intervention needed.

- **Grep for bank imports** in each retry's `generated.py`:
  `grep -c "^from\|^import.*bank\|from.*success_bank" retry_attempts/*/generated.py`.
  Goal: ≥ 4 of 7 explicitly import a bank module (vs B9's inline-only
  pattern).

- **X-crossing family** (矢/失): if either PASSes, X-crossing ceiling
  is broken by v10 trajectory-view for that family; back-schedule
  乔/癶 for B11. If neither PASSes: TERMINAL_FREEZE both and publish
  the X-crossing-family finding.

- **Overall B10 target**: PASS rate ≥ 25% on mains (below B9's 28% is
  acceptable if item pool got harder; below 20% is concerning).
  A-verdict count remains 0-expected per v12 code-format-ceiling
  diagnosis.

## A-tier gate — reaffirmed

Per scan_450, bank promotions this batch: **0** (0 A verdicts). All
14 B9 PASSes are PASS-tier scaffolds — usable as recipes to consult
via pass_index.md but not promoted to `success_bank/code/` as bank
entries. This keeps INDEX quality high while pass_index absorbs the
PASS-tier evidence for the drawer to browse.

Under v13 BANK_DEVIATION channel, variant promotions this batch: **0**
(0 BANK_DEVIATION blocks detected in B9 PASSes — see note above about
prompt-build audit).

## Notable structural finding — bank retrieval preference

Cross-referencing B9's 14 PASSes:
- 6 called bank primitives at least once (光 uses inline, 甸 uses none,
  这 imports wen, 町 imports ding_char, 里 fully inline, 作 inline,
  疔 inline, 进 inline, 亩 inline, 伯 inline, 佃 imports ren_pang, 但
  inline, 佇 inline, 佐 inline).
- Only 3/14 (~21%) actually imported a bank module.
- 11/14 chose inline PIL over bank calls — including cases where the
  composition WAS bank-composable (作 has ren_pang left; 但 has ri_char
  center-right; 伯 has ri variant).

**This is the same pattern as the 5 B9 fails' retrieval leak: drawers
under v8 "trust GT + inline fresh" posture are DEFAULTING to inline
even when bank aliases would work.** The inline preference is helping
survive the code-format ceiling on cursive items (where bank primitives
would be too heavy) but is losing "free" bank-composition PASSes.

**Recommendation for head curator**: consider a v14 prompt tweak that
requires the drawer to explicitly answer "for each stroke/component,
is there a bank alias?" and, if yes, "why NOT call it?" before
inlining. This puts the inline choice under audit without forcing it.

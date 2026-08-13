# Errata scan @ position 450 (B8 end / B9 start) — G3 curator

**Regime**: v9 visual-diff retry prompt (2nd rerun). B8 retries 0/7
under v9-2nd-rerun (vs 3/10 in B7r first-rerun). v9 lift is fading —
appears to have been a one-time effect on items whose prior PNGs had
easily-namable visual gaps.

**v10 change (going forward, B9)**: retry drawers now see FULL attempt
trajectory (all past attempts, including any past PASSes with their
verdicts labeled) — not just the most recent fail. Distinct lever from
v9's visual-diff; deserves its own test. Also, judge tool gains an "A"
(perfect) verdict beyond PASS — informational for curator promotion
priority, doesn't change retry eligibility.

**Cooldown-50 rule**: no item may be retried within 50 curriculum items
of its last retry. Items retried at position 400 (B8) are cooldown
until position 450 — B9 (451–500) is the earliest eligible re-window
for the 6 that FAILed the v9-2nd-rerun (匕 was TERMINAL_FROZEN).

## Retry candidates for B9 (positions 451–500)

### (a) Prospective — prereqs for 451–500

Peek at upcoming items 451–500 (from curriculum ordering; the 亻-family
density likely continues through position 460, then may transition to
compound characters with 女/宀/木/水/心 left radicals):
- **匕-family compounds** — 化 already retry_2 FAIL. 比 (247+ ish),
  花, 华 all need 匕 which is now TERMINAL_FROZEN. **Do not schedule
  匕 retries.** For chars needing 匕 as sub-radical, drawer_memory
  "give up on 匕 as bank primitive" note applies.
- **也-family compounds** — 池/驰/她 likely in 451–500 band; 也 has
  no bank entry and 他 v9 rerun failed. Deferred (blocked on 也
  sub-radical mastery — but no protocol path to master a sub-radical
  as a fresh Phase-2 attempt).
- **戈-family compounds** (成/伐/戏/戚) — 戈's 斜钩 arc unmastered;
  the tapered-bezier recipe from da_char (bank #201) can partially
  transfer. Consider one retry of 成 under v10 trajectory-view.

### (b) Retrospective — items now more likely to pass under v10 trajectory-view

Under v10, retry drawers see ALL prior attempts. Items whose past
trajectory INCLUDES a PASSing template (from a related item) benefit
most; items whose only trajectory is a chain of same-flavored fails
benefit least.

- **p3_char_0173_仔** (retry_2 FAIL B8) — HIGH-CONFIDENCE candidate.
  Trajectory-view will surface p3_char_0049_子 PASS (bank #122 zi_char)
  and the drawer will finally see that calling zi_char verbatim is an
  option. Recipe: `draw_zi(t, ox=+40, oy=0, scale=0.65)` + inline 亻
  on left. B8 attempt inlined a fresh 子 rather than using zi_char.
- **p3_char_0176_平** (retry_2 FAIL B8) — MEDIUM. No exact bank ancestor;
  trajectory-view surfaces past 主 (bank #202 GRADUATED) which shares
  the same "dots above heng" motif. B8 attempt diagnosed the top
  correctly but hand-render off. One more shot under v10; then
  TERMINAL_FREEZE if fails.
- **p3_char_0154_他** (retry_2 FAIL B7r) — LOW. Trajectory has only
  fails. 也 sub-radical unsolved; no PASSing ancestor to surface.
  Deferred; do not schedule until 也 is solvable.
- **p3_char_0134_化** (retry_2 FAIL B7r) — LOW. 匕 now TERMINAL_FROZEN;
  no PASSing ancestor. Deferred; do not schedule.
- **p3_char_0197_矢** (retry_1 FAIL B8) — MEDIUM. Trajectory-view
  surfaces 大 (bank #201 GRADUATED) — same X-crossing family. B8
  attempt cited 大_char.py recipe in the visual diff. One more retry
  under v10 to see if seeing 大's full PASSing trajectory produces
  cleaner geometry propagation.
- **p3_char_0216_失** (retry_1 FAIL B8) — MEDIUM. Same as 矢 — X-crossing
  cousin of 大. One more retry under v10.
- **p3_char_0226_乔** (retry_1 FAIL B8) — LOW-MEDIUM. 夭-top family;
  further from 大's exact recipe than 矢/失. Defer.
- **p3_char_0193_癶** (retry_1 FAIL B8) — LOW. Bilateral X-crossing;
  even 大 (unilateral) needed 5 retries. Defer.

### Freeze / skip

- **p2_radical_011_匕** — TERMINAL_FREEZE (retry_5 all FAIL across
  v7/v9-rerun/v9-2nd). Do NOT schedule for B9 or later. Same format
  ceiling as 人/入 (2-stroke primitives where every calligraphic
  detail is load-bearing).
- **p2_radical_028_人, p2_radical_030_入** — TERMINAL_FREEZE_AGAIN
  (B7r v9 rerun FAIL). Not schedulable.
- **p3_char_0154_他, p3_char_0134_化** — blocked on unsolved sub-
  radicals (也, 匕). No protocol path to solve. Deferred indefinitely.
- Cursive hook family (刀, 弓, 己, 马, 长, 见, 巛, 幺, 书, 引, 必, 发,
  乎) — format ceiling holds.
- B8 mains left in errata — 41 items; most are single-shot fails.
  Only the 3 v10-retry-worthy candidates above get B9 slots.

## Retry queue for B9 (in dispatch order — max 5 slots)

1. p3_char_0173_仔 (retry_2 → retry_3) — HIGH: v10 surfaces zi_char
   PASS. EXPLICIT instruction to call `zi_char(t, ox=+40, scale=0.65)`
   verbatim rather than inlining fresh 子.
2. p3_char_0176_平 (retry_2 → retry_3) — MEDIUM: v10 surfaces 主 PASS
   template (bank #202). Last-shot; TERMINAL_FREEZE if FAIL.
3. p3_char_0197_矢 (retry_1 → retry_2) — MEDIUM: v10 surfaces 大 PASS
   (bank #201) full trajectory. Try da_char recipe.
4. p3_char_0216_失 (retry_1 → retry_2) — MEDIUM: same as 矢. Try
   da_char recipe.
5. Slot free — reserve for a B8-main FAIL if it turns up an obvious
   prereq for 451–500 curriculum items.

## Measurement plan for B9 retry channel

- Grep retry `generated.py` files for citations of PAST-PASSING
  attempts (not just descriptions but explicit path references, e.g.
  `success_bank/code/da_char.py`, `success_bank/code/zi_char.py`).
  Goal: ≥ 3 of 4-5 retries cite a v10-trajectory-surfaced ancestor.
- Retry PASS rate: goal ≥ 20% (vs B7r 30%, B8 0%). Anything less
  means v10 trajectory-view didn't earn its keep as a distinct
  lever from v9 visual-diff.
- Bank template propagation for the X-crossing family (矢/失):
  goal is ≥ 1 that visibly uses `from success_bank.code.da_char import
  draw_da_char` (or equivalent module import). Not just "cite in
  comments" — actually IMPORT and CALL.
- If retry pass rate < 15% AND no import-level template propagation:
  v10 trajectory-view falsified as a retrieval mechanism. Recommend
  the head curator retire the retry mechanism a second time (final)
  and publish the format-ceiling finding.

## "A" verdict signal (informational for B9)

Judge now returns A/PASS/FAIL. Curator will:
- Promote **only A-tier PASSes** to `success_bank/code/` as bank
  entries (elevated quality gate).
- Log **PASS but not A** items to bank as "aliases/reference" only —
  usable as scaffolds but not held up as the exemplar recipe.
- Continue to log FAIL to errata.

This distinction changes bank promotion policy going forward. Existing
bank entries (through B8) are grandfathered as PASS-tier. The B9
promotion policy under A-tier gate will likely reduce promotion count
by half — an intentional quality-over-quantity shift.

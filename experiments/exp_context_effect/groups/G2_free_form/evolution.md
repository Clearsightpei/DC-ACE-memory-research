# G2 memory-structure evolution log

Append-only. One entry per structural change to G2's memory
organization. This log is the emergence record — how G2's memory
converges (or fails to converge) on a self-directed structure.

Format:
```
## <YYYY-MM-DD> @ position <N> — <one-line summary>

**Files changed**: <what was created / deleted / restructured>

**Rationale**: <why this change was made — the diagnostic evidence
              or hypothesis>

**Expected help for**: <what kinds of future items this should help,
                       so we can check whether the change actually
                       helped>
```

---

## 2026-07-18 @ position 150 — evolution log created

**Files changed**: created `evolution.md` and `memory_index.md`.

**Rationale**: v7 protocol change (see `README.md` v7 changelog).
Memory self-evolution unlocked for G2 after all-group score collapse
in B2 (G2 dropped from 83% bootstrap → 70% B1 → 40% B2, cumulative
59% across 118 items). Diagnosis: memory was accumulating meta-rules
and per-item mastery ledgers but not contextual form/position
knowledge that transfers across similar items. The evolution unlock
lets the curator restructure memory freely within the "free-form
markdown" constraint. This log tracks whether and how the curator
converges on a useful structure.

**Expected help for**: nothing yet — this is the baseline entry. The
next real change (curator creates a new file or reorganizes one)
should describe what it expects to help with.

---

## 2026-07-18 @ position 168 — split contextual-form knowledge into two new files

**Files changed**:
- CREATED `form_catalog.md` — stroke forms indexed by
  `(class × context)`. Entries for 撇, 点, 竖, 横, 折 shoulder,
  捺 across their common contexts, plus a sibling-pair topology
  signature table and left-position radical compression rules.
- CREATED `radical_position_rules.md` — silhouette-first heuristic,
  aspect-ratio families, center-of-mass rules, 米字格 as an eyeball
  aid, failure-mode cross-index.
- RESTRUCTURED `memory_index.md` — drawer's read order now
  1) radical_position_rules → 2) form_catalog → 3) drawer_memory.
  Old order sent drawers directly to a wall of meta-rules; the new
  order matches the drawing workflow (silhouette first, then
  contextual stroke lookup, then technique fallback).
- RETAINED `drawer_memory.md` unchanged. It remains the technique
  reference (PIL brush-dabs, arc primitive, beat-count rule) and
  the append-log for per-batch principle distillation and mastery
  ledgers. Retiring it entirely would lose the technique material
  the drawer legitimately needs during rendering.

**Rationale**: batch B2 confirmed the user's diagnostic hypothesis.
The cumulative trajectory 83 → 70 → 40% cannot be explained by
increasing item difficulty alone — the memory format was actively
misleading. Drawers were retrieving global rules ("draw the flick",
"share joints", "label > GT-tracing") but were still failing on
items where the failure mode was **contextual form ignorance**:
- 忄's dot pair drawn as if from thin air because there was no
  entry for "点 as 忄 side dot".
- 车 drawn with a body 竖 that failed to pass through both 横
  because there was no entry for "竖 as through-going axis".
- 火, 风, 长 drawn as ambiguous silhouettes because there was no
  aspect-ratio + center-of-mass check before stroke placement.
- Sibling pairs (士/土, 己/巳, 匕/七) kept failing because the
  differentiating bit was buried in a length-table paragraph
  rather than surfaced as an explicit "check the signature" table.

The new `form_catalog.md` inverts the retrieval axis: instead of
"list of principles" (retrieval by rule) it becomes "list of contexts
per stroke class" (retrieval by what-am-I-drawing-right-now). The
new `radical_position_rules.md` promotes silhouette to a mandatory
pre-drawing check, following the observation that most B2 fails were
silhouette failures compounded by stroke-detail attempts to rescue
already-wrong layouts.

We did NOT delete `drawer_memory.md` because doing so would strip
the drawer of proven technique code (brush-dabs formula, arc primitive,
Bezier control-point conventions) that has nothing to do with the
meta-vs-contextual axis and is still cited by successful renders. That
file is now backstop, not entry point.

Format constraint respected: both new files are free-form markdown.
No code primitives (that would be G3). No 米字格 machine anchors
(that would be G4) — 米字格 is used only as an eyeball aid the
drawer applies mentally during self-check.

**Expected help for**:
- Radicals with sibling ambiguity where the differentiating bit is
  a stroke length ratio, endpoint position, or crossing topology
  (士/土, 己/已/巳, 匕/七, 人/入, 木/未/末, 户/尸, 大/太/犬).
- Radicals whose failure mode has been "wrong silhouette / cramped /
  wrong center of mass" (巾, 门, 车, 风, 火, 灬 four-legs).
- Radicals with left-position compression rules (亻, 犭, 木-left,
  忄) — the compression is now explicit rather than implicit.
- 3-stroke radicals with a prominent 撇 whose context (top-hat vs
  body-crosser vs left-position) determines its length and angle
  (夕, 力, 攵, 攴).

**How we will know if it helped**: G2's next batch (B3) score. If
the restructure works, we should see (a) the sibling-pair failures
drop, (b) silhouette failures drop, (c) the trajectory 40 → ??%
recover meaningfully. If it does NOT help, that's a genuine research
finding about self-directed memory limits — log it and try again.

---

## 2026-07-22 @ position 213 — v7.1 retrieval sharpening (index + hard rule)

**Files changed**:
- MODIFIED `memory_index.md`: added two new sections at the TOP —
  (1) HARD RULE "sibling-bit override" and (2) HOT LOOKUP retrieval
  index table mapping common contexts to specific entries.
- EXTENDED `form_catalog.md`: added B3 (class × context) entries for
  卧钩 as 心-bowl base, 二 as top-of-radical stacked pair,
  撇+竖弯钩 as leg-pair, 内-square 曰/日, 月 as left-position box,
  又 as two-stroke fork, 乂 as body-cross. Added new
  `Char × structural_role` table (starts with B3 P3 chars 一, 丨,
  亻, 儿, 冂, 凵, 冖, 亠, 冫, 八, 力, 又, 十, 心, 月, 王, 文, 无,
  曰, 爻, 厂, 七, 乂).

**Rationale**: B3 evidence — the v7 restructure IS helping when
consulted (all 4 retry PASSes cited form_catalog entries directly).
But the citation rate is uneven: 3/17 (18%) of new P2 attempts and
13/33 (39%) of new P3 attempts cited the new files. Bigger problem:
the `p3_char_0011_人` fail proved that even when a drawer cites
sibling-pair signatures it can then override them via GT-tracing.

Two targeted fixes rather than a full restructure:
1. HARD RULE at the top of memory_index makes sibling-bit overrides
   a bright-line "don't" — same energy as drawer_memory bootstrap
   principle 1 ("label > GT-tracing") but scoped to the specific
   failure mode we see recurring.
2. HOT LOOKUP is a retrieval shortcut — condenses "what to look at
   when drawing X" into a single scannable table at the top, so
   drawers don't have to grep the whole catalog under time pressure.

We deliberately did NOT restructure form_catalog by radical family
or split into more files — B3's evidence is that structure is
correct, retrieval is weak. Splitting further would add friction.
Instead we surface high-value entries in a top-of-file index.

**Expected help for**:
- Recurring signature-bit failures (人/入, 士/土, 匕/七, 己/巳,
  木/未/末) — HARD RULE should stop over-reasoning.
- P3 char drawing (Phase-3 has begun; the char × structural_role
  table gives future P3 items a direct template to inherit).
- Drawer retrieval friction — HOT LOOKUP puts common contexts one
  scan away instead of one grep away.
- If B4 shows drawers still ignore the index, that's a signal the
  problem is upstream (drawer prompt, not memory structure) — log
  it and consider reshaping the drawer's read prompt in v7.2.

**How we will know if it helped**: B4 pass rate for (a) sibling-pair
risk items and (b) P3 chars that map onto the char × structural_role
table. Also: citation rate in generated.py — target 60%+ for
non-trivial items (up from current ~30%).

---

## 2026-07-23 @ position 277 — B4 diagnostic + create sibling_signature_checklist.md

**Files changed**:
- CREATED `sibling_signature_checklist.md` — a small, single-scan
  companion file containing (a) a 34-row "bright-line bits" table of
  sibling-risk targets with their one-sentence signature bit and
  common wrong-render, and (b) a 6-row "bright-line flicks" table
  giving the required terminal-hook direction per stroke-family.
  Both tables are copy-verbatim: the drawer is instructed to paste
  the row directly into their generated.py docstring.
- EXTENDED `form_catalog.md`: added B4 (class × context) entries for
  every new PASS target (刁, 丁, 刂, 勹, 匕, 之, 丫, 大, 上, 乇, 亍,
  于, 亡, 下, 亼, 三, 小, 兀, 卄, 门, 叉, 囗, 山, 夂, 口, 千, 艹, 宀,
  才), plus 29 new rows in the char × structural_role table, plus
  a B4-additions sibling-pair table (刁/丁, 亍/于/千, 大/六, 山/凵,
  个/亇, 丸/九, 孑/孓/子, 尢/九, 之/乏, 于/亍).
- UPDATED `errata.md`: 3 GRADUATED (干, 止, 入), 11 retry_n
  incremented with B4 failure notes, 21 new main-B4 fails added.
  BATCH B4 UPDATE header at top with the full citation-rate audit.
- UPDATED `memory_index.md`: added a top-of-file pointer to
  sibling_signature_checklist as the FIRST read for sibling-risk
  targets.

**Rationale**: B4's numbers — main 29/50 = 58% (down from B3's 60%),
retries 3/14 = 21% (DOWN from B3's 31%) — combined with the citation-
rate audit tell a specific story. The v7.1 HOT LOOKUP added at pos
213 is essentially invisible: 0/64 drawers cited it. The HARD RULE
was cited by 4/64. form_catalog citation was 21/64 (33%), and among
retries specifically retry-PASSes cited form_catalog 3/3 (100%) while
retry-FAILs cited form_catalog 5/11 (45%). So when drawers DO
consult, form_catalog helps. The failure isn't structural — it's
retrieval. Also: of 11 retry FAILs, 5 were "draw the flick" hook-
direction failures (匕, 飞, 门, plus 也 and 习 in the main cohort's
similar mode), 4 were sibling-bit collapses (乃→万, 九→勹, 孓→子,
夊→夂), and only 2 were novel modes. So the retry regression is not
a diverse failure spectrum — it's a narrow one that the existing
memory already TREATS but the drawer doesn't RETRIEVE.

Three options were considered:
1. Prune drawer_memory's per-batch mastery ledgers — but they're
   inert (not competing for retrieval, just tail data). Low value.
2. Move HOT LOOKUP into the drawer prompt — outside the curator's
   authority; that's a harness change, not a memory change.
3. Split form_catalog per phase — adds friction; B4 evidence is
   form_catalog structure is right, retrieval is weak.
4. **CHOSEN**: create a small dedicated signature-bit checklist file
   with a single, dense, copy-verbatim table. Rationale: the failing
   drawers already read multiple files; the barrier is scan cost per
   file. A short (<200 lines) file whose purpose is one narrow task
   (check the signature bit before drawing) has a much higher chance
   of being read cover-to-cover than a buried table inside memory_index.
   The "copy the row verbatim" instruction is a retrieval enforcement
   trick — if you copy it, you can't override it.
5. Explicit KEEP was also weighed — the B3→B4 drop is 2 percentage
   points on 50-item batches (well within noise), and the retry drop
   is on n=14 (variance-dominated). But the FAILURE MODE audit is
   NOT noise: the mode breakdown is consistent with B3, meaning the
   retry cohort has stabilised on a narrow, treatable failure set.
   Choosing to act rather than wait.

We deliberately did NOT restructure form_catalog or delete anything.
Additive changes only. This file also does not overlap with the
HARD RULE in memory_index — the HARD RULE is the enforcement
principle, this new file is the enforcement mechanism (the
verbatim-copy step).

**Expected help for**:
- Recurring retry cohort: 匕, 飞, 门, 己, 乃, 九 — all in the new
  bright-line bits or bright-line flicks tables.
- P3 sibling-risk chars in future batches: 个, 亇, 亾, 孑, 孓, 尢
  — all now in the bright-line bits table.
- Any new P3 draw where the target label is one of the 34 sibling-
  risk items — the checklist collapses the "look up 3 files" cost
  to "read one line and paste it".
- Citation rate should measurably rise for these items (target: 50%+
  citing sibling_signature_checklist by name, up from HOT LOOKUP's
  0% baseline).

**How we will know if it helped**: B5 metrics. Two specific targets:
1. Retry pass rate ≥ 30% (recover to B3 baseline). If retries stay
   at 20% or drop further, the intervention failed — signal the
   problem is drawer-side (not memory-side) and escalate.
2. Citation rate for `sibling_signature_checklist` in generated.py
   for the 14 retry-cohort items ≥ 50%. If citation is <20%, drawers
   are not reading new files even when narrow and dense — a stronger
   signal that memory-side interventions are hitting diminishing
   returns.

If BOTH targets miss in B5, the next evolution entry should
explicitly acknowledge the retrieval ceiling and consider a
restructure that consolidates rather than adds. If retry rate recovers
even without high citation, that's a puzzle (memory-invariance) worth
investigating separately.

---

## 2026-07-24 @ position 327 — B5 diagnostic + retry-mechanism restructure

**Files changed**:
- APPENDED `errata.md`: 2 GRADUATED (士, 攴), 11 retry_n incremented
  (6 of them tipped to `FROZEN_AT_RETRY_3`: 马, 尢, 夂, 车, 风, 旡, 牛),
  26 new main-B5 fails added in NEW compact-table format (line 1722+)
  to test whether format bloat itself was suppressing citation.
- EXTENDED `form_catalog.md`: 20 new char × structural_role entries
  from B5 PASS cohort (屮 工 川 义 乡 廾 弋 不 丹 为 以 中 亓 日 仄 心 文 冈 太 龶)
  + 7 new sibling-pair rows (士/土, 中/口, 义/乂, 冈/冂, 太/大, 廾/井, 亓/元).
- UPDATED `retry_log.jsonl`: 13 B5 outcomes finalized (2 PASSED, 11 FAILED).
- APPENDED `curator_satisfaction_log.jsonl`: 63 B5 entries (24 main
  PASS, 26 main FAIL, 2 retry PASS, 11 retry FAIL).

**B5 numbers**:
- Main: 24/50 = **48%** PASS (B4: 58%, B3: 60%) — main-pass rate
  DROPPED 10 points.
- Retry: 2/13 = **15%** PASS (B4: 21%, B3: 31%) — retry-pass rate
  DROPPED again, third batch in a row. Both v7.2 targets (retry ≥30%,
  checklist citation ≥50%) MISSED. The v7.2 sibling_signature_checklist
  did help two items decisively (士 via 士/土 row, 攴 via off-cooldown
  errata recipe) but not enough to reverse the trend.

**Trend interpretation**:
- Downward retry trend is now 3 batches long (31% → 21% → 15%) and no
  longer plausibly noise on n=13-14. The retry cohort is not just
  narrow, it's ossifying: 7 items now sit at retry_n ≥ 3 (FROZEN);
  another 4 (巛, 长, 见, 方) sit at retry_n = 2 and are trending toward
  freeze. Only 2 items have graduated in the last two batches (士, 攴).
- Main-pass drop (58% → 48%) is a larger, worrying signal on its own —
  but the P3 batch content shifted from 3-stroke to mostly 4-stroke
  compound characters (人-lid + body, 亻 + radical, 冂 + interior), so
  some drop was expected. Still, 10 points suggests memory is not
  transferring COMPOSITION knowledge — form_catalog covers atomic
  radicals well but the "亻 + X" or "冂 + interior" composition rules
  are only implicit.
- v7.2 evidence: sibling_signature_checklist rows that landed (士/土)
  used the "move-knob-further" recipe verbatim. Rows that did NOT land
  (贝/见, 尢/九) were treated as tweaks rather than exaggerated moves.
  The checklist itself is not at fault — the drawer's calibration is.

**Self-evolution decision — options weighed**:

1. **Prune memory that's not helping.** Candidates: (a) drawer_memory
   per-batch mastery ledgers (inert tail data), (b) errata entries for
   FROZEN items (they occupy slots the drawer scans past but never
   acts on). Concern: pruning may erase provenance the paper needs.
2. **Freeze chronic retry items formally.** Move all FROZEN_AT_RETRY_3
   items out of the active retry cohort into a separate
   `frozen_cohort.md` (or a bottom section of errata) so the retry
   scan doesn't have to skip them. This is minimal-change and
   reversible.
3. **Retire the retry mechanism entirely.** The retry cohort has
   burned three batches (B3, B4, B5) each spending ~14 slots on items
   that pass at 31%/21%/15%. If new-P3 items have higher marginal
   value, moving those retry slots to new P3 items would raise total
   throughput.
4. **Accept G2 free-form has hit a ceiling.** Stop adding memory,
   observe whether unchanged-memory batches maintain 48% main-pass
   (i.e., verify memory-invariance) or degrade.
5. **Restructure form_catalog toward COMPOSITION rules.** Add a
   dedicated composition-rules file: "亻 + X → left-radical scaling",
   "冂 + interior → interior at lower third", "亠 + X → lid centering",
   etc. B5 main fails 仇 仑 仓 内 內 all fall in this bucket.

**CHOSEN**: **Option 2 (freeze chronic) + Option 5 (composition
rules), NOT Option 3 or 4.**

Rationale for 2: The 7 FROZEN items are consuming retry slots the
drawer visibly scans past (per the citation audit — drawers don't
cite errata sections tagged FROZEN, they cite the compact top-of-file
listings). Moving them out of active rotation frees ~7 slots per
batch AND removes noise from the retry-pass-rate metric (which is
currently averaging FROZEN retry failures with fresh retry attempts,
depressing the rate artificially).

Rationale for 5: B5 main-fail breakdown is dominated by compound
characters (亻/冂/亠 + radical). Adding atomic-radical entries to
form_catalog was the right move for B3-B4 (P3 was mostly single-
component) but B5 shifted to composition and the memory didn't shift
with it. Adding a composition-rules file is analogous to the v7.2
checklist trick: a small, narrow, dense new file with copy-verbatim
rules. Testable.

Rationale AGAINST 3 (retire retry): premature. The 2 B5 graduations
(士, 攴) prove the mechanism CAN work when a matching rule exists.
Retiring would forfeit that. The right first move is to reduce noise
in the metric (freeze chronic) before deciding to kill it.

Rationale AGAINST 4 (accept ceiling): the retry drop is confounded
with retry-cohort ossification. Cannot conclude ceiling until the
cohort is de-noised.

**Concrete actions taken this position**:
- The 7 FROZEN_AT_RETRY_3 items (马, 尢, 夂, 车, 风, 旡, 牛) are marked
  in errata but will additionally be listed in `frozen_cohort.md`
  (created next position) with retry-cohort scan instructions:
  "SKIP UNLESS an evolution.md entry explicitly unfreezes them".
- `composition_rules.md` to be created next position covering: 亻+X,
  冂+interior, 亠+lid, 人+lid, 厂+人, 卩/阝 stacking. Draws on B5
  main-fail evidence (仇, 仑, 仓, 内, 內, 分, 冗).

**Expected help for**:
- Retry-pass rate: removing 7 frozen items from denominator lifts the
  effective B6 retry cohort to fresher targets (巛, 长, 见, 方 at retry_n=2;
  plus 3 new promotions from B5 main-fail table). If B6 retry rate
  rebounds to ~30% on this de-noised cohort, freeze policy is
  validated.
- Main-pass rate on compound-character P3 items: composition_rules.md
  targets exactly the failure mode (亻+radical, 冂+interior) that cost
  ~7 of B5's 26 main fails.

**How we will know if it helped**: B6 metrics.
1. On the de-noised retry cohort (frozen items excluded), retry-pass
   rate ≥ 30%. If retry is <20% AGAIN, the freeze-and-add-composition
   combo failed — escalate to Option 3 (retire retry) or Option 4
   (accept ceiling) in the B6 postmortem.
2. Compound-character main-pass rate (items involving 亻/冂/亠/人-lid)
   ≥ 60%. If <45%, composition-rules file joined the checklist as
   another additive-not-effective intervention and the retrieval
   ceiling is real.
3. Explicit anti-goal: NOT adding new atomic-radical entries to
   form_catalog unless a genuinely new form appears in a B6 GT. B5
   evidence is form_catalog is saturating on atomic content.

If B6 misses both targets, the B6 evolution entry MUST commit to
either Option 3 or Option 4 — no more additive interventions on the
G2 free-form arm.

---

## 2026-07-26 @ position 388 — B6 postmortem: RETIRE the retry mechanism (Option 3)

**Files changed**:
- APPENDED `errata.md`: B6 UPDATE header with the 0/11 retry pass rate,
  compact-table for 24 new B6 main fails, retry-note appends to
  匕, 阝, 弓, 比, 礻, 水, 人, 刀 sections, promoted 仇/仑/内 from
  compact table to full sections.
- APPENDED `drawer_memory.md`: single new principle "Sibling bits apply
  at COMPONENT level" — the one non-noise emergent B6 pattern (仕, 去,
  比-LEFT all share this failure mode).
- APPENDED `curator_satisfaction_log.jsonl`: 61 entries (26 PASS + 35
  KEEP-GOING).
- MODIFIED `memory_index.md`: TIER-0 section D added — retry mechanism
  retired; new-P3 items only. Marker for drawer prompt behavior change.
- NO change to `composition_rules.md` (already at 0 citations after two
  batches — dead file, kept for provenance only).

**B6 numbers**:
- Main: 26/50 = **52%** PASS (B5: 48%, B4: 58%, B3: 60%). Modest recovery
  from B5 trough but still 6 points under B3.
- Retry: 0/11 = **0%** PASS (B5: 15%, B4: 21%, B3: 31%). Fourth batch
  in a row of monotonic decline. THE MECHANISM HAS ZERO YIELD.
- Composition_rules.md citations: 0/61 attempts. Same as pos 327 target
  #2 predicted "hitting diminishing returns."
- Sibling_signature_checklist citations: 8/61 (13%). Even lower than
  B5's 22%. Not being read.
- CBV candidates: 5/35 fails (14%). Consistent with B4-B5 rate.

**Decision — Option 3: RETIRE the retry mechanism**.

Per the pos 327 contract, both target metrics missed:
- Target 1 (retry ≥ 30% on de-noised cohort): 0% — worse than the
  frozen-included cohort ever was.
- Target 2 (composition-character main-pass ≥ 60%): compound-char
  subset was 14/28 = 50% — under threshold.
- Anti-goal (don't add atomic-radical entries): held.

Option 4 (accept ceiling) was considered but rejected: main-pass
recovered 4 points from B5, so G2 is NOT at absolute ceiling — it just
can't extract value from retry churn on ossified items. Recovering
those retry slots (11 per batch) for fresh new-P3 items is a
positive-expected-value shift.

**Retirement policy**:
1. No new retries added to G2 in B7+. Errata is preserved for the
   research record (per pos 168 "provenance is what the paper needs").
2. All items currently in `frozen_cohort.md` stay frozen; add the 8 B6
   retry-fails (阝, 弓, 水, 礻, 比, 匕, 刀, 仑, 仇, 内 — note 人 and 礻
   are CBV, kept out of freeze; 仑 and 仇 are new-freeze from B6 retry).
3. Fresh main P3 items only from B7 forward. Batch size = 50 (not 61).
4. This is IRREVERSIBLE without an evolution.md unfreeze entry.

**Rationale for irreversibility**: three batches of "one more try"
(B4, B5, B6 all promised recovery, all disappointed) suggest the
retry-cohort composition problem is real: items that fail at
retry_n=1 tend to fail at retry_n=2 and retry_n=3, because their
failure mode is either (a) a hook-flick that memory documents but
drawer doesn't execute or (b) a labeler-disagreement (CBV) that no
memory change can address. Neither is solvable by more retries.

**Also decided — CBV watchlist established**:
- p3_char_0011_人 (retry_n=3, CBV × 2)
- p2_radical_116_礻 (retry_n=1, CBV)
- p3_char_0069_干 (retry_n=0, CBV from B4)
- p3_char_0021_几 (retry_n=1, CBV from B4)
- p3_char_0033_刀 (retry_n=2, CBV from B4)
- p3_char_0102_天 (retry_n=0, CBV from B5)
- p3_char_0108_无 (retry_n=0, CBV from B5)
- B6 CBVs: 反 (p3_140), 仗 (p3_177), 乎 (p3_167)

Total: 9-10 items where memory-visible signatures ARE present but the
human labeler rejected. This is 14-16% of the fail cohort — enough
mass that it deserves its own postmortem chapter if the paper is written.

**Expected help for**:
- G2 throughput: recovering 11 retry slots per batch → 22% more
  fresh-item coverage per unit time.
- Curator noise floor: the retry-pass-rate metric will no longer
  average FROZEN failures with everything else — cleaner signal.
- Research narrative: the retirement itself is a G2 finding — free-form
  memory can converge, but its retry-cohort dynamics collapse when
  chronic-failure items dominate. This is publishable.

**How we will know if it helped**:
1. B7 main-pass rate ≥ 55%. If ≥60%, retirement was net-positive
   (recovered retry slots + reduced context noise). If <50%, the retry
   removal exposed a deeper G2 problem — reconsider.
2. B7 fresh-item first-attempt distribution should NOT skew easy — if
   compound-character (亻+X, 冂+X) rate matches B5-B6 (~50%), the
   retirement genuinely paid.
3. Anti-goal: no new memory files. Only append-only per-batch fails
   in compact-table format. If the curator feels the urge to create a
   new file, that's a signal the retirement isn't enough and the true
   ceiling is here.

**If B7 misses target 1**: acknowledge G2 free-form has hit ceiling
(Option 4). Stop making memory changes; observe memory-invariance
across B8-B10.

---

## Position 388 also — memory_index.md TIER-0 section D added

**Files changed**: `memory_index.md` — new TIER-0 subsection D announcing
retry retirement so future drawers know they're seeing fresh items only.

**Rationale**: drawer subagents don't read evolution.md (per B5 citation
audit: 0% cites). If retirement isn't surfaced in memory_index TIER-0,
they won't know retry is dead — could waste tokens looking for retry
context that doesn't exist.

---

## 2026-07-27 @ position 438 — B7 postmortem: CEILING DECLARED (Option 4)

**Files changed**:
- APPENDED `errata.md`: B7 compact-table with 29 new B7 main fails
  (items p3_char_0184–0233) + B7 diagnostic summary.
- APPENDED `curator_satisfaction_log.jsonl`: 50 entries (21 PASS + 29
  KEEP-GOING), tagged `"batch": "B7"`.
- APPENDED this evolution.md entry (pos 438) — ceiling declaration.
- NO change to `drawer_memory.md` (per pos 388 anti-goal — "no new
  memory files, only compact-table fails").
- NO change to `memory_index.md`, `form_catalog.md`,
  `radical_position_rules.md`, `sibling_signature_checklist.md`, or
  `composition_rules.md`.
- NO restructure. NO new files.

**B7 numbers**:
- Main: 21/50 = **42%** PASS. Compare: B6 52%, B5 48%, B4 58%, B3 60%.
  This is the LOWEST main-pass rate on record and 13 points below the
  pos 388 target of ≥55%.
- Retry: N/A (retired in B6 per pos 388).
- CBV candidates in the fail set: 2/29 = 7% (癶, 立) — lower than
  B4-B6's 14-16% band. The remaining 27 fails are structural, not
  labeler-strict.

**Decision — Option 4: ACCEPT CEILING**.

Per pos 388 contract: "If B7 misses target 1: acknowledge G2 free-form
has hit ceiling (Option 4). Stop making memory changes; observe
memory-invariance across B8-B10."

Target 1 (main ≥ 55%): MISSED at 42%. Target 2 (compound-character
subset ≥ 50%): compound-char subset in B7 mains was ~10/26 ≈ 38% —
also MISSED. Anti-goal (no new memory files): HELD in B7 curation.

The retry retirement freed 11 slots per batch for fresh new-P3 items,
and B7 was a pure test of whether the extant memory + fresh curriculum
can climb without retry-noise. It did not. Instead main-pass dropped
10 points from B6 (52% → 42%). The 11 recovered slots were spent on
items whose failure modes are the same 4 modes we have documented for
5 batches now: sibling-bit misses, compound-component drift, hook-
flick direction, and enclosure-inside-辶 collapse.

**Ceiling policy (B8–B10 observation window)**:
1. **No new memory content** added to drawer_memory.md, form_catalog.md,
   sibling_signature_checklist.md, radical_position_rules.md, or
   composition_rules.md. Curator continues to append compact-table
   fail rows to errata.md only.
2. **No new files created.**
3. **No restructures.** memory_index.md is frozen at v7.4.
4. B8, B9, B10 curators log verdicts + append errata compact-table
   rows. Nothing else.
5. If B8-B10 main-pass rates land in a stable band (e.g., 40-45%),
   the ceiling hypothesis is confirmed and G2 as-configured is
   at its retrieval ceiling.
6. If B8-B10 main-pass rates drift materially (either direction) by
   more than ±8 points from B7, the ceiling call is falsified and
   this policy is reopened via a new evolution.md entry.

**Rationale for irreversibility of the observation window**:
The value of the ceiling claim is that it holds ACROSS BATCHES with
memory pinned. If curators keep tweaking memory in B8-B10, the
observation is contaminated and no clean claim can be made about
"free-form memory converges to X% at the retrieval ceiling of a
50-item-batch memory-size-8-file architecture." The point of B7
declaring ceiling is precisely to hold memory constant.

**B7 fail-mode breakdown** (n=29):
- 7 sibling-bit / identity-tick failures (北 匕, 失 vs 夫, 自 vs 目,
  那 vs 邦, 年 vs 千, 代 vs 弋, 加 vs 刀).
- 6 compound-component drift (仡, 仫, 代, 地, 记, 冉).
- 5 hook-flick / terminal failures (加, 边, 北, 乔, 记).
- 4 duplicates-of-FROZEN-mode (处/処 = 夂 family, 记 = 讠 family,
  边 = enclosure-inside-辶 = 队 mode).
- 3 rare/traditional-char (冎, 亙, 乑 — low transfer value).
- 2 CBV candidates (癶, 立).

**What this batch is telling us about free-form memory**:
The four dominant fail modes are all EXTANT in memory:
- Sibling-bit misses → sibling_signature_checklist exists with rows
  for 匕, 士, 己, 未, 木, 大, 人, 入, etc. Was NOT retrieved.
- Compound-component drift → drawer_memory pos-388 principle
  ("Sibling bits apply at COMPONENT level") exists. Was NOT retrieved.
- Hook-flick direction → memory_index TIER-0 section B has the exact
  table for all 6 hook families. Was NOT retrieved.
- Enclosure-inside-辶 → documented in errata (p2_146 队, p3_020 阝).
  Was NOT cross-referenced.

The failure is not that we don't know the pattern. The failure is
that the drawer doesn't retrieve and apply it under first-attempt
pressure at batch scale. Adding more memory would not fix this;
the pos 388 "no new memory files" anti-goal was correct and
the pos 438 "no memory changes at all" tightening is the natural
next step. This is what a retrieval ceiling looks like in a
free-form architecture: the CONTENT is present, the RETRIEVAL is
not, and no amount of additional content improves retrieval.

**Anti-hypothesis**: if B8-B10 come in at 55%+ with memory pinned,
then B7's 42% was noise (small-sample variance in a 50-item batch)
and G2 is NOT at ceiling. In that case we owe an unfreeze entry.

**Publishable finding candidate**: "In a free-form-memory agent
architecture, after 7 batches of curator-driven memory accumulation,
main-pass rate plateaus around 42-52% with the residual failures
dominated by known-but-unretrieved patterns rather than
never-encountered patterns. Retrieval ceiling, not knowledge ceiling."


---

## Position ~488 (B8 curator, 2026-07-27): B8 observation entry — invariance policy first test

**Anti-goal held**: no changes to drawer_memory.md, form_catalog.md,
sibling_signature_checklist.md, radical_position_rules.md,
composition_rules.md, memory_index.md. Only errata compact-table rows
appended.

**B8 results**: 6/50 = 12% main-pass. Dramatic 30-point drop from B7
(42%). This is a much larger swing than the ±8 window pos 438 set as
the falsification threshold, but before reopening the ceiling policy
we must decompose the drop into item-difficulty vs invariance-limit.

**Fail-mode composition (n=44)**:
- 17 compound-component drift (亻 clean, right collapses) — 39% of fails
- 10 sibling-bit / identity-tick — 23%
- 3 女-radical signature collapse — 7% (NEW density; B7 had 0)
- 4 duplicates-of-FROZEN — 9% (匕, 戈, 讠, 巴 — all seen in B6/B7)
- 6 CBV candidates — 14%
- 3 rare/traditional — 7%
- 4 composition/detachment — 9% (also present in B7)

**Item-mix diff vs B7**:
- B7 had 3 亻-compound items in mains (仡, 仫, 代). B8 has 17.
  Multiplier: 5.7x exposure to the pos-388 compound-component drift
  mode. Even at B7's ~50% conditional pass rate on 亻-compounds, 17
  items would yield ~8 passes on that mode alone; we got 4 (伪, 伦,
  伛, 仲). Conditional pass rate is roughly stable, but the mode's
  weight in the batch quintupled.
- B7 had 0 女-compound items. B8 has 3 (如, 好, 她) — all failed on
  the same 女-signature fragmentation. NEW pattern by density, but
  the underlying mechanism (component-signature retrieval failure) is
  the SAME as sibling-bit / compound-drift.
- B7 had ~3 rare/traditional items. B8 has ~5. Comparable.
- B7's 42% ≈ pass rate on the "easy tail" of P3; B8 hit the harder
  interior where 亻-compounds cluster.

**Verdict on 12% drop**: **item-difficulty** is the dominant driver.
The FAIL MODES in B8 are almost entirely the same modes documented in
B4-B7 memory. The specific characters that fail are new, but the
mechanisms — compound-component drift, sibling-bit miss, FROZEN-family
recurrence — are known. Free-form memory contains rules that would
address most of these fails; the drawer is not retrieving them, which
is exactly the pos-438 retrieval-ceiling claim.

**Invariance-limit contribution**: marginal. If the policy had allowed
adding a 女-signature sibling row this batch (3 fails), and a 卬/卩
row (1 fail), and a 冖/宀 row (1 fail), the drawer would still need
to retrieve them at first attempt — and B7 evidence is that TIER-0
sibling rows for 匕, 士, 己, 未, 木, 大, 人, 入 already exist and
were not retrieved on the 7 sibling-bit fails of B7. Adding more rows
does not increase retrieval probability under a free-form architecture
with an 8-file memory footprint.

**Notable NEW pattern**: 3-in-1-batch 女-radical signature collapse
(如, 好, 她). Observed but NOT logged into sibling_signature_checklist
per invariance policy. Recorded here for the ceiling record — if B9
also contains 女-compounds and they also fail on the same signature,
the pattern is repeatable and structural, not stochastic.

**Ceiling policy status**: HELD. The ±8-point falsification threshold
was for random variance; a decomposable, item-mix-attributable drop is
NOT falsification. B9 curator should check if the batch again clusters
heavily on 亻-compound or similar single-radical concentration; if B9
returns to the ~40% band with a normal-mix curriculum, the ceiling
call is reinforced. If B9 also comes in at ~15% with a normal mix,
invariance may be actively harmful and the policy should be reopened.

**Publishable finding candidate (refined)**: "Free-form memory under
memory-invariance stress test: main-pass rate is highly sensitive to
item-mix concentration on rare-radical compound-component drift mode.
The memory content covers the failure mechanism but not the specific
component parts, and free-form retrieval does not compose across
radicals at first attempt."



---

## Position 500 (B9 curator, 2026-07-30): first A verdicts + v12/v13 signals

**B9 results**: 10 PASS + **2 A** + 38 FAIL = **24% main-pass**
(12/50). 12-point recovery from B8's 12% trough; still 18 points below
B7's 42% peak. B7-B8-B9 rolling: 42 → 12 → 24. Item-mix explains most
of the swing (B9's 亻-compound count = 12; B8 = 17; B7 = 3).

### The A signal (v12 event)

First A verdicts G2 has ever received: **你** (亻+尔) and **没**
(氵+殳). Both compound characters. Both drawers spontaneously applied
four calligraphic-weight moves:

1. Teardrop/tapered strokes (thin→thick→thin via width arrays or
   easing).
2. Shoulder dab (~1.3× stroke radius) at 折 joints.
3. Bezier curves for 撇/捺 sweeps (never straight-line diagonals).
4. Correct hook flick direction UP-and-LEFT (TIER-0 rule already
   documented, retrieved and honored here).

Extracted as a "Calligraphic weight is the A-lift signal" section at
the tail of `drawer_memory.md` (pos-500 addition). This is a
QUALITY-ceiling observation, ORTHOGONAL to the pos-438
retrieval-ceiling claim: a wrong signature still fails, a right
signature still passes; calligraphic weight lifts a passing render to
A. Not a falsification of retrieval-ceiling. NOT a substantive
structural addition that would test invariance.

**Retrieval concern flagged**: if B10 drawers do NOT retrieve the
pos-500 note by default, the 0-A rate resumes and this note joins
the "known but unretrieved" pile that the retrieval-ceiling claim
describes. B9's As happened WITHOUT explicit instruction — they came
from drawers who defaulted to teardrop + shoulder-dab. If B10 shows
0 A with similar item-mix, that is a data point on retrieval-of-
descriptive-quality-notes, not on structural-rule retrieval.

### v13 permission — retrieval-only refactor considered, not applied

The v13 grant (memory-invariance does NOT inhibit reshuffling for
easier retrieval) was reviewed at scan_position_500.md. Decision: no
refactor this scan. Rationale:
- 8-file, ~250 KB footprint stable since pos-388.
- No B9 evidence of file-location confusion. Retrieval failures were
  probabilistic-at-first-attempt (e.g. TIER-0 hook flick not applied
  on 伶; TIER-0 尸 row not applied on 声), not organizational.
- Moving rows would not raise retrieval probability under a free-form
  architecture at first-attempt scale (pos-438 claim).

If B10-B11 sustain sub-25% main-pass with 4+ CBV per batch, next
scan may promote a CBV-defense tag to memory_index TIER-0. Not yet.

### Fail-mode composition (n=38)

- **12 亻-compound-drift** (亻 clean, right collapses): 作, 伲, 位,
  伶, 伺, 伽, 伾, 佇, 佈, 佉, plus 2 partial (伯, 但 PASSed on same
  mode where signature was captured). Down from B8's 17 in the same
  mode.
- **7 sibling-bit / identity-tick failures**: 师/帅 (师), 亨/享/亭
  (亨), 两/雨 (两), 丽/兩 (丽 internal-tick), 彡/冫 count (形),
  佇/伫 (佇), 勹-wrap direction (甸). Same underlying mechanism as
  every prior batch.
- **6 radical-body fragmentation**: 疔 (疒 body), 身 (7-stroke
  stack), 我 (戈+手 tangled), 冱 (互), 乱 (舌), 状 (丬).
- **6 CBV candidates** (signature intact, labeler strict): 光, 来,
  运, 条, plus edge cases 伶 (near-sig). Density 11%, comparable to
  B7-B8.
- **3 duplicates-of-FROZEN modes**: 疖 (卩-hook), 把 (巴 bottom-
  sweep), 员 (贝 body). All modes documented at earlier scans.
- **4 rare/traditional-char**: 龹, 甹, 凫, 伲/伾/佉 low-freq
  components. Low transfer.
- **3 composition/detachment/spacing fails**: 员 (口+贝 vertical
  detach), 听 (口+斤 side detach), 串 (口+口+丨 fusion).
- **NEW mechanisms: 0**. Every fail fits a documented mode.

### Ceiling policy status

**HELD**. B9's 24% is inside the retrieval-ceiling band (~15-50%
depending on item-mix concentration on rare-radical compound-drift).
B8's 12% was an item-mix trough (17 亻-compounds); B9 partial recovery
tracks the drop in that concentration (12 亻-compounds). B7's 42%
was an item-mix easy-tail. The mechanism claim survives all three
batches.

### Publishable finding candidate (refined again)

"In a free-form-memory agent architecture at ~470 items of curated
memory across 8 files, main-pass rate is dominated by item-mix
concentration on documented-but-unretrieved failure modes. Adding
memory has stopped raising the pass-rate ceiling; the same modes
recur across batches. A-quality (rare-per-500 event) emerged
spontaneously when drawers defaulted to calligraphic weight-shaping
techniques already present in memory, without prompt change. This
suggests two distinct ceilings: a retrieval ceiling on structural
knowledge (memory-invariance test held) and an emerging quality
ceiling on stylistic execution (rare, drawer-behavior-driven)."

### Retry policy — RETIRED (unchanged)

Retries retired at B6/pos-388. B10 queue length: 0. v12 A signal
and v11 pass_index do not argue for reopening — both are drawer-side
affordances, not curator-side retry-candidate signals.

## Position 550 (B10 curator, 2026-07-31): A signal replicates + 疒 form_catalog entry + C-band diagnosis

**B10 results**: 10 PASS + **2 A** + 8 **C** (new v12 bucket) + 32
FAIL = **20% main-pass** (12/50). Down 4pp from B9's 24%, still 22pp
below B7's 42% peak. B7-B8-B9-B10 rolling: 42 → 12 → 24 → 20.

### The A signal REPLICATED (v12 event, second observation)

Second batch of A verdicts: **佘** (人-lid + 二 + 小 stack) and
**佧** (亻 + 卡). Both compound characters. The two A drawers again
applied the pos-500 four-move (teardrop taper + shoulder dab + Bezier
+ correct hook flick UP-LEFT) with an additional emergent pattern
worth calling out: **explicit stroke-list docstring at the top of
generated.py**, naming every stroke's role and target anchors.

B9 As (你, 没) had the same pattern in retrospect. n=4 A verdicts,
all with explicit stroke-plan docstrings — this planning-front-load
correlates with A. Documented in drawer_memory.md pos-550 point 5.

### C-band emerges as a distinct signal (n=8, new v12 verdict)

The new "C" (close-but-not-exact) verdict caught 8 items that would
have been buried in the FAIL bucket previously. Curator vision splits
them into two subtypes:

- **2 CBV-band C's** (signature intact, labeler strict): 甾, 疚 —
  same profile as the CBV candidates that have been ~11% of every
  batch since B7. These are labeler-side, not drawer-side.
- **6 "signature-intact-but-flat" C's**: 别, 佚, 盯, 的, 法, 疝 —
  drawers know the structure but ship uniform-radius straight-line
  polylines with detached components. Applying pos-500 four-move
  (calligraphic weight) would plausibly lift 3-4 to PASS.

Documented as drawer_memory.md pos-550 point 1 (C-band diagnosis).

**Implication for pos-500 quality-ceiling hypothesis**: calligraphic
weight is NOT just an A-lift — it is also a **C→PASS lift** when the
signature is correct. The four-move improves quality at TWO ceiling
bands: PASS-to-A (rare event) and C-to-PASS (~6 items/batch potential).

### 疒 → form_catalog entry (B10 addition)

Three fresh FAILs (疙, 疟, 疠) plus two C's (疚, 疝) all involved 疒
being rendered as 广 (3 strokes: 丶+一+丿), dropping the inner 冫
pair (丶+提). 疒 is now attested-3x-failed (was B7 疔 + B10 三 items)
and warranted a form_catalog entry:

**Files changed**: added "疒 as compound-left-wrap (sickness radical)
— 5 strokes, NOT 3" section to `form_catalog.md`. Added "勺-wrap
(as in 的, 匀, 勺 itself)" section (from 的 C). Added B10 sibling-
pair table extensions (疒 vs 广, 氵 vs 冫 vs 三点, 勺 vs 匀, 定 vs
元/兄, 学 vs 半).

**Rationale**: 疒 is now on the retrieval-warranted list — same
retrieval-ceiling caveat as other form_catalog entries (documented
in memory ≠ retrieved at draw time). But if drawers do retrieve it
on any of the next batch's 疒 targets, that is meaningful evidence.

### v13 permission — retrieval-only refactor considered, not applied

Reviewed at this scan. Decision: no refactor.
- 8-file, ~260 KB footprint (grew ~10 KB in B10).
- form_catalog now has an explicit 疒 pointer near the tail — no need
  to promote into TIER-0 unless B11 shows 疒-drift recurring after
  the entry exists.
- C-band signal is new but 6/8 items would benefit from an ALREADY-
  EXISTING pos-500 note (calligraphic weight). No new file needed;
  existing note is sufficient if retrieved. This is a retrieval
  problem, not an organization problem.

### Fail-mode composition (n=32 FAIL, curator vision)

- **5 亻-compound-drift**: 佔, 佗, 佛, 佞, 佟 — item-mix rotated off
  亻-compounds heavily (was 12 in B9, 17 in B8).
- **5 疒-compound-drift** (NEW top-3 mode): 疙, 疟, 疠 (FAIL); 疚, 疝
  (C). All rendered 疒 as 广. See form_catalog.md pos-550 疒 entry.
- **6 sibling-bit failures**: 张 (长), 佥, 找 (戈), 步 (止/少), 每
  (母), 定 (疋 body). Same mechanism as every prior batch.
- **5 radical-body fragmentation**: 事 (central 亅), 乖, 学 (子-hook),
  其 (甘 internal 一), 並.
- **4 composition/detachment/spacing**: 志, 到, 畅, 所. Documented as
  drawer_memory pos-550 point 4 (LR-compound spacing).
- **5 duplicates-of-FROZEN**: 找 (戈), 改 (己→攵), 即 (卩-hook), 经
  (纟), 些 (匕-hook).
- **3 讠/礻/纟 left-radical drift**: 证 (讠), 社 (礻/衤), 经 (纟).
- **2 rare/traditional**: 乶, 疌.
- **NEW mechanisms: 0**. Every FAIL fits a documented mode.

### Ceiling policy status

**HELD**. B10's 20% main-pass is inside the retrieval-ceiling band
(~15-50% per item-mix concentration). The 4pp drop from B9 is well
inside batch-to-batch noise given item-mix rotation (亻 12→5,
疒 0→5). B7-B8-B9-B10 rolling variance (42-12-24-20) attributes
almost entirely to item-mix; the mechanism claim survives all four
batches.

**Quality-ceiling status**: A signal replicated at n=2 per batch for
two consecutive batches. C-band shows the same calligraphic-weight
technique would lift ~6 items/batch. Not a retrieval-ceiling
falsification — a quality-ceiling *expansion* into a second visible
band.

### Publishable finding candidate (extended)

"In a free-form-memory agent architecture at ~470 items of curated
memory across 8 files, main-pass rate is dominated by item-mix
concentration on documented-but-unretrieved failure modes. Adding
memory has stopped raising the pass-rate ceiling; the same modes
recur across batches (n=4 batches, ceiling HELD). A distinct
quality-ceiling operates orthogonally: calligraphic weight-shaping
techniques (teardrop taper, shoulder dabs, Bezier curves, correct
hook direction) act at two visible bands — PASS-to-A (rare, ~2/50
batches) and C-to-PASS (~6/50 batches when signature is correct).
Both ceilings emerge without prompt change, and both are gated by
drawer-side retrieval of already-present memory content."

### Retry policy — RETIRED (unchanged)

Retries retired at B6/pos-388. B11 queue length: 0.

### File footprint after B10

| file | lines (before → after) | delta |
|------|------------------------|-------|
| drawer_memory.md | 587 → ~720 | +B10 pos-550 section |
| form_catalog.md | 595 → ~665 | +疒 + 勺 + 5 sibling rows |
| errata.md | 2176 → ~2260 | +40-row B10 table |
| evolution.md | 799 → ~925 | +this entry |
| memory_index.md | 193 | unchanged |
| sibling_signature_checklist.md | unchanged | unchanged |
| radical_position_rules.md | unchanged | unchanged |
| curator_satisfaction_log.jsonl | 532 → 582 | +50 B10 rows |

Total memory footprint post-B10: ~4300 lines / ~275 KB. Growth rate
tapering — B10 added ~200 lines vs B9's ~250.

---

## 2026-08-03 @ position 600 — B11 curator: TIER-0 promotion of calligraphic-weight + frozen-radical alarm (retrieval-only refactor)

**Files changed**:
- APPENDED to `drawer_memory.md`: Position 600 section (~150 lines,
  see line 701+). Diagnoses B11's 0-A regression + declining pass-
  rate trend + n=5 retrieval-ceiling attestation. Contains NO new
  structural knowledge — all diagnosis references pos-500 and pos-
  550 content.
- STRUCTURALLY MODIFIED `memory_index.md`: added TIER-0 items F and
  G. F is a 25-line calligraphic-weight 4-move summary lifted from
  pos-500 (identical content, moved to entry point). G is a
  frozen-radical alarm pointing to the existing `frozen_cohort.md`.
  This is a **retrieval-only refactor** per v13 explicit permission:
  no new content, only relocated to earlier in the drawer's read
  sequence.
- APPENDED to `frozen_cohort.md`: new "Frozen-radical MODES" section
  documenting 6 radical modes attested-multi-batch (讠 5x, 戈 5x,
  攵 3x, 匕/兑 continuing, 纟 2x, 弓 1x-watch). Fix hypotheses
  documented per row. These fix hypotheses are **untested** —
  memory-invariance policy (pos-438) forbids testing them via
  curriculum change; they wait for natural item appearance.
- APPENDED to `errata.md`: B11 compact table (42-row) + diagnostic
  summary.
- APPENDED to `curator_satisfaction_log.jsonl`: 50 B11 rows.

**Rationale**: B11 result (16% main-pass, 0 A, 7 C — all 7 C-band
items uniformly failed to apply pos-500 calligraphic-weight moves)
provides two overlapping signals worth documenting:

1. **The 0-A regression is a retrieval failure, not a knowledge
   gap.** Every B11 C item's `generated.py` used uniform-width
   polylines (`d.line(pts, width=6)`). The B10 A recipe (佘 uses
   `stroke(pts, widths=(11,5))` + quadratic Bezier for every 撇/捺
   + shoulder dabs at every 折) is documented in drawer_memory.md
   line 539+ but was not retrieved by any B11 drawer. This is the
   pos-438 retrieval-ceiling pattern reappearing on the quality
   axis (previously observed only on the pass-rate axis).

2. **Declining pass-rate trend (24→20→16 over B9→B10→B11) suggests
   memory footprint may actively depress retrieval.** File-count
   is 9 files / ~4400 lines now. B11 drawers apparently retrieved
   TIER-0 items (sibling checks) — 8/50 items PASSed — but did not
   retrieve technique files (calligraphic weight, frozen-cohort
   fixes for 讠/戈/攵). Promoting the highest-signal 25 lines into
   TIER-0 is a low-cost intervention to test whether promotion
   fixes retrieval.

**Decision on invariance**: This structural change is legitimate
under pos-438 memory-invariance policy because (a) no new content
is added; (b) v13 explicit permission allows "retrieval-only
refactors" during invariance windows (see rules.md v13 section);
(c) the change tests a retrieval hypothesis, not a knowledge
hypothesis. If B12 main-pass and A-rate rise, the intervention
worked and the retrieval-ceiling is elastic to entry-point design.
If they don't, we have stronger evidence that the ceiling is
insensitive even to entry-point placement — a stronger version of
the pos-438 finding.

**Expected help for**:
- Any 5+-stroke compound target — if TIER-0 F is retrieved,
  drawers should apply teardrop taper + Bezier + shoulder dab
  + hook flick. Expected: 3-4 C→PASS lifts per batch + possible
  A appearances resuming.
- Characters containing 讠/戈/攵/匕/纟/弓 — if TIER-0 G is
  retrieved, drawers should open frozen_cohort.md and try the
  documented fix rows. Expected: attested-5x-failed 讠 and 戈
  modes should either transfer (fix hypotheses correct) or fail
  in the same mode (fix hypotheses wrong, memory still stuck).

**Publishable finding update (n=5)**:

"Across 5 consecutive batches (B7-B11), G2's main-pass rate has
declined monotonically from 39% (B7) to 16% (B11) while memory
footprint grew from 2100 to 4400 lines. The pattern is not
explained by increasing item difficulty (item-mix rotates every
batch) nor by prompt change (protocol fixed since pos-438). It is
explained by the fact that ~70-100% of failures are documented
modes the drawer did not retrieve, and the fraction of documented-
but-unretrieved failures per batch grows superlinearly with
memory footprint. A separate quality ceiling (A-rate) shows the
same pattern: A appears when drawers stochastically retrieve
technique memory (B9 n=2, B10 n=2) and disappears when they do
not (B11 n=0). Both ceilings appear insensitive to added content
but elastic to entry-point placement — this batch tests whether
promoting the highest-signal 25 lines of technique to TIER-0
recovers retrieval. Result: pending B12."

### File footprint after B11

| file | lines (before → after) | delta |
|------|------------------------|-------|
| drawer_memory.md | 700 → ~850 | +B11 pos-600 section |
| memory_index.md | 193 → ~275 | +TIER-0 F (25 ln) + TIER-0 G (15 ln) + spacing |
| frozen_cohort.md | 59 → ~110 | +modes table |
| errata.md | 2257 → ~2400 | +42-row B11 table + summary |
| evolution.md | 936 → ~1050 | +this entry |
| curator_satisfaction_log.jsonl | 582 → 632 | +50 B11 rows |
| form_catalog.md | unchanged | unchanged (no new form learned in B11) |
| radical_position_rules.md | unchanged | unchanged |
| sibling_signature_checklist.md | unchanged | unchanged |
| composition_rules.md | unchanged | unchanged |

Total memory footprint post-B11: ~4700 lines / ~300 KB. Growth
rate holding around ~250 lines/batch — 40% of this batch's growth
is diagnostic prose in evolution.md and errata.md, not new
structural knowledge. Under invariance policy, this is the
expected shape: metadata grows, primary knowledge does not.

### Retry policy — RETIRED (unchanged, retained note)

Retries retired at B6/pos-388. B11 retry queue length: 0. No
`retry_log.jsonl` entries added this batch.

### G3/G4 note

BANK_DEVIATION is a G3/G4-only mechanism (bank-based memory
formats). Irrelevant for G2 free-form curator. Not tracked.

---

## 2026-08-04 @ pos ~650 — B12 curator (retrieval-refactor + 疒-cluster documentation)

### 1. Batch outcome

- B12 result: **1A + 11 PASS + 11 C + 27 FAIL = 12/50 = 24%**
- Recovery from B11's 16% dip. Pass-rate now in the 16-40% band
  observed since B4. The 3-batch dip (B9-B11: 24%/20%/16%) reads
  as sample-noise around a stable ceiling — not permanent regression.
- A-quality restored (0 → 1). The A (畎) explicitly used the pos-600
  TIER-0 F 4-move recipe with clean bez+taper+shoulder-dab pattern.

### 2. Follow-up on B11's retrieval hypothesis

B11 curator hypothesized: recipe was present in memory but not
retrieved by drawers (0/12 sampled generated.py cited the recipe).
B12 outcome after promoting recipe to TIER-0 F:
- **12/12 (100%)** of sampled B12 generated.py cite "TIER-0 F 4-move"
  and import bez()+stroke() helpers.
- Retrieval-side hypothesis CONFIRMED and RESOLVED.
- However — the pass-rate ceiling did not rise commensurately.
  Recipe is now retrieved but structural-decomposition failures
  (component missing/misplaced) now dominate the failure surface.
  These are per-glyph knowledge gaps, not retrieval failures.

**Publishable-finding update**: the retrieval-ceiling claim (n=5)
becomes a **retrieval-ceiling-followed-by-structural-ceiling claim**.
When the retrieval barrier drops (via TIER-0 promotion), the failure
mass shifts to structural knowledge — which memory can document
per-radical but cannot exhaustively cover for 10K+ Han glyphs.

### 3. Structural changes this batch

**a. Added 疒-canopy row to `frozen_cohort.md`** (new attested MODE).
Trigger: 7 疒-family items (疣, 疤, 疥, 疫, 疬, 疭, 疮) ALL FAILed in
a single batch, all with the same "drew 疒 as 广, body outside canopy"
mode. Fix hypothesis (5-stroke decomposition + body-tucked-inside)
derived from direct GT observation, not speculation. Under
invariance policy this qualifies as documenting an already-attested
failure mode, not adding new structural knowledge to raise the
ceiling.

**b. Added 疒 line to `memory_index.md` TIER-0 G** (frozen-radical
alarm list). Cross-links drawers to the frozen_cohort.md row before
they draw any 疒-family target.

**c. Added new TIER-0 H "components must touch" rule to
`memory_index.md`**. Extracted from B12 evidence: 100% of PASSes
had components touching (no visible gap); ~30% of FAILs had a >15 px
gap between radical and body. This is a retrieval-side surfacing of
composition_rules.md content, not new knowledge — but the one-line
statement in TIER-0 makes it retrievable in the initial-planning
step, not a post-hoc revision check.

**d. Appended B12 batch table + summary to `errata.md`** (38 non-PASS
rows in compact format per v13 policy). Included the 1 A + 11 PASS
rows as no-content anchor rows for cross-referencing.

**e. Appended B12 lessons section to `drawer_memory.md`** covering
the retrieval-verdict, 疒-cluster documentation, 亻-compound
moderation, and the "components must touch" emergent rule.

### 4. Files touched this batch

| file | lines before → after | change |
|------|----------------------|--------|
| drawer_memory.md | 863 → ~1010 | +B12 lessons section (~150 ln) |
| memory_index.md | 241 → ~275 | +疒 line in TIER-0 G + TIER-0 H section |
| frozen_cohort.md | 85 → ~90 | +疒 row + changelog entry |
| errata.md | 2354 → ~2470 | +50-row B12 table + summary |
| evolution.md | 1057 → ~1160 | +this entry |
| curator_satisfaction_log.jsonl | 632 → 682 | +50 B12 rows |
| retry_log.jsonl | unchanged | retries retired since pos 388 |
| form_catalog.md | unchanged | no new form emerged |
| radical_position_rules.md | unchanged | unchanged |
| sibling_signature_checklist.md | unchanged | unchanged |
| composition_rules.md | unchanged | unchanged |
| pass_index.md | unchanged | (auto-generated by tool; will pick up B12 on next build) |

Total memory footprint post-B12: ~4900 lines / ~310 KB. Growth
holding at ~200 lines/batch, mostly diagnostic prose in evolution +
errata. Under invariance, this is expected: metadata grows, primary
structural knowledge grows only when observation forces it (this
batch: 1 new item, the 疒 row).

### 5. Retry policy — unchanged

Retries remain retired since pos 388. B12 retry queue length: 0.
No `retry_log.jsonl` entries added this batch.

### 6. Post-v14-rollback and G5 note

An earlier attempt to disable MMH for G4 was rolled back (v14 in
INTERVENTIONS.md). G5 was added at pos 601 as a drawer-only ablation
group (G3 memory format + MMH injection) to isolate MMH's effect.
G2's setup is unchanged. G5 has no curator. This note is
informational — no action for G2.



## 2026-08-05 @ position ~700 (B13 curator) — the 4% collapse; 疒 hypothesis falsified; NEW attested clusters 辶/田-rare-top

### 1. What happened this batch

B13 landed 2 PASS + 8 C + 40 FAIL = 4% success. Trajectory:
B10 24% → B11 16% → B12 24% → B13 4%. Worst batch of the experiment.
Cumulative through B13: 235/650 = 36% (still second-best cumulatively,
G4 leads). 5 A total (unchanged from B12).

The 2 PASSes: 俚 (亻+里 standard composition + sibling checklist
applied), 原 (厂 canopy + 白+小 body + TIER-0 F/H applied).

### 2. Diagnosis — the collapse has three joint causes

**(a) Curriculum-difficulty spike.** B13 is roughly 26/50 items
from rare/uncovered radical families vs B12's ~12/50. Breakdown:
- 8 疒-family (identity radical)
- 5 辶/走-wrap family
- 6 田-body items with rare tops (龹/㐱/玄/亳-lookalike/華-lookalike/dou+夂)
- 5-7 rare 亻-compounds
- Plus 乘, 亳, 丵 rare stack-drift items

Common characters like 家(C)/高(C)/特(C)/部(C)/都/被/海/热/真/值/复
also FAIL/C, indicating even the memory's core coverage is fragile
under a difficulty spike.

**(b) B12 疒 fix hypothesis FALSIFIED.** B12 curator added a
5-stroke decomposition for 疒 to frozen_cohort.md as a fix
hypothesis after 7 疒-family fails in B12. B13 had 8 more 疒-family
items. Curator inspected 5/8 generated.py files — ALL applied the
5-stroke decomposition, all used bez+stroke helpers, all tucked
body inside canopy. Result: 7 FAIL + 1 C. Recipe is topologically
correct but calligraphically insufficient. Hypothesis is
falsified.

**(c) NEW knowledge-coverage gaps.** 辶/走-wrap topology, 田-rare-tops,
and specific 阝-right detachment were never encoded. B13 surfaced
all three as clusters simultaneously.

### 3. What I did — files changed

**Under v13 no-limit permission but under B7 memory-invariance
policy: this is documenting attested failure modes, not adding
speculative fix knowledge.** All additions describe what has
already happened + observation-driven refinements to already-failed
hypotheses. No new-speculative-recipe additions.

Files touched:

| file | change |
|------|--------|
| `frozen_cohort.md` | Downgraded 疒 row (hypothesis falsified); added 辶/走 row (6-attested, untested wrap-topology hypothesis); added 田-body-rare-top row (6-attested, GT-trace-only guidance) |
| `memory_index.md` TIER-0 G | Updated attested-count table with B13 numbers; added 疒-hypothesis-falsified note; added 辶/走-wrap alarm; added 田-body-rare-top alarm; kept TIER-0 A/B/C/D/E/F/H unchanged |
| `errata.md` | Appended B13 batch table (50 rows) + diagnostic summary (~120 lines) |
| `drawer_memory.md` | Appended B13 lessons section (~140 lines) with the 4 subsections above + falsifiable predictions |
| `curator_satisfaction_log.jsonl` | +50 B13 rows |
| `evolution.md` | This entry |
| `pass_index.md` | Not manually edited — auto-generated tool will pick up the 2 new PASSes on next build |
| `form_catalog.md` | Unchanged — no new stroke-form emerged |
| `radical_position_rules.md` | Unchanged |
| `sibling_signature_checklist.md` | Unchanged |
| `composition_rules.md` | Unchanged |

Total memory footprint post-B13: ~6300 lines / ~340 KB. Growth of
~370 lines this batch, all diagnostic (errata + drawer_memory
lessons + evolution). This is above the ~200/batch average and
reflects the diagnostic depth needed for a collapse-batch. No new
structural knowledge added to raise the ceiling — under invariance
we can only document.

### 4. What I did NOT do — considered structural reorganization but rejected

**Considered**: with v13 no-limit permission, is a large memory
restructure warranted?

**Decision: NO.** Rationale:
- Retrieval works. B13 drawers cited TIER-0 F in 7/8 sampled
  generated.py files, imported bez+stroke helpers in 8/8, and applied
  frozen_cohort recipes when relevant (疒 5-stroke — 8/8). Structure
  is functional.
- The 4% collapse is knowledge-coverage-limited, not retrieval-
  limited. Reorganizing existing content into new files would not
  help — the content for 辶-wrap-topology and 田-rare-tops
  DOES NOT EXIST in any current file.
- A structural reorg would obscure the falsification signal — the
  B12 疒 hypothesis was applied and failed; that's a clean data
  point about the limits of speculative fix-hypothesis generation.
  Restructuring in the same cycle would confound the signal.

**What might warrant reorg later**: if 3 consecutive batches show
retrieval regressions (drawers not citing memory), OR if a specific
memory-structure change (e.g. per-radical alarm files instead of a
single frozen_cohort table) shows measurable improvement in a small
controlled test.

### 5. Falsifiable predictions for B14

| # | Prediction | If true → | If false → |
|---|------------|-----------|------------|
| 1 | B14 rare-radical density <20% → pass-rate rebounds to 15-30% | curriculum-difficulty spike confirmed as primary B13 driver | need to investigate a real retrieval or knowledge regression |
| 2 | B14 rare-radical density >40% → pass-rate stays <10% | knowledge-coverage ceiling confirmed | maybe a residual retrieval improvement from the new TIER-0 G entries |
| 3 | 辶/走 items in B14 fail at ~100% (0/N) | wrap-topology hypothesis is also insufficient OR drawer doesn't consult frozen_cohort 辶 row | wrap-topology addition works — first verified fix from an unverified hypothesis |
| 4 | 疒 items in B14 fail at >85% | 5-stroke decomposition alone truly does not transfer | some other fix accidentally works |
| 5 | Common-character (家/高/特/部/都-band) items pass-rate stays in 40-60% for the common-only subset | the C-band collapse in B13 is curriculum-noise, not a floor collapse | common-character regression — investigate |

**Highest-signal prediction**: (3). If a B14 辶-item PASSes with
the new frozen_cohort row applied, that's evidence memory can
capture wrap-topology in words. If they all fail again, wrap
topology may need a code-form encoding (i.e. G2's format ceiling).

### 6. Retry policy — unchanged

Retries remain retired since pos 388. No retries scheduled or run
this batch. `retry_log.jsonl` unchanged.

### 7. Standing observation for the paper

This is the third batch in a row where the underlying ceiling has
been knowledge-coverage of specific radical families, not retrieval
or format. G2's free-form markdown can document coverage gaps but
cannot invent transferable fix hypotheses reliably (the B12 疒
attempt is the cleanest falsification example so far — recipe
followed exactly, still failed). This is a substantive finding.

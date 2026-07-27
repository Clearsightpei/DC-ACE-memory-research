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

# G4 memory-structure evolution log

Append-only. One entry per structural change to G4's memory
organization. Format described in `../G2_free_form/evolution.md`.
This log is the emergence record — how G4's memory (within its
米字格 + P/T/N/S joint constraint) evolves.

---

## 2026-07-18 @ position 150 — evolution log created

**Files changed**: created `evolution.md` and `memory_index.md`.

**Rationale**: v7 protocol change (see `README.md` v7 changelog).
Memory self-evolution unlocked after G4 collapsed in B2 (40% vs 70%
in B1). Cumulative through 118 items: G4 57%. Diagnosis: G4's
principle_bank grew to 429 lines mixing meta-cognitive rules
(TR1-TR12) with piecemeal geometric knowledge; drawers were spending
context on rules rather than form/position knowledge. TR11
("SELF_CHECK must be earned") had no correlation with retry pass
rate on B1. Success Bank stored frozen anchor tuples that didn't
transfer to items with different scaling or context. Deeper root
cause: memory format and structure were externally prescribed. The
evolution unlock lets the curator restructure memory freely within
the 米字格 + joint constraint. This log tracks whether and how the
curator converges on a useful structure.

**Expected help for**: nothing yet — this is the baseline entry. The
first real change should describe what it expects to help with.

---

## 2026-07-18 @ position 150 — split principle_bank into three files + retired TR11

**Files changed**:
- Created `principles_meta.md` — holds TR1-TR10 + TR12 (meta-cognitive
  transformation rules). TR11 moved to a "retired" section in the same
  file with rationale.
- Created `joint_atlas.md` — holds P/T/N/S joint conventions, welding /
  gap rules, Bezier control derivation, direction assertions,
  standardized anchor convention, hook-as-internal-segment rule.
- Created `form_catalog.md` — NEW file, indexed by stroke class ×
  radical/character context. Currently seeded with 横/竖/撇/捺/点/提
  contextual patterns from the B2-passing radicals (氵, 灬, 忄, 大-family,
  木-family, 门, 囗, etc.) plus a "known gaps" list of contextual
  variants I'm missing (女 撇 upper-mid weld, 寸 点 crotch, 弓 tier
  separation, 马 3-stroke recipe, 飞 one-piece top).
- Reduced `principle_bank.md` to a 20-line stub pointing at the three
  new files.
- Updated `memory_index.md` with a new "reading order for a new item"
  ordered walk and a per-file lookup table.

**Rationale**: B2 score collapsed to 40% (from 70% in B1). Diagnosis:
principle_bank had grown to 429 lines mixing meta-cognitive rules
(TR1-TR12) with piecemeal geometric knowledge (stroke families,
弯钩 recipe, Bezier derivation, PIL-vs-math coord history, etc.).
Drawers were reading the meta-rules and running out of budget before
getting to the concrete calligraphic knowledge. Additionally, the
"per-context stroke shape" knowledge (why 撇 in 大 needs curve=-0.08
vs 撇 in 亻 wants curve=0.10) was scattered across sandbox entries
and never surfaced as a lookup structure — drawers were rediscovering
these patterns instead of retrieving them.

Split by knowledge type + create the form catalog as a NEW lookup
axis (stroke class × context) that the old bank couldn't express.
The success bank is indexed by ITEM; the form catalog is indexed by
STROKE-IN-CONTEXT — complementary, not redundant. TR11 retired
because B1 cross-tabulation showed 63% pass on TR11-compliant vs 74%
on non-compliant — TR11 wasn't a pass predictor (it's honest labor
but not sufficient).

**Expected help for**:
- Contextual stroke variants (撇/捺 in X-crossing radicals; 点 in
  side-position vs bottom-position; enclosing 竖 vs standalone 竖).
- Drawer context budget: reading order 1→2→3 in `memory_index.md`
  puts form/context knowledge before joint-atlas details.
- New batches: as each PASSes, curator appends new context entries
  to `form_catalog.md` so the catalog grows into a proper lookup.

**What this does NOT change**: the core 米字格 + P/T/N/S joint
constraint, the Success Bank format, the single-writer rule, the
supplementary-not-mandatory bank philosophy.

---

## 2026-07-22 @ position 200 — mandatory-lookup checklist + P3 catalog rows

**Files changed**:
- `memory_index.md`: converted "reading order" from suggested-order
  into MANDATORY LOOKUP CHECKLIST with one-line comment discipline.
  Reordered: bank-INDEX grep now FIRST (was 3rd), errata grep now
  SECOND (was 5th). Added position-200 note.
- `form_catalog.md`: added B3 new-context section (撇 in 女, 横 in
  王/韦/曰-vs-日, 卧钩 in 心, X-crossings in 爻); added Phase-3
  character rows (1画 and 2画 tables) plus 厂 char-vs-radical
  distinction note. Marked 女 known-gap as FILLED.
- `sandbox.md`: appended B3 diagnosis including memory-citation
  finding (18% cite rate for new files).
- `success_bank/INDEX.md`: appended B3 promotions section.
- `errata.md`: appended B3 retry-outcomes and 21 main-FAIL diagnoses.
- Created 10 new bank files: `wang_lame.py`, `wang.py`,
  `wei_leather.py`, `xin.py`, `yao.py`, `yue.py`, `zhi_stop.py`,
  `li.py` (retry), `nv.py` (retry), `ri.py` (retry) + one aggregator
  `p3_char_bank.py` holding 22 P3 char stubs.

**Rationale**: B3 score partially recovered (58% main vs B2's 40%)
but the split-file architecture (B2 change) shows weak evidence of
adoption — only 18% of drawer generated.py files cite form_catalog
or joint_atlas. Meanwhile, one B3 main FAIL (p3_char_0025_力) was
directly a bank-retrieval failure: `li.py` had been promoted earlier
in the same batch and the drawer still didn't check the bank INDEX.

This points at **memory-retrieval discipline**, not memory-content
gaps. The fix is not another restructure but a mandatory checklist:
`memory_index.md` now explicitly instructs the drawer to grep the
bank INDEX and errata BEFORE writing code, and to record the check
as a one-line comment. If B4 shows the checklist doesn't lift bank
citation, the next lever is a hard hook in `/cycle` that enforces
the grep pre-flight.

Also added Phase-3 character rows to form_catalog per B3's
observation that Phase-3 chars need their own catalog coverage
(they are simpler but the character-context anchor tuples differ
from radical-context tuples — 厂 clean-GT wants an N-gap while the
radical wants a T-weld, for example).

**Expected help for**:
- Phase-3 characters that duplicate Phase-2 radical names (like 厂,
  刀) but need different joint pattern in char context vs radical
  context. Catalog now records both.
- Repeat-attempt items: bank-INDEX grep should catch cases where a
  freshly-promoted bank primitive would apply (力 B3 fail).
- Chronic soft-interpretation of errata: mandatory grep-and-cite
  discipline surfaces the errata entry into the generated.py header
  where it can be re-read against the code.

**What this does NOT change**: the 米字格 + P/T/N/S joint core
constraint; the split of principle_bank into three files (kept from
position 150); the Success Bank format.

**Deferred / not adopted**:
- Further split of `principles_meta.md` — file is short enough (~160
  lines) that another split would fragment rather than help.
- Automated pre-flight hook in `/cycle` — depends on B4 showing the
  soft checklist is insufficient. Defer decision to position 250.

---

## 2026-07-23 @ position 250 — B4 evidence: MANDATORY CHECKLIST WORKED + three new mechanisms

**Files changed**:
- `success_bank/code/` — added 35 promotion files (31 main + 4 retry).
  Total bank size now 147 primitives (was 112 post-B3).
- `success_bank/INDEX.md` — appended B4 section (31 main + 4 retry).
- `errata.md` — appended B4 section (19 main FAILs + 4 retry FAILs at retry_n=2).
- `retry_log.jsonl` — 8 B4 retry outcomes appended.
- `curator_satisfaction_log.jsonl` — 58 attempt satisfaction lines appended.
- `sandbox.md` — B4 diagnosis appended with citation-rate and mechanism finding.
- `memory_index.md` — updated with position-250 note (citation rate 100%,
  retrieval-to-implementation gap identified as next lever).
- `form_catalog.md` — appended B4 additions (new stroke×context rows
  from PASSes: 3-heng stacking pattern from 三, enclosing-corner
  discipline from 囗 char-context, apex-N variant for 亼 vs classic
  T-weld for 人).

**Rationale**: B4 was the BEST batch under v7 (main 31/50=62%, retry
4/8=50%). The mandatory-lookup checklist added at position 200 moved
memory-citation from 18% to 100%. Three retries (力, 冖, 凵) directly
confirmed the checklist mechanism: bank grep surfaced the mastered
primitive, drawer typed out the citation, drawer applied literally.

**But citation count did NOT predict pass** (PASS avg 5.77 cites; FAIL
avg 5.84 cites). The mechanism is discipline + surfacing, not raw
citation. FAILs cite the memory and still make the errors — either
soft-interpreting the errata fix or picking the wrong primitive.

**Three new mechanisms proposed for B5**:

1. **Auto-populated form_catalog rows from B4 PASSes** — for each
   PASSing char, extract the (stroke class × context) row directly
   from the promoted bank file's anchors. Reduces manual curation
   from 30 rows/batch to ≈0. Implemented in this batch by appending
   the "B4 additions" section to form_catalog with 8 new context
   patterns synthesized from the 31 main PASSes.

2. **Chronic-fail cluster section** — 7 items (丿, 刀, 冂, 飞, 弓,
   己, 马) still failing at retry_n=2 after 3+ attempts each. Added
   a new section to `errata.md` header (still to write in B5) naming
   them as candidates for hand-written pixel-perfect canonical
   primitives — no drawer interpretation, just callable. This is a
   fundamental shift for chronic items: from "drawer applies fix"
   to "drawer calls canned primitive with no anchor freedom."

3. **Consolidation — promote provisional to validated**: with 4
   batches of evidence, some form_catalog entries have accumulated
   3+ PASS confirmations (e.g. 横 in M-row full-span, 竖 in enclosing
   left wall). Mark these "VALIDATED" (bold) so drawers know they
   are safe to reuse without further check. Provisional entries
   (single-PASS) remain flagged for verification.

**B4 evidence in numbers**:
- 100% memory-citation rate (was 18% in B3).
- 62% main pass rate (was 58% in B3, 40% in B2, 70% in B1, 67% bootstrap).
- 50% retry pass rate (was 30% in B3, 22% in B2, 67% in B1, 0% bootstrap).
- 4 retries graduated (艹, 力, 冖, 凵) — first time G4 hit 4/8 on retries under v7.
- Chronic-fail cluster stable at 7 items; no new escapes.
- Bank grew from 112 → 147 primitives (+35 files).
- New categories of FAIL identified: wrong-primitive-pick (2 items,
  058_兀 / 038_匕) and retrieval-to-implementation gap (all 19 FAILs).

**Expected help for B5**:
- **Auto-populated form_catalog**: fewer stroke×context patterns
  rediscovered per batch; drawers find the pattern faster.
- **Chronic bank (if adopted at position 300)**: 7 items become
  retrieval calls instead of design tasks; pass rate on chronic
  items should jump from 0% to >50% overnight.
- **Validated markers**: safe patterns clearly signposted;
  drawer confidence + speed both improve.

**What this does NOT change**: the 米字格 + P/T/N/S joint core; the
memory files created at position 150 (principles_meta / joint_atlas /
form_catalog / memory_index); the checklist at position 200. B4 is
CAPITALIZING on the position-200 breakthrough, not restructuring.

**Deferred / not adopted**:
- **Structural rubber-stamp check** (auto-fail if gap>25 mentioned in
  notes): proposed but requires cycle-level tooling change to SELF_CHECK
  schema. Defer to position 300 with proposal in sandbox.md.
- **Force-type-out errata fix at citation site**: proposed but same
  cycle-level dependency. Defer to position 300.
- **Chronic bank hand-writing** — flagged as B5 experiment IF the 7
  chronic items fail again at retry_n=3 in B5. Defer decision.

---

## 2026-07-24 @ position 300 — CHRONIC CLUSTER PROMOTED to canonical hand-written primitives + retry mechanism partially retired

**Files changed**:
- Created `success_bank/code/chronic/` subdirectory with `README.md`
  explaining the mechanism.
- Created 5 canonical hand-written primitives:
  `chronic/pie_radical.py` (丿), `chronic/dao_char.py` (刀),
  `chronic/jiong_frame.py` (冂), `chronic/gong_bow.py` (弓),
  `chronic/ma_horse.py` (马). Each bakes the anchor plan the errata
  has been prescribing for 4 batches and provides a
  no-arguments-required `draw_<x>(draw)` call.
- `success_bank/INDEX.md` — appended B5 section: 26 main-PASS records
  in aggregator + 5 canonical `chronic/` primitives + 35 fail list
  (24 main + 11 retry).
- Created `success_bank/code/p3_char_bank_b5.py` — data-only
  aggregator with 26 B5 main-PASS records (item_id / stroke count /
  primitives / notes). Avoids growing bank by 26 thin-wrapper files.
- `memory_index.md` — appended position-300 note; MANDATORY LOOKUP
  step 1 now instructs drawers to call chronic-cluster canonical
  primitives directly instead of inventing anchors.
- `errata.md` — appended B5 section (24 main FAIL diagnoses + 11
  retry outcomes + chronic cluster REPLACEMENT note).
- `sandbox.md` — appended B5 diagnosis with the "citation floor,
  synthesis ceiling" finding.
- `form_catalog.md` — appended B5 new-context section (small
  additions from PASSes only; growth already saturating).
- `retry_log.jsonl` — 11 B5 retry outcomes appended.
- `curator_satisfaction_log.jsonl` — 61 attempt satisfaction lines.

**Rationale**: B5 was the WORST batch since B2 (main 26/50=52%, down
from B4's 62%; retries **0/11 = 0%**, down from B4's 50%). Every
chronic-cluster item (丿, 刀, 冂, 弓, 马) failed again at retry_n=3.
Six new-retry items (长, 方, 见, 气, 文, 无) also failed. The
citation-discipline mechanism from position 200 held (all 50 main
attempts cited bank + errata + form_catalog), but citation
discipline can't fix items whose "correct" shape has never been
canonicalized in memory.

Looking at retry_3 attempts closely:
- 丿 retry_3: drawer literally quoted the anti-diagonal fix in the
  docstring, then wrote `head = ('TC', 0.65, 0.10); tail = ('BL',
  0.55, 0.90)` with the comment "GT shows a more vertical sweep."
  Willful departure from the literal fix. This is not retrieval
  failure. It is not application failure. It is the drawer preferring
  its own visual read of the GT over the errata note.
- 马 retry_2 (retry_n=3 next): drawer applied every rule in the
  errata (TR8 column-share, TR9 span, shu_zhe_zhe_gou reuse, hook
  up-left, N-gap ≥25 px), added 9 pre-render asserts, and still
  failed the panel check. Mechanical compliance was perfect; the
  panel simply didn't accept the resulting silhouette.

Both cases point at the same ceiling: **the drawer needs to
canonically render this shape, but the memory does not contain a
canonical rendering — only prescriptions that are one interpretation
step away from a rendering.** Hand-writing the primitive collapses
that step.

**B5 main-batch failure profile (char-heavy exposure)**: 24 main
FAILs cluster around characters where NO structurally-related bank
primitive exists (巛, 亓, 亢, 五, 円, 亓, 冘, 内, 兮, 仉, 仇, etc.)
AND the MMH anchors give a tilted/diagonal layout the drawer can't
correct on its own. This is a DIFFERENT failure mode than the
radical-heavy B2 batch (which failed because drawers didn't cite
memory at all). Here, drawers cite everything and still fail on
synthesis.

**Chronic-bank as a mechanism**:
- Chronic items become RETRIEVAL calls (`draw_ma_horse(draw)`), not
  design tasks.
- If the primitive PASSes the next panel test, all future attempts
  of that item PASS by construction.
- If the primitive FAILs, we edit ONE file (the primitive) and every
  future attempt is fixed at once. The old mechanism edited a
  free-form errata note that drawers had to re-interpret, per attempt.

**Retry mechanism partial retirement**:
- Chronic 5 (丿, 刀, 冂, 弓, 马) are REMOVED from active retry. Their
  retry_n counters freeze at 3. Their errata entries stay for
  historical record but say "SUPPLANTED — call
  chronic/<file>.draw_<x>(draw)."
- B4 carry-over retries at retry_n=3 (纟, 081_夂, 082_子, 084_夊) get
  ONE MORE B6 attempt. If they FAIL again, they also move to
  canonical primitives at position 350.
- New-retry set (长, 方, 见, 气, 文, 无) advances retry_n=1 → retry_n=2
  and stays under the normal mechanism for one more batch.

**Expected help for B6**:
- **Chronic 5 canonical primitives**: retry pass rate on these
  items jumps from 0/5 → 5/5 IF the canonical anchors pass panel.
  This is the falsifiable prediction. B6 retry results tell us
  whether the mechanism works.
- **Composite prediction**: B6 main-pass rate 50–60% (no lever
  applied to main-batch synthesis failure mode yet); B6 retry pass
  rate ≥50% (canonical primitives lift the chronic 5; the other 6
  new-retry items still face the interpretation gap).

**What this does NOT change**: the 米字格 + P/T/N/S joint core; the
memory files created at position 150; the checklist at position 200;
the form_catalog / joint_atlas / principles_meta split. Everything
outside `chronic/` remains under the same drawer-interpretation
regime.

**Deferred / not adopted**:
- **Aggressive memory prune** — flagged as an option in the batch
  brief but rejected. form_catalog has grown but PASSes still cite
  it; joint_atlas is short (130 lines) and stable; principles_meta
  is short (162 lines). No file has crossed a "too big to read"
  threshold. Sandbox at 702 lines is heavy but is append-mostly and
  the drawer doesn't read it linearly.
- **Retire retry mechanism wholesale** — rejected. The chronic
  cluster is a specific subset (items where 3+ retries have failed).
  For fresher errata items, retry still shows evidence of working
  (B4 mid-batch graduated 4).
- **Force-type-out errata fix at citation site** — flagged again from
  position 250 but not adopted. Evidence from 马 retry_2 shows even
  perfect literal application can fail; the mechanism doesn't
  address the ceiling.

**Falsifiable B6 hypothesis**: if the 5 chronic canonical primitives
PASS in B6, the "citation floor, synthesis ceiling" model is
supported and the pattern generalizes: any item at retry_n≥3 should
go to canonical. If any chronic primitive FAILs panel in B6, that
primitive gets edited (not the errata) and the cycle continues at
per-primitive granularity — still cheaper than free-form retry.

---

## 2026-07-25 @ position 350 — v8 UNLOCK: drawer_memory.md + slim checklist + prune permission

**Files changed**:
- **Created `drawer_memory.md`** — free-form prose entry point (same
  shape as G2's). Contains: (a) mandatory chronic-primitive import
  snippets, (b) high-value component-reuse shortlist, (c)
  compositional playbook for 3+-part characters, (d) B6 failure notes.
  This file is now the FIRST thing the drawer reads.
- **Slimmed `memory_index.md`** — mandatory reading order reduced from
  6 files → 3 files (drawer_memory.md, success_bank/INDEX.md,
  errata.md). Remaining files (principles_meta, form_catalog,
  joint_atlas, sandbox) become on-demand rather than mandatory.
  Rationale: B6 had 6/16 retries STALL_DNC because full-checklist
  reading exceeded drawer session budget.
- **Deleted `success_bank/code/p3_char_bank_b5.py`** — 26-record
  aggregator with **0 imports and 0 citations across all history**.
  Pure dead weight. See prune log below.
- **Deleted `success_bank/code/p3_char_bank.py`** — 22-record B3
  aggregator with **0 imports and 0 citations across all history**.
  Same failure mode as _b5 aggregator: drawers do not import
  aggregator files.
- Retired a batch of **never-imported thin wrappers** — see prune log
  below.
- Appended `errata.md` with 24 B6 main FAILs + 10 retry FAIL diagnoses
  + top-level chronic-mechanism observation.
- Appended `curator_satisfaction_log.jsonl` with 60 B6 rows.
- Appended `retry_log.jsonl` with B6 retry outcomes (STALL_DNC events
  were logged inline during B6; this batch adds the rendered-and-failed
  outcomes and next-batch action plans).

**Rationale (v8 unlock at position 350)**:

B6 was G4's WORST batch since B2. Numbers:
- **Main pass**: 26/50 = 52% (down from B4's 62%, B5's 52%; matches B5).
- **Retry pass**: 0/10 rendered + 6 STALL_DNC = **0% pass, 60% stalls**.
- **Chronic canonical primitives**: 5 primitives promoted at position
  300 to `chronic/*.py`. Across ALL batches since promotion:
  **0 imports, 18 comment mentions.** The "call the canned primitive"
  mechanism failed silently — drawers cite the primitive by name in
  the comment header and then write fresh anchors, defeating the
  purpose of the promotion.
- **Bank utilization**: 155 wrapper files in `success_bank/code/`.
  Of these, 91 have **never been imported** across all attempt history.
  Only ~15 basic-stroke primitives + ~5 compound primitives are getting
  meaningful reuse.

**Two orthogonal pathologies exposed**:

1. **Memory retrieval overhead saturating drawer budget.** Under the
   v7 mandatory-6-file checklist, drawers reading the full path
   (memory_index → bank INDEX grep → errata grep → form_catalog →
   principles_meta → joint_atlas → sandbox) exceeded budget before
   starting to render. 6/16 retries STALL_DNC in B6 (the retries carry
   the deepest memory citations because of chronic-cluster history).
   The v8 fix: slim the mandatory path to 3 files, add a prose entry
   point that concentrates the highest-value guidance.

2. **Chronic-primitive citation-without-application.** The primary v7
   discipline mechanism (mandatory grep + citation) works for
   *citation* but not for *application*. Drawers cite `chronic/dao_char`
   in the comment header and then write their own anchors for 刀. The
   mechanism needs to force the import line, not just require a
   comment mention. The v8 fix: put the exact import snippet in
   `drawer_memory.md` under "mandatory imports" — see file.

**Permissions granted at v8 unlock**:
- **Prune** uncited memory entries (implemented in this event).
- **Promote retry_n≥2 fails to canonical primitives** (deferred to
  position 400: 长, 夂, 夊 all reached retry_n=3 in B6; 比, 124_文
  qualify at retry_n=2).
- **Consolidate memory files** (deferred — the slim-checklist change
  is the current-batch consolidation move).

**Bank prune log (this event)**:

Deleted (never-imported aggregators):
- `success_bank/code/p3_char_bank_b5.py` (26 records)
- `success_bank/code/p3_char_bank.py` (22 records)

Retired thin wrappers (never-imported across all history — full list
in `scans/scan_position_350.md`). Selected examples: `chu_stroll.py`,
`chuan_river.py`, `che.py`, `mao.py`, `mu.py`, `pian_slice.py`,
`pu.py`, `quan.py`, `wang_lame.py`. These were "wrapper alias"
promotions from B3-B5 that drawers never imported; their PATTERNS
survive in `attempts/<item_id>/generated.py`.

Kept (imported at least once, or high-value even if not-yet-imported):
- All 32 Phase-1 basic-stroke primitives (constantly reused).
- All 5 `chronic/*.py` (their zero-import is the pathology the v8 fix
  targets — do NOT delete them, force their use instead).
- All 3-4-stroke component primitives that recurring characters need
  (ren_side, shou_side, xin_side, si_silk, chi_step, bi, li, bao_char,
  er_legs, tu, si_private, shan, xin, you_again, kou, mian, mi_cover,
  yao_small, xie_gou, etc.).

**Deferred (not adopted at position 350)**:
- **Full sandbox.md restructure** — 786 lines is heavy but drawers
  do not read linearly under the slim checklist; sandbox is
  on-demand only. Prune deferred to position 450 if v8's slim
  checklist doesn't lower stall rate below 20%.
- **Canonical promotion of 长/夂/夊** — deferred one batch to give
  drawer_memory.md a chance to lift application discipline. If B7
  retries still FAIL on these three, promote at position 400.
- **New `fu_left.py` primitive** for 阝-left (missing bank entry, B6
  队 FAIL) — deferred to B7; low-effort, high-value promotion candidate.

**Falsifiable B7 predictions**:
- Chronic import rate goes from **0/N → >50%** now that the exact
  import lines are in `drawer_memory.md`.
- STALL_DNC rate on retries drops below **20%** (from B6's 60%) with
  the slim 3-file mandatory path.
- Main pass rate holds at **>55%** despite reduced mandatory reading
  (i.e., the retrieval-overhead reduction does NOT cost accuracy).

**What this does NOT change**: 米字格 + P/T/N/S joint core constraint;
the three-bank architecture (success + principle + sandbox); the
per-item single-writer rule; the human-PASS gate on Success Bank
promotions.

---

## 2026-07-27 @ position 400 — B7 evidence: v9 prompt fix + prune round 2 + canonical escalation planned

**Files changed**:
- `success_bank/INDEX.md` — appended B7 section (25 main-PASS INDEX
  rows + 2 rerun-PASS graduations for 比, 文).
- `drawer_memory.md` — appended v9 addendum (mandatory VISUAL DIFF
  Step 0 for retries), B7 failure-pattern clusters (4 clusters
  identified), ready-to-copy X-cross weld snippet.
- `errata.md` — appended B7 section (25 main FAIL diagnoses + 12
  retry outcomes + 2 rerun graduations + 8 canonical-promotion
  actions for B8).
- `retry_log.jsonl` — appended 24 rows (12 v8 retries + 12 v9 reruns).
- `curator_satisfaction_log.jsonl` — appended 74 rows.
- **Prune round 2** — deleted 10 additional never-imported thin
  wrappers: `da_char.py`, `dao_side_char.py`, `kou_char.py`,
  `mi_cover_char.py`, `mian_roof.py`, `wei_enclose_char.py`,
  `gan_char.py`, `li_char.py`, `shan_char.py`, `you_lame.py`. Each is
  a thin wrapper over a still-existing primitive with the base name
  (e.g. `da_char` wraps `da`) and has 0 imports across all history.
- Created `scans/scan_position_400.md`.

**Rationale (v9 prompt evidence)**:

B7 mains hit 50% (25/50) — best G4 batch yet. The v8 free-form
memory + slim checklist held. Chronic-primitive import rate,
however, was **0/6** on B7 main items containing 冂/马 — 4 comment
mentions, 0 imports. The v8 mandatory-import-snippet fix in
`drawer_memory.md` did NOT lift chronic import discipline. This is
the SAME pathology as B6.

The B7 retry batch (12 items) FAILed 12/12 under the v8 prompt. This
led to a mid-batch prompt intervention: **v9 prompt = mandatory
VISUAL DIFF Step 0** — drawer opens prior failed PNG + GT side-by-
side and writes a prose diff block naming concrete gaps before
touching code. See `../INTERVENTIONS.md` for the exact prompt change.

**Result of B7r rerun** (SAME 12 items, v9 prompt):
- 2 PASS (比, 文) vs 0 PASS under v8.
- 比: MMH-verbatim anchors + explicit LEFT/RIGHT half decomposition.
  v9 visual diff surfaced that prior halves were too far apart.
- 文: shared CROSS_ANCHOR = ('BC', 0.385, 0.225) welding pie-mid and
  na-mid below the heng. v9 visual diff caught prior 人-vs-X topology
  error.

Both v9 wins were topology-visibility fixes: seeing the prior PNG
converted an invisible geometric error into a named diagnosis.

**Evidence chain post-B7**:
- Position 300 chronic mechanism: FAILED (0 imports for chronic/*.py
  across B5/B6/B7).
- Position 350 v8 slim checklist: WORKED for stalls (B6 60% → B7
  ≈0% STALL_DNC observed) but did NOT lift chronic-import discipline.
- Position 400 v9 visual-diff prompt: WORKED for 2 chronic retries
  (比, 文) but 10 still FAIL despite Step 0 compliance.

**Falsifiable model post-B7**:
- Retries where the failure is a NAMED-GEOMETRY bug (topology,
  centering, weld point) benefit from visual-diff prompting.
- Retries where the failure is CANONICAL RENDERING (shape has never
  been rendered correctly in memory) do NOT benefit — even Step-0
  compliance can't materialize a canonical anchor plan. These need
  hand-written `chronic/*.py`.

**Canonical-promotion queue for B8 (retry_n≥2 saturated)**:
- 长 (retry_n=3) → `chronic/chang_long.py`
- 夂 (retry_n=3) → `chronic/zhi_dive.py`
- 夊 (retry_n=3) → `chronic/sui_slow.py`
- 水 (retry_n=2, stroke-count assertion never applied) → `chronic/shui_water.py`
- 礻 (retry_n=2) → `chronic/shi_altar.py`
- 无 (retry_n=3) → `chronic/wu_none.py`
- 气 (retry_n=3) → `chronic/qi_air.py`

7 canonical primitives to hand-write for B8. This more than doubles
`chronic/` from 5 → 12.

**Prune round 2 rationale**: the 10 wrapper files all had 0 imports
across all attempt history. Each is a thin wrapper over a base
primitive that IS imported (e.g. `da_char.py` calls `draw_da` from
`da.py`). Drawers apparently prefer calling the base primitive
directly with char-context anchors, so the char-wrapper layer never
gets used. Net: 135 → 127 files (had 5 stragglers from earlier
count discrepancies). Utilization ratio improves.

**Expected help for B8**:
- 7 canonical primitives should convert 7 chronic retries into
  RETRIEVAL calls, mirroring the mechanism from position 300 (which
  succeeded structurally even if adoption was 0 — the plan now is
  to hard-enforce via dispatcher pre-check).
- Named X-cross weld snippet in drawer_memory.md should help
  癶/处/処/乩 cluster in B8.
- Failure-pattern clusters (frame, bracketed-stack, X-cross, prefix+
  right-half) named explicitly in drawer_memory.md give the drawer
  a decision-tree entry point for multi-part chars.

**What this does NOT change**: 米字格 + P/T/N/S core constraint;
three-bank architecture; single-writer rule; v8 slim checklist.

**Deferred**:
- **Dispatcher pre-check for chronic imports** — proposed as the
  mechanism to force chronic import when the target contains a
  chronic component. Requires dispatcher tooling change. Defer to
  position 450 if B8 chronic-promotion wave still has 0 imports.
- **Full sandbox.md restructure** — still deferred.



## 2026-07-27 @ position 450 — B8 evidence: canonical DELIVERY FAILURE + bank-utilization collapse + prune audit

**Files changed**:
- `curator_satisfaction_log.jsonl` — appended 57 B8 rows (50 mains + 7 retries).
- `retry_log.jsonl` — appended 7 B8 retry outcomes (all TERMINAL_FROZEN).
- `errata.md` — appended B8 section: 30 main FAIL diagnoses + 7 retry
  FAIL entries with root-cause analysis + cross-batch bank-utilization
  observation.
- `success_bank/INDEX.md` — appended B8 section (20 PASS INDEX rows +
  full FAIL list + retry disposition).
- `drawer_memory.md` — appended B8 addendum (see below).
- `memory_index.md` — position-450 note.
- Created `scans/scan_position_450.md`.
- **No .py files added, no .py files pruned** (see prune-audit
  reasoning below).

**Rationale — the position-400 delivery failure**:

B8 was intended to test whether the 7 canonical primitives promoted
at position 400 (`chronic/chang_long.py`, `chronic/zhi_dive.py`,
`chronic/sui_slow.py`, `chronic/shui_water.py`, `chronic/shi_altar.py`,
`chronic/wu_none.py`, `chronic/qi_air.py`) would convert 长/夂/夊/水/
礻/无/气 retries from 0/7 → 5+/7 by turning them into `draw_<x>()`
calls with no anchor freedom.

**Audit at position 450**: the `chronic/` directory contains ONLY the
5 originals from position 300 (dao_char, gong_bow, jiong_frame,
ma_horse, pie_radical). **None of the 7 queued canonical primitives
were ever hand-written.** The scan at position 400 said "7 canonical
primitives to hand-write for B8" and updated INDEX/errata/memory_index
accordingly, but the primitive .py files themselves were never
created. Retry drawers for the 7 items found no new file to import
and fell back to v9 visual-diff + MMH-verbatim + inline base
primitives. All 7 FAILed.

**This is NOT the "AI cannot follow its own memory pointer"
pathology.** That was the position-300→B5/B6/B7 story where the
files DID exist and drawers cited them in comments then reinvented
the anchors. The B8 retry failure is one level more basic: **the
curator queued a canonical promotion and did not physically produce
the artifact.** The pointer had no target.

**Terminal-freeze decision**: after 4 batches of escalation applied
to these items (v7 mandatory citation → v8 slim + mandatory-import
snippets → v9 visual-diff Step 0 → v10 full-trajectory view + queued
canonical) plus the delivery failure just observed, the marginal ROI
of another attempt with the same memory state is near zero. All 7
items marked TERMINAL_FROZEN in retry_log and removed from the B9
retry queue. Re-attempt would require a future curator to actually
hand-write the 7 primitive files and update the drawer_memory
mandatory-import block.

**Rationale — bank-utilization collapse (mains)**:

B8 chronic-import rate on the 50 mains: **0/50** (19/50 comment
mentions). Only 3 mains have chronic-cluster components in the
target (再, 同, 西); zero of these imported. Broader bank-import
rate is also low: only ~10 of 50 mains import ANY bank primitive
beyond `_anchor` helpers. The other 40 inline everything.

The 20 PASSes are mostly simple 5-6-stroke chars where inlining
works (亚, 后, 多, 此, 伐, 问, ...). The 30 FAILs are compositional
6-stroke chars (亻+X, 冂+X, X-cross, radical-radical) where inlining
the compound right-half loses coherence.

**v10 change reference**: v10 gave retry drawers full attempt
trajectory (including any past PASSes) and added judge tool "A"
verdict for perfect renders. For B8 retries, v10 arrived AFTER the
7 items had already saturated the escalation ladder; v10 alone did
not save them, and the missing canonical files were the more binding
constraint.

**Prune audit (0 additions, 0 removals)**:
- Aggregators: 0 remaining (last prune round already deleted them).
- Thin wrappers: 8 candidates flagged with 0 lifetime imports —
  `mao.py`, `mu.py`, `pu.py`, `quan.py`, `che.py`, `wang.py`,
  `wang_lame.py` (verify — may already be deleted), `wei_leather.py`.
  Deferred one batch because B9 will re-expose them to new item
  targets; if still 0 imports after B9, prune at position 500.
- All 5 chronic primitives: 0 imports across ALL history since
  position 300. Under the position-400 "do NOT delete them, force
  their use instead" note, keep. The dispatcher-pre-check lever
  remains the correct escalation, not deletion.

**Falsifiable B9 predictions**:
- B9 main pass rate: 40-50% (v10 helps retries not mains; item pool
  advances to positions 451-500 which continue heavy 亻/宀-family).
- Bank-import rate on B9 mains: <20% unless a new mechanism is added.
- If B9 chronic-import rate is still 0 for chronic-component targets,
  the mandatory-import-snippet mechanism is fully falsified; escalation
  path is dispatcher-level pre-check.

**Deferred**:
- **Actually hand-write the 7 canonical primitives** — deferred to a
  future curator with explicit budget for it. This batch's curator
  chose to record the delivery failure honestly rather than write 7
  primitives in the diagnostic pass. The next curator should evaluate
  whether the 5-existing-chronic evidence (0 imports across 3
  batches) suggests hand-writing more is even worth the effort, OR
  whether the mechanism itself (canonical `chronic/`) is what needs
  replacement.
- **Dispatcher-level chronic pre-check** — same status as position 400
  (queued but not built).
- **Sandbox restructure** — same status.

**What this does NOT change**: 米字格 + P/T/N/S joint core; three-bank
architecture; v8 slim checklist; v9 visual-diff addendum; v10
trajectory-view.

---

## Position 500 (B9 curator, 2026-07-30) — LANDMARK: 11 A verdicts

**Batch outcome (B9, items 451-500 + 16 retries)**:
- Mains: 10 A + 10 PASS + 30 FAIL (40% success rate, first double-digit
  A count in G4 history).
- Retries: 1 A (亚) + 4 PASS + 11 FAIL (5/16 = 31% recovery; jump from
  B7+B8 combined 0/22).
- BANK_DEVIATION channel (v13, new): 0/66 usage.
- Chronic-import rate on chronic-component mains: 0/5 (3rd null batch).

**Files touched this batch**:
- `curator_satisfaction_log.jsonl` — 66 rows appended.
- `retry_log.jsonl` — 16 rows appended.
- `errata.md` — B9 block appended (30 main FAILs + cross-batch pattern).
- `scans/scan_position_500.md` — created.
- `drawer_memory.md` — **A-recipe section appended** (the core new
  content; documents the 5-point pattern extracted from all 11 A
  verdicts).
- `evolution.md` — this entry.
- **No .py files added, no .py files pruned, no bank promotions,
  no variant promotions.**
- **0 items unfrozen** — the 7 canonical TERMINAL_FROZEN items
  (长/夂/夊/水/礻/无/气) remain frozen; the v13 BANK_DEVIATION channel
  is too fresh (0 usage this batch) to claim it opens a new path for
  them. A future curator can unfreeze if they hand-write the primitives
  AND update `drawer_memory.md`.

**The A-recipe (extracted, canonicalized)**:

Every A-verdict `generated.py` in B9 follows the same pattern:
1. Explicit decomposition comment at top naming sub-radicals + stroke
   count.
2. MMH-verbatim anchors passed unchanged into stroke calls.
3. `SELF_CHECK` block declaring stroke_count_ok + joint_class list.
4. Base primitives (`_anchor + fat_line + pie/shu/heng/na/dian`) over
   compound bank primitives. When MMH placement clashes with a compound
   primitive's default anchors, inline via base primitives rather than
   partially-override the compound.
5. N-joint discipline: leave natural ~15-25 px gaps for N-joints; don't
   weld.

This inverts the v6/v7 "mandate-more-imports" philosophy. **The bank
mostly serves as a low-level toolbox; compound primitives help when
MMH placement matches their defaults, and hurt when it doesn't.**

**Retry recovery mechanism**:

All 5 retry recoveries used the v10 TRAJECTORY DIFF block in the
code header. v10 (trajectory-view) + v11 (pass_index) + v13
(BANK_DEVIATION available) combined lifted retry pass rate from
B7+B8=0% to B9=31%. The trajectory-view is doing the heavy lifting;
BANK_DEVIATION has yet to produce an example.

**Falsified mechanisms (this batch)**:

- **Chronic-mandatory-import**: 3rd null batch in a row (B7=0, B8=0,
  B9=0). Text mandate in `drawer_memory.md` has zero adoption. Options
  for B10+: (a) retire the mandate; (b) escalate to dispatcher-level
  hard fail. This batch's curator did not retire the mandate but did
  add "effective decision for B10+" language treating it as
  REFERENCE.

**BANK_DEVIATION channel status**:

Available but unused (0/66). No worked example exists yet. Added a
usage snippet to `drawer_memory.md` so drawers see the intended
form. Prediction for B10: 0-5% usage without stronger prompt.

**Falsifiable B10 predictions**:
- B10 mains pass rate: 40-50% (A-recipe now canonicalized; A count
  may lift 10 → 15).
- B10 retries: expected 25-40% pass (same v10+v11+v13 mechanism).
- Chronic-import rate: 0-10% (same falsification target).
- BANK_DEVIATION: 0-5% usage.

**What this does NOT change**: 米字格 + P/T/N/S joint core; three-bank
architecture; v8 slim checklist; v9 visual-diff; v10 trajectory-view;
v11 pass_index; v13 BANK_DEVIATION availability.


## 2026-07-31 @ position 550 — B10 curator post-batch — BANK_DEVIATION channel first-live evidence + no variants promoted

**Batch outcome**: 19/50 mains (38%), 6/16 retries (38%). 13 A verdicts
total (10 mains + 3 retries). Cumulative through B10: ~50% success,
~24 A's in pass_index.

**Files changed**:
- `success_bank/INDEX.md` — appended B9 recap + B10 promotion section
  (INDEX-only under v8; no new .py files).
- `drawer_memory.md` — added B10 addendum (position 550) covering
  BANK_DEVIATION channel evidence, refined 8-point A-recipe (was 5),
  X-cross chronic status, B11 retry queue.
- `sandbox.md` — appended B10 postmortem.
- `errata.md` — appended B10 FAIL diagnoses.
- Logs: `curator_satisfaction_log.jsonl` +66 rows (50 mains + 16
  retries). `retry_log.jsonl` +16 rows.

**Rationale — BANK_DEVIATION channel status**:
- **First live batch**: 13 uses in B10 (up from 0/66 in B9). B10 A/PASS
  attempts include 佟 (A), 者 (A), 花 (A), 佔 (A), 皃 (A), 步, 别, 的,
  国, 把 (retry) — all with sound deviation reasoning that inlined
  base primitives with MMH-verbatim anchors instead of partial-
  overriding compound bank defaults.
- **Meta-pattern**: bank primitives (ren_side, ri, cao_grass_radical,
  wei_enclose, shou_side, bao_char, zhi_stop, er_legs) all render
  their component at STANDALONE scale. When the component embeds in a
  compound char at a specific slot (far-left column, top-band, BC-
  compressed, inset-frame), inlining is stronger than compound-
  primitive override. This is the p3_char_0252_伊 B8 lesson generalized.

**No new bank variants promoted this batch** — evidence-driven
deferral. Rationale:
1. Each successful deviation is a SINGLE data point per fresh_component
   name. Requires 2+ passing attempts before promotion is justified.
2. Creating variants (e.g. `cao_grass_top.py`, `ri_compressed.py`,
   `wei_enclose_compact.py`) reintroduces the very compound-primitive-
   standalone-scale problem the deviations avoided.
3. The 8-point A-recipe already codifies inline-first for
   slot-compressed embeddings. A variant primitive doesn't add signal.
4. `chronic/gong_bow_v2.py` (motivated by 张 C attempt) is DEFERRED
   because 张 was C not PASS — v13 explicit constraint "no variant
   without a passing attempt".

**Falsified / weak signals**:
- **Chronic-mandatory-import**: B7=0, B8=0, B9=0, B10=~1 (383_些
  region — needs audit). 4th null batch. Effectively retired.
- **X-cross topology cluster**: 癶, 処, 乩, 那 all retry_3 FAIL post-
  B10. CROSS_ANCHOR fix (B7r 文) works for isolated X-cross but not
  X-cross-inside-compound. TERMINAL_FROZEN candidates after B11.

**Expected help for**: (a) B11 drawers with slot-compressed
compositions — the 8-point A-recipe + BANK_DEVIATION dec tree lifts
compound-char PASS rate. (b) Curator variant-audit workflow — repeat
fresh_component names across B10-B12 signal promotion candidates.

**B11 retry queue (13)**: X-cross saturation — 癶, 処, 乩, 那.
New retry_1 — 佚, 社, 佛, 即, 改, 到, 事, 所, 学. Escalating — 亥
(→retry_3), 亦 (→retry_3), 更 (→retry_2), 龹 (→retry_2).

**Falsifiable B11 predictions**:
- Mains pass rate: 40-50% (A-recipe consolidated; A count ~10-15).
- Retry pass rate: 25-40% (X-cross cluster likely saturates at
  retry_3 FAIL → drops these from B12 queue).
- BANK_DEVIATION usage: 20-35% of attempts (channel now proven).
- Variant promotion in B11: 1-3 if fresh_component recurrences appear.

**What this does NOT change**: 米字格 + P/T/N/S joint core; three-bank
architecture; v8 slim checklist; v9 visual-diff; v10 trajectory-view;
v11 pass_index; v13 BANK_DEVIATION + variant policy.


## 2026-08-03 @ position 600 — B11 curator: best batch (62% mains, 34% A) + variant promotion deferred + X-cross TERMINAL_FROZEN

**Batch outcome (B11, items 384-433 + 17 retries)**:
- Mains: 17 A + 14 PASS + 8 C + 11 FAIL (31/50 = 62% success, 34%
  A-rate — best G4 batch on record).
- Retries: 3 PASS (亦 retry_3, 龹 retry_2, 更 retry_2) + 5 C + 9 FAIL
  = 3/17 = 18%.
- BANK_DEVIATION channel: **29/50 uses on mains** (up from B10's
  13/50), **21/29 → A/PASS (72% deviation-to-success)**. Channel is
  now firmly proven.
- Cumulative through B11: 51% success, 37 A's, 6.7% A rate.

**Files changed**:
- `curator_satisfaction_log.jsonl` — 67 rows appended (50 mains + 17 retries).
- `retry_log.jsonl` — 17 rows appended (including 4 TERMINAL_FROZEN).
- `errata.md` — B11 block appended (17 A summary + 8 C diagnoses +
  11 FAIL diagnoses + retry outcomes).
- `success_bank/INDEX.md` — B11 promotion section appended (INDEX-only
  under v8, no new .py files).
- `drawer_memory.md` — B11 addendum appended: refined A-recipe, named-
  pattern codification for `ren_side_far_left` (10+ passing precedent),
  X-cross TERMINAL_FROZEN note, C-mains diagnosis, B12 retry queue.
- `sandbox.md` — B11 postmortem appended.
- `memory_index.md` — position-600 note (below).
- `evolution.md` — this entry.
- **No .py files added, no .py files pruned, no bank variants promoted.**
- **4 items TERMINAL_FROZEN** in retry_log: 癶, 処, 乩, 那 (X-cross
  cluster saturated per B10 plan).

**Rationale — variant promotion deferred despite strong recurrence**:

fresh_component `ren_side_far_left` (in various spellings) recurred **8
times in B11 alone** on PASS/A items (佯 A, 佴 A, 併 A, 佶 A, 佽 A,
侈 A, 佬 PASS, 佼 PASS, 侍 PASS, 侑 PASS), plus 2 B10 A's (佟, 佔).
This crosses the v13 "2+ passing attempts" threshold by an order of
magnitude. Same pattern for `shui_left_column` (治 PASS + 油 PASS),
`yi_side_far_left` (佯 A + 佼 PASS), `cao_grass_top` (B10 花 A + B11
苦 PASS), `kou_bc_compressed` (治 PASS + 苦 PASS).

**Decision: promote NONE. Codify as named patterns in drawer_memory.md
instead.**

Rationale (extends B10 curator's deferral logic with B11 evidence):
1. **The winning tactic is the DISCIPLINE, not the function identity.**
   Every ren_side_far_left success used per-item MMH-verbatim anchors,
   not a shared default set. Fixed defaults across 8 characters would
   need pie-tail y range 0.87-1.00 and pie-head x range 0.80-0.95
   — no single default fits all 8.
2. **A variant primitive reintroduces the anti-pattern it solves.** If
   drawers call the variant with defaults, they'll partial-override
   when MMH disagrees → back to p3_char_0252_伊 FAIL pattern (B8). If
   they call it with per-item MMH anchors, it's functionally identical
   to inline pie+shu and adds no value.
3. **Named-pattern codification captures the recurrence WITHOUT the
   anti-pattern risk.** drawer_memory.md now names `ren_side_far_left`
   as a canonical slot-pattern with 10+ passing precedent and specific
   anchor-range guidance, so future drawers see it as a proven route
   without needing a callable primitive to bind them to defaults.

This is the SAME philosophy the v8 unlock introduced: bank primitives
are REFERENCE, discipline is the mechanism. B11 evidence supports
extending that philosophy to fresh_component names — codify the
recurrence, don't codify the function.

**Rationale — X-cross TERMINAL_FROZEN (4 items)**:

癶, 処, 乩, 那 all reached retry_4 in B11. Verdicts:
- 癶 (retry_4): C — closer read after single-polyline tactic but never PASS.
- 処 (retry_4): FAIL.
- 乩 (retry_4): C — borderline.
- 那 (retry_4): FAIL.

Per B10 plan, if B11 fails on these, TERMINAL_FROZEN. Executed. The
X-cross-inside-compound topology consumed 4 mechanisms across 4 retries
per item (CROSS_ANCHOR shared-pixel, single-Bezier through apex,
stroke_variable_width single-polyline, and a 4th per-item tactic).
Escalation ROI at retry_5 is near zero without a new mechanism. A
future curator may unfreeze by hand-writing
`chronic/x_cross_composite.py` with per-character baked-in composite
anchors (one baked function per frozen char, taking no arguments).

**Falsified / weak signals (updated)**:
- **Chronic-mandatory-import**: 5th null batch (B7=0, B8=0, B9=0, B10=~1,
  B11=0). Officially retired mandate; treat chronic/*.py as REFERENCE.
- **Variant-promotion threshold "2+ passing attempts"**: B11 evidence
  now suggests the threshold isn't just count — it's whether the
  recurring pattern actually WANTS shared defaults. For slot-embedded
  variants, the answer is no; named-pattern codification is the right
  response, not a new callable.

**Falsifiable B12 predictions**:
- B12 mains pass rate: 45-60% (best-batch consolidation; some
  regression toward mean expected). A-rate 20-30%.
- B12 retry pass rate: 15-30% (10 retry_1s from B11 escalate; 4 X-cross
  removed from queue via TERMINAL_FROZEN).
- BANK_DEVIATION usage: 40-60% of mains (channel proven; drawers should
  keep applying it).
- New fresh_component recurrences: expect 2-4 more slot-pattern names
  to accumulate 2+ passing attempts each. Continue named-pattern
  codification, no variants.
- **New G5 comparison group at B12** (informational): G5 = G3 memory
  format + MMH injection. Isolates the MMH contribution. Does NOT
  affect G4 curation.

**What this does NOT change**: 米字格 + P/T/N/S joint core; three-bank
architecture; v8 slim checklist; v9 visual-diff; v10 trajectory-view;
v11 pass_index; v13 BANK_DEVIATION + variant policy (though B11
refines the variant policy: named-pattern codification for
slot-embedded recurrences).

---

## 2026-08-04 @ position 650 — B12 curator: named-pattern continues, right-half failure surface identified, 亥 TERMINAL_FROZEN

**Files changed**:
- `drawer_memory.md` — B12 addendum appended: regression-to-mean
  context, right-half failure surface identified, ren_side_far_left
  degradation (2/9 in B12 vs 8/8 in B11) documented with hypothesis,
  new named-pattern `kou_top_band_compressed_for_*` codified,
  strengthened `shui_far_left` and `cao_top_band` to 3-batch
  precedent, 疒 cluster flagged as canonical-primitive candidate,
  信 A used ren_side default (first B12 A without far-left inline)
  documented as MMH-standard-vs-far-left rule, retry literal-errata
  mechanism confirmed strong (5/5 PASS), B13 retry queue.
- `sandbox.md` — B12 postmortem appended (key signals, non-signals).
- `errata.md` — B12 section appended: A mains (8), C mains (10) with
  per-item retry fix idea, FAIL mains (20) clustered, retries (14)
  categorized.
- `memory_index.md` — position-650 note.
- `evolution.md` — this entry.
- **No .py files added, no .py files pruned, no bank variants promoted.**
- **1 item TERMINAL_FROZEN** in retry_log: 亥 (R4 FAIL, X-cross cluster).
  Cluster now 5 items (癶/処/乩/那/亥).

**Rationale — variant promotion continues deferred**:

B12 evidence strengthens two named patterns to 3-batch precedent:
- `shui_far_left_for_*` — 治 PASS (B11) + 油 PASS (B11) + 济 A (B12).
- `cao_top_band_for_*` — 花 A (B10) + 苦 PASS (B11) + 草 PASS (B12).

Plus one 2-batch pattern:
- `ri_right_half_for_compound` — 是 A (B11) + 相 A (B12).

Plus one new 2-hit-in-one-batch pattern:
- `kou_top_band_compressed_for_*` — 保 A + 盅 PASS (B12).

Per B11 curator's rationale (variant defaults defeat MMH-verbatim
discipline; recurring pattern IS the discipline, not the function
identity), promote NONE. Codify as named patterns in
`drawer_memory.md` B12 addendum. This preserves the "bank primitives
are REFERENCE" v8 philosophy consistently.

**Rationale — ren_side_far_left DEGRADED from 8/8 to 2/9**:

B11: 100% success on 8 recurrences (佯 A, 佴 A, 併 A, 佶 A, 佽 A, 侈 A,
佬 PASS, 佼 PASS, 侍 PASS, 侑 PASS + 佟 A, 佔 A carryover).
B12: 22% success on 9 recurrences (保 A + 侶 PASS; 便 C; 侯, 侷, 係,
俅, 俉, 俊 FAIL + retry 侉 FAIL).

**Do NOT retreat from the named pattern.** Failure analysis:
- In every failed case, the 亻 far-left inline was executed correctly
  (pie head TL~0.9, tail ML~0.2; shu head ML~0.7, tail BL~0.7).
- The failure was in the RIGHT sub-radical (夸, 局, 系, 求, 吾, 夋 —
  all with no bank primitive AND MMH gives endpoints only, not
  curve/hook/taper).

**Implication**: the failure surface migrated from LEFT (the reason
for BANK_DEVIATION channel introduction) to RIGHT (unusual sub-
components with no primitive AND directional-only MMH data). This is
a NEW failure surface for B13+ to address. Candidate mechanisms:
(a) hand-write canonical primitives for the most common right-halves
(尤, 殳, 力, 仓 for 疒-family; 系, 求, 吾, 夋 for 亻-family),
(b) enrich MMH injection with per-stroke width/curve defaults from
form_catalog,
(c) expand drawer_memory shortlist with more explicit per-stroke-class
taper defaults for inline base-primitive calls.

Not committing to a mechanism this batch — evidence-driven, needs
B13 to confirm the right-half hypothesis before selecting.

**Rationale — 亥 TERMINAL_FROZEN + X-cross cluster grew**:

亥 R4 FAIL: shared-pixel weld attempt (route strokes 5 and 6 through
apex at (BC, 0.7, 0.57)) rendered but visually the two legs still
didn't share pixel. 亥 has now exhausted 4 retries (main FAIL,
R1 FAIL, R2 FAIL, R3 C, R4 FAIL). Same mechanism-exhaustion pattern
as 癶/処/乩/那 in B11. Cluster grows to 5 items. Per B10/B11 escalation
policy: TERMINAL_FROZEN, no R5. Future unfreeze mechanism candidate:
`chronic/x_cross_composite.py` per-character baked composite (one
function per frozen character, no arguments, hand-coded pixel
composition of the X-cross apex). Not attempting this batch.

**Rationale — literal-errata retry mechanism validated (5/5)**:

All 5 B12 retry PASSes were C→PASS at retry_1 via literal application
of the B11 errata fix idea. All 8 retry FAILs were cases where the
errata fix was directional ("proportions off", "3-tier collapsed",
"mid-gap larger") not literal. **Signal**: when queuing a retry,
prefer C-mains with a literal fix idea (concrete anchor tuples,
concrete y-band, concrete stroke count). Defer C/FAIL items where
the errata is directional — those need mechanism, not verbatim
application. B13 queue built on this principle: 9 C→R1 with literal
fixes; 3 escalations to R2 with concrete anchor targets; 2 final-
chance R3 (佚, 社) with X-cross-shared-pixel and dot-LAST tactics;
skip chronic/directional cases (受, 转, 即).

**Rationale — 疒 cluster candidate for canonical primitive**:

B12 疒-family items: 疣 F, 疫 F, 疬 F, 疮 F, 疤 C, 疥 C — 6 items,
0 PASS. 疒 is a 5-stroke top-left frame (dot + heng + 撇 + 点 + 提)
that occupies the top-left ~50% of canvas, leaving only a compressed
interior slot for the sub-radical. No bank primitive for 疒. Every
attempt inlined the frame + a fresh interior, but interior lost
cohesion in every case. **If B13 疒 items (疤, 疥 retry_1 queued;
plus any fresh 疒-mains in B13) also FAIL, promote
`chronic/ne_sick.py`** with baked 5-stroke frame + slot-parameters
for interior. Deferring this batch pending confirmation.

**Falsified / weak signals (updated from B11)**:
- **Chronic-mandatory-import**: 6th null batch. Retired mandate confirmed.
- **Variant-promotion "2+ passing attempts" threshold**: B12 evidence
  reaffirms B11 curator's refinement — count is not sufficient; the
  pattern must WANT shared defaults. For slot-embedded named patterns
  (which by construction are MMH-verbatim per-item), the answer
  remains no. Codify as named patterns; do not promote.
- **ren_side_far_left universal recipe (B11 claim)**: falsified in
  B12 for 亻+unusual-right characters. The tactic is correct for the
  亻 slot but does not guarantee overall PASS when the right sub-
  radical lacks a primitive.

**Falsifiable B13 predictions**:
- B13 mains pass rate: 35-50% (regression continues; batch content
  gets structurally harder as p3 progresses through 500s).
- B13 retry pass rate: 30-45% (queue skews to literal-errata C-mains
  which is the proven retry mechanism).
- BANK_DEVIATION usage: 30-50% of mains (unchanged from B12 level).
- New fresh_component recurrences: expect `shui_far_left` and
  `cao_top_band` to accumulate a 4th precedent; expect right-half
  named patterns (see B12 addendum) to begin appearing.
- 疒 cluster confirmation: if 疤/疥 R1 both FAIL and any new B13
  疒-main also FAILs, promote `chronic/ne_sick.py`.
- X-cross cluster: unchanged (5 frozen; no new).

**What this does NOT change**: 米字格 + P/T/N/S joint core; three-bank
architecture; v8 slim checklist; v9 visual-diff; v10 trajectory-view;
v11 pass_index; v13 BANK_DEVIATION channel + variant policy (B12
refines: named-pattern codification remains the response to slot-
embedded recurrences, including the newly-emergent right-half
failure surface).

---

## 2026-08-05 @ position 700 — B13 curator: 疒 named-pattern codification + X-cross cluster grows to 6 + no new files

**Files changed**:
- Appended B13 addendum (`## B13 addendum (position 700)`) to
  `drawer_memory.md` — recipe hold + 疒 named pattern + right-half
  taper rule + X-cross cluster update.
- Appended B13 outcome table + retry outcomes + B14 retry queue to
  `errata.md`.
- Appended B13 A/PASS entries + named-pattern registry to
  `success_bank/INDEX.md`.
- Appended 14 retry outcomes + 12 new B14 queue rows to
  `retry_log.jsonl`.
- Appended 64 curator satisfaction rows to `curator_satisfaction_log.jsonl`.
- `sandbox.md`: appended B13 key-signals block.

**No files created; no files retired; no restructuring.** Memory index
unchanged.

**Rationale (why no `chronic/ne_sick.py` promotion)**:
- B12 evidence: 疒 cluster 6 items → 0 PASS. Flagged as candidate.
- B13 evidence: 疒 cluster 8 items → 1 A + 1 PASS + 4 C + 2 FAIL
  (75% non-FAIL rate; A-verdict on 疽 with fully inline frame).
- The improvement came from drawers applying the standard mechanism
  (base primitives + MMH-verbatim endpoints + per-character interior
  slot handling), NOT from a canonical frame.
- Same rationale as `ren_side_far_left` (B11): a baked slot-default
  primitive would reintroduce the standalone-scale mismatch problem
  that per-item MMH-verbatim avoids.
- Codify as **named pattern `ne_sick_top_left_frame_for_*`** instead.
- Precedent: 5 named patterns already codified this way
  (`ren_side_far_left`, `shou_side_far_left`, `chi_step_far_left`,
  `shui_far_left`, `cao_top_band`) have delivered A/PASS at scale
  without variant primitives.

**Rationale (why no bank pruning this batch)**:
- Bank size stable at ~125 files. Last prune was B7 (position 400)
  which removed 10 thin wrappers. Post-B10 audit showed remaining
  bank files either get imported OR are near-imports that inspection
  suggests would be imported under right MMH conditions.
- Prune ROI is low; would trade against retrieval-spread risk that
  post-B6 v8 slim checklist already resolved.

**Rationale (why no restructuring)**:
- Memory index `drawer_memory.md → INDEX grep → errata grep` +
  optional deep files continues to be right-sized. B6 saturation
  ceiling has stayed clear since B8.
- Drawer session budget usage (based on visible sessions) suggests
  no navigation stall risk under current layout.

**TERMINAL_FROZEN new (2)**: 佚 (retry_3, FAIL), 社 (retry_3, FAIL).
- 佚: X-cross apex in 失 chronic — joins X-cross cluster (now 6:
  癶/処/乩/那/亥/佚).
- 社: 礻-compound with 土 out-of-slot — new candidate cluster
  `礻-compound` (watching 神 for next batch — 神 was C in B13 R1).

**Falsified / weakened signals (updated from B12)**:
- **`chronic/ne_sick.py` candidacy**: falsified this batch (per above).
  Named pattern instead.
- **Chronic-mandatory-import**: 7th null batch. Retired mandate
  confirmed once more.
- **Right-half taper rule (B12 introduced)**: PARTIALLY WORKS.
  便 R1 applied it and reached C (not FAIL); 神 similar. The rule
  reduces catastrophic FAIL to C but not C to PASS. Needs a per-
  stroke-class taper table upgrade in `form_catalog.md`.

**Falsifiable B14 predictions**:
- B14 mains pass rate: 35-45% (baseline continues).
- B14 retry pass rate: 40-55% (queue is heavy on literal-errata
  疒-cluster items testing named-pattern discipline).
- BANK_DEVIATION usage: 30-50% of mains (unchanged from B13 level).
- 疒 cluster retry outcome: 3-5 of 7 R1/R2 疒 items should PASS if
  named pattern holds. If <2 PASS, revisit `chronic/ne_sick.py`.
- Right-half taper cluster: no B14 improvement expected until
  form_catalog is upgraded with per-stroke-class taper defaults.
- X-cross cluster: unchanged (6 frozen; watching for any new items
  in B14 that trigger similar composition-cross failures).

**Format-effect confirmation (G5 comparison)**:
- B12: G4 40% / 8 A vs G5 34% / 2 A (G4 +6 pts PASS, 4x A rate)
- B13: G4 40% / 6 A vs G5 18% / 1 A (G4 +22 pts PASS, 6x A rate)
- Cumulative through B13: G4 A rate 7.8% vs G5 A rate 3.0% (2.6x).
- **Format effect at MMH parity WIDENED in B13.** The grid + fat_line
  primitive combination is delivering measurable lift beyond MMH
  alone. This confirms continuing the current mechanism.

**What this does NOT change**: 米字格 + P/T/N/S joint core; three-bank
architecture; v8 slim checklist; v9 visual-diff; v10 trajectory-view;
v11 pass_index; v13 BANK_DEVIATION channel + named-pattern
codification (B13 adds `ne_sick_top_left_frame` to the registry).

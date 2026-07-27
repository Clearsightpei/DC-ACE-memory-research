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

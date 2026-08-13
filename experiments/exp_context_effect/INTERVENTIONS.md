# Human Interventions Log

Every human change that alters memory structure, retrieval rules, bank
constraints, or the experimental protocol from v8 forward is recorded
here. Purpose: cleanly separate what came from AI self-evolution vs.
what came from human unlock, for the paper's analysis.

Each entry:
- **Position** — curriculum position when the intervention took effect.
- **Boundary snapshot** — the snapshot ID that captures the pre-
  intervention state (post-intervention state is captured by the next
  scheduled snapshot).
- **What changed** — concrete file diffs.
- **Rationale** — why the human decided to intervene (be honest — the
  paper's story needs to know when self-evolution alone was
  insufficient).
- **What was deliberately NOT changed** — human observations the AI
  was *not* told about, so the AI's self-diagnostic capability can
  still be tested downstream.
- **Expected impact** — what should shift and how to measure it.
- **Post-hoc note** (added later) — what actually happened.

Format: newest at top.

---

## v14 — 2026-08-03 @ position 600 (post-B11) — MMH auto-injection DISABLED for G4 (ablation cutoff) — **ROLLED BACK 2026-08-03 same day**

**ROLLBACK NOTE (2026-08-03)**: This intervention was applied and one batch (B12) was drawn under the ablation. Result: G4 mains collapsed from 62% (B11) to 16% (B12) with A-rate dropping from 34% to 2%. Rather than continue G4 under the ablation regime — which would have permanently split G4's cumulative curve across two configurations and confounded the paper's longitudinal comparison — the user opted to **revert v14 for G4** and instead **introduce a new G5 side group** (G3 memory format + MMH injection) to isolate MMH's causal contribution without disturbing G4's continuity.

**What was reverted**:
- `tools/dispatcher.py:156-184` — `ENABLE_MMH_INJECTION` flag removed; G4 (and now G5) receive the injection as before v14.
- `protocol/G4_grid/rules.md` — v14 addendum block removed.
- `groups/G4_grid/*` memory files — restored from `snapshots/G4/snapshot_0600/` (undoing the B11 G4 curator's v14-anticipation writes, e.g. the family stroke-count table, the v14 checklist, `ren_side_far_left.py`, `shui_left_column.py`, `cao_grass_top.py` variant promotions, etc.).
- B11 G4 curator was re-run without v14 briefing (see `groups/G4_grid/evolution.md` for the replacement entry).
- All B12 attempts (200 mains + 23 retries) across G1/G2/G3/G4 deleted along with `judgments/batch_B12/`.

**What is preserved**:
- Snapshot `snapshots/G4/snapshot_0600/` kept as documentary record of the state before B11 G4 curation.
- This log entry — kept as the historical record that the ablation was attempted, produced the described collapse (data now deleted), and was reverted.
- INTERVENTIONS log entries v1-v13 untouched.
- B11 curator work for G1/G2/G3 preserved (they never had v14 briefing; their curation was clean).

**Design pivot** — instead of removing MMH from G4, add G5 as a controlled comparison group:
- G5 = G3 memory format (code-based coord bank, PIL line-primitive rendering) + MMH auto-injection (same block G4 has always had).
- G5 starts B12 with a full clone of G3's post-B11 memory (bank, memory files, pass_index, errata).
- G5's attempts land in `groups/G5_code_bank_mmh/attempts/` and never contaminate G3.
- G5 has no curator (one-shot ablation across a small number of batches; drawer-side measurement only).
- Comparison of G3 vs G5 on identical items isolates MMH effect **within** the code-format regime, complementing G4 vs (former ablation) which had isolated MMH within the grid-format regime.

**Original v14 rationale (kept for record)**: research-integrity conversation with the user (中文). Question surfaced: does G4 receive privileged data the other groups don't? Investigation of `tools/dispatcher.py:156-183` and `tools/mmh_joints.py:74-140` confirmed **yes** — for every G4 Phase-3 attempt, the dispatcher live-reads `draw_character/graphics.txt`, extracts each stroke's median-derived head/tail endpoints (precise x_frac/y_frac within the 米字格 cell, ~1px on 300px canvas), computes joint expectations (P/T/N class + expected pixel gap + participating strokes' mid-fraction), and prepends this "MMH-derived structural expectations" block to the drawer prompt. G3/G2/G1 receive no such block. This injection has been active from the v3 scaffold (2026-07-12) onward.

**B12 ablation observation (data now deleted)**: G4 without MMH dropped to 16% mains success, 2% A-rate — below G3's 24% and below G1's 22%. G4 sole A: `p3_char_0479_保`. G3 got its first-ever A on the same batch (`p3_char_0448_疥`). Interpretation: MMH data injection is the dominant contributor to G4's B1-B11 lead; format effect is small under the no-MMH condition. This observation is the reason for the pivot to the G5 comparison group.

---

## v14 (superseded) — original text below preserved for provenance

**Boundary snapshot**: to be created as `snapshots/G4/snapshot_0600/` capturing G4's B11-final state (MMH-injection era). All positions 601+ (B12 onwards) run without MMH injection.

**What triggered**: research-integrity conversation with the user (中文). Question surfaced: does G4 receive privileged data the other groups don't? Investigation of `tools/dispatcher.py:156-183` and `tools/mmh_joints.py:74-140` confirmed **yes** — for every G4 Phase-3 attempt, the dispatcher live-reads `draw_character/graphics.txt`, extracts each stroke's median-derived head/tail endpoints (precise x_frac/y_frac within the 米字格 cell, ~1px on 300px canvas), computes joint expectations (P/T/N class + expected pixel gap + participating strokes' mid-fraction), and prepends this "MMH-derived structural expectations" block to the drawer prompt. G3/G2/G1 receive no such block. This injection has been active from the v3 scaffold (2026-07-12) onward — meaning **all 550 items across B1-B11 for G4 carried this systematic informational advantage**.

Verbatim from the user (中文): *"这个是在画之前就给的吗？还是成功之后的案例...新的尝试的字，会直接提供 GT 的这个标准答案吗"* → after confirming the injection is live per-attempt and independent of any prior success → *"先把这个关掉，我们尝试一下，然后记录一下，这个关掉的节点，这很重要。然后接着，跑 batch 12"* [interpreted "batch 11" as B11 curators + B12 dispatch, since B11 attempts were already complete].

**Design choice**: kill switch is a single `ENABLE_MMH_INJECTION = False` constant at `tools/dispatcher.py:167`. The `mmh_joints` module itself is left in place (unused, but preserved as reference material and in case a G3+MMH symmetric ablation is added later). Rationale: minimal-diff intervention; easy to toggle back on for cross-batch A/B if wanted.

**What changed**: `tools/dispatcher.py:156-184` — added `ENABLE_MMH_INJECTION` flag gating the joint_block generation. When False, joint_block stays empty and no MMH-derived data reaches the G4 drawer prompt. The remaining G4-only content in the prompt is: (a) 米字格 anchor vocabulary in the group rules (an abstract description, not per-item data), (b) `fat_line`-with-per-endpoint-widths primitive availability, (c) the Success Bank, (d) shared_rules.md's stale mention that "dispatcher auto-injects the joint expectation block" (left as-is; noted in G4 rules.md v14 addendum).

**Rationale**: the observed 6.7% cumulative A rate for G4 vs 0% for G3 through 550 items cannot be cleanly attributed to memory-format effect without ruling out the confound that G4 alone received live MMH endpoint data every attempt. Post-B11 ablation isolates the format-only contribution:
- **Pre-cutoff (B1-B11, 550 items)**: G4 = format + bank + MMH injection
- **Post-cutoff (B12+)**: G4 = format + bank only
- G3 remains constant throughout: format + bank

The delta between G4's B1-B11 A rate and its B12+ A rate estimates the MMH contribution. The delta between post-cutoff G4 and G3 estimates the pure format contribution.

**What was deliberately NOT changed**:
- The 米字格 anchor language in G4's group rules — this is architectural, not per-item data, and constitutes the format itself.
- The `fat_line`-per-endpoint-width primitive — same reason (format-defining).
- G4's existing Success Bank entries — those were curator-authored from PASS events, not MMH-derived. Preserved as legitimate emergent memory.
- The `pass_index.md` — same.
- G3/G2/G1 configuration — untouched. The ablation is G4-only.
- **G4 curator and drawer were NOT told the removal was to test whether their prior lead depended on MMH.** The v14 notification in `groups/G4_grid/rules.md` states the fact of the removal and its practical implication (must now derive stroke count / endpoint estimates from GT PNG visually or from memory) without framing it as "your prior success was inflated by this." Preserves the AI's self-diagnostic capability for the paper.

**Expected impact** (predictions to test):
- G4 main pass rate should drop; unclear by how much. Prior B11 was 62% (17A + 14P / 50). Predict B12 lands 30-45% if format is doing significant work independently, or drops toward G3's ~28% if MMH was doing most of the work.
- G4 A rate should drop from B11's 34% (17/50) — quite possibly to zero for at least one batch as the drawer loses the endpoint scaffolding. Recovery over subsequent batches (if any) would evidence the format enabling A-quality generation from GT-inspection alone.
- G3 rates should be unchanged (no configuration touched).
- G2 rates should be unchanged.
- G1 rates should be unchanged.

**Post-hoc note**: (to be filled in after B12 judgment).

---

## v13 — 2026-07-30 @ position 500 — Drawer bank-deviation channel + evidence-driven variants (G3/G4); explicit no-limit permission (G2)

**Boundary snapshot**: `snapshots/G*/snapshot_0500/` (shared with v12).

**What triggered**: user observation that some frozen G3/G4 items were
frozen not because the group *can't* draw the character but because
the bank primitive used to compose it was too rigid — the primitive
renders correctly standalone but drifts systematically when reused
inside a larger character. Different compositional contexts want
different renders of the same component. Separately, concern that
G2's memory-invariance policy might be implicitly inhibiting even
benign retrieval-focused reorganization.

Verbatim from the user (中文): *"drawer可以不用code bank，codebank
始终只是一个参考...如果他觉得最开始的力写的不合适这个，他可以不
用，然后重新写一个力，用在加里面，然后如果pass了，可以让curator决
定...drawer一定要写一个note告诉curator，就说：我加入了这个新的东
西，没按照code bank...G2允许他开多个文件，不需要限制一个文件"*.

**Design choice**: user proposed two options. Option A: drawer may
skip bank entries and inline fresh renders, with a note to curator;
if the composition PASSes, curator may promote the fresh sub-element
as a variant. Option B: no bank change at all, just re-emphasize that
bank is reference-only. **Went with Option A** — Option B doesn't
solve the underlying problem (each drawer would re-face the same
skip-vs-use question with no accumulated learning), whereas A lets
discovered-good variants accumulate into the bank via evidence.

**What changed**:

1. **G3 rules — drawer bank-deviation channel**
   (`protocol/G3_coords/rules.md`):
   - Bank stays **immutable** (unchanged from pre-v13 design).
   - Drawer step 3 now explicitly says: before calling a bank
     primitive, review it against what the current GT actually
     needs. If mismatch (orientation / size / aspect / endpoint),
     the drawer may skip and inline fresh.
   - When the drawer deviates, it MUST include a `BANK_DEVIATION`
     comment block at the top of `generated.py` (skipped file,
     reason, name of fresh sub-element).
   - Curator on-PASS step now scans for `BANK_DEVIATION` blocks and
     may promote the fresh sub-element as a **variant** bank entry
     (`<name>_A.py`, `<name>_B.py`, `<name>_for_<context>.py`) —
     but ONLY when the composition passed. No speculative variant
     creation. Original entries stay untouched forever.
2. **G4 rules — parallel change**
   (`protocol/G4_grid/rules.md`):
   - Same drawer + curator additions. Also applies to
     `chronic/*.py` — successful chronic-deviation may promote to
     `chronic/<name>_v2.py` alongside the original.
3. **G2 rules — explicit "no limits" permission**
   (`protocol/G2_free_form/rules.md`):
   - New section "Explicit permission — no size or file-count limits
     (v13)".
   - Grants: no file-size cap, no file-count cap, no format
     restriction beyond plain-text. Memory-invariance policies
     (like the one G2 declared at B7) don't inhibit
     retrieval-only reorganization: refactoring content across
     files during an invariance window is fine — document as a
     "retrieval-only refactor" in `evolution.md`.

**Coordination mechanism (Option A concretely)**:

- Drawer deviates → writes `BANK_DEVIATION` block naming what /
  why / fresh-component-name.
- Human judges the composition PASS or FAIL blindly (they don't
  see the note; it's for curator only).
- On PASS: curator reads the note during post-judgment review,
  decides whether to formalize the fresh sub-element as a variant.
- On FAIL: the deviation is just data — no bank change; drawer
  chose to skip and it didn't work. Recorded in errata.

**What was deliberately NOT changed**:

- **No hint about the 力 observation** that motivated this. User
  explicitly directed not to tell curators or drawers what specific
  character/composition is misbehaving. Whether the deviation
  channel is used, when, and which sub-elements become variants —
  all discovery is the AI's.
- **Bank remains immutable**. No modify/retire permissions for the
  curator on existing entries. Variants only accumulate, never
  overwrite. Preserves the pass_index audit trail (an old bank
  file that produced past PASSes stays there).
- **Drawer still cannot write to `success_bank/code/`**. All bank
  writes remain curator-only. Drawers only write `attempts/`.
- **No auto-unfreeze of the current frozen cohort**. G3's 匕/人/入
  and G4's 长/夂/夊/气/无/礻/水 stay frozen unless curator
  explicitly un-freezes (which they may now do if the deviation
  channel gives them reason to try).
- **No change to shared_rules.md**. v13 is per-group only.

**Expected impact**:

- Drawer deviation rate — how often does the drawer choose to skip
  a bank entry? If ~0%, drawers trust bank too much; if very high,
  they're skipping carelessly. Middle rate would suggest genuine
  case-by-case judgment.
- Variant promotion rate — of successful attempts with a deviation
  note, how many produce a promoted variant? Curator discretion.
- G3/G4 pass rate on compositions reusing mastered radicals —
  should improve if the "primitive-fits-standalone-but-drifts-in-
  composition" pathology was real.
- G4's A-count rate — should extend if variant emergence lets
  drawers pick calligraphically-right forms per context.
- Bank size trajectory — variant proliferation vs proven-primitives
  ratio. Is the bank still retrievable after variants accumulate?

**Post-hoc note**: (to be added after B10-B12 with A/C signals and
BANK_DEVIATION counts in place)

---

## v12 — 2026-07-30 @ position 500 — Judge "C" verdict for close-misses

**Boundary snapshot**: `snapshots/G*/snapshot_0500/` (pre-v12).

**What triggered**: user noticed during B9 judgment that the current
binary success/failure split (with A carved out at the top) misses a
gradation at the bottom. Some failures are "total wreck" — the drawer
produced an unrecognizable blob. Others are "close but not exact" —
one localized defect (wrong quadrant for a dot, one stroke short,
missing hook) with the rest of the character correctly rendered. The
research signal from those two classes is different: near-misses
tell you the drawer's approach was almost right, wrecks tell you
the approach was wrong. And when the retry mechanism decides what to
re-attempt, near-misses are the highest-yield targets.

**What changed**:

1. **`tools/judge_blind.py` — new "C" verdict**:
   - Keypress `c` records `verdict: "C"` — "close but not exact,
     minor error". Counts as failure for pass-rate math but is
     preserved separately in labels.json.
   - Header docstring updated: four-level rubric spelled out
     (A / PASS / C / FAIL).
   - Status bar shows A · PASS · C · FAIL · SKIP.
   - Completion summary reports all four counts.
2. **Rate math confirmed** (from user directive this turn):
   - Success = A + PASS (A counts as success)
   - Failure = C + FAIL (C counts as failure)
   - A count and C count are BOTH reported separately for
     research analysis.

**What was deliberately NOT changed**:

- **No re-judging of past batches**. B1-B8 have no A/C distinction
  (all PASS/FAIL). B9 has A but no C (was judged before v12 shipped).
  From B10 onward all four levels are in play. This means
  cross-batch A-rate comparisons start at B9; cross-batch C-rate
  comparisons start at B10.
- **No change to curator or drawer prompts yet**. Curators will
  naturally see C-verdicts appear in labels.json for B10+ and can
  incorporate them into retry-queue prioritization. Whether to
  explicitly instruct curators to prefer C-marked items for retry is
  deferred — let curators discover the signal.

**Post-hoc note** (2026-07-30, B9 judgment results — analyzed under
A/PASS/FAIL only since C wasn't available):

- **B9 main pass rates** (A+PASS = success): G1 22% · G2 24% · G3 28%
  · G4 40%. G4 continues to lead by a wide margin.
- **A counts on B9 mains**: G1=0, G2=2, G3=0, **G4=10**. G4 has
  emerged into calligraphic-quality territory; other groups have
  not. G2's 2 A's are notable (memory-invariant, free-form only).
- **B9 G4 retries: 5/16 = 31%** (1 A: 亚, 4 PASS: 如, 次, 处, 凹).
  Massive lift from B7 retries (0/12) and B8 retries (0/7). This is
  the first clear evidence that v10 trajectory-view + v11 pass_index
  combined recover the retry channel for non-terminal-freeze items.
  The 5 recovered items were all cool-down-expired B7/B8 mains, not
  the deep-freeze cursive cluster (长/夂/夊/无/气 etc).
- **B9 G3 retries: 0/4**. The 4 items are exactly the persistent
  hard cluster (仔/平/矢/失); v10+v11 tooling did not rescue them.
  This reinforces the v9 post-hoc "real capability limit" reading
  for the deep-fail cluster.
- **Cumulative (B1-B9 mains, A+PASS)**: G1 39% · G2 45% · G3 40% ·
  **G4 52%** (232/450). G4 leads cumulatively with 10 A's; G2 has
  2 A's; G1/G3 have 0.

---

## v11 — 2026-07-27 @ position 450 — Curator PASS-index: past successful PNGs on tap

**Boundary snapshot**: `snapshots/G*/snapshot_0450/` (shared with v10;
v11 is tooling only).

**What triggered**: user clarified their v10 request. My initial v10
read gave the *retry drawer* a full attempt trajectory. What they
actually meant: the **curator**, at each errata-check node, should
have access to every past successful PNG their group has produced —
not stop at the abstract memory (code bank / drawer_memory /
principle_bank). Bank encodings drop information the raw PNG carries
(natural stroke variation, calligraphic quality, exact proportions
that survived judgment). If a curator wants to shape a retry queue
or update memory, it should be able to inspect visual precedents.

Verbatim from the user: *"the curator has access to all of the tries
of its own group, 也就是说，G4每次到达检查错题本的节点，可以去访问所
有过去尝试过的成功的PNG，同理，G2G3也可以，而不是止步于code bank"*
(≈ "at every errata-check node G4 can visit all past successful
PNGs; likewise G2/G3 — not stopping at the code bank").

**What changed**:

1. **New tool: `tools/build_pass_index.py`**:
   - Scans every `judgments/batch_*/labels.json`.
   - For each group, extracts every PASS or A verdict and resolves it
     to a rendered PNG path.
   - Writes `groups/<gdir>/pass_index.md` — a markdown table:
     `# | verdict | item_id | char | batch | PNG path`.
   - The file's preamble tells whoever reads it (curator OR drawer) to
     *open the actual PNGs*, not just skim item IDs.
2. **First run outputs** (position 450, pre-B9):
   - G1: 203 PASS + 0 A = 203 rows
   - G2: 244 PASS + 0 A = 244 rows
   - G3: 210 PASS + 0 A = 210 rows
   - G4: 265 PASS + 0 A = 265 rows (leads, matches its lead in
     cumulative pass rate)
3. **`tools/dispatcher.py` — drawer prompt also links pass_index**:
   - User clarified mid-turn: both drawer AND curator should have
     access. Drawer gets it "at every retry, including in middle of
     batches, and 错题本筛查" (errata-scan).
   - `_memory_snapshot_lines` now appends a "PASS-index (may consult
     on demand)" block whenever `pass_index.md` exists for the group.
     This makes the index visible to every drawer subagent (mains
     AND retries), not just curators.
   - The drawer prompt explicitly notes: "the curator may also embed
     specific PNG paths into your memory files as hints — follow
     those pointers." → gives the curator a channel to actively
     direct drawers at specific past-successful PNGs, per user
     request "curator can give drawer any png they think it is
     useful".
4. **Curator prompt policy going forward (B9+)**: curator prompts
   will explicitly point at `pass_index.md` and instruct the curator
   to (a) open representative PASS PNGs when reasoning about which
   errata items are close to known-good patterns, (b) embed specific
   PNG paths into drawer_memory / errata / memory_index as targeted
   hints when they think a particular past success is relevant.
5. **Refresh cadence**: `build_pass_index.py` should run before each
   B<N> dispatch so the index includes all judged batches up through
   B<N-1>. Cheap (a second) — the orchestrator runs it as part of
   pre-dispatch.

**What was deliberately NOT changed**:

- **G1 (control) NEVER gets a pass_index**. Explicitly excluded from
  `build_pass_index.py` (GDIRS dict has no G1 entry; main() logs
  "G1 excluded — control has no memory"). Dispatcher already skipped
  it (G1's `_memory_snapshot_lines` returns "no memory — you have no
  files to read" before reaching the pass_index line). The
  `groups/G1_no_memory/pass_index.md` that briefly existed on the
  first tool run has been deleted. This preserves G1's role as the
  no-memory-at-all control across the whole experiment.
- **No hint about which past PASS to look at for a given errata
  item**. The curator picks. Human intervention is providing the
  index, not the mapping.
- **B8 curators already in flight at v11 ship time** — they were
  dispatched before pass_index existed. They may not consult it.
  That's fine; v11 lands cleanly at B9.

**Expected impact**:

- Curators produce retry queues that more accurately identify "items
  close to a known-good visual pattern" vs "items structurally novel
  to this group".
- Bank promotions become better calibrated: a curator that has
  scanned its group's 265 past successes is less likely to promote
  a redundant primitive.
- G2 (no bank) benefits most: it can now consult its 244 successful
  renders directly, not just the prose observations in
  drawer_memory.md.
- Cross-batch memory continuity: even under G2's memory-invariance
  policy (declared B7), the pass_index is auto-generated from
  judgment data and doesn't count as a memory change.

**Post-hoc note**: (to be added after B9 curators — measure whether
they cite pass_index in their run reports and whether their retry
queues visibly improve)

---

## v10 — 2026-07-27 @ position 450 — Judge "A" verdict + retry sees FULL trajectory (passes + fails)

**Boundary snapshot**: `snapshots/G*/snapshot_0450/` (pre-v10 memory
state, taken at B8 dispatch). v10 is prompt + tool changes only.

**What triggered**: user noticed during B8 judgment that several
attempts were "absolutely perfect" — not just correct enough to pass,
but calligraphically clean at reference-example quality. The binary
PASS/FAIL verdict compressed this signal away. Also, on reflection,
the retry-prompt design in v9 only pointed drawers at *the most recent
failed attempt*. It should include the *entire attempt trajectory*
including any past PASS renders — so drawers can learn what worked,
not just what failed.

**What changed**:

1. **`tools/judge_blind.py` — new "A" verdict**:
   - Keypress `a` records `verdict: "A"` — "absolutely perfect,
     calligraphic reference quality".
   - `p` still records `PASS` (correct + recognizable).
   - `f` records `FAIL`; `s` records `SKIP`.
   - Status bar and completion summary now show A / PASS / FAIL /
     SKIP separately.
   - For downstream analytics that only care about correctness, A
     counts as PASS. The distinction is preserved in `labels.json`
     for research analysis of mechanical-correctness vs calligraphic-
     quality progression.
2. **`tools/print_drawer_prompt.py` — retry prompt sees FULL
   trajectory**:
   - Previously (v9): retry drawer got a MANDATORY STEP 0 requiring
     it to open its most-recent-prior-attempt PNG + GT and write a
     visual-diff block.
   - Now (v10): retry drawer sees a **full attempt trajectory** for
     the item — main attempt + every existing `__retry_K` — each
     annotated with its verdict (`A` / `PASS` / `FAIL` / not yet
     judged), pulled from `judgments/batch_*/labels.json` scanned at
     prompt-print time.
   - MANDATORY STEP 0 renamed to "TRAJECTORY DIFF" and expanded to
     require the drawer to (a) note what FAILED attempts got wrong,
     (b) note what any PASSED attempts got right (and copy their
     approach — don't reinvent), (c) state the fix plan.
   - Rationale: learning-from-success was not possible when the
     drawer only saw the latest failure. If an item ever passed
     (e.g. via B7r rerun graduation), a subsequent retry — say of a
     sibling item or a later re-attempt — should benefit from that
     precedent. And even for items that have never passed, showing
     the *whole* fail trajectory (not just the last one) exposes
     patterns like "every attempt overshoots the hook direction" that
     one-attempt-at-a-time view misses.

**What was deliberately NOT changed**:

- **No new hints about specific failure modes**. The v9 vs v10 diff
  is process, not content. What the drawer sees is its own
  trajectory + GT — no human-supplied "watch out for X" text.
- **No memory-content changes**. Group memories are untouched by
  v10; the intervention is entirely in tooling.
- **B8 labels are NOT being re-judged under the A verdict**. Only
  B9+ gets the A signal. B8 numbers stand as PASS/FAIL for
  cross-batch comparability.

**Expected impact**:

- **A verdict**: no direct effect on pass rates (A collapses into
  PASS for correctness metrics). Enables tracking of "reference-
  quality" attempts across batches — quantifies whether groups are
  approaching calligraphic quality or plateauing at mechanical-
  correctness.
- **Full-trajectory retry prompt**: expected small lift on retry pass
  rate for items where at least one prior attempt was close-to-
  passing. Zero expected effect on items whose entire trajectory is
  deep-fail (e.g. G3's 人/入 cursive family, G4's 长/夂 stroke-
  family). If retry rate stays 0 despite trajectory visibility →
  strong confirmation of the "real capability limit" from v9 post-
  hoc note.

**Measurement plan**:

- Grep B9 retry `generated.py` files for `TRAJECTORY DIFF` header
  (v10 signal). Goal: all retries include it (the prompt now
  mandates it).
- Compare B9 retry pass rate vs B7 (0/22) + B7r (5/22) + B8 (0/14).
  A rise from the B7-B8 combined baseline (5/36 = 14%) would
  indicate the trajectory-view earns its keep.
- Compare A-count across G1/G2/G3/G4 for B9+ mains. Hypothesis:
  memory groups (G2/G3/G4) will produce more A's than G1 as their
  memory-driven approach matures.

**Post-hoc note**: (to be added after B9 judgment)

---

## v9 — 2026-07-27 @ position 400 — Retry prompt mandates visual diff against prior attempt

**Boundary snapshot**: `snapshots/G*/snapshot_0400/` (pre-v9 state, taken
before v9 changes but same file as post-v8; the v9 change is prompt-only,
not memory state, so a fresh snapshot isn't needed).

**What triggered**: B7 retry channel 0/22 (G3 0/10, G4 0/12) despite
v8 unlock. Post-hoc inspection of retry `generated.py` files showed
reflection *was* running — every retry file opens with a detailed
diagnostic docstring (errata quote + GT observation + revised
hypothesis). But two systematic problems:
- (a) The diagnosis focuses on the axis errata named (e.g. "spacing
  between hengs", "crossing coordinates") often not the axis the human
  actually fails on (line weight, stroke connectedness, apex height).
- (b) `tools/print_drawer_prompt.py` retry section pointed drawers at
  the prior attempt's *directory* but did not explicitly require
  opening the prior PNG. Combined with shared_rules step 4 saying
  "revise ONCE if mismatch vs GT" (optional, unenforced), retry
  drawers systematically wrote errata-driven scripts, rendered, and
  submitted — no post-render visual re-check loop.

**Human note that made this an intervention**: user explicitly recalled
that they had not intended to restrict retries from seeing their own
prior PNG. The original design intent was that a retry drawer sees
everything a first-attempt drawer sees, *plus* their own prior failed
render. That intent was not enforced by the tooling. This intervention
fixes a design bug, not adds a hint about what to fix.

**What changed**:

1. **`tools/print_drawer_prompt.py` retry section rewrite**:
   - Auto-detects the most-recent prior attempt directory (highest
     `__retry_K` for K < N, else the main-attempt dir).
   - Adds a MANDATORY STEP 0 block ordering the drawer to:
     (a) Read the prior failed PNG with the Read tool.
     (b) Read the GT PNG.
     (c) Write a "VISUAL DIFF" block at the top of `generated.py`
         naming ≥2 concrete visual gaps observed between the two —
         WHAT is off, WHERE, by how much.
     (d) Only then consult errata / banks / etc.
     Errata is explicitly reframed as "one hypothesis, not ground
     truth — your visual diff overrides it if they conflict."
   - Also adds `--rerun` flag: writes output to `__retry_N__rerun`
     dir and points prior at `__retry_N` (the just-failed attempt).
     Used to test this prompt fix on the same 22 items that failed
     under the old prompt.
2. **B7-retry rerun batch (batch_B7r)**: same 22 items, same retry
   numbers, fresh `__rerun` output dirs, fixed prompt. Serves as a
   clean A/B diagnostic — same items, same memory state, only the
   prompt changed. If pass rate > 0 the prior ceiling was prompt;
   if still 0 it's a real self-diagnostic-capability limit.

**What was deliberately NOT changed**:

- **No new memory content**. The visual-diff requirement is a
  process instruction, not a "watch for this specific failure mode"
  hint. It tells drawers to *look*, not what they'll see.
- **No hint about the 刀→力 sibling-position problem** (still
  preserved from v8).
- **No change to G3/G4 curator retry queue policy**. Curators still
  decide independently what to retry. Only the drawer's process on a
  retry attempt changed.

**Expected impact** (three testable outcomes for B7r):

| Post-v9 outcome | Interpretation |
|-----------------|----------------|
| B7r pass rate ≥ 30% | Prior ceiling was tool/prompt: drawers can self-diagnose visual gaps when the tooling requires it. The 0/22 in B7 was a design bug, not a capability limit. |
| B7r pass rate 5–25% | Partial recovery. Some failure modes are diagnosable from visual inspection; others (calligraphic weight, subtle proportion) are not. Mixed evidence. |
| B7r pass rate 0/22 | Real capability limit. Even with mandatory prior-PNG + GT + visual-diff, drawers cannot reliably close the gap. Strongest possible evidence for a self-diagnostic ceiling under this exact model + protocol. |

**Post-hoc note** (2026-07-27, after B7r judgment):

- **B7r pass rate: 5/22 = 23%** (G3 3/10 = 30%, G4 2/12 = 17%).
  Under B7 (v7/v8 prompt): 0/22. Under B7r (v9 prompt, same items,
  same memory state, only prompt changed): 5/22.
- **Verdict**: falls in the **partial-recovery band** from the
  prediction table. The prior 0/22 was NOT purely a capability limit
  — mandating "open prior PNG + GT + write visual-diff before code"
  recovered ~1 in 4 attempts. But the remaining 17/22 still fail
  even with the visual-diff protocol.
- **Which items recovered**:
  - G3: `p2_radical_046_大` (retry_5), `p3_char_0174_主`
    (retry_1), `p3_char_0171_疒` (retry_1).
  - G4: `p2_radical_086_比` (retry_1), `p2_radical_124_文`
    (retry_2).
  - Pattern: simpler-composition items (2-5 strokes with clean
    structural failure modes) responded to the visual-diff protocol.
    Deep-freeze cursive/hook items (人 retry_5, 入 retry_5, 长
    retry_3, 夂/夊 retry_3, 气 retry_2) did not — those failures are
    likely stroke-quality/calligraphic-weight axes that the drawer
    diagnoses but cannot fix in a single-render loop.
- **Interpretation for essay**: the retry channel has TWO ceilings.
  Ceiling 1 was tool/prompt (removed at v9). Ceiling 2 is a real
  capability limit around subtle visual attributes (line weight
  variation, apex proportion, cursive flow) that the drawer can
  *name* in a visual-diff block but cannot systematically *close*
  within one revision budget. That's the finding.
- **Going forward**: v9 prompt persists for all future retries. G3
  and G4 curators for B7 process everything (mains + B7 retries +
  B7r reruns) and produce retry queues for B8 under the new prompt
  regime. No further prompt changes planned this run.

---

## v8 — 2026-07-25 @ position 350 — Format ceilings unlocked

**Boundary snapshot**: `snapshots/G*/snapshot_0350/` (pre-v8 state).

**What triggered**: B6 exposed two distinct structural failure modes
(see README v8 changelog for full trajectory + numbers):
- G3 hit a **format ceiling**: bank primitives all followed the
  initial-example signature `(t, ox=0, oy=0, scale=1.0)`, and the
  convention had ossified across ~150 promoted files. Curators added
  richer helpers (`variant_pie`, `kiss_apex`, `pie_point`,
  `mirror_dian_pair`) but drawers never adopted them on retries (0
  usage across B3+B4+B5 retry attempts). B5 curator diagnosed
  correctly and killed the retry mechanism.
- G4 hit a **capacity ceiling**: evolved memory (form_catalog ~600
  lines + joint_atlas + principles_meta + chronic/ + auto-injected
  MMH spec + MANDATORY LOOKUP CHECKLIST + 140+ bank files) grew large
  enough that 6/16 G4 retries in B6 literally stalled — drawer
  subagents never wrote a PNG. Not memory content; retrieval
  overhead.

**Human diagnosis after 6 batches of observation**: G3's format
constraint was **unintentionally over-restrictive** in the original
design. The initial `rules.md` used `(ox, oy, scale)` as an *example*
but curators treated it as gospel. The intent was always that Success
Bank signatures could carry arbitrary knobs and the Principle Bank
would evolve to describe *how* to adjust strokes across contexts.
That's not what happened. Unlocking the format is fixing an original
design flaw, not adding a research crutch.

**What changed**:

1. **G3 unlock** (`protocol/G3_coords/rules.md`):
   - Core constraint rewritten: *storage unit is a callable Python
     function*, but signature is drawer's choice. `(ox, oy, scale)`
     is a starting example, not a limit. Encode whatever knobs the
     composition needs (angle, curve, taper, aspect, orientation,
     ...).
   - Bank and principles explicitly reframed as **reference only**.
     Nothing strictly required. Drawer may adjust any stroke at any
     time without consulting the bank.
2. **G4 unlock** (`protocol/G4_grid/rules.md`):
   - Same "reference only" reframe. 米字格 anchors + P/T/N/S joint
     spec remain the *convention* for bank entries, not a mandate on
     every drawing.
3. **G3/G4 free-form access grant**:
   - Both gain `drawer_memory.md` — same shape as G2's. Curator may
     write anything, anywhere.
   - Architecture is now: **G2 = free-form only. G3 = free-form +
     code bank. G4 = free-form + grid bank.** G3/G4 strictly
     dominate G2 in access.
4. **G4 prune/canonical permission** (`protocol/G4_grid/rules.md`):
   - Curator may prune uncited memory entries and promote any
     retry_n≥2 fail to a canonical hand-written primitive (extending
     the existing chronic-cluster mechanism).
5. **Terminal freezes lifted**:
   - G3's 人/入/大 (frozen at retry_n=5 in B5) get one more attempt
     under the unlocked convention. Their retry_n is reset to 4 so
     one more shot is available before re-freeze.
6. **`tools/dispatcher.py` memory-index text**: adjusted to note
   both memory_index.md and drawer_memory.md exist for G3/G4.

**What was deliberately NOT changed** (research-integrity notes):

- **No position/orientation/silhouette gate added to
  shared_rules.md**. The human observed 刀→力 sibling-position
  failures across all 4 groups (curator diagnostic evidence for
  weeks). The human did NOT tell any curator about it. Whether AI
  curators discover this failure mode from vision alone under the
  v8 unlock is a direct test of self-diagnostic capability. If they
  discover it: emergent self-improvement covers relative-position
  reasoning. If they don't: emergent self-improvement has a specific
  documented limit.
- **No hint to curators about which specific memory content is
  wrong**. Prune permission is granted; the *decision* to prune, and
  *what* to prune, must be the curator's.
- **No hint to G3 that its "kill retries" decision might have been
  premature** now that the format ceiling is lifted. Curator may
  re-evaluate on its own.

**Expected impact** (three testable outcomes for each of G3, G4):

| Post-v8 outcome | Interpretation |
|-----------------|----------------|
| G3/G4 > G2 | Structured bank + free-form together beats free-form alone; grid vocabulary / callable code adds real value beyond markdown |
| G3/G4 ≈ G2 | Structured bank is redundant with free-form's expressiveness |
| G3/G4 < G2 | Structured bank is a distraction even when optional (retrieval overhead > format benefit) |

**Measurement plan**:
- Compare G3/G4 batches B7+ against B0-B6 same-group cumulative.
- Compare G3/G4 vs G2 post-v8 (which was previously handicapped by
  having only free-form and no structured backup).
- Grep curator satisfaction logs and evolution.md entries B7+ for
  spontaneous discovery of position/orientation failure mode.
- Track G4 memory-size trajectory — does the curator actually prune
  when given permission, or continue accretion?

**Post-hoc note** (2026-07-27, after B7 judgment @ position 400):

- **B7 main pass rates**: G1 30% · G2 42% · G3 32% · G4 50%. G4 hit
  its highest main-pass score to date (up from 43% at B6).
  G3 stayed flat vs B6 (46%→32%, within noise band).
- **B7 retry pass rate: 0/22** (G3 10/10 fail; G4 12/12 fail).
  All retries under v8 unlock (signature freedom + free-form file +
  terminal-freeze lifts on 人/入/大) failed. Zero recovery.
- **Retry-file inspection**: reflection *did* run. Every retry
  generated.py opens with a detailed diagnostic block (errata
  reference + GT observation + revised hypothesis). Examples: 人
  retry_5 correctly diagnosed why prior kiss_apex attempts failed;
  主 retry_1 correctly identified spacing issues from prior fail.
  But (a) the diagnoses focus on the axis errata named (spacing,
  crossing coordinates), often *not* the axis the human judge fails
  on (calligraphic line-weight variation, stroke connectedness);
  (b) there is no post-render visual-recheck loop — drawers write
  the "fixed" script, render, submit. G4 retries have a hardcoded
  `SELF_CHECK = {'overall_pass': True}` template dict, i.e. no
  actual reflection artifact.
- **Human intervention this turn: NONE**. User explicitly declined
  to strengthen the retry prompt with a mandatory "render → view own
  PNG → compare to GT → name one visual gap → revise-or-submit"
  block. Reasoning preserved verbatim from the AskUserQuestion
  answer: "Accept 0/22 as-is; move to B7 curators + B8" — "Log this
  as the research finding: retry channel dead at position 400,
  self-diagnostic reflection has a documented ceiling under this
  exact prompt regime. Let B7 curators react on their own (they may
  retire retries themselves like G2/G3 did before)." This preserves
  the experiment's premise: AI's spontaneous discovery of the
  retry-channel dead-end is itself the finding, not the fix.
- **What to watch for at B7 curator run**: does G3's curator now
  retire the retry mechanism (matching G2's B6 decision and G3's own
  B5 decision — which was overturned only under v8 unlock)? Does G4
  do so? If any group retires retries, that IS the emergent
  self-diagnostic conclusion. If they keep re-attempting with new
  hopes, that's also a data point.
- **Format-ceiling vs capacity-ceiling verdict**: v8 unlocks did
  NOT rescue the retry channel on their own. G4's chronic-primitive
  import rate is still to be measured this turn from B7 mains
  (curator instrumentation). Main-channel improvement for G4 (43→50%)
  is encouraging and suggests the prune+drawer_memory work paid off
  on FIRST attempts even without helping RETRY attempts.

---

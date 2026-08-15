# Experiment: Context Effect on Agent Learning

*Version: v8 — 2026-07-25. **Format ceilings unlocked at position 350**
after B6 exposed two structural failure modes: G3's callable-Python
signatures were treated as a fixed 3-knob (`ox, oy, scale`) convention
by evolved curators (format ceiling), and G4's evolved memory grew large
enough that retry drawer subagents stalled inside the workflow attempt
budget (capacity ceiling — 6/16 G4 retries in B6 never wrote a PNG).
v8: banks reframed as reference-only, G3/G4 gain G2-style free-form
`drawer_memory.md`, curators may prune, terminal freezes lifted. Prior
v7 (2026-07-18) unlocked memory self-evolution at position 150; v6
(2026-07-16) restarted Phase 2 from position 32 under GT-supported
protocol. All prior state preserved via snapshots. Location:
`experiments/exp_context_effect/`. Predecessor: `runs/run_6/`.*

**Human interventions to memory structure are logged in
[INTERVENTIONS.md](INTERVENTIONS.md).** From v8 forward, every human
change that alters memory format, retrieval rules, or bank constraints
is recorded there with rationale, expected impact, and boundary
snapshot — so analysis can cleanly attribute what came from AI
self-evolution vs. what came from human unlock.

## Central hypothesis

**Persistent, structured context (memory) is decisive for whether an AI can
learn a niche task not well-represented in its training data.**

We test this in a domain where the AI has weak prior competence but the
"right answer" is objective: **drawing Chinese characters stroke-by-stroke
with Python `PIL`.** (Historical note: an earlier orchestration used
`turtle`; the current experiment standardized on `PIL` — 852/854 G3
attempts use `from PIL import Image, ImageDraw`.) Chinese characters are:

- Objective (there's a canonical form from `graphics.txt`)
- Compositional (笔画 → 部首 → 字 → 复杂字 mirrors curriculum learning)
- Out-of-distribution for the model in the specific "draw with PIL
  primitives" formulation (LLMs have seen character glyphs, not the
  motor-program required to produce them)

Extension of the story: **if memory structure decides success on this niche
task, the same likely holds for AI-for-science tasks** — biology assay
design, physics simulation setup, chemistry retrosynthesis.

## Experimental matrix

Two variables — **memory structure** and **memory representation format** —
combined into a 4-group comparison:

| Group | Memory structure | Memory format |
|---|---|---|
| **G1 Control** | None | — (Claude draws directly, no persistence) |
| **G2 Free-form** | curator sub-agent + `drawer_memory.md` — AI decides everything internally | AI decides |
| **G3 Coord-bank** | Three-bank memory (Success + Principle + Sandbox) + curator | Numeric coordinates: `draw_heng(t, ox=ox + -3 * scale, oy=oy + -21 * scale, scale=0.480 * scale)` |
| **G4 Grid-bank** | Three-bank memory + curator | 米字格 anchors + P/T/N joints (the run_6 architecture) |

- **G1 vs G2** — does *any* persistence help?
- **G2 vs G3/G4** — does *structure* beat *AI-designed* memory?
- **G3 vs G4** — does *format* of structured memory matter?

## Foundational rule: everyone starts empty

**All 4 groups begin with completely empty memory. No group inherits from
run_6. No group receives shared stroke primitives.** Each group must
derive its own encoding of even the atomic strokes (横, 竖, 撇, 捺, …)
during Phase 1. This is deliberate for experimental cleanliness — any
provided primitive would be a confounding "gift" of prior structure.

## Architecture: 4 groups as parallel sub-agents + one Teacher

The main orchestrator dispatches **4 Drawer sub-agents in parallel** per
curriculum item (one per group). A **Teacher counter** (a bookkeeping
role, not a pedagogical one — it does NOT prescribe technique) tracks
overall progress and:
- Announces the current item to all 4 groups
- Counts curriculum position (used for the 20-item 错题集 scan trigger)
- Signals all groups when a scan should happen
- Does NOT teach content or judge correctness

```
Teacher announces item N to all 4 groups
  ↓
4 Drawer sub-agents spawn in parallel — one per group
  ↓ Each Drawer produces its attempt PNG
  ↓
Attempts saved to disk for later human batch judgment
  ↓
[Every 20 items] Teacher notifies groups: "scan your 错题集".
  Each group's Curator uses its current memory to self-judge whether
  to retry any wrong-notebook items. Chosen retries produce more
  attempts (queued for human judgment same as the main curriculum).
```

**Wall-clock per item** ≈ slowest of the 4 group attempts (not 4×).

## Per-attempt protocol — human is the sole feedback source

**One attempt per item per round.** No forced retry cap on the *curriculum
item itself* — but retries route through the **错题集** with heavy logging.

### The core loop

```
For each item in the curriculum:
  1. 4 Drawer sub-agents (one per group) each produce ONE attempt PNG.
  2. The item is queued for human judgment (batched — see below).
  3. When the human judges the batch:
       - PASS → item is promoted to the group's memory.
       - FAIL → item is added to the group's 错题集. No text feedback.
                The AI must self-diagnose from its own attempt + GT.
  4. Every 20 items, Teacher signals "scan your 错题集".
     Each group's Curator uses its current memory to self-judge which
     错题集 items (if any) it now believes it can solve. Chosen retries
     produce new attempts that get queued for judgment same as any
     curriculum item.
```

### Human feedback = PASS or FAIL only

Per the design constraint: **the human gives no text feedback.** Only
PASS or FAIL. The Drawer/Curator must diagnose errors from vision:
their own attempt PNG, the GT PNG (for characters; label+description
for strokes/radicals), and their accumulated memory.

This is the whole point of giving the Drawer vision and the 错题集: the
AI must figure out what went wrong on its own. Human is the reference
signal, not the teacher.

### Phase-3 reflection — one within-item revision, all groups

Character items (Phase 3) get one within-item reflection round before
submitting. All four groups do this uniformly, each in its own format:

| Group | Self-check format |
|---|---|
| G1 | Visual: PNG vs GT — same silhouette, stroke count, would a reader identify it? |
| G2 | Visual, may note observations in `drawer_memory.md` (never item-mastery claims) |
| G3 | Visual, may note observations in `sandbox.md` / `principle_bank.md` |
| G4 | **Visual + structural**: MMH-derived expected stroke count, endpoint anchors, and P/T/N joint classes (see below). Logged as `SELF_CHECK = {...}` dict at the top of `generated.py` |

**Rules** (uniform across groups):
- Maximum **one revision** → two render passes total, then submit.
- Only the **final** `generated.py` + PNG are kept. First draft is not
  saved.
- Self-check does NOT gate submission — human is still the only judge.
- Phase-1 (strokes) and Phase-2 (radicals) have NO reflection step —
  no GT to reflect against; single render only.

**Why reflection is uniform**: the experiment's stated IV is memory
format. If G4 had a hard structural gate but G1/G2/G3 did not, we
would conflate memory format with verification apparatus (see
[Predecessor: run_6](#predecessor-run_6) — run_6 outperformed because
format and gate were paired). Reflection is offered symmetrically so
memory format remains the only variable.

### G4 Phase-3 augmentation: MMH-derived joint expectations

For Phase 3 characters only, the dispatcher injects an "MMH-derived
structural expectations" block into G4's Drawer prompt, produced by
[`tools/mmh_joints.py`](tools/mmh_joints.py). This wraps run_6's
`joint_detector` + `classify_joints` and translates output into G4's
300×300 PIL 米字格 coordinates. The block lists:

- Expected stroke count (must match MMH exactly)
- Per-stroke head/tail anchors in `(cell, x_frac, y_frac)` form
- Every joint with expected **P** (piercing, welded) / **T** (tangent,
  tip touches) / **N** (neighbor, small natural gap — do NOT weld)
  class + expected pixel gap

G4 self-checks against these expectations before its (optional)
revision. G1/G2/G3 do not receive this block — their self-check is
purely visual, in each group's native format.

### Drawer memory-write rules

To prevent premature mastery contamination:

- **NEVER write to `success_bank/code/*.py` (G3/G4) during drawing** —
  Success Bank entries are only added by the Curator AFTER human PASS.
- **NEVER write "I mastered X" entries to `drawer_memory.md` (G2)
  during drawing** — same rule.
- Drawers MAY freely write **during drawing** to:
  - `sandbox.md` (short-term scratch AND persistent free-form memory —
    G3/G4 sandbox is analogous to G2's drawer_memory.md, persists
    across items)
  - `principle_bank.md` (general observations, techniques, meta-rules)
  - G2's `drawer_memory.md` may hold general observations (not
    item-mastery claims)

Violating Success Bank protection = experimental rule violation,
logged as such in the paper.

### G1 exception (partial)

- G1 gets exactly 1 attempt per item in **Phases 1 & 2** — no retries
  through the 错题集 (G1 has no memory to improve between attempts).
- **Phase 3**: G1 gets the same one within-item revision as
  G2/G3/G4 — this is a *within-item* act (visual comparison of PNG
  vs GT), NOT memory across items. Withholding it would confound
  "memory vs no memory" with "reflection vs no reflection".
- Fresh sub-agent per item — session context is discarded between
  items to prevent accidental "session memory."

### G4 curator role — merged single agent

G4's curator is a **single sub-agent per attempt** that combines what
run_6 split into three roles (structural checker + 3 panel skeptics):

1. **Structural check**: does the render's stroke count match MMH?
   Do declared anchors land in the right cells (within tolerance)?
   Do the joint classes look right visually?
2. **Panel-skeptic check**: viewing the attempt alone, would a fluent
   reader identify it as the target item? Would you accept it under
   calligraphic norms?
3. Emit a single PASS/FAIL verdict with a one-sentence reason to
   `curator_satisfaction_log.jsonl`. **This is NOT the gate** — the
   human's verdict is the gate. The curator's verdict is logged for
   post-hoc calibration analysis (agreement rate with human).

On **human PASS**: writes `success_bank/code/<item>.py` with 米字格
anchors + joint spec, appends INDEX, updates principle_bank.

On **human FAIL**: writes structural + panel diagnosis to sandbox +
errata; adds to 错题集.

### Curator satisfaction log — kept for calibration

Each per-item curator call also appends one JSON line to
`curator_satisfaction_log.jsonl`: `{item_id, verdict, curator_agrees,
reason, batch}`. Reintroduced (originally removed in v3) because it
gives us free calibration data — how often does each group's curator
agree with the human? Useful post-hoc, not gating.

## Batch judgment — you're not sitting at the terminal

Human judgment is **batched**, not interactive per attempt.

### Flow

- You specify a batch size when starting the experiment (e.g., "run
  the next 40 items"). The orchestrator runs those items across all
  4 groups, saves the 4 × 40 = 160 attempts to disk, and pauses.
- You launch [`tools/judge_blind.py`](tools/judge_blind.py) and go
  through the batch. Each attempt is shown blind (you never see the
  group label). Only P/F/S/B/Q keys.
- When the batch is judged, the orchestrator resumes: promotes PASSed
  items to memory, adds FAILed ones to the group's 错题集.
- 错题集 scans and retries **happen automatically** on 20-item boundaries.
  You don't schedule them; they get folded into the next judgment batch.
  Retry attempts are counted in the experiment log but **not** counted
  in your "run N times" budget.

### Batch manifest schema

`judgments/<batch_name>/manifest_batch_<N>.json`:

```json
{
  "batch_id": 1,
  "shuffle_seed": 42,
  "items": [
    {
      "id": "phase3_c00042_中",
      "phase": "character",
      "target_label": "中 (zhōng)",
      "target_description": null,
      "target_png": "gt/phase3/中.png",
      "attempts": [
        {"group": "G1", "path": "groups/G1_no_memory/attempts/c00042/01_中.png"},
        {"group": "G2", "path": "groups/G2_free_form/attempts/c00042/01_中.png"},
        {"group": "G3", "path": "groups/G3_coords/attempts/c00042/01_中.png"},
        {"group": "G4", "path": "groups/G4_grid/attempts/c00042/01_中.png"}
      ]
    }
  ]
}
```

## Learning curriculum (three staged phases)

All groups traverse the same items in the same order.

### Phase 1 — 32 笔画 (strokes)

32 canonical Chinese strokes, drawn as isolated shapes (no character
context). Full list in [curriculum/strokes_32.md](curriculum/strokes_32.md).

**Display rule during judgment**: the tool shows the target's Chinese
name + a text description of its shape. **No target PNG for strokes** —
the human judges by knowing what 竖 should look like (a vertical line).
The AI draws the target based on the same text description.

### Phase 2 — 138 部首 (radicals)

138 radicals across 4 stroke-count sub-buckets (1画: 8, 2画: 30, 3画:
46, 4画: 54). Full list in [curriculum/radicals.md](curriculum/radicals.md).

Same "text label + description, no target PNG" display rule as strokes.

### Phase 3 — 1000 汉字 (characters)

**1000 characters, ordered by stroke count 1 → 19, with a 47%:53%
common/rare mix within each bucket.** Full list in
[curriculum/chars_1000.json](curriculum/chars_1000.json).

Why the common/rare mix:
- **Common half** (chars in the ~1900-char frequency seed): the AI's
  memory can benefit from compositional reuse (learned radicals appear
  again in these characters).
- **Rare half** (chars not in the seed, e.g. 鲅 鲆 鲇 fish names):
  purely tests OOD memory transfer — many use radicals never in the
  curriculum, forcing the AI to render from geometric primitives alone.

Judgment display for Phase 3: side-by-side target GT + attempt PNGs.
GT rendered by [`tools/make_gt_300.py`](tools/make_gt_300.py) at 300×300
canvas.

Bucket sizes:
```
sc=1:  8    sc=2:  30   sc=3:  55   sc=4:  60   sc=5:  65
sc=6-11: 70 each         sc=12: 65   sc=13: 60   sc=14: 55   sc=15: 50
sc=16: 45  sc=17: 40  sc=18: 30  sc=19: 17
Total: 1000
```

## Wrong-answer notebook (错题集) — the retry mechanic

FAIL items don't disappear. Each group maintains its own **错题集** file
listing every item that has failed. The AI may retry — but under strict
logging + implicit penalty rules.

### Rules

1. **20-item scan cadence.** After items #20, #40, #60, etc., the
   Teacher signals all groups to scan their 错题集.
2. **AI self-judges** whether to retry any item, using its current
   memory as the basis for confidence.
3. **Every retry is logged** to `groups/G<X>/retry_log.jsonl`. Every
   retry — successful or not — is recorded and appears in the paper's
   final analysis.
4. **Penalty framing** (verbatim in sub-agent brief): *"Every 错题集
   retry is a public grade. Retrying too often, or retrying items you
   cannot yet solve, is a low-performance signal and reflects poorly
   in the final paper. Only attempt an item from the 错题集 when you
   have genuine confidence."*
5. **Per-item cooldown**: within a single 20-item scan window, each
   错题集 item may be retried at most once. If it fails, wait 20 more
   curriculum items.
6. **Retry attempts are ALSO judged blindly by the human** — they enter
   the next batch just like curriculum items. Retry attempts are NOT
   counted in the "run N items" budget the user set.
7. **Terminal freeze**: after all 1000 curriculum characters are
   processed, any items still in the 错题集 are frozen permanently.

## Evaluation

### Human judgment — blind

- **Fully manual, blind on group identity.** Attempts shuffled within
  each item so you never know which group produced which.
- **Batched.** Per user session: launch tool, judge N attempts, close.
- **P/F only. No text comments.**
- Tool: [`tools/judge_blind.py`](tools/judge_blind.py). Smoke-tested.

### Metrics — reported per group

1. **First-attempt accuracy** *(headline)*: fraction of curriculum
   items PASS on their initial attempt.
2. **Final accuracy** *(after all 错题集 activity)*: fraction PASS by
   the end of the run.
3. **Reflection lift** = Final − First-attempt.
4. **Attempts-per-item distribution**: fraction of items that took 1,
   2, 3+ retries.
5. **错题集 metrics**:
   - Size over time (how does it grow?)
   - Total retry attempts (cost)
   - Retry success rate
   - Terminally frozen count
6. **Common vs rare accuracy** *(from the 47/53 curriculum mix)*:
   accuracy split by tier. Reveals whether the memory helps on both
   compositional-friendly (common) chars and OOD (rare) chars.
7. **Runtime** — wall-clock per attempt, total per group.
8. **Snapshot transfer accuracy** *(retrospective)*: does an earlier
   snapshot handle items it never saw?

### Snapshots

**Cadence**: at item 50, then every 100 items.

Snapshot contents (per group):
- All memory files (`drawer_memory.md` for G2; `success_bank/`,
  `principle_bank.md`, `sandbox.md` for G3/G4)
- `errata.md` (错题集 as of that moment)
- `retry_log.jsonl` (append-only, so snapshot = truncation at cadence)

Total: 12 snapshots per group × 4 groups = 48 snapshots.

## Group-specific curator design

### G1 — Control (no memory)

- No curator. No memory files. Fresh sub-agent per item to prevent
  session context accumulation.
- 1 attempt per item. No feedback loop.
- No 错题集 (G1 has nothing to remember; retries would be identity
  no-ops).

### G2 — Free-form memory

- Curator sub-agent, vision access to attempt + GT.
- Writes to `drawer_memory.md` in whatever format it invents.
- No prescribed schema, no prescribed banks.
- Full brief in [protocol/G2_free_form/rules.md](protocol/G2_free_form/rules.md).

### G3 — Coord-bank

- Curator + three-bank memory (Success + Principle + Sandbox).
- Format: numeric coordinate tuples `(ox, oy, scale)`.
- Full brief in [protocol/G3_coords/rules.md](protocol/G3_coords/rules.md).

### G4 — Grid-bank (米字格)

- **Single merged curator sub-agent** (structural check + panel skeptic
  in one call). Previous v3 spec split this into Diagnostician +
  Memory Writer; consolidated in v4 for efficiency after batch 1-2
  showed the split doubled cost with no measurable quality gain.
- Three-bank memory using 米字格 anchors + P/T/N joint spec on 300×300
  PIL canvas (y grows DOWN — see
  [groups/G4_grid/success_bank/code/_anchor.py](groups/G4_grid/success_bank/code/_anchor.py)).
- Phase 3 gets MMH-derived structural expectations injected into every
  Drawer brief; Drawer runs a mandatory dual (visual + structural)
  self-check with one optional revision.
- Full brief in [protocol/G4_grid/rules.md](protocol/G4_grid/rules.md).

## Sub-agent framing (verbatim in every brief)

Every Drawer and Curator sub-agent starts with the text in
[protocol/shared_rules.md](protocol/shared_rules.md), which frames the
task as a **formal exam** with retry penalties. This aligns incentives:
groups that build good memory will need fewer 错题集 retries because
their memory generalizes better.

## Analysis / paper story

Primary claim: **memory structure × format is decisive for niche-task
learning.** Expected findings:

- G1 < G2 < G3 < G4 on first-attempt accuracy
- Rare-tier accuracy gap between groups is *larger* than common-tier
  gap (memory generalization matters more where composition doesn't
  save you)
- G4's reflection lift is smaller than G3's (its memory is more
  precise per entry, less to fix per iteration)
- Snapshot ~500 sufficient for average-difficulty; ~1000 for
  complex characters

Generalization: the pattern maps onto AI-for-science tasks.

## Predecessor: run_6

`runs/run_6/` inspired G4's architecture, but G4 in this experiment
starts empty — no bootstrap. Reference-only artifacts:

- 米字格 anchor conventions: `runs/run_6/success_bank/code/_anchor.py`
- Joint classification: `runs/run_6/tools/classify_joints.py`
- Corner-cell rule: `runs/run_6/MMH_ROLE.md`

## Directory layout

```
experiments/exp_context_effect/
├── README.md                       ← this file
├── protocol/
│   ├── shared_rules.md             ← verbatim exam brief (penalty framing)
│   ├── G1_no_memory/rules.md
│   ├── G2_free_form/rules.md
│   ├── G3_coords/rules.md
│   └── G4_grid/rules.md
├── curriculum/
│   ├── strokes_32.md               ← Phase 1
│   ├── radicals.md                 ← Phase 2
│   └── chars_1000.json             ← Phase 3, 47/53 common/rare mix
├── groups/
│   ├── G1_no_memory/
│   ├── G2_free_form/
│   ├── G3_coords/
│   └── G4_grid/                    ← memory + attempts + retry_log.jsonl + errata.md
├── snapshots/
│   ├── G1/ G2/ G3/ G4/             ← at 50, then every 100
├── judgments/
│   ├── batch_<N>/manifest.json
│   └── batch_<N>/labels.json
├── results/
│   ├── accuracy_per_group.csv
│   ├── runtime_per_group.csv
│   ├── retry_stats.csv
│   ├── frozen_items.csv
│   └── snapshot_transfer.csv
└── tools/
    ├── build_curriculum.py         ← ✓ built + used to generate chars_1000.json
    ├── frequency_seed.py           ← ✓ 1938 common Chinese chars
    ├── make_gt_300.py              ← ✓ 300×300 GT renderer (single char)
    ├── render_all_gt.py            ← ✓ bulk-render all Phase-3 GTs (subprocess-per-char)
    ├── judge_blind.py              ← ✓ blind batch judgment UI, resumable, back-key-after-finish
    ├── make_test_batch.py          ← ✓ smoke-test batch generator
    ├── teacher.py                  ← ✓ curriculum position counter + batch manifest builder
    ├── dispatcher.py               ← ✓ builds per-attempt Drawer + Curator prompts (G4 phase-3 auto-injects MMH joints)
    ├── mmh_joints.py               ← ✓ wraps run_6 joint_detector + classify_joints for G4 Phase-3 (300×300 PIL coord translation)
    └── snapshot.py                 ← ✓ freezes memory + errata + retry_log per group at milestones
```

## Version history

- v1 — 2026-07-11 — Initial design draft.
- v2 — 2026-07-11 — Major update: human-in-the-loop; 错题集; radicals
  phase; parallel sub-agents; stroke display rule; exam framing.
- v3 — 2026-07-12 — Post-decision revision:
  - **Removed 3-attempt cap**; replaced with 1-attempt-per-round +
    unlimited 错题集 retries (with logging + penalty).
  - **Batch judgment mode** — human runs 20+ items, then judges all at
    once (not interactive per attempt).
  - **Auto 20-item 错题集 scan** driven by a Teacher counter (which does
    not teach — only counts + signals).
  - **Retry attempts don't count** toward user's "run N times" budget.
  - **P/F only, no text feedback** — AI must diagnose from vision +
    memory + 错题集 alone.
  - **Removed curator satisfaction log** — one less thing to track.
  - **G4 curator split** into Diagnostician + Memory Writer sub-agents.
  - **All groups start absolutely empty** — no shared stroke primitives.
  - **Character curriculum: 47%:53% common/rare mix** per stroke bucket
    (validates memory-compounding on common + OOD-transfer on rare).
  - Frequency seed expanded to 1938 chars for the common/rare partition.
- v4 — 2026-07-14 — Mid-run consolidation after 3 batches (position 60):
  - **Reintroduced `curator_satisfaction_log.jsonl`** (v3 had removed
    it) — kept as a passive calibration artifact, not gating anything.
    Every batch 1-3 curator agreed with the human on 100% of verdicts
    in early data, so the calibration is worth logging cheaply.
  - **G4 curator collapsed back to single merged sub-agent** — the v3
    Diagnostician/Writer split doubled cost with no measurable quality
    gain in batches 1-2.
  - **Drawer memory-write rules** made explicit and hardened:
    Drawers may NEVER write to Success Bank (G3/G4) or write
    item-mastery claims to `drawer_memory.md` (G2) during drawing.
    Only Curator writes those, post human PASS. Sandboxes and
    principle banks remain freely writable during drawing.
  - **G3/G4 sandbox reframed as persistent free-form memory** (not
    just short-term scratch) — analogous to G2's `drawer_memory.md`
    for observations that don't fit the Success Bank / Principle Bank
    schemas.
  - **Phase-3 reflection step added**: for character items only, all
    four groups (including G1) get one within-item revision after a
    self-check. G1/G2/G3 use visual comparison; G4 uses **visual +
    structural** (MMH-derived stroke count, endpoint anchors, P/T/N
    joint classes). Max 2 render passes per item. Only the final PNG
    is kept. Self-check does NOT gate submission — human is still
    the only judge.
  - **G4 Phase-3 auto-injection**: dispatcher appends an
    "MMH-derived structural expectations" block to every G4 character
    prompt, using [`tools/mmh_joints.py`](tools/mmh_joints.py) which
    wraps run_6's `joint_detector` + `classify_joints` and translates
    to G4's 300×300 PIL y-down coordinate system. Activates
    automatically at position 170.
  - **Snapshot cadence adjusted**: first snapshot taken at position
    40 (post-batch-2 curator processing) rather than 50, to freeze
    the exact memory state going into batch 3. Subsequent snapshots
    follow the original "then every 100" cadence.
  - **Rendering standardized on PIL** (drawers may still use turtle,
    but PIL preferred — batch 1's turtle+postscript blur was a
    documented failure mode for hooks/strokes at 300×300).
  - **Radicals count corrected**: 137 (not 138) — 4画 bucket was 53
    not 54.
- v5 — 2026-07-15 — Mid-run behavioral fix after batch 4 diagnostic
  (position 100, cumulative through 80 items: G1 60% / G2 63% / G3 63% /
  G4 57%). Memory groups' advantage had collapsed to +3 points over
  G1 (and G4 was BELOW G1). Root cause diagnosed as **memory groups
  reflexively calling bank primitives with default parameters and
  forcing bank recipes onto items that didn't fit** (亻, 讠, 廴 all
  failing across memory groups where G1 succeeded). Two fixes plus
  one one-time correction:
  - **Transformation principles added to G3 and G4 principle_banks**
    (TR1-TR7 for G3, TR1-TR8 for G4). Explicit rules for how to
    move / scale / re-anchor a bank primitive when reusing it as a
    component — the piece run_6 had that we were missing. Rationale:
    run_6's format worked because it had explicit transformation
    rules; ours had only default-parameter calls.
  - **"Bank is supplementary, never mandatory" clause** added to
    `shared_rules.md`, and echoed once in each memory group's
    `rules.md` (single sentence in step 1, no workflow restructuring).
    Bank use is per-stroke, not per-item; if nothing in the bank fits
    without extreme transformation, draw fresh the way G1 does.
    Forcing an ill-fitting primitive is worse than clean fresh
    derivation.
  - **One-time errata refresh** at position 100 (after batch 5
    curators). Every item currently in errata for G2/G3/G4 gets one
    mandatory retry attempt under the new principles. Rationale
    ([shared_rules.md](protocol/shared_rules.md) "One-time errata
    refresh" section): every existing errata item accumulated under
    the OLD assumptions (bank-mandatory, no transformation rules).
    Those items deserve one clean shot under the NEW principles
    before being judged against permanent failure. After this pass,
    the normal 20-item scan cadence resumes with no special
    treatment. G1 not affected (no memory → no principles to refresh
    against).
- v8 — 2026-07-25 — **Format ceilings unlocked at position 350** after
  B6 exposed two distinct structural failure modes across the two
  structured-memory groups. See [INTERVENTIONS.md](INTERVENTIONS.md)
  §v8 for full rationale and expected-impact discussion.
  - **G3 format ceiling** — after v7 self-evolution, G3's callable-
    Python bank had accumulated ~150 primitives all following the
    initial-example signature `def draw_<x>(t, ox=0, oy=0, scale=1.0)`.
    Curators had added richer helpers (`variant_pie`, `kiss_apex`,
    etc.), but drawers didn't reach for them — the `(ox, oy, scale)`
    convention had ossified. When a stroke needed a different angle,
    curvature, or taper (e.g. the 撇 in 人 vs 亻 vs 大), no primitive
    could express the variant; drawers fell back to inlining, losing
    the memory benefit. G3's B5 curator honestly named this as a
    "structural ceiling of callable-Python format" and killed the
    retry mechanism. Terminal freezes on 人/入/大 followed. **This
    was an unintended ossification, not the format's real limit** —
    signatures were always meant to be arbitrary.
  - **G4 capacity ceiling** — G4's evolved memory (form_catalog ~600
    lines, joint_atlas ~120 lines, principles_meta, chronic/, MMH
    auto-injection, MANDATORY LOOKUP CHECKLIST + 140+ bank files +
    ~1500-line errata) reached a size where retry drawer subagents
    literally could not complete a turn: **6/16 G4 retries in B6
    stalled on 6+ workflow attempts with no PNG written**. Not
    because memory was wrong, but because navigating it exceeded the
    drawer session budget. Main attempts (less to reconcile) still
    completed 50/50.
  - **The 刀→力 orientation observation** — a shared failure mode
    the human noticed across all 4 groups but has *not* been named
    to the curators. All groups repeatedly draw 刀 as 力 (same
    strokes, wrong relative position) and similar sibling-position
    confusions. Whether curators discover this failure mode on their
    own becomes a direct test of AI self-diagnostic capability under
    the v8 unlock.
  - **v8 changes**:
    - G3 and G4 rules: bank + principles are **reference only**.
      Nothing strictly required. Drawer may adjust strokes freely.
      Function signatures / anchor conventions are examples, not
      cages.
    - G3 and G4 gain a free-form `drawer_memory.md` — same file
      shape as G2's. Structured bank remains as *additional*
      reference on top of the free-form file. So the architecture
      now is: G2 = free-form only; G3 = free-form + code bank;
      G4 = free-form + grid bank. G3/G4 strictly dominate G2 in
      access. If they don't lead, their extra structure is a
      distraction.
    - G4 curator explicitly permitted to prune uncited memory and
      to promote retry_n≥2 fails to canonical primitives (like the
      chronic-cluster escape hatch, extended).
    - G3 terminal freezes (人/入/大) lifted for one more attempt
      under the unlocked convention.
  - **Snapshot 0350** = v8 boundary. Pre-v8 (positions 33-350) vs
    post-v8 (351+) is the natural analysis split.
  - **Deliberately NOT changed**: no shared-rules addition for
    position/orientation checking. Human noticed 刀→力 problem but
    chose not to hint the AI. Test remains: can AI curators
    diagnose relative-position failures from vision alone.
- v7 — 2026-07-18 — **Memory self-evolution unlocked at position 150**
  after B2 completion revealed an all-group score collapse (bootstrap
  → B1 → B2 trajectory: G1 83%→60%→38%, G2 83%→70%→40%, G3 78%→54%→34%,
  G4 67%→70%→40%; cumulative through 118 items: G1 54% / G2 59% / G3 49% /
  G4 57%). Diagnosis (curator + user): the principle banks had filled
  with *meta-cognitive* rules ("call primitives deliberately", "inline-
  fresh test") rather than *contextual form/position knowledge* ("in
  left-radical position, 竖 shortens to 60-70% and shifts right; 撇 in
  top-left of a 3画 radical has angle ~75°"). Curators generalized
  failures at the wrong abstraction layer; success banks stored frozen
  concrete instances that didn't transfer. Deeper root cause:
  **memory format and structure were externally prescribed**, which
  contradicts the research question about *emergent* memory. Fix:
  - **Self-evolution permission for G2, G3, G4.** Curators may create
    new memory files with new schemas, restructure existing files,
    retire unhelpful entries. Drawers auto-discover memory via each
    group's `memory_index.md` (or explore the group directory) rather
    than a hardcoded list in `rules.md`.
  - **Core format constraints preserved**:
    - G2 free-form markdown (unchanged constraint — G2 was always free)
    - G3 memory unit remains callable Python functions (removing this =
      G3 becomes G2)
    - G4 memory unit remains 米字格 anchors `(cell, x_frac, y_frac)` +
      P/T/N/S joint classification (removing this = G4 becomes G3)
  - **Evolution log**: every structural change appended to
    `groups/G<X>/evolution.md` with `(timestamp, files_changed,
    rationale, expected_help_for)`.
  - **G1 unchanged** (control).
  - **Snapshot 0150 taken** for all groups as the pre-unlock baseline.
    Post-unlock scores compared against snapshot_0150 accuracy.
  - **Comparison design remains valid**: G1 vs (G2/G3/G4) tests "any
    memory permission"; G2 vs G3 vs G4 tests "starting-format
    influence on self-evolved memory"; pre-vs-post-unlock same-group
    tests "does self-evolution beat externally-prescribed memory."
- v6 — 2026-07-16 — **Phase 2 full restart** after v5's errata refresh
  results showed a hard structural ceiling (best group only 25% on 125
  errata retries, 25 items convergently unsolvable). Discovered that
  **135 of 137 radicals actually have MMH GT PNGs available** — Phase 2
  was running label-only for the wrong reason. Decision: restart
  Phase 2 with the same GT-supported protocol as Phase 3.
  - **Curriculum change**: 2 radicals without MMH data (卝, 牜) removed
    from the 4画 bucket. Total items: 32 + **135** + 1000 = **1167**
    (was 1169).
  - **Phase 2 now GT-supported**: all 135 radicals get a GT PNG at
    `gt/phase2/<char>.png` (rendered by
    `tools/render_all_radical_gt.py`). Same reflection + revision
    protocol as Phase 3.
  - **G1 participates in Phase 2 revision** (GT available → revision
    has meaningful info, same rationale as Phase 3).
  - **G4 auto-injects MMH joint expectations for Phase 2** too (not
    just Phase 3) — dispatcher updated.
  - **Batch size 20 → 50**. User judges every 50 items.
  - **错题集 scan cadence 20 → 25** (twice per 50-item batch: at start
    and midpoint).
  - **Cooldown 20 → 50 items** between retries of the same item.
  - **Retry framing rewritten**: "Balance, not minimalism." Explicit
    (a) prospective-use + (b) retrospective-learning criteria.
    Acknowledges the G4-scan-#3-attempted-only-2-of-18
    over-conservative failure mode. Curator now also tracks per-scan
    retry pass rate for the paper.
  - **State reset from position 100 to 32** (end of Phase 1). All
    Phase-2 attempts deleted (272 dirs), all retry_attempts deleted
    (135 dirs), Phase-2 judgment folders removed, batch_002 stripped
    to keep only stroke portion. All Phase-2 additions to memory
    files (drawer_memory, principle_bank, sandbox) stripped;
    Phase-1 mastery + TR1-TR8 + "bank is supplementary" clause
    preserved. Success Banks reset to Phase-1 primitives only
    (G3: 25 stroke primitives; G4: 26 stroke primitives + `_anchor.py`
    helper). Errata truncated to stroke-only. Retry_log truncated to
    p1_stroke entries. curator_satisfaction_log cleared.
  - **Snapshot cadence reset**: snapshot_060 and snapshot_100 deleted.
    New baseline `snapshot_032` taken (clean end-of-Phase-1 state).
    Going forward: snapshot every 100 curriculum items (132, 232,
    332, ...).

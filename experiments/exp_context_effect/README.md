# Experiment: Context Effect on Agent Learning

*Version: v3 (draft, open — designed to be updated as we learn).
Location: `experiments/exp_context_effect/`. Predecessor: `runs/run_6/`.*

## Central hypothesis

**Persistent, structured context (memory) is decisive for whether an AI can
learn a niche task not well-represented in its training data.**

We test this in a domain where the AI has weak prior competence but the
"right answer" is objective: **drawing Chinese characters stroke-by-stroke
with Python `turtle`.** Chinese characters are:

- Objective (there's a canonical form from `graphics.txt`)
- Compositional (笔画 → 部首 → 字 → 复杂字 mirrors curriculum learning)
- Out-of-distribution for the model in the specific "draw with turtle
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

### G1 exception (unchanged)

- G1 gets exactly 1 attempt per item. No retries even through the
  错题集 (G1 has no memory to "improve" between attempts, so the
  errata concept doesn't apply).
- Fresh sub-agent per item — session context is discarded between
  items to prevent accidental "session memory."

### G4 curator role — split into two sub-agents

G4's curator does two logically distinct jobs. For efficiency and clean
responsibility separation, we run them as **two sub-agents**:

- **Diagnostician sub-agent** — reads attempt + GT + memory, uses the
  run_6-style structural check (stroke count, anchor placement, joint
  taxonomy) + panel-skeptic vision judgment to identify what went
  wrong. Emits a fix hypothesis.
- **Memory Writer sub-agent** — on human PASS, writes the mastered
  entry into the Success Bank with 米字格 anchors + P/T/N joint spec.

This split keeps each call focused; the Diagnostician has a well-defined
"find the bug" task, and the Writer has a well-defined "encode the
success" task.

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

- Curator split into **Diagnostician + Memory Writer** sub-agents.
- Three-bank memory using 米字格 anchors + P/T/N joint spec.
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
    ├── make_gt_300.py              ← ✓ 300×300 GT renderer
    ├── judge_blind.py              ← ✓ blind batch judgment UI (smoke-tested)
    ├── make_test_batch.py          ← ✓ generates smoke-test batch
    ├── run_group.py                ← TBD — main orchestrator
    ├── teacher.py                  ← TBD — curriculum position counter
    └── snapshot.py                 ← TBD — freeze/thaw memory
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

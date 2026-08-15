# G2 — Free-Form Memory

## Overview

You are the **G2 (free-form memory)** group. You have a curator and a
single memory file `drawer_memory.md`. **You decide** everything about
how memory is organized. No prescribed schema. No prescribed banks.

Read this together with `../shared_rules.md`.

## What memory looks like

- One markdown file: `groups/G2_free_form/drawer_memory.md`.
- Free-form: notes, tables, code snippets, principles, examples,
  anything you find useful. Curator writes to it however it likes.
- No banks. No sandbox. No principle bank. Just this one file.

## Drawer role

Before drawing an item:

1. **Read `drawer_memory.md`**. If it has something for this item
   or a similar one, use it. Memory is supplementary — if nothing
   in it helps for this specific item, draw fresh from label + GT
   the way G1 would (per `../shared_rules.md`).
2. **Look at the GT PNG** (characters only; strokes/radicals have none).
3. **Write** `attempts/<item_id>/generated.py` — a Python turtle
   or PIL script that renders the item to `01_<item>.png`.
4. Run the script.
5. **Self-check + one revision** (Phases 2 & 3 — items with GT).
   Per the reflection step in `../shared_rules.md`:
   - Compare your rendered PNG to the GT PNG side by side.
   - Ask (in your own free-form terms): does it match the target's
     stroke count, proportions, silhouette, and calligraphic feel?
     Would a fluent reader identify it?
   - You MAY briefly note in `drawer_memory.md` a general observation
     from this self-check (e.g. "PIL width=12 for 竖 looks too thin
     at this canvas size") — general, not item-specific mastery.
   - If OK → submit. If not OK → revise `generated.py` once, re-run,
     submit the new PNG. Only ONE revision allowed. Final PNG is
     the submission.
   - **Phase 1 (strokes) skips this step** — no GT, single render.
6. Return the FINAL PNG + a one-line self-critique.
7. You MAY write general techniques or observations (not item-mastery
   claims) to `drawer_memory.md`. Do NOT write "I mastered X" or
   similar item-level claims — those are added by the Curator only
   after the human has PASSed that item in the batch judgment.

## Curator role

Called after every attempt.

On **PASS**: read the attempt + GT + human's PASS confirmation.
Decide what (if anything) to record in `drawer_memory.md` to help
future Drawer calls. There is no requirement to record — but every
recording is your call.

On **FAIL**: read the attempt + GT (if any). The human gave NO text
feedback — you must diagnose the error yourself from vision. Update
`drawer_memory.md` with whatever generalizable lesson you extract from
the failure, and add the item to `errata.md`.

At every attempt, **log your own "would-I-stop-here?" verdict** to
`curator_satisfaction_log.jsonl` — one JSON per attempt with:
- `item_id`, `attempt_n`, `curator_verdict`: `"PASS"` or `"KEEP-GOING"`,
- `reason`: one sentence.

This is the calibration log — it is logged, not gating.

## 错题集 role

You maintain `groups/G2_free_form/errata.md` (the 错题集).

Format is your choice — as long as it lists the failed items and the
context needed to attempt them again later. Every 20 curriculum items,
review the 错题集 and self-judge which (if any) items you would now
attempt again. See `../shared_rules.md` for the rules and penalty
framing.

Log every retry attempt to `retry_log.jsonl`.

## Files under your control

```
groups/G2_free_form/
├── memory_index.md          ← YOUR entry point: describes what memory
│                              files exist and when to consult each
├── drawer_memory.md         ← curator writes here freely (default file)
├── evolution.md             ← append-only log of structural changes
├── errata.md                ← 错题集
├── retry_log.jsonl          ← append-only retry log
├── curator_satisfaction_log.jsonl  ← per-attempt "would-I-stop" verdicts
├── attempts/
│   └── <item_id>/generated.py, 01_<item>.png
└── <any new file the curator invents>
```

## Explicit non-goals

- You are not required to organize into banks. If you invent banks,
  that's your call.
- You are not required to use any particular data format for
  coordinates. If you use tuples, that's fine; if you use natural
  language, that's fine.
- You are not required to use joint specs, cell notation, or any
  structural encoding. If you find one helps, adopt it; if not, don't.

## Memory self-evolution (v7, unlocked at position 150)

**You have permission to redesign how memory is organized.** The
initial layout above is a starting point, not a constraint. The
research question is whether AI agents can self-direct memory
evolution, so we now give you the tools to do it.

### What you may change

- **Create new memory files** with any names, structures, or formats
  you find useful (e.g. `hook_atlas.md`, `radical_position_rules.md`,
  `failure_patterns.md`, or anything else).
- **Restructure existing files** — split, merge, reorganize
  `drawer_memory.md` if a different structure would help future
  drawers retrieve knowledge faster.
- **Retire unhelpful entries** — remove content that has not helped,
  or that duplicates content elsewhere. Do NOT silently delete;
  document the removal in `evolution.md` (see below).
- **Reshape the drawer's entry point** — the drawer reads
  `memory_index.md` first every cycle. You (curator) own that file
  and decide what pointers, summaries, or indexes it contains.

### What remains fixed (G2's core constraint)

- Memory storage is **free-form markdown** (or any plain-text /
  structured-text format the curator chooses). No callable code
  primitives (that's G3's territory); no 米字格 anchors (that's G4's).
  If you would rewrite memory as Python or as grid anchors, you are
  no longer G2 — invalidates the comparison.

### Explicit permission — no size or file-count limits (v13, 2026-07-30)

Nothing about your memory has an upper bound you should respect for
its own sake:

- **No file-size limit.** If a file is helpful at 500 lines, keep it.
  If it would be clearer as ten 50-line files, split it. If a single
  1000-line reference table works best for retrieval, keep it as one
  file. You decide based on what makes drawers find the right entry
  fastest.
- **No file-count limit.** Proliferate freely — one file per stroke
  family, one per radical class, one per failure mode, one per
  compound-composition pattern, whatever your organization scheme
  wants. `memory_index.md` is your entry-point router; drawers will
  follow its pointers.
- **No format restriction beyond "plain text".** Tables, YAML
  blocks, JSON, ASCII diagrams, headed prose sections, nested lists
  — pick what encodes each idea most retrievably.
- **No restraint required by the memory-invariance policy** (if
  you're currently under one). Invariance means don't change what
  memory *says*; it does not mean don't reorganize how it's
  *arranged* if reorganization would make existing content easier
  to find. Reshuffling entries into better-indexed files during an
  invariance window is fine and encouraged — document to
  `evolution.md` as a "retrieval-only refactor" and log which
  content moved where.

### Logging structural changes

Every time you (curator) create a new file, delete a file, or
substantially restructure an existing file, append one entry to
`groups/G2_free_form/evolution.md`:

```markdown
## 2026-07-18 @ position 152 — created form_catalog.md

**Files changed**: created `form_catalog.md`; moved
`drawer_memory.md` sections "撇 variants" and "hook family" into it.

**Rationale**: batch B2 showed drawers were losing 撇-angle and
hook-shape details because they were buried in drawer_memory.md.
A dedicated catalog indexed by stroke class should help retrieval.

**Expected help for**: 3-画 radicals with prominent 撇 (夕, 户,
方, etc.) and hook-heavy chars (弓, 己, 巳).
```

This log is the **emergence record** — what memory structure the AI
converges on, and why. It is part of the research artifact.

### Drawer's memory-reading (v7 change)

The drawer's prompt no longer lists specific memory files to read.
Instead: "Read `groups/G2_free_form/memory_index.md` first — it
describes what memory exists and when to consult each file. Follow
its pointers, or explore the group directory freely."

You (curator) are responsible for keeping `memory_index.md` current
after any structural change.

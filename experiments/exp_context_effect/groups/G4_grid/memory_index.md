# G4 memory index — entry point for the drawer

## v8 UPDATE (2026-07-25 @ position 350)

A free-form file `drawer_memory.md` was added at v8 unlock. **Read it
FIRST every cycle.** It contains: (a) mandatory import snippets for
chronic-cluster primitives (which had ~0 uses under v7 despite being
in the bank), (b) shortlist of high-value component primitives to
reuse, (c) compositional playbook for 3+-part characters, and (d)
per-batch failure notes.

Everything in the structured bank + principles + form_catalog +
joint_atlas is **REFERENCE ONLY** under v8. No hard mandate to call
or comply. If GT and memory disagree, trust GT — with the exception
that literal errata fixes on repeat items should be followed verbatim
(v7 chronic-cluster evidence).

*Maintained by the curator. Drawer reads `drawer_memory.md` first,
then this file, then follows pointers.*

## Core format constraint (fixed — do not violate)

G4's memory storage uses **米字格 anchors + P/T/N/S joint spec**:
- Every stroke endpoint is `(cell, x_frac, y_frac)` where cell is one
  of TL, TC, TR, ML, C, MR, BL, BC, BR.
- Every joint declares its class: **P** (piercing, welded crossing),
  **T** (tangent, tip touches body), **N** (neighbor, small natural
  gap — do NOT weld), **S** (same-stroke internal corner / separate).
- This is a STORAGE convention for bank entries. Drawer attempts may
  depart from it under v8 if the item needs it. See
  `../protocol/G4_grid/rules.md`.

The dispatcher auto-injects MMH-derived structural expectations for
every Phase-2/3 item into your prompt. That is separate from the
memory files below.

## Reading order for a new item (v8 slim checklist)

**Do these in order, BEFORE writing code. Log each with a one-line
comment at the top of `generated.py`.**

1. **`drawer_memory.md`** — read top-to-bottom. Contains the mandatory
   chronic-import snippets, the component-reuse shortlist, and the
   compositional playbook. Highest value per token; costs less than
   the full 6-file walk that saturated B6.
2. **`success_bank/INDEX.md` grep** — Ctrl-F the target character AND
   Ctrl-F each named sub-radical from the split you did in step 1.
   If a mastered item exists, IMPORT it (not just cite it).
3. **`errata.md` grep** — Ctrl-F the target. If listed, follow the fix
   idea LITERALLY. Soft-interpretation = 2× retry FAIL rate.

**Optional (only if steps 1–3 leave anchors uncertain):**
4. `principles_meta.md` — TR1-TR12 meta-rules.
5. `form_catalog.md` — stroke × context patterns.
6. `joint_atlas.md` — joint-class conventions.
7. `sandbox.md` — deep-scratch notes.

The v7 checklist enforced steps 1-6 as mandatory. Under v8, only steps
1-3 are mandatory; the deeper files are on-demand. Rationale: B6 had
6/16 retries STALL_DNC because full-checklist reading exceeded drawer
budget. Trim the mandatory path.

## Memory files (v8 layout)

| File                            | Purpose                                             |
|---------------------------------|-----------------------------------------------------|
| **`drawer_memory.md`**          | **NEW v8** — free-form prose entry point            |
| `success_bank/INDEX.md`         | Master list of mastered items                       |
| `success_bank/code/*.py`        | Per-item 米字格 anchors + joint spec                 |
| `success_bank/code/chronic/*.py`| **Canonical** hand-written primitives — call these  |
| `errata.md`                     | 错题集 — failed items + literal fix ideas            |
| `principles_meta.md`            | TR1-TR12 meta-cognitive transformation rules        |
| `form_catalog.md`               | Stroke × context anchor patterns (from PASSes)      |
| `joint_atlas.md`                | P/T/N/S joint conventions                           |
| `sandbox.md`                    | Free-form persistent scratch (heavy — on-demand)    |
| `principle_bank.md`             | STUB — kept for back-compat                         |
| `retry_log.jsonl`               | Append-only retry log                               |
| `curator_satisfaction_log.jsonl`| Per-attempt curator verdict (calibration only)      |
| `scans/`                        | Per-position errata scan decisions                  |
| `evolution.md`                  | Append-only log of memory structural changes        |

## When to consult what — quick lookup

- **Drawing any Phase-3 character**: (1) split into named sub-radicals,
  (2) IMPORT each sub-radical primitive from bank, (3) place per the
  compositional playbook in `drawer_memory.md`. Do not redraw
  sub-components from scratch when a mastered primitive exists.
- **Character contains 丿/刀/冂/弓/马**: import from `chronic/`.
  Comment-only mention is treated as mechanism failure in B7+.
- **Enclosing frame** (囗/门/冂/内-containing): `chronic/jiong_frame.py`.
- **Stroke count off** (e.g. 水 rendering as 3): assert count before
  rendering. See B6 note in `drawer_memory.md`.
- **Symmetry pair** (比/丱/从/双 = two copies of same sub-radical):
  compute anchors once, mirror via `(cell, 1 - x_frac, y_frac)`.

## Change history

See `evolution.md` for the append-only log of structural changes.

---

*v7 initial 2026-07-18. Position 200 added mandatory checklist. Position
250 evidence: checklist worked (18% → 100% citation). Position 300
promoted 5 chronic primitives. Position 350 v8 unlock: added
drawer_memory.md, slimmed mandatory checklist from 6 files → 3 files,
made bank/principles REFERENCE ONLY, granted prune + canonical-promotion
permissions.*

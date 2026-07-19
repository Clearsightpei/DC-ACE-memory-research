# G2 memory index — entry point for the drawer

*Maintained by the curator. Drawer reads this file first every cycle,
then follows the pointers below (or explores the group directory
freely if you need to find something not listed).*

## What memory G2 currently holds

- **`drawer_memory.md`** — the main free-form memory file. Contains:
  - Radical-composition principles (batches bootstrap, B1)
  - "Draw the flick" family of hook-shape rules
  - Length-ratio distinguishers for stacked-horizontal radicals
  - Topology overhang rules (人 vs 入 sibling pairs)
  - Multi-fold body-connection patterns
  - Stroke-direction and hook family reference material
  - Compound "turn" strokes reference
  - 折/弯 family shape rules
  - Batch mastery ledgers (which items PASSed per batch)

- **`errata.md`** — the 错题集. Failed items with per-item diagnosis,
  fix ideas, retry_n counter.

- **`scans/`** — per-position errata scan decisions (scan_position_050.md,
  scan_position_100.md, ...).

- **`retry_log.jsonl`** — append-only retry log.

- **`curator_satisfaction_log.jsonl`** — per-attempt "would-I-stop?"
  verdicts (calibration data, not gating).

- **`evolution.md`** — append-only log of any time the curator creates
  a new file, deletes one, or restructures. This lets us track how
  memory organization emerges over time.

## When to consult what

- **Drawing an unfamiliar radical**: read the "Radical-composition
  principles" section of `drawer_memory.md`. If your item has a hook,
  scan the "Draw the flick" and "Hook family" sections.
- **Drawing a stacked-horizontal item (士 vs 土, 干, etc.)**: check
  the "Length-ratio distinguishers" section.
- **Drawing a sibling pair (人 vs 入, similar shapes)**: check the
  "Topology overhang" section.
- **Wondering if this item has been attempted before**: grep the
  batch mastery ledgers at the bottom of `drawer_memory.md`.
- **You've drawn once and want to revise**: no dedicated file yet;
  compare your PNG to GT visually, note any observations to
  `drawer_memory.md`.

## Change history

See `evolution.md` for the append-only log of structural changes to
G2's memory organization.

---

*v7 initial version — created at position 150 as part of the memory
self-evolution unlock. Curator: update this index whenever you add,
remove, or restructure memory files.*

# Cycle 9 — Focus: 横折钩 (heng_zhe_gou, L-corner with hook)

Phase 2. Single-phase. Self-preview 2.

## What 横折钩 is

= 横折 (c7) + 钩 (the hook tail from c8). A complete enclosure-style corner stroke with hook. Used in 月, 力, 刀, 勺, 司, 习, 见, 风, 句, ...

## Canonical form (3 segments)

- **Seg A (heng arm):** (-100,+120) → (+100,+120). Same as 横折 heng. w 16→11→15.
- **Seg B (shu arm):** (+100,+120) → (+100,-100). Vertical drop. w 15→11→14 (pre-hook thicken).
- **Seg C (hook arm):** (+100,-100) → (+50,-60). Up-left hook. w 14→3.

## Reuse / composition

You can either:
(a) import 横折's `draw` and add a hook segment, OR
(b) build all three segments fresh.

Option (a) is cleaner (composes mastered code) — but 横折.draw doesn't expose the inner segment widths for the pre-hook thicken. So just inline three brushed_bezier calls. Both A and B follow §1.5 tangency rules; C is the hook.

On mastery → `success_bank/code/heng_zhe_gou.py`.

`attempts/cycle_9/generated.py` → `01_横折钩.png`. Marker `# ── Task 01 | 横折钩 | heng_zhe_gou`.

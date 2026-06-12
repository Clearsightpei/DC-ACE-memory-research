# Principle Bank (Part B of memory) — run_6

Curator-owned. General-purpose rules graduated from Sandbox observations after they prove themselves on real promotions.

run_6 starts with the architectural rules below. Per-stroke recipes (§1.1+) populate as atomic strokes are mastered c1–c6.

---

## §0 — How the Drawer works (run_6)

The Drawer is a fresh subagent dispatched once per cycle. It reads:
- The structural brief (anchors + joints from MMH).
- The GT PNG (visual reference).
- The Success Bank primitives.

It writes a turtle script whose top-level `draw_<primitive>()` calls match the MMH stroke count exactly, and whose endpoints land within tolerances of the declared anchors.

`tools/` is quarantined during the Drawer's turn. Anchor translation lives in `success_bank/code/_anchor.py` (a copy of the main utility, dropped in by the orchestrator so the Drawer can use it without the joint detector).

## §0.1 — The 5-gate

To promote: structural_pass AND judge_panel.unanimous_yes. Numerical OCR + visual_score logged but not gated on.

## §1 — Brushwork primitives

(Populated as atomic strokes master in c1–c6. Each entry will include its width profile, canonical anchors, and brushwork rules.)

## §2 — Composition rules

### §2.1 — Anchor reuse (declared, not derived)

Every Success Bank entry's `draw()` function takes the same interface: `(t, ox=0, oy=0, scale=1.0)`. The body translates declared anchors to turtle math-coords via `anchor_to_xy(...)` and computes the primitive's `(ox, oy, scale)` so its rendered endpoints land on the anchors. **No magic numbers in entry bodies.**

For character entries that compose multiple primitives, the entry's docstring lists every anchor and every joint, sourced from the Teacher's brief at promotion time.

### §2.2+ — character-composition rules

(Populated as patterns emerge.)

## §3 — Operating notes

- **One MMH stroke = one primitive call.** Compound strokes (横折钩 etc.) are ONE call. Drawer's stroke-count gate enforces this mechanically.
- **The brief's anchors are ground truth.** Do not silently override them; if they seem wrong, log it in `sandbox.md` and let the Curator handle.
- **Foundation must be perfect.** Atomic strokes c1–c6 propagate into every later character; flawed atoms infect compounds.

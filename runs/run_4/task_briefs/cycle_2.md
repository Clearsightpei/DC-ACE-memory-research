# Cycle 2 — Focus: 竖 (shu, vertical stroke)

## Phase
1 — atomic strokes. **Single-phase** (no GT, eval=vision).

## Prerequisites
None (atomic).

## What 竖 is

A vertical stroke (shu). The second-most-common Chinese brush primitive,
after 横. Appears in 十, 丨, 工, 王, 中, 山, 川, 木, 林, and as the
central trunk of countless characters.

Canonical 楷书 form:
- **Direction:** top to bottom.
- **Length:** comparable to 横's length, but vertical — about 400 px.
- **Center x:** typically at the canvas origin (0, 0).
- **Tilt:** essentially vertical — no lean.
- **Brushwork:**
  - Weighted entry at the TOP (the brush pressing in as it touches down).
  - Slightly thinner shaft through the middle.
  - Weighted closing press at the BOTTOM (the 收笔), often the heaviest point.
  - There are two stylistic variants:
    - **悬针竖** (suspended needle): tapers to a fine point at the bottom — used in lone 竖 (e.g. 中's 竖, the single 竖 in 十). For run_4, prefer **垂露竖** (hanging dew): rounded/weighted bottom press — more universally reusable inside compound characters.
  - We'll teach the **垂露 (rounded bottom)** version here. The 悬针 variant can be a separate Success Bank entry later if needed.
- **Curvature:** essentially straight.

## Suggested numeric targets
- Start (top): ~(0, +200).
- End (bottom): ~(0, -200).
- Peak pensize: 16–18 at top entry, similar at bottom press.
- Shaft pensize: 10–12 (≥ 50% of peak).
- Symmetric "barbell" profile: peak-shaft-peak.

## Reuse the existing Principle Bank

`principle_bank.md` §1.0 has the universal brushwork rules and the
`brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)` helper.
You can either inline it again or import from `success_bank/code/heng.py`
(which already exports `brushed_bezier`). Importing is preferred — that
reuses the mastered helper.

## Eval
`eval: "vision"`, `use_ocr: false`. Mastery: rubric ≥ 7 with no criterion = 0.

## Self-preview budget
2 internal iterations.

## File outputs
- `attempts/cycle_2/generated.py`
- `attempts/cycle_2/01_竖.png`

Marker: `# ── Task 01 | 竖 | shu`

On mastery, the Curator will add `success_bank/code/shu.py` (tag:atomic-stroke tag:shu tag:垂露竖).

# Cycle 5 — Focus: 提 (ti, upward flick)

## Phase 1, single-phase (eval=vision).

## What 提 is

A short stroke that flicks UP-AND-RIGHT from a weighted base in the
lower-left. Tapered tip, like 撇's tail. Used at the bottom-left of
many radicals (e.g. 习 习, the left of 河, 江, 沙, ...) and as the
final stroke of 习.

Canonical form:
- **Direction:** lower-left (heavy base) → upper-right (fine point).
- **Length:** shorter than 撇/捺 — about 250 px.
- **Brushwork:**
  - **Weighted base** at lower-left (peak 14).
  - **Shaft** narrows progressively.
  - **Fine taper to point** at upper-right (pensize 3 floor).
- **Curvature:** essentially straight or with a very gentle bow.
  Smaller curvature than 撇.

## Suggested numeric targets
- Base (head): (-100, -80).
- Tip (tail): (+150, +60).
- Peak pensize 14 at base; shaft 11→9; tail 3.

## Reuse
`from heng import brushed_bezier`. The width profile pattern is the
**same family as 撇** (heavy head → taper to point), but with smaller
peak (14 vs 18) and shorter length.

## Eval
`vision`, mastery rubric ≥7 no 0. Self-preview budget 2.

## Output
`attempts/cycle_5/generated.py` → `01_提.png`. Marker `# ── Task 01 | 提 | ti`.

On mastery → `success_bank/code/ti.py` (tag:atomic-stroke tag:提 tag:tapered-tip).

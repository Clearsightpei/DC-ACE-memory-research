# Cycle 10 — Focus: 竖弯钩 (shu_wan_gou)

Phase 2 compound. Single-phase. Self-preview 2.

## What 竖弯钩 is

Vertical drop → smooth quarter-circle curve to the right → small upward hook (上钩). The bottom stroke of 也, 已, 巴, 七, 元, 见, 元, ...

## Form (3 segments via §1.5)

- **Seg A (vertical drop):** (0,+150) → (0,-100). w 16→11.
- **Seg B (curve to right):** Quarter-arc from (0,-100) → (+150,-150). Concave-up — this is a single Bézier with control points placed to make a smooth curve. w 11→13 (slight thicken in the curve).
- **Seg C (up hook):** (+150,-150) → (+200,-100). w 13→3 (taper). Hook goes up-right.

For Seg B's arc, controls B1=(0,-150), B2=(+100,-150) work well — pulls the curve down-right then sweeps right.

## Reuse
`from heng import brushed_bezier`.

On mastery → `success_bank/code/shu_wan_gou.py`.

`attempts/cycle_10/generated.py` → `01_竖弯钩.png`. Marker `# ── Task 01 | 竖弯钩 | shu_wan_gou`.

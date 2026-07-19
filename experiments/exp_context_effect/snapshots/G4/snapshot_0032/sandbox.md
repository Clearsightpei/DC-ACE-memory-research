# Sandbox (G4 grid-bank) — free-form persistent notes

Sandbox reset with Phase-2 restart. Persistent free-form memory.

## Carry-over observations (Phase-1 → Phase-2, applies to any GT-supported drawing)

- **Anchor-plan comments before code.** Writing the anchor plan as a
  comment block (each stroke's head/tail cells + fracs + width, plus
  joint class per pivot) before touching primitive calls catches
  mismatches early. Same discipline applies whether the target is a
  standalone stroke, a radical, or a full character.
- **Assert direction invariants immediately after anchor→pixel
  conversion.** One-line asserts (`assert p_hook.x > p_corner.x`,
  `assert p_tip.y < p_flick_start.y`, etc.) turn silent geometry bugs
  into loud failures. Cheap in code, expensive if omitted.
- **Prefer raw belly as Bezier control** unless the shape genuinely
  requires the curve to pass THROUGH the belly point. The
  `2*belly - midpoint` derivation is fragile when belly and chord
  midpoint diverge and can throw the control point off-canvas.

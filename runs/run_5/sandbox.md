# Sandbox (Part C of memory) — run_5

Curator-owned. Short-term scratch space for whatever is currently
being worked on. Resets when a focus is mastered.

---

## Cycle 3 task 3 — 下 — CARRY OVER

**Vision identity verdict**: ambiguous — reads as "十 with an extra dot" rather than unambiguous 下. OCR confirms: returned 十, not 下.

**Reads as**: 十 with a small diagonal dot on the right side. The structural error is that the **竖 starts ABOVE the top 横 instead of starting AT or just below it**. In proper 下, the 竖 hangs straight down from the heng without poking above; the top heng IS the cap of the character.

**What's missing**: the structural rule. 下 = 横 (top, long) + 竖 (hanging straight down from the heng's middle, NOT crossing through) + 点 (right of the 竖).

**Specific next-attempt direction**:
- Top 横: `draw_heng(d, ox=0, oy=+80, length=330, scale=1.0)` (unchanged — looked good).
- 竖: `draw_shu(d, ox=0, oy_top=+70, length=240, scale=1.0)` — note `oy_top=+70` (10 below the heng's centerline at +80) so the 竖's top-hook sits AT or just below the heng, not above. The 竖 then extends 240px downward.
- 点: small diagonal teardrop to the right of the 竖, anchored at ~(+50, +25). Keep the c3 `draw_dian` style — it read as a 点 clearly.

The structural lesson: when a 竖 sits BELOW a heng (as in 下), its top-hook must not pierce above the heng. When a 竖 crosses through a heng (as in 十), it does pierce above. Same primitive, different `oy_top` choice.

## Generalizable finding (draft, not yet promoted)

**Composition rule — when 竖 sits BELOW a 横 (hanging stroke)**:
- the 竖's top entry-press must be at or below the 横's centerline
- the 竖 must NOT visibly extend above the 横

vs.

**When 竖 crosses through a 横 (intersecting stroke)** (e.g. 十, 千, 干):
- the 竖's top entry-press can be 50–100px above the 横's centerline
- the 竖 should visibly poke above the 横

These two patterns are distinguished only by `oy_top` choice when calling `draw_shu`. If the Drawer treats them identically, characters like 下 collapse into 十-with-dot.

Promote to Principle Bank §2.2 if the next 下 attempt verifies the rule works.

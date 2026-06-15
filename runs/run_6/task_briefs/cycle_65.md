# Cycle 65 — Focus: 力

## Phase
2

## Carry-over from cycle 55 (3rd attempt — last chance before 3-attempt freeze)

Previous attempts:
- c33 (raw MMH, 0/3): pie crossing height + invisible hook.
- c44 (joint-snapped, 0/3): mid-joint snap didn't fire; same as c33.
- c55 (pie lifted slightly down to heng level, 0/3): pie too short → reads as 撇 wrong direction.

**Strategy this attempt**: revert to RAW MMH anchors per to_be_learned note. The
pie SHOULD exceed the box (canonical 力 has a long pie). Joint is P-class
(piercing, d=0.0 from MMH) — the heng_zhe_gou is crossed by pie at mid.
Brief panel that 力's pie is canonically long.

## MMH stroke count
2 (Drawer's turtle-call count must equal this)

## Strokes
1. heng_zhe_gou(from=("ML", 0.364, 0.464), corner=("C", 0.444, 0.464), to=("BC", 0.444, 0.996))
2. pie(from=("TC", 0.364, 0.368), to=("BL", -0.04, 1.336))

## Joints (classified via tools/classify_joints)
- s1.mid(0.23) ⇆ s2.mid(0.30) @ C : P (piercing — pie crosses through heng_zhe_gou's heng segment, welded by brush sampling)

## Internal corners (find_corners — informational)
- s1 @ C (heng_zhe_gou bend — welded by primitive)

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_65/generated.py and attempts/cycle_65/01_力.png

# Cycle 67 — Focus: 个

## Phase
2

## Carry-over from cycle 58 (3rd attempt — last chance before 3-attempt freeze)

c58 panel 1/3: 3-way apex_share applied (all 3 stroke heads at TC y_frac 0.348) but shu's dunbi head blob still appeared detached from the pie/na apex meeting point.

**Strategy this attempt**: lift shu.head.y by ~20 px ABOVE the pie/na apex so the shu's dunbi blob *lands AT* the apex (rather than starting below it). y_frac 0.248 in TC (= 0.348 minus 20 px / 200 px per cell).

## MMH stroke count
3 (Drawer's turtle-call count must equal this)

## Strokes (raw MMH + apex_share override + shu_apex_lift)
1. pie(from=("TC", 0.364, 0.348), to=("BL", -0.084, 0.296))      # raw MMH after apex_share lifted pie.head.y to max(pie,na)
2. na(from=("TC", 0.54, 0.348), to=("MR", 1.3, 0.996))            # raw MMH after apex_share
3. shu(from=("TC", 0.368, 0.248), to=("BC", 0.512, 1.3))          # APEX_LIFT — shu.head.y_frac lifted from 0.348 → 0.248 (~20 px above apex) so dunbi blob lands AT apex

## Joints (classified via tools/classify_joints)
- s1.mid(0.20) ⇆ s2.head @ TC : N (d=44.6, expect ~18 px gap — pie/na apex contact)

## Overrides
- apex_share_pie_na: s1.from.y_frac = s2.from.y_frac = 0.348 (both at TC band, sharing apex y)
- shu_apex_lift: s3.from.y_frac = 0.248 (lift shu.head ~20 px ABOVE apex so dunbi blob lands AT apex)

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_67/generated.py and attempts/cycle_67/01_个.png

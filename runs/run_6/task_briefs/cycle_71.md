# Cycle 71 — Focus: 明

## Phase
2 (8-stroke ramp continued)

## MMH stroke count
8 (日 left + 月 right = 4 + 4)

## Composition
明 = 日 (left half, s1-s4) + 月 (right half, s5-s8).

## Strokes (raw MMH)
1. shu(from=("TL", 0.06, 0.732), to=("BL", 0.176, 0.468))                       # 日 left wall
2. heng_zhe(from=("TL", 0.256, 0.756), corner=("BC", 0.976, 0.756), to=("BL", 0.976, 0.444))  # 日 top + right wall
3. heng(from=("ML", 0.312, 0.544), to=("ML", 0.716, 0.46))                      # 日 internal middle heng
4. heng(from=("BL", 0.3, 0.232), to=("BL", 0.836, 0.112))                       # 日 closing bottom heng
5. pie(from=("TC", 0.596, 0.46), to=("BL", 0.704, 1.3))                         # 月 left-side pie (clamped y 1.56→1.3)
6. heng_zhe_gou(from=("TC", 0.924, 0.628), corner=("BC", 0.92, 0.628), to=("BR", 0.148, 1.116))  # 月 top+right with hook
7. heng(from=("C", 0.876, 0.316), to=("MR", 0.428, 0.224))                      # 月 internal upper heng
8. heng(from=("BC", 0.796, 0.048), to=("MR", 0.444, 0.96))                      # 月 internal lower heng

## Joints
- All N-class (small ~13-30 px gaps at intersections — correct calligraphy)

## Overrides
- pie_clamp: s5.to.y_frac 1.56→1.3 (in canvas)

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_71/generated.py and attempts/cycle_71/01_明.png

# Cycle 72 — Focus: 明 (retry from c71)

## Phase
2

## Carry-over from cycle 71

c71 brief-bug: heng_zhe corner placed in BC cell — dropped 日's right wall to bottom. **Fix**: corner cell = same row as head, same column as tail. For 日: corner = same TL row, tail's x_frac.

## MMH stroke count
8 (日 + 月)

## Strokes (raw MMH + corrected corners)
1. shu(from=("TL", 0.06, 0.732), to=("BL", 0.176, 0.468))                              # 日 left wall
2. heng_zhe(from=("TL", 0.256, 0.756), corner=("TL", 0.976, 0.756), to=("BL", 0.976, 0.444))  # CORRECTED corner: TL (same row as head), x_frac=tail's
3. heng(from=("ML", 0.312, 0.544), to=("ML", 0.716, 0.46))                             # 日 internal middle heng
4. heng(from=("BL", 0.3, 0.232), to=("BL", 0.836, 0.112))                              # 日 closing bottom heng
5. pie(from=("TC", 0.596, 0.46), to=("BL", 0.704, 1.3))                                # 月 left-side pie
6. heng_zhe_gou(from=("TC", 0.924, 0.628), corner=("TR", 0.148, 0.628), to=("BR", 0.148, 1.116))  # CORRECTED: TR (same row as head TC, x_frac=tail's)
7. heng(from=("C", 0.876, 0.316), to=("MR", 0.428, 0.224))                             # 月 internal upper heng
8. heng(from=("BC", 0.796, 0.048), to=("MR", 0.444, 0.96))                             # 月 internal lower heng

## Overrides
- pie_clamp: s5.to.y_frac 1.56→1.3.

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_72/generated.py and attempts/cycle_72/01_明.png

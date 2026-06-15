# Cycle 69 — Focus: 米

## Phase
2

## Carry-over from cycle 61 (3rd attempt — last chance before 3-attempt freeze)

c61 panel 1/3: top dots lowered closer to heng (OK), but the lower pie (s5) and na (s6) extend too far past the box.

**Strategy this attempt**: shorten s5.tail and s6.tail x-extent so they don't protrude past character body.

## MMH stroke count
6

## Strokes
1. dian(from=("TL", 0.528, 0.896), to=("ML", 0.964, 0.292))            # left top dot
2. dian(from=("TR", 0.228, 0.544), to=("C", 0.812, 0.212))             # right top dot
3. heng(from=("ML", 0.108, 0.808), to=("MR", 0.744, 0.608))            # middle heng
4. shu(from=("TC", 0.264, 0.232), to=("BC", 0.384, 1.4))               # vertical shu (slightly clamped from MMH 1.728 → 1.4 to stay in canvas)
5. pie(from=("C", 0.336, 0.848), to=("BL", 0.20, 1.0))                 # SHORTENED — tail x_frac -0.06 → 0.20, y_frac 1.232 → 1.0 (less protrusion)
6. na(from=("C", 0.548, 0.824), to=("BR", 0.80, 1.0))                  # SHORTENED — tail x_frac 1.268 → 0.80

## Joints
- All N-class around center (5 strokes meeting near C cell)

## Overrides
- pie_na_clamp: s5 and s6 tails brought in toward character body (don't protrude past box edges).
- shu_clamp: s4 to.y_frac 1.728 → 1.4 (in-canvas).

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_69/generated.py and attempts/cycle_69/01_米.png

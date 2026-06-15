# Cycle 73 — Focus: 国

## Phase
2

## MMH stroke count
8

## Structure
国 = 囗 (outer box, s1-s2 + s8) + 玉 (inside, s3 s4 s5 s6 s7).
- s1 shu (left wall)
- s2 heng_zhe (top + right wall) [programmatic corner = TR]
- s3 heng (玉 upper internal)
- s4 heng (玉 middle internal)
- s5 shu (玉 vertical)
- s6 heng (玉 below middle)
- s7 dian (small dot)
- s8 heng (closing bottom of 囗)

## Strokes
1. shu(from=("TL", 0.316, 0.568), to=("BL", 0.348, 1.3))                                    # clamped from 1.448
2. heng_zhe(from=("TL", 0.616, 0.812), corner=("TR", 0.744, 0.812), to=("BR", 0.744, 1.3))  # clamped from 1.544
3. heng(from=("ML", 0.928, 0.288), to=("MR", 0.104, 0.152))
4. heng(from=("ML", 0.888, 0.988), to=("MR", 0.024, 0.912))
5. shu(from=("C", 0.364, 0.364), to=("BC", 0.408, 0.532))
6. heng(from=("BL", 0.724, 0.716), to=("BR", 0.304, 0.624))
7. dian(from=("BR", 0.08, 0.048), to=("BR", 0.432, 0.34))
8. heng(from=("BL", 0.48, 1.3), to=("BR", 0.54, 1.156))                                     # clamped from 1.348

## Overrides
- y_clamp on s1, s2, s8 (MMH out-of-range)

## Eval
vision+ocr+gt+structural

## Self-preview budget
1 self-iteration (2-attempt rule).

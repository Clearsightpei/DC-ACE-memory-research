# Cycle 74 — Focus: 果

## Phase
2

## MMH stroke count
8

## Structure
果 = 田 (s1-s5: box with cross) + 木 (s6 shu + s7 pie + s8 na).
- s1, s2: top corners of 田 (small slanted strokes — render as pie/dian)
- s3: 田's right wall (heng_zhe down)
- s4: 田's internal horizontal
- s5: 田's bottom heng
- s6: 木 vertical (long shu)
- s7: 木 pie (sweeping down-left to BL)
- s8: 木 na (sweeping down-right to BR)

## Strokes
1. shu(from=("TL", 0.48, 0.532), to=("ML", 0.856, 0.632))
2. heng_zhe(from=("TL", 0.604, 0.508), corner=("TC", 0.9, 0.508), to=("C", 0.9, 0.44))
3. heng(from=("ML", 0.94, 0.056), to=("TC", 0.784, 0.944))
4. heng(from=("ML", 0.936, 0.54), to=("C", 0.856, 0.356))
5. heng(from=("BL", 0.068, 0.076), to=("MR", 0.808, 0.936))
6. shu(from=("TC", 0.316, 0.576), to=("BC", 0.412, 1.3))
7. pie(from=("BC", 0.296, 0.064), to=("BL", -0.032, 1.256))
8. na(from=("BC", 0.536, 0.048), to=("BR", 1.272, 1.188))

## Overrides
- shu_clamp on s6: 1.66→1.3.

## Eval
vision+ocr+gt+structural

## Self-preview budget
1 self-iteration (2-attempt rule).

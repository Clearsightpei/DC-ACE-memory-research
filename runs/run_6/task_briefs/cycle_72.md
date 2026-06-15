# Cycle 72 — Focus: 京 (re-verify after demotion)

## Phase
2

## MMH stroke count
8

## Structure
京 = 亠 (s1 dot + s2 long top heng) + 口 (s3 shu + s4 heng_zhe + s5 heng) + 小 (s6 shu + s7 pie + s8 na).

## Strokes (raw MMH + programmatic heng_zhe corner)
1. dian(from=("TC", 0.224, 0.156), to=("TC", 0.684, 0.492))                       # top dot
2. heng(from=("ML", -0.036, 0.028), to=("TR", 1.124, 0.844))                      # long top heng
3. shu(from=("ML", 0.724, 0.432), to=("BC", 0.064, 0.224))                        # 口 left vertical
4. heng_zhe(from=("ML", 0.808, 0.408), corner=("C", 0.91, 0.41), to=("C", 0.908, 0.884))  # 口 top + right (corner programmatic)
5. heng(from=("BC", 0.132, 0.144), to=("BR", 0.128, 0.028))                       # 口 bottom (and top of 小)
6. shu(from=("BC", 0.392, 0.148), to=("BC", 0.036, 1.284))                        # 小 vertical
7. pie(from=("BL", 0.668, 0.484), to=("BL", 0.276, 1.176))                        # 小 left
8. na(from=("BR", 0.044, 0.484), to=("BR", 0.74, 1.192))                          # 小 right

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 1 self-iteration (2-attempt rule total).

## Output
attempts/cycle_72/generated.py and attempts/cycle_72/01_京.png

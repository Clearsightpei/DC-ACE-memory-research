# Cycle 70 — Focus: 林

## Phase
2 (first 8-stroke char of curriculum ramp)

## MMH stroke count
8

## Composition
林 = 木 (left) + 木 (right). Two identical components, left-right symmetric. Component 木 is in success bank (mu.py) but we derive both 木s directly from MMH for this brief.

## Strokes (raw MMH)
1. heng(from=("ML", -0.112, 0.588), to=("C", 0.168, 0.408))           # left-木 top heng
2. shu(from=("TL", 0.504, 0.38), to=("BL", 0.588, 1.456))             # left-木 shu (vertical)
3. pie(from=("ML", 0.568, 0.636), to=("BL", -0.288, 0.964))           # left-木 pie
4. na(from=("ML", 0.764, 0.9), to=("BC", 0.048, 0.144))               # left-木 na
5. heng(from=("C", 0.376, 0.432), to=("MR", 0.792, 0.204))            # right-木 top heng
6. shu(from=("TC", 0.808, 0.232), to=("BC", 0.928, 1.456))            # right-木 shu (clamped from MMH 1.616 to in-canvas)
7. pie(from=("C", 0.876, 0.516), to=("BC", 0.012, 0.82))              # right-木 pie
8. na(from=("MR", 0.096, 0.648), to=("BR", 1.392, 0.728))             # right-木 na

## Joints (classified — abbreviated)
- s1.mid(0.61) ⇆ s2.mid(0.38) @ ML : P (piercing — left-木's heng crosses shu)
- s5.mid(0.44) ⇆ s6.mid(0.35) @ MR : P (piercing — right-木's heng crosses shu)
- Multiple N-class joints among pie/na intersections (correct calligraphy gaps)

## Overrides
- shu_clamp: s6.to.y_frac 1.616 → 1.456 (keep in canvas)

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_70/generated.py and attempts/cycle_70/01_林.png

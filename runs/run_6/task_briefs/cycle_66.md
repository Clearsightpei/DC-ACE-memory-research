# Cycle 66 — Focus: 自

## Phase
2

## Carry-over from cycle 57 (3rd attempt — last chance before 3-attempt freeze)

c57 panel: 2/3 YES. The 1 NO complained about "3 internal hengs" instead of 2 — counting ambiguity, not a structural defect (MMH genuinely has s4 + s5 as 2 internal hengs PLUS s6 as the box-closing bottom heng = 3 horizontal-looking strokes total).

**Strategy this attempt**: same anchors as c57 (they were close), but the panel prompt explicitly clarifies that the bottom heng (s6) IS the closing-bottom of the 日-box, NOT a 3rd internal heng. The 2 internal hengs (s4, s5) should be clearly inside the box, distinct from the bottom edge.

## MMH stroke count
6 (Drawer's turtle-call count must equal this)

## Strokes
1. pie(from=("TC", 0.308, 0.224), to=("ML", 0.664, 0.016))
2. shu(from=("ML", 0.664, 0.016), to=("BL", 0.764, 1.252))
3. heng_zhe(from=("ML", 0.92, 0.112), corner=("C", 0.96, 0.112), to=("BC", 0.96, 1.132))
4. heng(from=("ML", 0.912, 0.864), to=("C", 0.96, 0.704))    # upper internal heng
5. heng(from=("BL", 0.912, 0.46), to=("BC", 0.96, 0.332))    # lower internal heng
6. heng(from=("BL", 0.868, 1.176), to=("BR", 0.048, 1.048))  # bottom-of-box closing heng

## Joints (classified via tools/classify_joints)
- s1.tail ⇆ s2.head @ ML : N (d=76.7, expect ~31 px natural gap — pie meets shu top-left, small gap is correct)
- s1.tail ⇆ s3.head @ C  : N (d=31.4, ~13 px gap)
- s2.head ⇆ s3.head @ ML : N (d=36.1, ~14 px gap — top-left corner of box)
- s2.mid(0.43) ⇆ s4.head @ ML : N (d=35.2, ~14 px — upper internal heng meets left vertical)
- s2.mid(0.65) ⇆ s5.head @ BL : N (d=30.0, ~12 px — lower internal heng meets left vertical)
- s2.tail ⇆ s6.head @ BL : N (d=32.2, ~13 px — bottom-left corner of box)
- s3.tail ⇆ s6.mid(0.82) @ BC : N (d=43.8, ~18 px — bottom-right area of box)

## Internal corners (find_corners — informational)
- s3 @ C (heng_zhe top-right corner — welded by primitive)

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_66/generated.py and attempts/cycle_66/01_自.png

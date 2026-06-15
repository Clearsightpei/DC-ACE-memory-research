# Cycle 68 — Focus: 古

## Phase
2

## Carry-over from cycle 60 (3rd attempt — last chance before 3-attempt freeze)

c60 panel 0/3: 十's shu (s2) pierced through the box (口) top. Box anchors from MMH differed from the mastered 口's anchors and box looked malformed.

**Strategy this attempt**: shorten s2 (shu) so it terminates ABOVE the box-top heng (s3 head). Keep MMH-derived box anchors but with a calligraphy-aware panel that accepts small N-class gaps at the box corners.

## MMH stroke count
5

## Strokes
1. heng(from=("ML", -0.044, 0.56), to=("MR", 1.184, 0.472))            # top heng of 十
2. shu(from=("TC", 0.372, 0.28), to=("BC", 0.26, 0.20))                # SHORTENED — tail.y_frac 0.352 → 0.20 so shu stops above box top
3. heng_zhe(from=("BL", 0.6, 0.42), corner=("BC", 0.968, 0.42), to=("BL", 0.968, 1.464))    # left wall + top of 口 (heng_zhe interpretation)
4. shu(from=("BL", 0.892, 0.444), to=("BC", 0.944, 1.072))             # right wall of 口
5. heng(from=("BC", 0.048, 1.232), to=("BR", 0.22, 1.24))              # bottom of 口

## Joints (classified via tools/classify_joints) — recomputed from MMH

(See classify_joints output; key joints are all N-class corners of the box, plus shu-to-heng tangent at top.)

## Overrides
- shu_lift_above_box: s2.to.y_frac changed from MMH 0.352 → 0.20 in BC, so shu ends clearly above the box top.

## Eval
vision+ocr+gt+structural

## Self-preview budget
Max 2 iterations.

## Output
attempts/cycle_68/generated.py and attempts/cycle_68/01_古.png

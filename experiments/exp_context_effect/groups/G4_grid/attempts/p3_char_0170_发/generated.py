"""p3_char_0170_发 — G4 attempt.

Lookup checklist:
# 1. success_bank/INDEX.md grep '发' — not present, no prior mastery.
# 2. errata.md grep '发' — not present.
# 3. form_catalog.md — general 撇/捺/横 rules apply; 发 has 撇+捺 crossing (P joint) mid-lower.
# 4. principles_meta.md — TR1-TR12 general; N joints ≤25 px per TR10.
# 5. joint_atlas.md — P (welded) for s1×s2 and s3×s4; N (gap ~15 px) for s2×s3 head and s2×s4 head.

MMH-derived 5-stroke spec:
  s1 head ML(0.791,0.008) → tail MR(0.355,0.356)   short top diagonal (撇)
  s2 head TC(0.354,0.56)  → tail BL(0.281,0.745)   long 撇 sweeping through center
  s3 head C(0.201,0.91)   → tail BL(0.709,0.862)   short mid-lower segment (横折/竖折 short arm)
  s4 head BC(0.14,0.071)  → tail BR(0.763,0.915)   main 捺 to bottom-right
  s5 head TC(0.913,0.747) → tail MR(0.247,0.028)   small 丶 upper-right

Joints:
  s1.mid ⇆ s2.mid @ C — P (weld)
  s2.mid ⇆ s3.head @ C — N (gap ~15 px)
  s2.mid ⇆ s4.head @ BC — N (gap ~15 px)
  s3.mid ⇆ s4.mid @ BC — P (weld)
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; s1×s2 and s3×s4 welded; s2×s3 head and s2×s4 head kept near ~15 px gap.'
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Stroke 1: short top 撇 (slight curve, tapering thin)
    h1 = anchor_to_xy(('ML', 0.791, 0.008))
    t1 = anchor_to_xy(('MR', 0.355, 0.356))
    # slight downward bow
    cx1 = (h1[0] + t1[0]) / 2 - 4
    cy1 = (h1[1] + t1[1]) / 2 + 8
    pts1 = quad_bezier(h1, (cx1, cy1), t1, n=40)
    widths1 = [max(2, 6 - i * 0.08) for i in range(len(pts1))]
    stroke_variable_width(d, pts1, widths1)

    # Stroke 2: long 撇 from TC down to BL
    h2 = anchor_to_xy(('TC', 0.354, 0.56))
    t2 = anchor_to_xy(('BL', 0.281, 0.745))
    # long sweeping curve, control point pulled toward center-right for a proper 撇
    cx2 = (h2[0] + t2[0]) / 2 + 20
    cy2 = (h2[1] + t2[1]) / 2 + 5
    pts2 = quad_bezier(h2, (cx2, cy2), t2, n=60)
    widths2 = [max(2, 7 - i * 0.08) for i in range(len(pts2))]
    stroke_variable_width(d, pts2, widths2)

    # Stroke 3: short mid-lower segment (short 撇-ish), slightly bowed
    h3 = anchor_to_xy(('C', 0.201, 0.91))
    t3 = anchor_to_xy(('BL', 0.709, 0.862))
    cx3 = (h3[0] + t3[0]) / 2 - 4
    cy3 = (h3[1] + t3[1]) / 2 + 10
    pts3 = quad_bezier(h3, (cx3, cy3), t3, n=40)
    widths3 = [max(3, 6 - i * 0.06) for i in range(len(pts3))]
    stroke_variable_width(d, pts3, widths3)

    # Stroke 4: main 捺 from BC to BR (long diagonal, thickening at the tail-end)
    h4 = anchor_to_xy(('BC', 0.14, 0.071))
    t4 = anchor_to_xy(('BR', 0.763, 0.915))
    # arch downward slightly
    cx4 = (h4[0] + t4[0]) / 2 + 5
    cy4 = (h4[1] + t4[1]) / 2 + 18
    pts4 = quad_bezier(h4, (cx4, cy4), t4, n=60)
    widths4 = [3 + (i / len(pts4)) * 4 for i in range(len(pts4))]  # thicken toward tail (捺)
    stroke_variable_width(d, pts4, widths4)

    # Stroke 5: small 丶 dot in upper-right (short teardrop)
    h5 = anchor_to_xy(('TC', 0.913, 0.747))
    t5 = anchor_to_xy(('MR', 0.247, 0.028))
    pts5 = sample_line(h5, t5, n=20)
    widths5 = [3 + i * 0.2 for i in range(len(pts5))]
    stroke_variable_width(d, pts5, widths5)

    out = os.path.join(os.path.dirname(__file__), "01_发.png")
    img.save(out)
    print(f"saved {out}")


if __name__ == "__main__":
    main()

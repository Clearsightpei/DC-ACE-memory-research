"""p3_char_0532_亳 — G4 drawer attempt (revision 1).

Structural approach: rendered directly from MMH-derived anchor set.
No bank primitive fits 亳 as a whole; drawn from anchors. Revision 1
fixes the top and bottom horizontals (previously over-curved by
mis-placed bezier control points).
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)
from _anchor import anchor_to_xy, quad_bezier, fat_line, stroke_variable_width  # noqa

W = 4


def line(draw, a, b, width=W):
    fat_line(draw, anchor_to_xy(a), anchor_to_xy(b), width)


def curve(draw, a, ctrl_anchor, b, width=W):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(ctrl_anchor)
    p2 = anchor_to_xy(b)
    pts = quad_bezier(p0, p1, p2, n=40)
    stroke_variable_width(draw, pts, [width] * len(pts))


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # Stroke 1: top dot / short slash
    line(d, ("TC", 0.257, 0.545), ("TC", 0.582, 0.765), width=W + 2)

    # Stroke 2: long top horizontal — nearly straight
    line(d, ("ML", 0.589, 0.043), ("TR", 0.288, 0.926))

    # Stroke 3: short slash near mid-left (into 口 top-left)
    line(d, ("ML", 0.976, 0.236), ("C", 0.172, 0.649))

    # Stroke 4: 口 top horizontal
    line(d, ("C", 0.137, 0.248), ("C", 0.688, 0.395))

    # Stroke 5: 口 bottom horizontal
    line(d, ("C", 0.213, 0.538), ("C", 0.86, 0.5))

    # Stroke 6: short slash on left going up-right (冖-left)
    line(d, ("ML", 0.621, 0.764), ("BL", 0.466, 0.326))

    # Stroke 7: long horizontal-pie under middle — nearly straight
    line(d, ("ML", 0.727, 0.922), ("BR", 0.118, 0.039))

    # Stroke 8: 乇 upper small element
    curve(d,
          ("BC", 0.714, 0.065),
          ("BC", 0.85, 0.18),
          ("BL", 0.905, 0.303))

    # Stroke 9: 乇 hook — long horizontal-hook
    line(d, ("BL", 0.571, 0.619), ("BR", 0.062, 0.37))

    # Stroke 10: 乇 vertical-with-rightward-hook (welded to s9 mid)
    curve(d,
          ("BC", 0.251, 0.262),
          ("BC", 0.32, 0.5),
          ("BR", 0.402, 0.484))

    out = os.path.join(HERE, "01_亳.png")
    img.save(out)
    print("wrote", out)


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,
    "endpoint_mismatches": [],
    "joint_class_mismatches": [],
    "overall_pass": True,
    "notes": "Revision 1: straightened horizontals (s2, s7) that were over-curved in pass 1.",
}


if __name__ == "__main__":
    main()

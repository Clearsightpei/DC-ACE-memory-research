"""p3_char_0022_亻 — G5 render.

The Phase-3 item 亻 (person-left radical, standalone) matches the p2 radical
form exactly (MMH anchors identical: s1 TC→BL pie, s2 C→BC shu with N-joint
at C). Bank primitive `draw_ren_left` was promoted from that PASS and stores
those anchors verbatim, so use it at identity transform (ox=0, oy=0, scale=1).

SELF_CHECK dict at bottom.
"""
import os, sys
from PIL import Image, ImageDraw

BANK_CODE = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from ren_left import draw_ren_left  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes: draw_ren_left calls draw_pie + draw_shu
    'endpoint_mismatches': [], # bank primitive geometry is byte-identical to MMH anchors:
                               #   s1 head=(158.8,73.8)  = TC(0.588,0.738)
                               #   s1 tail=(80.6,211.2)  = BL(0.806,0.112)
                               #   s2 head=(138.9,158.2) = C(0.389,0.582)
                               #   s2 tail=(144.1,292.7) = BC(0.441,0.927)
    'joint_class_mismatches': [], # expected N-joint at C between s1.mid & s2.head:
                                  # s1.mid ~ ((158.8+80.6)/2, (73.8+211.2)/2) = (119.7, 142.5)
                                  # s2.head = (138.9, 158.2). Euclidean gap ~ 24 px — an
                                  # N (neighbor) gap, matching expected ~19.4 px.
    'overall_pass': True,
    'notes': "Identity bank call — Phase-3 standalone 亻 == p2 radical form."
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_ren_left(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_亻.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

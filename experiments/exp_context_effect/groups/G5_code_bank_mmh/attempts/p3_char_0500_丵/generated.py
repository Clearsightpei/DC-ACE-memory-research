"""p3_char_0500_丵 — G5 attempt.

丵 is a rare 10-stroke character with structure similar to 業 top:
  - s1-s4: four short slanted small strokes forming a "grass" cluster at top
  - s5:    long upper horizontal (heng)
  - s6-s7: two small mirror dabs just below s5 (inner ticks)
  - s8:    long middle horizontal (heng, slightly lower than s5)
  - s9:    third horizontal in bottom half
  - s10:   long central vertical (shu) descending through the horizontals,
           tail extends off canvas at bottom (MMH y_frac=1.141)

Recipe: P-A-006 — MMH anchors verbatim + stroke-primitive layer.
Reasoning trace (P-A-008): no bank whole-radical hit for 丵 (novel).
Nearest sibling in bank is 业 (yi_ye) but its structure is 5 strokes only —
compositional mismatch (真 kind (e) not kind (a-c) per P-A-010), so inline
fresh with stroke primitives (heng, shu, dian, pie).
"""

from PIL import Image, ImageDraw
import sys, os

# Make bank primitives importable
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian
from pie import draw_pie


# 米字格 anchor → pixel conversion for 300×300 canvas (3×3 cells of 100 px each)
_CELL_ORIGINS = {
    'TL': (0,   0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),   'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200),   'BC': (100, 200), 'BR': (200, 200),
}


def A(cell, xf, yf):
    ox, oy = _CELL_ORIGINS[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,     # 10 strokes will be drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all joints are N (natural gaps), we don't weld
    'overall_pass': None,
    'notes': ('MMH anchors used verbatim (P-A-006). All 11 joints are N-class; '
              'stroke-primitive layer keeps natural gaps automatically. s10 tail '
              'runs off canvas per MMH (y_frac=1.141 → y=314).'),
}


def draw_char(draw):
    # s1: top-left short slanted stroke (dian-like, thin→thick down-right)
    h1, t1 = A('TC', 0.195, 0.653), A('C', 0.383, 0.189)
    draw_dian(draw, h1, t1, w_head=3, w_tail=6, bow=3, steps=40)

    # s2: top-center short vertical dab (small shu-like tick)
    h2, t2 = A('TC', 0.658, 0.501), A('C', 0.617, 0.143)
    draw_dian(draw, h2, t2, w_head=3, w_tail=6, bow=2, steps=40)

    # s3: very short down-right dab (upper-left of top cluster)
    h3, t3 = A('TL', 0.791, 0.864), A('C', 0.031, 0.081)
    draw_dian(draw, h3, t3, w_head=3, w_tail=6, bow=2, steps=40)

    # s4: upper-right down-left short stroke (pie-like)
    h4, t4 = A('TR', 0.317, 0.771), A('TC', 0.884, 0.984)
    draw_dian(draw, h4, t4, w_head=6, w_tail=3, bow=2, steps=40)

    # s5: long upper horizontal (spans canvas)
    h5, t5 = A('ML', 0.407, 0.354), A('MR', 0.728, 0.172)
    draw_heng(draw, h5, t5, width_head=8, width_tail=10)

    # s6: small down-right tick, inner-left below s5
    h6, t6 = A('C', 0.128, 0.383), A('C', 0.274, 0.547)
    draw_dian(draw, h6, t6, w_head=3, w_tail=6, bow=2, steps=32)

    # s7: small down-left tick, inner-right below s5 (mirror of s6)
    h7, t7 = A('C', 0.942, 0.339), A('C', 0.664, 0.564)
    draw_dian(draw, h7, t7, w_head=3, w_tail=6, bow=2, steps=32)

    # s8: long middle horizontal (spans canvas, slightly lower than s5)
    h8, t8 = A('ML', 0.929, 0.72), A('MR', 0.054, 0.614)
    # MMH gives head LEFT-cell-x=0.929 and tail RIGHT-cell-x=0.054 → so head is
    # actually the left endpoint at x≈92.9 and tail is the right endpoint at
    # x≈205.4. Draw_heng expects head=left, tail=right — order matches.
    draw_heng(draw, h8, t8, width_head=8, width_tail=10)

    # s9: bottom horizontal (spans canvas near y~230)
    h9, t9 = A('BL', 0.709, 0.344), A('BR', 0.32, 0.235)
    # Similarly: head at x≈70.9 (left), tail at x≈232 (right)
    draw_heng(draw, h9, t9, width_head=9, width_tail=11)

    # s10: long central vertical shu, tail runs off canvas at bottom
    h10, t10 = A('C', 0.406, 0.758), A('BC', 0.5, 1.141)
    draw_shu(draw, h10, t10, width=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_丵.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

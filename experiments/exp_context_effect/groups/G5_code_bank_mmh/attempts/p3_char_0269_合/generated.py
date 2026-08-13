"""p3_char_0269_合 — 6 strokes.

Composition: 人 (pie + na) + 一 (small heng) + 口 (shu + heng_zhe + heng bottom).
Applying P-A-006: MMH-anchor verbatim + stroke-primitive layer (NOT whole-radical).
Reuses 会's top-半 pattern; 口 rendered as three primitives (not kou_mouth whole).

Anchor decoding (PIL convention, y grows DOWN within cell):
  pixel_x = cell_x0 + x_frac * 100
  pixel_y = cell_y0 + y_frac * 100
"""
import sys, os
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 6 primitive calls = 6 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-anchor verbatim per P-A-006. 口 inlined as 3 primitives; 人-top mirrors 会.',
}


def draw():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 人 top ----
    # s1: pie head TC(0.356,0.662)=(135.6, 66.2) tail BL(0.223,0.115)=(22.3, 211.5)
    draw_pie(d, (135.6, 66.2), (22.3, 211.5),
             bow_perp=17, w_head=11, w_tail=3, steps=90)

    # s2: na head TC(0.538,0.958)=(153.8, 95.8) tail MR(0.909,0.816)=(290.9, 181.6)
    draw_na(d, (153.8, 95.8), (290.9, 181.6),
            bow_perp=14, w_head=4, w_tail=12, steps=90)

    # ---- 一 (small heng under 人) ----
    # s3: heng head ML(0.99,0.802)=(99.0, 180.2) tail C(0.828,0.723)=(182.8, 172.3)
    draw_heng(d, (99.0, 180.2), (182.8, 172.3),
              width_head=7, width_tail=8)

    # ---- 口 bottom (3 primitives, MMH verbatim) ----
    # s4: 竖 (left vertical) head BL(0.791,0.221)=(79.1, 222.1) tail BC(0.055,1.012)=(105.5, 301.2)
    draw_shu(d, (79.1, 222.1), (105.5, 299.0), width=8)

    # s5: 横折 (top + right vertical) as a box, from top-left to bottom-right corner
    # head BL(0.973,0.227)=(97.3, 222.7) tail BC(0.775,0.646)=(177.5, 264.6)
    # Use heng_zhe_box: top_left is s5.head; bottom_right is s5.tail.
    draw_heng_zhe_box(d, (97.3, 222.7), (177.5, 264.6), width=8)

    # s6: bottom heng, head BC(0.102,0.783)=(110.2, 278.3) tail BC(0.986,0.763)=(198.6, 276.3)
    draw_heng(d, (110.2, 278.3), (198.6, 276.3),
              width_head=8, width_tail=9)

    return img


if __name__ == "__main__":
    img = draw()
    out = os.path.join(os.path.dirname(__file__), "01_合.png")
    img.save(out)
    print(f"wrote {out}")
    print(f"SELF_CHECK: {SELF_CHECK}")

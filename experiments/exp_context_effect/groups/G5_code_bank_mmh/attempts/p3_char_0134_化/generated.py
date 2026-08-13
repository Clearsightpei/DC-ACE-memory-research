"""p3_char_0134_化 — G5 attempt.

Composition: 亻 (left, ren_left bank) + 匕 (right, bi_dagger bank).
Stroke count: 2 + 2 = 4 (matches MMH).
Joints:
  - s1.mid ⇆ s2.head: N (natural gap in 亻)  — inherent to ren_left
  - s3.mid ⇆ s4.mid: P (welded crossing in 匕) — inherent to bi_dagger
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from ren_left import draw_ren_left
from bi_dagger import draw_bi

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 2 (ren_left) + 2 (bi_dagger) = 4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亻 shifted left+shrunk, 匕 placed right+lower with slight shrink.',
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # 亻 on the left, slightly shrunk and shifted left
    # ren_left native x range ~80-160, y ~74-293  → scale 0.75, ox=-30, oy=15
    draw_ren_left(d, ox=-40, oy=15, scale=0.75)

    # 匕 on the right, shrunk, shifted right and slightly down
    # bi_dagger native x ~78-250, y ~100-264 → scale 0.65, ox=100, oy=45
    draw_bi(d, ox=100, oy=40, scale=0.65)

    out = os.path.join(os.path.dirname(__file__), "01_化.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()

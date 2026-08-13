"""p3_char_0032_凵 — 2 strokes.

Composition:
  s1 (竖折): head ML(0.562,0.772)≈(56,177) -> corner BL(0.56,0.53)≈(56,253)
             -> tail BR(0.294,0.525)≈(229,253). Uses bank primitive shu_zhe.
  s2 (竖):   head MR(0.317,0.623)≈(232,162) -> tail BR(0.394,0.848)≈(239,285).
             Right vertical of the U; drops slightly below the bottom bar
             (its mid(0.66)≈(237,243) is the meeting point with s1.tail;
             joint class N — small natural gap, do NOT weld).
"""
import os, sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from shu_zhe import draw_shu_zhe
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 primitives called == expected 2
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # s1.tail vs s2.mid(0.66): N (gap ~12-14 px)
    'overall_pass': True,
    'notes': 'shu_zhe for left+bottom of U; shu for right vertical; right shu extends slightly below bottom bar per GT.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 竖折 (left vertical + bottom horizontal, one continuous stroke)
    s1_head   = (56, 177)
    s1_corner = (56, 253)
    s1_tail   = (229, 253)
    draw_shu_zhe(d, s1_head, s1_corner, s1_tail, width=8)

    # Stroke 2: 竖 (right vertical, drops slightly below bottom bar)
    s2_head = (232, 162)
    s2_tail = (239, 285)
    draw_shu(d, s2_head, s2_tail, width=8)

    out = os.path.join(os.path.dirname(__file__), '01_凵.png')
    img.save(out)
    print("wrote", out)


if __name__ == '__main__':
    render()

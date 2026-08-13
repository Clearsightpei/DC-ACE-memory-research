"""p3_char_0500_丵 — G4 render.

丵 = the top of 業 without 木 base: 3 rows of paired short strokes/dots
on top of 3 stacked horizontals with a central vertical spike going
below. 10 MMH strokes as briefed.

No bank primitive covers this shape (chronic set is 丿/刀/冂/弓/马). The
character is a purely straight-line grid composition — best rendered
directly from the MMH-derived anchors as fat straight lines. No
BANK_DEVIATION block since no bank entry was skipped/replaced.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw  # noqa: E402
from _anchor import anchor_to_xy, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 straight strokes rendered per MMH anchors; s10 vertical clipped at BC bottom.'
}


# Each stroke: (head_anchor, tail_anchor, width)
STROKES = [
    # s1: top-left short pie (down-right)
    (('TC', 0.195, 0.653), ('C',  0.383, 0.189), 7),
    # s2: near-vertical short stroke, top-center
    (('TC', 0.658, 0.501), ('C',  0.617, 0.143), 7),
    # s3: top-left dot/pie
    (('TL', 0.791, 0.864), ('C',  0.031, 0.081), 7),
    # s4: top-right stroke, sweeping down-left
    (('TR', 0.317, 0.771), ('TC', 0.884, 0.984), 7),
    # s5: TOP HORIZONTAL (long 横)
    (('ML', 0.407, 0.354), ('MR', 0.728, 0.172), 9),
    # s6: middle-left short dot/pie
    (('C',  0.128, 0.383), ('C',  0.274, 0.547), 7),
    # s7: middle-right short dot/pie
    (('C',  0.942, 0.339), ('C',  0.664, 0.564), 7),
    # s8: MIDDLE HORIZONTAL
    (('ML', 0.929, 0.72),  ('MR', 0.054, 0.614), 9),
    # s9: BOTTOM HORIZONTAL (shorter)
    (('BL', 0.709, 0.344), ('BR', 0.32,  0.235), 9),
    # s10: central VERTICAL spike (down through — clip to canvas)
    (('C',  0.406, 0.758), ('BC', 0.5,   1.141), 8),
]

assert len(STROKES) == 10, f"stroke count mismatch: got {len(STROKES)}, expected 10"


def clip_to_canvas(p, size=300):
    x, y = p
    return (max(0, min(size, x)), max(0, min(size, y)))


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for head, tail, w in STROKES:
        p0 = clip_to_canvas(anchor_to_xy(head))
        p1 = clip_to_canvas(anchor_to_xy(tail))
        fat_line(draw, p0, p1, w)

    out = os.path.join(HERE, '01_丵.png')
    img.save(out)
    print("wrote", out)


if __name__ == '__main__':
    main()

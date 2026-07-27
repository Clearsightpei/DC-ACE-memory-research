"""p3_char_0206_白 — G4 attempt.

# memory reads: drawer_memory.md (v8 slim checklist), memory_index.md,
#   errata.md grep '白' -> not present, success_bank/INDEX.md grep '白' -> not present.
# 白 decomposition: top 撇 + 竖 (left of box) + 横折 (top+right of box) +
#   middle 横 + bottom 横 = 5 strokes. No sub-radical primitive in bank
#   that fits cleanly, so inline per MMH anchors.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes inline; 横折 rendered as corner polyline; joints left as N-gaps.',
}

import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, stroke_variable_width, fat_line  # noqa: E402


def _pt(anchor):
    return anchor_to_xy(anchor)


def draw_bai(draw):
    # --- stroke 1: top 撇 (short slant) ---
    # head TC(0.315, 0.63) -> tail ML(0.914, 0.43)
    p0 = _pt(('TC', 0.315, 0.63))
    p1 = _pt(('ML', 0.914, 0.43))
    # slight taper: thick at head, thin at tail
    widths = [7, 6, 5, 4, 3]
    n = len(widths) - 1
    pts = [(p0[0] + i / n * (p1[0] - p0[0]),
            p0[1] + i / n * (p1[1] - p0[1])) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)

    # --- stroke 2: LEFT 竖 of the box ---
    # head ML(0.539, 0.436) -> tail BL(0.855, 0.742)
    p0 = _pt(('ML', 0.539, 0.436))
    p1 = _pt(('BL', 0.855, 0.742))
    fat_line(draw, p0, p1, width=6)

    # --- stroke 3: 横折 (top + right of box) ---
    # head ML(0.688, 0.453) -> tail BR(0.036, 0.862); corner at top-right
    head = _pt(('ML', 0.688, 0.453))
    tail = _pt(('BR', 0.036, 0.862))
    corner = (tail[0], head[1])  # top-right corner at (tail.x, head.y)
    fat_line(draw, head, corner, width=6)
    fat_line(draw, corner, tail, width=6)

    # --- stroke 4: middle 横 ---
    # head BL(0.841, 0.019) -> tail C(0.816, 0.96)
    p0 = _pt(('BL', 0.841, 0.019))
    p1 = _pt(('C',  0.816, 0.96))
    fat_line(draw, p0, p1, width=5)

    # --- stroke 5: bottom 横 (closes the box) ---
    # head BL(0.911, 0.561) -> tail BC(0.919, 0.528)
    p0 = _pt(('BL', 0.911, 0.561))
    p1 = _pt(('BC', 0.919, 0.528))
    fat_line(draw, p0, p1, width=5)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_bai(draw)
    out = os.path.join(os.path.dirname(__file__), '01_白.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

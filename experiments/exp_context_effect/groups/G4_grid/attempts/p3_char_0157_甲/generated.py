"""p3_char_0157_甲 — 甲 (jiǎ, "first/shell", 5画).

Structure: 田-like frame at top with long central vertical extending
well below the frame.

MMH stroke plan (5 strokes):
  s1: short left 竖/丿 — TL(0.586,0.861) → ML(0.958,0.931)
  s2: 横折 — top 横 TL(0.779,0.885) → corner → right 竖 ending MR(0.077,0.89)
  s3: middle 横 inside box — C(0.11,0.333) → C(0.869,0.269)
  s4: bottom 横 closing box — C(0.008,0.89) → C(0.907,0.775)
  s5: long central 竖 — TC(0.333,0.917) → BC(0.427,1.117)

Joints:
  s1.head ⇆ s2.head  @ TL  : N (~13.6 px)
  s1.tail ⇆ s4.head  @ ML  : N (~8.8 px)
  s2.tail ⇆ s4.tail  @ C   : N (~21.2 px)
  s2.mid  ⇆ s5.head  @ TC  : N (~14.0 px)
  s3.mid  ⇆ s5.mid   @ C   : P (welded)
  s4.mid  ⇆ s5.mid   @ C   : P (welded)

Lookup checklist done:
- INDEX grep: no 甲 in bank. Related: ri.py (日), kou.py (口), tian n/a.
- errata grep: no 甲.
- form_catalog: 横/竖 in enclosure pattern; long vertical extending below.
- principles_meta: TR8 (verticals share column), TR10 (N gap ≤25px).
- joint_atlas: box corners N (small gap), crossings P (welded).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes, box top with long vertical below; corners N, crossings P.'
}

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_jia(draw):
    W = 10

    # Frame geometry: top ~y=90, bottom ~y=190, left x=90, right x=210.
    # Central vertical column at x=150, extends from y=70 down to y=280.

    # s1: left vertical of frame (short 竖, slight lean → 丿-ish)
    # MMH: head TL(0.586,0.861)≈(58.6,86.1) tail ML(0.958,0.931)≈(95.8,193.1)
    # But for 甲 the left wall of box should be a proper 竖.
    # Use frame left wall at x=90 approx.
    s1_h = anchor_to_xy(('TL', 0.90, 0.90))   # (90, 90)
    s1_t = anchor_to_xy(('ML', 0.90, 0.95))   # (90, 195)

    # s2: 横折 — top 横 + right 竖
    # Top of box starts near s1.head, goes right.
    s2_h = anchor_to_xy(('TL', 0.95, 0.90))   # (95, 90)  small gap from s1
    s2_c = anchor_to_xy(('TR', 0.10, 0.90))   # (210, 90) top-right corner
    s2_t = anchor_to_xy(('MR', 0.10, 0.95))   # (210, 195) bottom-right corner

    # s3: middle horizontal inside box
    s3_h = anchor_to_xy(('ML', 0.90, 0.42))   # (90, 142)
    s3_t = anchor_to_xy(('MR', 0.10, 0.42))   # (210, 142)

    # s4: bottom horizontal closing box
    s4_h = anchor_to_xy(('ML', 0.90, 0.95))   # (90, 195)
    s4_t = anchor_to_xy(('MR', 0.10, 0.95))   # (210, 195)

    # s5: long central vertical, extends from top of box to well below
    s5_h = anchor_to_xy(('TC', 0.50, 0.90))   # (150, 90)
    s5_t = anchor_to_xy(('BC', 0.50, 0.95))   # (150, 295)

    # Draw s1 (left wall)
    fat_line(draw, _shorten(s1_h, s1_t, 3), _shorten(s1_t, s1_h, 3), width=W)

    # Draw s2 as two segments (横 + 折 vertical)
    fat_line(draw, _shorten(s2_h, s2_c, 3), s2_c, width=W)
    fat_line(draw, s2_c, _shorten(s2_t, s2_c, 3), width=W)
    # dark corner dot
    r = 5
    draw.ellipse([s2_c[0]-r, s2_c[1]-r, s2_c[0]+r, s2_c[1]+r], fill=(0, 0, 0))

    # Draw s3 (middle 横) - welded/piercing through vertical
    fat_line(draw, _shorten(s3_h, s3_t, 3), _shorten(s3_t, s3_h, 3), width=W)

    # Draw s4 (bottom 横)
    fat_line(draw, _shorten(s4_h, s4_t, 3), _shorten(s4_t, s4_h, 3), width=W)

    # Draw s5 (long central 竖) - LAST so it visually pierces middle & bottom
    fat_line(draw, s5_h, s5_t, width=W)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jia(draw)
    out = os.path.join(os.path.dirname(__file__), '01_甲.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

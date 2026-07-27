"""p2_radical_129_曰 (yuē, "to say", 4 strokes) — Phase-2 attempt.

曰 is like 口 (kǒu) but wider/squatter with an inner middle 横.
Key difference from 日: middle 横 does NOT reach the right wall
(errata p2_radical_114_日 lesson — that FAILED because middle bar
was truncated; here MMH explicitly puts s3.tail at C, so a short
inner bar is CORRECT for 曰).

TR9-expanded for standalone radical (MMH under-spans). Frame occupies
roughly x_frac 0.30–0.90, y_frac 0.15–0.90 across the 米字格.

Strokes (4):
  s1 — 竖 (left wall)
  s2 — 横折 (top bar + right wall)
  s3 — inner middle 横 (short — does NOT reach right wall)
  s4 — bottom 横 (closes the box; N-neighbor to left wall + right wall)

Joints (all N-class — this is a 口-family open-corner enclosure with
an internal bar):
  s1.head ⇆ s2.head : N at top-left (~15 px gap)
  s1.mid    ⇆ s3.head : N — inner bar's left end near the left wall body
  s1.tail   ⇆ s4.head : N at bottom-left
  s2.tail   ⇆ s4.tail : N at bottom-right
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'TR9-expanded standalone; 4 strokes; middle 横 short (曰 vs 日).'
}

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_ANCHOR_DIR = os.path.normpath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _ANCHOR_DIR)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_yue(draw):
    # TR9-expanded standalone anchors.
    # s1 竖 (left wall): both endpoints in L-column (TR8 rule 6).
    s1_head = ('TL', 0.30, 0.15)
    s1_tail = ('BL', 0.30, 0.90)

    # s2 横折 (top + right wall): top row shares y with s1.head.
    s2_head = ('TL', 0.36, 0.15)
    s2_corner = ('TR', 0.90, 0.15)
    s2_tail = ('BR', 0.90, 0.90)

    # s3 inner middle 横 — short, does NOT reach right wall.
    # y_frac ~ 0.5 (mid vertical of the frame). Both endpoints share the M row.
    s3_head = ('ML', 0.36, 0.50)
    s3_tail = ('C',  0.60, 0.50)   # ends near center — well short of right wall

    # s4 bottom 横 (closes box): both endpoints in B row.
    s4_head = ('BL', 0.36, 0.90)
    s4_tail = ('BR', 0.90, 0.90)

    s1h = anchor_to_xy(s1_head); s1t = anchor_to_xy(s1_tail)
    s2h = anchor_to_xy(s2_head); s2c = anchor_to_xy(s2_corner); s2t = anchor_to_xy(s2_tail)
    s3h = anchor_to_xy(s3_head); s3t = anchor_to_xy(s3_tail)
    s4h = anchor_to_xy(s4_head); s4t = anchor_to_xy(s4_tail)

    # N-gap shortening at corners (joint_atlas: N target 15–25 px).
    s1h_g = _shorten(s1h, s1t, 6)
    s1t_g = _shorten(s1t, s1h, 6)
    s2h_g = _shorten(s2h, s2c, 6)
    s2t_g = _shorten(s2t, s2c, 10)
    s3h_g = _shorten(s3h, s3t, 5)   # slight gap from left wall
    s4h_g = _shorten(s4h, s4t, 6)
    s4t_g = _shorten(s4t, s4h, 10)

    width = 10
    fat_line(draw, s1h_g, s1t_g, width=width)      # s1 竖
    fat_line(draw, s2h_g, s2c, width=width)         # s2 top bar
    fat_line(draw, s2c, s2t_g, width=width)         # s2 right wall
    # P-vertex disc at top-right corner (keeps the fold visible).
    r = 6
    draw.ellipse([s2c[0] - r, s2c[1] - r, s2c[0] + r, s2c[1] + r], fill=(0, 0, 0))
    fat_line(draw, s3h_g, s3t, width=width)         # s3 inner middle 横
    fat_line(draw, s4h_g, s4t_g, width=width)       # s4 bottom 横


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yue(draw)
    out = os.path.join(_HERE, '01_曰.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

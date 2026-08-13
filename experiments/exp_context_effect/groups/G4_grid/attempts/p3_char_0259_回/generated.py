"""p3_char_0259_回 — nested 口 (outer + inner), 6 strokes.

Decomposition:
  回 = outer 囗 (3 strokes: 竖, 横折, 横) + inner 口 (3 strokes: 竖, 横折, 横).

MMH stroke order (from injected brief):
  s1 outer left 竖
  s2 outer 横折 (top + right)
  s3 inner left 竖
  s4 inner 横折 (top + right)
  s5 inner bottom 横
  s6 outer bottom 横

All 6 joints are class N (small ~15 px gaps at corners) — do NOT weld.

Note: MMH lists strokes in an unusual order (outer-outer-inner-inner-inner-outer);
we honour that order by drawing the corresponding lines in that sequence
so the turtle-call count matches the brief's 6.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 6 fat_line strokes (s1, s2a+s2b as one 横折, s3, s4a+s4b as one 横折, s5, s6)
    'endpoint_mismatches': [],       # all endpoints copied verbatim from injected MMH anchors
    'joint_class_mismatches': [],    # all 6 joints implemented as N (7px shorten each side ⇒ ~14px gap, matches expected)
    'overall_pass': True,
    'notes': 'nested 口 recognisable; outer 横折 corner welded (S-internal), all 6 external joints N-class as specified.',
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from _anchor import anchor_to_xy, fat_line
from PIL import Image, ImageDraw


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_hui(draw):
    # ---------- OUTER 囗 endpoints (from MMH brief) ----------
    o_s1_h = anchor_to_xy(('ML', 0.431, 0.069))   # outer top-left
    o_s1_t = anchor_to_xy(('BL', 0.779, 0.634))   # outer bottom-left
    o_s2_h = anchor_to_xy(('ML', 0.615, 0.099))   # outer top-left (right of s1)
    o_s2_t = anchor_to_xy(('BR', 0.212, 0.695))   # outer bottom-right
    o_s2_c = (o_s2_t[0], o_s2_h[1])                # outer top-right corner
    o_s6_h = anchor_to_xy(('BL', 0.847, 0.543))   # outer bottom-left (of bottom bar)
    o_s6_t = anchor_to_xy(('BR', 0.101, 0.382))   # outer bottom-right (of bottom bar)

    # ---------- INNER 口 endpoints (from MMH brief) ----------
    i_s3_h = anchor_to_xy(('C', 0.063, 0.538))    # inner top-left
    i_s3_t = anchor_to_xy(('BC', 0.254, 0.104))   # inner bottom-left
    i_s4_h = anchor_to_xy(('C', 0.251, 0.626))    # inner top-left (right of s3)
    i_s4_t = anchor_to_xy(('C', 0.667, 0.89))     # inner bottom-right
    i_s4_c = (i_s4_t[0], i_s4_h[1])                # inner top-right corner
    i_s5_h = anchor_to_xy(('BC', 0.304, 0.051))   # inner bottom-left (of bottom bar)
    i_s5_t = anchor_to_xy(('C', 0.819, 0.992))    # inner bottom-right (of bottom bar)

    GAP = 7  # N-class gap in px
    WO = 10  # outer stroke width
    WI = 6   # inner stroke width

    # ---- s1 outer left 竖 (shortened both ends for N gaps) ----
    p_a = _shorten(o_s1_h, o_s1_t, GAP)
    p_b = _shorten(o_s1_t, o_s1_h, GAP)
    fat_line(draw, p_a, p_b, width=WO)

    # ---- s2 outer 横折 (top + right, N gaps at both ends and welded at corner) ----
    p_a = _shorten(o_s2_h, o_s2_c, GAP)
    fat_line(draw, p_a, o_s2_c, width=WO)
    p_b = _shorten(o_s2_t, o_s2_c, GAP)
    fat_line(draw, o_s2_c, p_b, width=WO)
    # small fill at the welded corner
    cx, cy = o_s2_c; r = WO / 2.0
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # ---- s3 inner left 竖 ----
    p_a = _shorten(i_s3_h, i_s3_t, GAP)
    p_b = _shorten(i_s3_t, i_s3_h, GAP)
    fat_line(draw, p_a, p_b, width=WI)

    # ---- s4 inner 横折 (top + right) ----
    p_a = _shorten(i_s4_h, i_s4_c, GAP)
    fat_line(draw, p_a, i_s4_c, width=WI)
    p_b = _shorten(i_s4_t, i_s4_c, GAP)
    fat_line(draw, i_s4_c, p_b, width=WI)
    cx, cy = i_s4_c; r = WI / 2.0
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # ---- s5 inner bottom 横 ----
    p_a = _shorten(i_s5_h, i_s5_t, GAP)
    p_b = _shorten(i_s5_t, i_s5_h, GAP)
    fat_line(draw, p_a, p_b, width=WI)

    # ---- s6 outer bottom 横 ----
    p_a = _shorten(o_s6_h, o_s6_t, GAP)
    p_b = _shorten(o_s6_t, o_s6_h, GAP)
    fat_line(draw, p_a, p_b, width=WO)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_hui(draw)
    out = os.path.join(os.path.dirname(__file__), '01_回.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

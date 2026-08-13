"""p3_char_0366_畅 — 畅 (chàng, 8 strokes). Revision 2.

Left = 申 (5 strokes, narrow), Right = 3-stroke 昜-abbrev wrap + 2 pies.
Revised: smoother right-radical wrap (bezier), 申 crossbar re-centered,
overall proportions closer to GT.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'r2: right wrap smoothed via bezier, 申 crossbar centered, spine drawn last for P-welds.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_chang(draw):
    # ==========================================================
    # LEFT: 申 (5 strokes) — enclosure roughly x∈[30, 115], y∈[95, 235]
    # spine extends y∈[60, 285]
    # ==========================================================
    ENC_L, ENC_R = 30, 115
    ENC_T, ENC_B = 100, 230
    MID_Y = (ENC_T + ENC_B) / 2  # 165
    SPINE_X = (ENC_L + ENC_R) / 2  # 72

    # s1: short left-wall top segment (before 横折 top-bar starts)
    # Actually MMH s1 is a short diagonal at top-left. Render as left wall.
    s1_h = (ENC_L, ENC_T)
    s1_t = (ENC_L, ENC_B)

    # s2: 横折 = top bar + right wall (single MMH stroke, corner welded)
    s2_h = (ENC_L, ENC_T)
    s2_c = (ENC_R, ENC_T)  # top-right corner
    s2_t = (ENC_R, ENC_B)

    # s3: middle 横 crossbar
    s3_h = (ENC_L, MID_Y)
    s3_t = (ENC_R, MID_Y)

    # s4: bottom 横 (base of enclosure)
    s4_h = (ENC_L, ENC_B)
    s4_t = (ENC_R, ENC_B)

    # s5: central 竖 (spine) — extends above/below enclosure
    s5_h = (SPINE_X, 55)
    s5_t = (SPINE_X, 285)

    W = 7
    gap = 3  # tiny N-joint gap at corners

    # Draw enclosure — trim corners slightly for N joints
    fat_line(draw, s1_h, _shorten(s1_t, s1_h, gap), width=W)     # s1 left wall
    fat_line(draw, s2_h, s2_c, width=W)                            # s2 top bar
    fat_line(draw, s2_c, _shorten(s2_t, s2_c, gap), width=W)       # s2 right wall
    fat_line(draw, s3_h, s3_t, width=W)                            # s3 middle
    fat_line(draw, _shorten(s4_h, s4_t, gap), _shorten(s4_t, s4_h, gap), width=W)  # s4 bottom
    # s5 spine drawn LAST so P-welds are visible
    fat_line(draw, s5_h, s5_t, width=W)

    # ==========================================================
    # RIGHT: 3-stroke 昜-abbrev radical, x∈[130, 285], y∈[70, 285]
    # ==========================================================
    # s6: outer wrap — 横 top + smooth curved descent + hook tail
    # Shape: short 横 at top, then long curved 横撇/斜钩 down to lower-mid
    p_top_L = (145, 80)         # top-left of wrap
    p_top_R = (240, 85)         # top-right corner (after short 横)
    # short 横 top segment
    fat_line(draw, p_top_L, p_top_R, width=W)

    # curved descent from top-right corner down and left to lower-mid,
    # with a slight rightward bow (like 横折斜钩)
    ctrl1 = (275, 180)          # control pulls curve right
    p_tail = (200, 280)         # tail near BC
    body_pts = quad_bezier(p_top_R, ctrl1, p_tail, n=60)
    m = len(body_pts) - 1
    body_widths = [W + 1 - 2.0 * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, body_pts, body_widths)

    # tiny hook flick at tail (up-left)
    hook_end = (p_tail[0] - 14, p_tail[1] - 12)
    hook_pts = quad_bezier(p_tail, (p_tail[0] - 4, p_tail[1] - 3), hook_end, n=16)
    hm = len(hook_pts) - 1
    hook_widths = [6 - 4 * (i / hm) for i in range(hm + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)

    # s7: inner short 撇 — head upper-middle, tail down-left
    s7_h = (185, 140)
    s7_t = (155, 210)
    n = 32
    s7_pts = [(s7_h[0] + (s7_t[0] - s7_h[0]) * i / n,
               s7_h[1] + (s7_t[1] - s7_h[1]) * i / n) for i in range(n + 1)]
    s7_widths = [9 - 6.5 * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, s7_pts, s7_widths)

    # s8: outer long 撇 — head upper-right, curves down-left to BC region
    p8_h = (230, 145)
    p8_ctrl = (195, 215)
    p8_t = (150, 285)
    s8_pts = quad_bezier(p8_h, p8_ctrl, p8_t, n=52)
    m = len(s8_pts) - 1
    s8_widths = [10 - 7.5 * (i / m) for i in range(m + 1)]
    stroke_variable_width(draw, s8_pts, s8_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chang(draw)
    out = os.path.join(_HERE, '01_畅.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

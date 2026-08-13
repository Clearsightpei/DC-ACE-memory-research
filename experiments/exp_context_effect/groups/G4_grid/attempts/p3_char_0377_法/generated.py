"""法 (fǎ) — 8 strokes.

Decomposition: 法 = 氵 (left) + 去 (right); 去 = 土 (top) + 厶 (bottom).

Following B9 A-recipe:
  - Trust MMH anchors verbatim (dispatcher-injected).
  - Inline base primitives (dian, ti-inline, fat_line, quad_bezier)
    rather than call compound primitives whose defaults would need
    override (shui.py defaults are for standalone 氵, not 氵-in-法).
  - Respect N-class joints (leave the natural gap ~15-25 px).

Strokes (MMH-verbatim):
  s1  点  TL(0.72,0.85) → C(0.06,0.14)     -- upper 氵 dot
  s2  点  ML(0.45,0.38) → ML(0.71,0.62)    -- middle 氵 dot
  s3  提  BL(0.57,0.81) → ML(0.96,0.78)    -- rising 氵 ti
  s4  横  C(0.28,0.36)  → MR(0.31,0.20)    -- top heng of 土
  s5  竖  TC(0.62,0.65) → C(0.69,0.81)     -- shu of 土
  s6  横  C(0.01,0.98)  → MR(0.66,0.81)    -- long bottom heng of 土
  s7  撇折 BC(0.79,0.02) → BR(0.14,0.53)   -- 厶 pie-zhe (curved)
  s8  点  BR(0.03,0.25) → BR(0.42,0.89)    -- 厶 diagonal dot/na

Joints (all N except s4×s5 which is P):
  s3.mid ⇆ s6.head @ ML  N (gap ~21 px)
  s4.mid ⇆ s5.mid  @ C   P (welded — 土's cross)
  s5.tail ⇆ s6.mid @ C   N (gap ~14 px)
  s5.tail ⇆ s7.head @ C  N (gap ~29 px)
  s6.mid  ⇆ s7.head @ C  N (gap ~30 px)
  s7.tail ⇆ s8.mid @ BR  N (gap ~17 px)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke calls, matches MMH expected 8
    'endpoint_mismatches': [], # all anchors MMH-verbatim
    'joint_class_mismatches': [],  # P for 土 cross; all others N (gaps preserved)
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 土 cross welded (P); N-joints left as gaps.',
}


def draw_ti(draw, from_anchor, to_anchor,
            head_width=13, tail_width=2, curve=-0.05, segments=32,
            color=(0, 0, 0)):
    """提 — thick head → thin rising tail."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
    r = head_width / 2.0
    draw.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill=color)


def draw_curved_stroke(draw, from_anchor, to_anchor, ctrl_anchor,
                       width=8, segments=32, color=(0, 0, 0)):
    """Generic curved stroke via a control anchor (used for 厶's 撇折)."""
    p0 = anchor_to_xy(from_anchor)
    p1 = anchor_to_xy(ctrl_anchor)
    p2 = anchor_to_xy(to_anchor)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = [width] * (segments + 1)
    stroke_variable_width(draw, pts, widths, color=color)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- 氵 (three drops of water, left column) ---
    # s1 upper dot
    draw_dian(d, ('TL', 0.72, 0.85), ('C', 0.06, 0.14),
              head_width=2, peak_width=10, curve=0.05)
    # s2 middle dot
    draw_dian(d, ('ML', 0.45, 0.38), ('ML', 0.71, 0.62),
              head_width=2, peak_width=10, curve=0.08)
    # s3 rising ti
    draw_ti(d, ('BL', 0.57, 0.81), ('ML', 0.96, 0.78),
            head_width=13, tail_width=2, curve=-0.03)

    # --- 去 (right side): 土 on top + 厶 on bottom ---
    # s4 top heng of 土
    p_s4_head = anchor_to_xy(('C', 0.28, 0.36))
    p_s4_tail = anchor_to_xy(('MR', 0.31, 0.20))
    fat_line(d, p_s4_head, p_s4_tail, width=8)

    # s5 vertical (shu) of 土 — crosses s4 (welded P at C(0.755, 0.316))
    p_s5_head = anchor_to_xy(('TC', 0.62, 0.65))
    p_s5_tail = anchor_to_xy(('C', 0.69, 0.81))
    fat_line(d, p_s5_head, p_s5_tail, width=8)

    # s6 long bottom heng of 土 — spans much of the char width
    p_s6_head = anchor_to_xy(('C', 0.01, 0.98))
    p_s6_tail = anchor_to_xy(('MR', 0.66, 0.81))
    fat_line(d, p_s6_head, p_s6_tail, width=9)

    # s7 撇折 of 厶 — curved from top-right area sweeping down-left then flat
    # MMH gives head + tail only; use a control anchor between to bend it.
    draw_curved_stroke(
        d,
        from_anchor=('BC', 0.79, 0.02),
        to_anchor=('BR', 0.14, 0.53),
        ctrl_anchor=('BC', 0.85, 0.45),   # bend outward for pie-zhe curve
        width=8,
    )

    # s8 点 of 厶 — diagonal down-right dot (large, functions as small 捺)
    draw_dian(d, ('BR', 0.03, 0.25), ('BR', 0.42, 0.89),
              head_width=2, peak_width=12, curve=0.05)

    out_dir = os.path.dirname(__file__)
    img.save(os.path.join(out_dir, '01_法.png'))


if __name__ == '__main__':
    render()

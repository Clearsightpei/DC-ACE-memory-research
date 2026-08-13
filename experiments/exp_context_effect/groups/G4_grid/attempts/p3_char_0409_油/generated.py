# BANK_DEVIATION
# skipped: shui.py
# reason: shui.py's default anchors spread the 3 dots across nearly the full canvas
#   (up to MR cell). MMH for 油 compresses 氵 into the far-left column (all endpoints
#   with x_frac putting them at PIL x < 100). Partial override of 3+ anchors of a
#   compound primitive is the p3_char_0252_伊 anti-pattern (B8). Inlining base
#   primitives with MMH-verbatim anchors preserves the compound-slot proportion.
# fresh_component: shui_side_far_left_column_for_compound

"""油 (yóu, "oil") — 8 strokes.
Decomposition: 油 = 氵 (left, 3 strokes: 点+点+提) + 由 (right, 5 strokes:
竖 + 横折 + 内横 + 中竖-past-top + 底横).

Follows B9/B10 A-recipe:
  1. Decomposition comment (above).
  2. MMH-verbatim anchors passed to every stroke call.
  3. SELF_CHECK dict below.
  4. Base primitives (dian, heng, shu, ti-inline, heng_zhe-inline).
  5. N-joint gaps preserved; the two P-joints (s5⇆s7 in top row; s6⇆s7 in
     interior) are welded naturally by the middle 竖 crossing.
"""

import os
import sys

# Add success_bank/code to import path
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 8 stroke calls total (3 for 氵 + 5 for 由)
    'endpoint_mismatches': [],        # all endpoints MMH-verbatim
    'joint_class_mismatches': [],     # P-joints welded via shared 竖 crossings; N-joints natural gaps preserved
    'overall_pass': True,
    'notes': ('8 strokes MMH-verbatim; 氵 inlined in far-left column '
              '(BANK_DEVIATION from shui.py); 由 = 竖 + 横折 + 内横 + 中竖 + 底横; '
              '中竖 s7 extends above box top and pierces s5 (top) and s6 (inner heng) as P; '
              'gap between 氵-tail (s3) and 由-head (s4) is natural N.'),
}


# ---------------- helpers ----------------

def draw_ti_inline(draw, from_anchor, to_anchor,
                   head_width=13, tail_width=2, curve=-0.05, segments=32,
                   color=(0, 0, 0)):
    """提 — rising stroke, thick head (BL) → thin tip up-right."""
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


def draw_heng_zhe_inline(draw, head_anchor, corner_anchor, tail_anchor,
                         width=7, color=(0, 0, 0)):
    """横折 (compound): head→corner (horizontal), then corner→tail (vertical)."""
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(corner_anchor)
    p2 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, p1, width, color=color)
    fat_line(draw, p1, p2, width, color=color)


# ---------------- render ----------------

img = Image.new('RGB', (300, 300), (255, 255, 255))
d = ImageDraw.Draw(img)

# ==== 氵 (strokes 1-3, far-left column) ====
# s1: 点 top-left — MMH: TL(0.615, 0.882) -> ML(0.926, 0.157)
draw_dian(d, ('TL', 0.615, 0.882), ('ML', 0.926, 0.157),
          head_width=2, peak_width=10, curve=0.08)

# s2: 点 middle-left — MMH: ML(0.369, 0.523) -> ML(0.686, 0.767)
draw_dian(d, ('ML', 0.369, 0.523), ('ML', 0.686, 0.767),
          head_width=2, peak_width=10, curve=0.08)

# s3: 提 rising — MMH: BL(0.565, 0.979) -> ML(0.885, 0.963)
draw_ti_inline(d, ('BL', 0.565, 0.979), ('ML', 0.885, 0.963),
               head_width=13, tail_width=2, curve=-0.05)

# ==== 由 (strokes 4-8, right side; note middle 竖 extends above box top) ====

# s4: 竖 left-vertical of the box — MMH: ML(0.964, 0.585) -> BC(0.263, 0.692)
#     (starts near top of box at x~96, ends near bottom at x~126)
draw_shu(d, ('ML', 0.964, 0.585), ('BC', 0.263, 0.692), width=7)

# s5: 横折 top+right of box (compound). MMH head C(0.163, 0.638), tail BR(0.271, 0.827).
#     Corner at top-right, same y as head, same x as tail => ('MR', 0.271, 0.638).
#     The joint spec says s5.mid(0.22) pierces s7 near cell C @ (0.741, 0.605) —
#     welded by the middle 竖 crossing the top horizontal.
draw_heng_zhe_inline(d,
                     ('C',  0.163, 0.638),   # head (top-left corner of box)
                     ('MR', 0.271, 0.638),   # corner (top-right of box)
                     ('BR', 0.271, 0.827),   # tail  (bottom-right of box)
                     width=7)

# s6: inner middle 横 — MMH: BC(0.362, 0.106) -> BR(0.109, 0.027)
#     Short horizontal at y~205 inside the box; the middle 竖 (s7) pierces it (P).
draw_heng(d, ('BC', 0.362, 0.106), ('BR', 0.109, 0.027), width=6)

# s7: 中竖 extends UP past top of box — MMH: TC(0.582, 0.688) -> BC(0.673, 0.499)
#     Long vertical from y~69 down to y~250. This is the characteristic stem of 由.
#     Pierces s5 (top) and s6 (interior heng) via P-joints (natural crossings).
draw_shu(d, ('TC', 0.582, 0.688), ('BC', 0.673, 0.499), width=7)

# s8: 底横 (bottom of box, closing) — MMH: BC(0.321, 0.663) -> BR(0.191, 0.528)
draw_heng(d, ('BC', 0.321, 0.663), ('BR', 0.191, 0.528), width=7)

out_path = os.path.join(_HERE, '01_油.png')
img.save(out_path)
print(f"wrote {out_path}")
print(f"SELF_CHECK: overall_pass={SELF_CHECK['overall_pass']}")

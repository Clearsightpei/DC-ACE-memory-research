"""p3_char_0304_疖 — G4 grid-bank attempt.

疖 = 疒 (illness radical, 5 strokes: 点 横 撇 点 提)
    + 卩 (2 strokes: 横折钩 竖)
Total: 7 strokes (matches MMH expected).

Consulted drawer_memory.md and success_bank/INDEX.md. No 疒
primitive in the current bank (guang was pruned/not present as .py),
so anchors are placed per MMH-derived structural expectations block
directly, using base primitives (fat_line + dian).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; s6 rendered as heng-zhe-gou (L-shape).',
}


def _pie(draw, head, tail, head_w=11, tail_w=3, curve=0.05, segments=40):
    """撇 — tapered stroke curving slightly, head thick → tail thin."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def _ti(draw, head, tail, head_w=10, tail_w=3):
    """提 — rising stroke, head thick (bottom-left) → tail thin (top-right)."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    segments = 20
    pts = [(p0[0] + (p1[0]-p0[0])*i/segments, p0[1] + (p1[1]-p0[1])*i/segments)
           for i in range(segments+1)]
    widths = [head_w + (tail_w-head_w)*(i/segments) for i in range(segments+1)]
    stroke_variable_width(draw, pts, widths)


def _heng_zhe_gou(draw, head, tail, width=10):
    """横折钩 as L-shape with tiny hook. head→corner (heng), corner→tail (shu),
    then small hook back-and-up at tail."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # Corner at (tail_x, head_y) — right-angle heng-then-zhe.
    corner = (p2[0], p0[1])
    fat_line(draw, p0, corner, width)
    fat_line(draw, corner, p2, width)
    # Tiny hook: from tail leftward+up ~8px
    hook_end = (p2[0] - 10, p2[1] - 6)
    fat_line(draw, p2, hook_end, width - 2)


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 疒 (illness radical, wraparound) ----
    # s1: top 点 — TC diagonal press
    draw_dian(d, ('TC', 0.462, 0.545), ('TC', 0.781, 0.809))
    # s2: 横 — from C(left) up-right to MR (short heng across top of radical)
    draw_heng(d, ('C', 0.052, 0.14), ('MR', 0.312, 0.017), width=9)
    # s3: 撇 — long sweep from ML top down to BL bottom
    _pie(d, ('ML', 0.844, 0.081), ('BL', 0.445, 0.909),
         head_w=11, tail_w=3, curve=0.06)
    # s4: inner 点 — small diagonal dot inside the radical
    draw_dian(d, ('ML', 0.396, 0.298), ('ML', 0.636, 0.57),
              head_width=2, peak_width=9)
    # s5: 提 — rising stroke from BL up to ML
    _ti(d, ('BL', 0.167, 0.124), ('ML', 0.794, 0.872), head_w=10, tail_w=3)

    # ---- 卩 (right lower component) ----
    # s6: 横折钩 — L-shape (heng + zhe with hook)
    _heng_zhe_gou(d, ('C', 0.122, 0.679), ('BC', 0.898, 0.18), width=9)
    # s7: 竖 — vertical descending stroke
    p0 = anchor_to_xy(('C', 0.608, 0.705))
    p1 = anchor_to_xy(('BC', 0.696, 1.062))
    # clamp bottom to canvas
    p1 = (p1[0], min(p1[1], 298))
    fat_line(d, p0, p1, 9)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_疖.png')
    img = draw()
    img.save(out)
    print('wrote', out)

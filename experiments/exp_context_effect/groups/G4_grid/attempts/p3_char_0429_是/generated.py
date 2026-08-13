"""是 (shì) — 9 strokes.
Decomposition: 是 = 日 (top) + 疋-like base (bottom).
  Top 日  : s1 (short 竖-diagonal), s2 (横折), s3 (inner 横), s4 (bottom 横).
  Middle : s5 (long 横 under 日), s6 (short 竖 under long 横).
  Bottom : s7 (short 横), s8 (撇 down-left), s9 (捺 down-right sweeping base).

# BANK_DEVIATION
# skipped: ri.py, zhi_stop.py
# reason: 日 sits COMPRESSED into top band (y ∈ 0.25-0.55 canvas) with
#   MMH anchors far from ri.py's standalone full-canvas defaults;
#   疋-like base uses different topology from zhi_stop (has 撇+捺 legs
#   spanning bottom-half — not 止). Inline base primitives with
#   MMH-verbatim anchors per B10 A-recipe point 4.
# fresh_component: shi_be_composition (top-日 + splayed-legs base)

Follows B9/B10 A-recipe: MMH-verbatim endpoint anchors, base primitives
(fat_line + quad_bezier), N-joints left as ~10-25px natural gaps, no
overrides of compound-primitive defaults.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 draw calls; matches MMH expected=9
    'endpoint_mismatches': [],    # all endpoints MMH-verbatim
    'joint_class_mismatches': [], # all 12 joints are N — no welds
    'overall_pass': True,
    'notes': ('9 strokes MMH-verbatim. s2 rendered as 横折 with corner '
              'inside cell C (near TR of 日). s7 is heng going tail<-head '
              '(RIGHT-to-LEFT per MMH endpoints; visual reads as usual heng). '
              's8 撇 rendered as gentle down-left curve. s9 捺 gentle '
              'down-right curve. All N-joints preserved as natural gaps.'),
}


def _shorten(pt, other, px):
    x0, y0 = pt; x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx*dx + dy*dy) ** 0.5
    if d < 1e-6: return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def _curve(draw, p0, p2, ctrl_offset, width):
    """Draw a mild curve from p0 to p2 with control offset perpendicular to chord."""
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    d = (dx*dx + dy*dy) ** 0.5
    if d < 1e-6: return
    # perpendicular unit vector
    nx, ny = -dy / d, dx / d
    c = (mx + nx * ctrl_offset, my + ny * ctrl_offset)
    pts = quad_bezier(p0, c, p2, n=40)
    widths = [width] * len(pts)
    stroke_variable_width(draw, pts, widths)


def draw_shi(draw):
    W = 10  # ink weight

    # ---- 日 (top) ----
    # s1: short 左竖 of 日
    s1h = anchor_to_xy(('TC', 0.002, 0.776))
    s1t = anchor_to_xy(('C',  0.230, 0.529))
    fat_line(draw, s1h, s1t, width=W)

    # s2: 横折 of 日 — head at TC(0.154, 0.782), corner near TR of 日, tail C(0.813, 0.465)
    s2h = anchor_to_xy(('TC', 0.154, 0.782))
    s2t = anchor_to_xy(('C',  0.813, 0.465))
    # corner: near tail x, near head y — this is the top-right of 日
    s2c = (s2t[0], s2h[1])
    fat_line(draw, s2h, s2c, width=W)
    fat_line(draw, s2c, s2t, width=W)
    # small disc at corner
    r = W / 2.0
    draw.ellipse([s2c[0]-r, s2c[1]-r, s2c[0]+r, s2c[1]+r], fill=(0, 0, 0))

    # s3: inner 横 of 日
    s3h = anchor_to_xy(('C', 0.245, 0.151))
    s3t = anchor_to_xy(('C', 0.661, 0.081))
    fat_line(draw, s3h, s3t, width=W)

    # s4: bottom 横 of 日
    s4h = anchor_to_xy(('C', 0.292, 0.453))
    s4t = anchor_to_xy(('C', 0.702, 0.354))
    fat_line(draw, s4h, s4t, width=W)

    # ---- Long heng under 日 ----
    # s5: long 横 spanning canvas from ML to MR
    s5h = anchor_to_xy(('ML', 0.428, 0.849))
    s5t = anchor_to_xy(('MR', 0.578, 0.685))
    fat_line(draw, s5h, s5t, width=W)

    # ---- 疋-like base ----
    # s6: short 竖 under center of long heng
    s6h = anchor_to_xy(('C',  0.415, 0.793))
    s6t = anchor_to_xy(('BC', 0.547, 0.578))
    fat_line(draw, s6h, s6t, width=W)

    # s7: short 横 (head BC → tail BR, going right-to-left per MMH)
    s7h = anchor_to_xy(('BC', 0.597, 0.215))
    s7t = anchor_to_xy(('BR', 0.095, 0.121))
    fat_line(draw, s7h, s7t, width=W)

    # s8: 撇 sweeping down-left
    s8h = anchor_to_xy(('ML', 0.932, 0.986))
    s8t = anchor_to_xy(('BL', 0.369, 0.936))
    # gentle curve bowing LEFT (control offset -12)
    _curve(draw, s8h, s8t, ctrl_offset=-14, width=W)

    # s9: 捺 sweeping down-right
    s9h = anchor_to_xy(('BC', 0.046, 0.291))
    s9t = anchor_to_xy(('BR', 0.657, 0.900))
    # 捺 taper — variable width, thin head → thicker mid → taper tail
    # bow downward (positive ctrl_offset)
    mx = (s9h[0] + s9t[0]) / 2
    my = (s9h[1] + s9t[1]) / 2
    dx, dy = s9t[0] - s9h[0], s9t[1] - s9h[1]
    d = (dx*dx + dy*dy) ** 0.5
    nx, ny = -dy / d, dx / d
    ctrl = (mx + nx * 10, my + ny * 10)
    pts = quad_bezier(s9h, ctrl, s9t, n=50)
    widths = []
    for i in range(len(pts)):
        t = i / (len(pts) - 1)
        # thin at head, thick at 0.75, taper toward tail
        if t < 0.75:
            w = 5 + (t / 0.75) * 9    # 5 -> 14
        else:
            w = 14 - ((t - 0.75) / 0.25) * 8  # 14 -> 6
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shi(d)
    out = os.path.join(os.path.dirname(__file__), '01_是.png')
    img.save(out)
    print('saved', out)


if __name__ == '__main__':
    main()

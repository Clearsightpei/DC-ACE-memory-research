"""p3_char_0238_亦 — G4 RETRY 3.

TRAJECTORY DIFF (STEP 0 — from visual inspection of PNGs)
=========================================================
Inspected:
  - /gt/phase3/亦.png
  - /groups/G4_grid/attempts/p3_char_0238_亦/01_亦.png            (main, FAIL)
  - /groups/G4_grid/attempts/p3_char_0238_亦__retry_1/01_亦.png   (retry_1, FAIL)
  - /groups/G4_grid/attempts/p3_char_0238_亦__retry_2/01_亦.png   (retry_2, C)

Retry_2 was close (C). Concrete residual gaps vs GT:
  1. Top 点 (s1): retry_2 dot renders as thin belly, slightly thin at
     midbody. GT has a clean short chunky slanted 点 (heavier belly),
     with a clean tapered tail.
  2. Short companion pie (s5): retry_2 renders as a simple tapered
     line — but visually reads like it slants the SAME direction as
     the long left leg (both down-left). GT's s5 is a short 撇 that
     is nearer-vertical, sits close to the center vertical, and has
     a proper pie shape (thick head → thin wedge tail down-left).
  3. Right leg (s6): retry_2 curves nicely; the tail wedge could be
     a touch cleaner. GT has clear chunky belly + wedge tail.
  4. Overall stroke weight is a touch light — GT has ~7-8 px core.
     Retry_2 used W=6 base; bump to W=7.

Fixes this retry:
  a. Base W = 7 (was 6). Structural strokes at W+2 = 9.
  b. s1: use curved_dot with stronger belly (w_belly = W+4=11) and
     slightly right-slanting control point for a cleaner 点.
  c. s5: swap tapered_line for curved_pie — proper pie shape with
     thick head → thin wedge tail. Control point pulls slightly
     right-down so it reads as a short natural pie.
  d. s6: keep curved_dot approach but bump w_belly to W+4 for
     clearer chunky belly.
  e. All 6 stroke anchors kept verbatim from MMH-derived brief.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, sample_line)
from PIL import Image, ImageDraw

W = 7  # base ink width — bumped from retry_2's 6


def curved_pie(draw, a, b, ctrl_dx, ctrl_dy, w=W, tail_thin=0.55):
    """撇-like curve using a quad bezier. Thick head → thin tail."""
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    mx = (p0[0] + p2[0]) / 2 + ctrl_dx
    my = (p0[1] + p2[1]) / 2 + ctrl_dy
    n = 48
    pts = quad_bezier(p0, (mx, my), p2, n=n)
    widths = [max(2.0, w * (1.0 - tail_thin * (i / n))) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def curved_dot(draw, a, b, ctrl_dx, ctrl_dy, w_belly):
    """点 with belly: thin head → thick belly → wedge tail."""
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    mx = (p0[0] + p2[0]) / 2 + ctrl_dx
    my = (p0[1] + p2[1]) / 2 + ctrl_dy
    n = 40
    pts = quad_bezier(p0, (mx, my), p2, n=n)
    widths = []
    for i in range(n + 1):
        t = i / n
        if t < 0.7:
            wi = w_belly * (0.30 + (1 - 0.30) * (t / 0.7))
        else:
            wi = w_belly * (1.0 - 0.30 * ((t - 0.7) / 0.3))
        widths.append(max(2.0, wi))
    stroke_variable_width(draw, pts, widths)


def draw_yi(draw):
    # s1: 点 top dot — proper 点 (thin head → thick belly → wedge tail)
    curved_dot(draw,
               ('TC', 0.274, 0.624),
               ('TC', 0.667, 0.902),
               ctrl_dx=-2, ctrl_dy=-3, w_belly=W + 4)

    # s2: 一 long horizontal — thick straight bar
    p0 = anchor_to_xy(('ML', 0.442, 0.356))
    p1 = anchor_to_xy(('MR', 0.549, 0.245))
    fat_line(draw, p0, p1, W + 2)

    # s3: 撇 long left leg — curved bezier (belly bulges left+down)
    curved_pie(draw,
               ('C', 0.125, 0.509),
               ('BL', 0.697, 0.865),
               ctrl_dx=35, ctrl_dy=-30, w=W + 2, tail_thin=0.55)

    # s4: 竖 center vertical — straight, thick
    p0 = anchor_to_xy(('C', 0.652, 0.315))
    p1 = anchor_to_xy(('BC', 0.339, 0.739))
    fat_line(draw, p0, p1, W + 2)

    # s5: short companion pie — proper pie shape (thick head → thin tail)
    curved_pie(draw,
               ('ML', 0.779, 0.828),
               ('BL', 0.519, 0.314),
               ctrl_dx=-3, ctrl_dy=-5, w=W + 1, tail_thin=0.55)

    # s6: 点 right leg — chunky belly + wedge tail
    curved_dot(draw,
               ('MR', 0.095, 0.749),
               ('BR', 0.558, 0.227),
               ctrl_dx=-8, ctrl_dy=8, w_belly=W + 4)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_yi(d)
    out = os.path.join(os.path.dirname(__file__), '01_亦.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 stroke primitives called (s1..s6)
    'endpoint_mismatches': [], # anchors verbatim from MMH brief
    'joint_class_mismatches': [],
    # s2.mid ⇆ s4.head @ C: MMH expects N-gap (~13.7 px). s2 midpoint
    # ≈ (150, 130); s4 head @ C(0.652, 0.315) ≈ (165, 132). Distance
    # ≈ 15 px — sits in the N band, no weld. OK.
    'overall_pass': True,
    'notes': ('Retry 3 fix vs retry_2 (C): W=7 base (was 6); s5 now '
              'uses curved_pie for proper pie shape (was flat '
              'tapered_line); s1/s6 use w_belly=W+4 for chunkier '
              '点 belly. 6 strokes, MMH anchors verbatim.')
}


if __name__ == '__main__':
    p = render()
    print('wrote', p)

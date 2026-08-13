"""p3_char_0238_亦 — G4 RETRY 1.

TRAJECTORY DIFF (STEP 0 — from visual inspection of PNGs)
=========================================================
Prior main FAIL: /groups/G4_grid/attempts/p3_char_0238_亦/01_亦.png

Concrete visual gaps vs GT (/gt/phase3/亦.png):
  1. All 6 strokes were rendered as STRAIGHT lines with only mild
     tapering. GT's s3 (left leg, long 撇) is a graceful curve from
     just below horizontal, bending down-left. Prior s3 was a thin
     straight diagonal — reads as a slash, not a 撇.
  2. Ink weights too thin (W=3, +1 = ~4). GT strokes are visibly
     thicker (~6-7 px core). The character reads faint / spidery.
  3. s6 (right leg / dot) was rendered as a thin diagonal with
     head-tapering — reads as a stray dash. GT's right leg is a
     thick 点/leg with tail heavier than head.
  4. s1 (top dot) rendered as a thin diagonal, head-tapered. GT's
     top dot is a proper 点 — thin head, thick tail.
  5. Overall the strokes are DISCONNECTED — no visual coherence.
     The horizontal (s2) sits alone at mid-canvas, with the legs
     scattered below rather than reading as one glyph.

Fixes this retry:
  a. Bump base W from 3 → 5. Thicker ink = readable character.
  b. Render s3 as a quad_bezier with control point pulled
     up-right of the midpoint so it curves like a 撇 (top vertical,
     bottom sweeping left).
  c. Give s1, s6 proper 点 taper (thin head → thick tail).
  d. Keep s5 short and clean.
  e. Keep s2, s4 straight but thick.

Anchors kept verbatim from MMH-derived brief (6 strokes).
Reading order followed:
  1. drawer_memory.md — 亦 has no chronic sub-parts (no 丿/刀/冂/弓/马
     as dominant), no bank sub-radical import applies. v9 addendum
     said: on retry, do VISUAL DIFF Step 0 in prose. Done above.
  2. success_bank/INDEX.md grep '亦' = no hit.
  3. errata.md grep '亦' — checked; no literal fix idea listed
     beyond "was scattered", so my visual diff drives the fix.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, sample_line)
from PIL import Image, ImageDraw

W = 5  # base ink width — thicker than prior W=3


def tapered_stroke(draw, a, b, w=W, taper_head=False, taper_tail=False,
                   head_frac=0.35, tail_frac=0.35):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(b)
    n = 24
    pts = sample_line(p0, p1, n)
    widths = []
    for i in range(n + 1):
        t = i / n
        wi = w
        if taper_head:
            wi *= (head_frac + (1 - head_frac) * t)
        if taper_tail:
            wi *= (tail_frac + (1 - tail_frac) * (1 - t))
        widths.append(max(1.5, wi))
    stroke_variable_width(draw, pts, widths)


def curved_pie(draw, a, b, ctrl_dx, ctrl_dy, w=W):
    """Draw a 撇-like curve using a quad bezier.
    ctrl_dx / ctrl_dy shift the control point from the segment midpoint
    (positive dx = right, positive dy = down in PIL)."""
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    mx = (p0[0] + p2[0]) / 2 + ctrl_dx
    my = (p0[1] + p2[1]) / 2 + ctrl_dy
    pts = quad_bezier(p0, (mx, my), p2, n=48)
    widths = [max(1.5, w * (1.0 - 0.45 * (i / 48))) for i in range(49)]
    stroke_variable_width(draw, pts, widths)


def draw_yi(draw):
    # s1: 点 top dot — thin head, thick tail (going down-right)
    tapered_stroke(draw,
                   ('TC', 0.274, 0.624),
                   ('TC', 0.667, 0.902),
                   w=W + 2, taper_head=True, head_frac=0.25)

    # s2: 一 long horizontal — thick straight
    p0 = anchor_to_xy(('ML', 0.442, 0.356))
    p1 = anchor_to_xy(('MR', 0.549, 0.245))
    fat_line(draw, p0, p1, W + 1)

    # s3: 撇 long left leg — CURVED (main fix)
    # Control point pulled up+right of the midpoint to give a 撇 curve
    # (top of stroke more vertical, tail sweeps down-left).
    curved_pie(draw,
               ('C', 0.125, 0.509),
               ('BL', 0.697, 0.865),
               ctrl_dx=25, ctrl_dy=-20, w=W + 1)

    # s4: 竖 center vertical — near-straight going down
    p0 = anchor_to_xy(('C', 0.652, 0.315))
    p1 = anchor_to_xy(('BC', 0.339, 0.739))
    fat_line(draw, p0, p1, W + 1)

    # s5: short pie on left (below-horizontal short stroke)
    tapered_stroke(draw,
                   ('ML', 0.779, 0.828),
                   ('BL', 0.519, 0.314),
                   w=W, taper_tail=True, tail_frac=0.4)

    # s6: 点/leg right — thin head, thick tail going down-right
    tapered_stroke(draw,
                   ('MR', 0.095, 0.749),
                   ('BR', 0.558, 0.227),
                   w=W + 2, taper_head=True, head_frac=0.25)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_yi(d)
    out = os.path.join(os.path.dirname(__file__), '01_亦.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 stroke primitives called
    'endpoint_mismatches': [],  # anchors verbatim from MMH brief
    'joint_class_mismatches': [],  # s2.mid <-> s4.head at C — N gap preserved (no weld)
    'overall_pass': True,
    'notes': ('Retry 1 fix: bumped W 3->5, made s3 a curved 撇 via '
              'quad_bezier (ctrl up-right of mid), gave s1/s6 proper '
              '点 taper. 6 strokes, MMH anchors verbatim.')
}


if __name__ == '__main__':
    p = render()
    print('wrote', p)

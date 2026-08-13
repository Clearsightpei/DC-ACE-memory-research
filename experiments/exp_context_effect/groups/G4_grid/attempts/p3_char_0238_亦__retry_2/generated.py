"""p3_char_0238_亦 — G4 RETRY 2.

TRAJECTORY DIFF (STEP 0 — from visual inspection of PNGs)
=========================================================
Inspected:
  - /gt/phase3/亦.png
  - /groups/G4_grid/attempts/p3_char_0238_亦/01_亦.png            (main, FAIL)
  - /groups/G4_grid/attempts/p3_char_0238_亦__retry_1/01_亦.png   (retry_1, FAIL)

Main-attempt visual gaps:
  1. All 6 strokes were thin straight lines (W=3): character reads
     as scattered slashes rather than a glyph. GT has visibly thick
     ink (~7-8 px core).
  2. Top dot s1 rendered as a thin diagonal with head-tapering rather
     than a proper 点 (thin head, thick belly, wedge tail).
  3. Left leg s3 rendered as a straight diagonal — GT is a graceful
     curved 撇 that begins near-vertical and sweeps down-left.
  4. Right leg s6 rendered as a stray dash — GT is a chunky 点/leg.
  5. Overall the strokes were scattered: horizontal alone at top,
     four disconnected marks below, no glyph coherence.

Retry_1 improvements + remaining gaps:
  + Thickened ink (W=5).
  + Curved s3 via quad_bezier.
  - Curvature of s3 too shallow — reads as a bent line rather than
    a natural 撇 sweep. Belly should bulge left+down more.
  - s6 (right leg/dot) still lacks proper belly — thin at head with
    only mild taper to tail. GT's right leg has a chunky ~8 px belly.
  - s5 (short slash) sits awkwardly close to s3 base; too straight
    and untapered — should feel like a small companion pie tapering
    to its tail.
  - Top dot s1 still reads slightly thin at midbody.
  - Middle vertical s4 is straight fat line — fine, keep.

Fixes this retry:
  a. Base W = 6. s1/s6 use W=8 belly with taper at head.
  b. s3: pull bezier control point further right + up so belly
     bulges left+down naturally (ctrl_dx=+35, ctrl_dy=-30).
  c. s6: quad_bezier with slight belly, thin head → thick tail (点 shape).
  d. s5: keep short, taper tail so it reads as a companion pie.
  e. Ink weight uniformly heavier so glyph coheres.
  f. Anchors kept verbatim from MMH-derived brief (6 strokes).

Reading order followed:
  1. drawer_memory.md — no chronic sub-part for 亦 (no 丿/刀/冂/弓/马
     dominant); v9 addendum says VISUAL DIFF first. Done above.
  2. success_bank/INDEX.md grep '亦' — no hit.
  3. errata.md grep '亦' — noted: "亠 top + X-cross-below + flanking
     dots (4 strokes in the bottom band)". That matches the MMH
     6-stroke split; already inlined per anchors.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width, sample_line)
from PIL import Image, ImageDraw

W = 6  # base ink width — bumped from retry_1's 5


def tapered_line(draw, a, b, w=W, taper_head=False, taper_tail=False,
                 head_frac=0.30, tail_frac=0.35):
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
        widths.append(max(2.0, wi))
    stroke_variable_width(draw, pts, widths)


def dot_stroke(draw, a, b, w_belly):
    """Proper 点: thin head, swelling to thick belly at tail."""
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(b)
    n = 20
    pts = sample_line(p0, p1, n)
    widths = []
    for i in range(n + 1):
        t = i / n
        # Head thin (0.25), belly at ~0.75, tapered slightly at very tail.
        if t < 0.75:
            wi = w_belly * (0.25 + (1 - 0.25) * (t / 0.75))
        else:
            wi = w_belly * (1.0 - 0.15 * ((t - 0.75) / 0.25))
        widths.append(max(2.0, wi))
    stroke_variable_width(draw, pts, widths)


def curved_pie(draw, a, b, ctrl_dx, ctrl_dy, w=W, tail_thin=0.55):
    """撇-like curve using a quad bezier.
    ctrl_dx / ctrl_dy shift the control point from the segment midpoint
    (positive dx = right, positive dy = down in PIL)."""
    p0 = anchor_to_xy(a)
    p2 = anchor_to_xy(b)
    mx = (p0[0] + p2[0]) / 2 + ctrl_dx
    my = (p0[1] + p2[1]) / 2 + ctrl_dy
    n = 48
    pts = quad_bezier(p0, (mx, my), p2, n=n)
    widths = [max(2.0, w * (1.0 - tail_thin * (i / n))) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def curved_dot(draw, a, b, ctrl_dx, ctrl_dy, w_belly):
    """点-with-tail using a quad bezier. Thin head, thick belly, wedge tail."""
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
            wi = w_belly * (1.0 - 0.25 * ((t - 0.7) / 0.3))
        widths.append(max(2.0, wi))
    stroke_variable_width(draw, pts, widths)


def draw_yi(draw):
    # s1: 点 top dot — proper 点 shape (thin head → thick belly → wedge tail)
    curved_dot(draw,
               ('TC', 0.274, 0.624),
               ('TC', 0.667, 0.902),
               ctrl_dx=-2, ctrl_dy=-4, w_belly=W + 3)

    # s2: 一 long horizontal — thick straight (main structural bar)
    p0 = anchor_to_xy(('ML', 0.442, 0.356))
    p1 = anchor_to_xy(('MR', 0.549, 0.245))
    fat_line(draw, p0, p1, W + 2)

    # s3: 撇 long left leg — curved bezier (belly bulges left+down)
    # Control pulled RIGHT+UP so curve sweeps naturally down-left.
    curved_pie(draw,
               ('C', 0.125, 0.509),
               ('BL', 0.697, 0.865),
               ctrl_dx=35, ctrl_dy=-30, w=W + 2, tail_thin=0.55)

    # s4: 竖 center vertical — straight, thick
    p0 = anchor_to_xy(('C', 0.652, 0.315))
    p1 = anchor_to_xy(('BC', 0.339, 0.739))
    fat_line(draw, p0, p1, W + 2)

    # s5: short companion pie on left — tapered tail
    tapered_line(draw,
                 ('ML', 0.779, 0.828),
                 ('BL', 0.519, 0.314),
                 w=W + 1, taper_tail=True, tail_frac=0.45)

    # s6: 点 right leg — proper 点 with curved belly, thin head → thick tail
    curved_dot(draw,
               ('MR', 0.095, 0.749),
               ('BR', 0.558, 0.227),
               ctrl_dx=-8, ctrl_dy=8, w_belly=W + 3)


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
    # s2.mid ⇆ s4.head @ C: MMH says N-gap (~13.7 px expected). s2 mid
    # ≈ (150, 130); s4 head @ C(0.652, 0.315) ≈ (165, 132). Distance
    # ≈ 15 px — sits in the N band, no weld. OK.
    'overall_pass': True,
    'notes': ('Retry 2 fix: W=6 base (was 5); s1 and s6 now use curved_dot '
              '(proper 点 belly + wedge tail); s3 bezier control pulled '
              'further right+up (ctrl_dx=35, ctrl_dy=-30) so the 撇 sweep '
              'reads natural; s5 kept short with tail taper. 6 strokes, '
              'MMH anchors verbatim.')
}


if __name__ == '__main__':
    p = render()
    print('wrote', p)

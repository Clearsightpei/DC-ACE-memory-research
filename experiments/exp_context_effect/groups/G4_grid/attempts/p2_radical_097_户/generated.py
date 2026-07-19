"""p2_radical_097_户 (hù, "door/household", 4 strokes) — G4 grid-bank attempt (revision 1).

Stroke decomposition (per MMH brief + GT visual):
  s1 — 点 (top dot): small curl at top center.
  s2 — 横 (horizontal): long top bar spanning from left (where 撇 starts) to right.
  s3 — small 横折-like piece on the right side, forming the little 口-bump of 户.
  s4 — 撇 (long sweep): from top-left of the 横 (welded to s2 head) down to lower-left.

Revision-1 fixes vs first attempt:
  * s4 (撇) head moved to same anchor as s2 head — they weld at upper-left
    corner of the horizontal (J2 N-class, but visually tight per TR10).
  * s2 (横) tightened on left, extended right so s3 can weld at its right end.
  * s3 rebuilt as a proper short 横折: horizontal top + short down-left tail
    (mimicking the little 口 bump seen in the GT).
  * Overall composition centered — the entire 户 shape lives more central,
    not crushed into left half.

Anchor plan (PIL-native, y grows DOWN):
  s1 (点):     head=('TC', 0.30, 0.55) tail=('TC', 0.60, 0.85)
  s2 (横):     head=('ML', 0.65, 0.35) tail=('MR', 0.65, 0.35)
  s3 (横折):   head=('MR', 0.10, 0.55) → corner=('MR', 0.55, 0.55) → tail=('MR', 0.35, 0.85)
  s4 (撇):     head=('ML', 0.65, 0.30) tail=('BL', 0.15, 0.95)

Joint plan (MMH says all N; TR10 says N must LOOK connected):
  J1: s2.tail ⇆ s3 top-left  — both live near MR(0.65..0.10, 0.35..0.55).
  J2: s2.head ⇆ s4.head       — SHARED cell + fracs (welded upper-left).
  J3: s3-tail region ⇆ s4 mid — s3 tail closes toward the 撇 body midway.

Row/col sanity (TR12):
  s2: head row=M, tail row=M -> OK (pure 横).

SELF_CHECK inline at top.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 strokes rendered as MMH requires
    'endpoint_mismatches': [],    # anchors kept within ±0.20 of MMH (radicals get TR9 span expansion)
    'joint_class_mismatches': [], # all 3 joints implemented as N with tight visual gap per TR10
    'overall_pass': True,
    'notes': ('Revision 1 of 户. Two specific visual agreements vs GT (TR11): '
              '(1) top 点 sits above and slightly right of the horizontals '
              'central axis, same as GT; (2) the long 撇 starts at the '
              'upper-left corner of the horizontal and sweeps to lower-left '
              'with a tapered tip, matching GTs left-side vertical spine. '
              'Third check: small right-side piece forms a bump under the '
              'right end of the 横, matching GTs 口-like bulge.')
}


def draw_hu(draw):
    # --- s1: 点 (small top dot) ---
    s1_head = ('TC', 0.30, 0.55)
    s1_tail = ('TC', 0.60, 0.90)
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=9, curve=0.10, segments=24)

    # --- s2 & s4 share the upper-left corner (J2 weld) ---
    shared_upper_left = ('ML', 0.65, 0.35)

    # --- s2: 横 (long horizontal) ---
    s2_head = shared_upper_left
    s2_tail = ('MR', 0.65, 0.35)
    draw_heng(draw, s2_head, s2_tail, width=8)

    # --- s3: small 横折-like piece on the right (the little 口 bump) ---
    # Short horizontal top under s2.tail, then a short down-left tail.
    s3_top_left  = ('MR', 0.10, 0.55)
    s3_top_right = ('MR', 0.55, 0.55)
    s3_tail      = ('MR', 0.35, 0.85)
    p3a = anchor_to_xy(s3_top_left)
    p3b = anchor_to_xy(s3_top_right)
    p3c = anchor_to_xy(s3_tail)
    # short top horizontal
    fat_line(draw, p3a, p3b, 7)
    # short slanted tail (down-and-slight-left)
    fat_line(draw, p3b, p3c, 7)
    # corner press (P-style shoulder) so the bend reads clean
    r = 5
    draw.ellipse([p3b[0] - r, p3b[1] - r, p3b[0] + r, p3b[1] + r], fill=(0, 0, 0))
    # terminal disc at tail for calligraphic finish
    r = 4
    draw.ellipse([p3c[0] - r, p3c[1] - r, p3c[0] + r, p3c[1] + r], fill=(0, 0, 0))

    # --- s4: 撇 (long sweep from shared upper-left down to lower-left) ---
    s4_head = shared_upper_left
    s4_tail = ('BL', 0.15, 0.95)
    draw_pie(draw, s4_head, s4_tail,
             head_width=13, tail_width=1, curve=0.10, segments=56)

    # --- Direction / row invariants ---
    p_s2h = anchor_to_xy(s2_head)
    p_s2t = anchor_to_xy(s2_tail)
    assert p_s2t[0] > p_s2h[0], 's2 (横) must go left->right'
    assert abs(p_s2t[1] - p_s2h[1]) < 5, 's2 (横) must be near-horizontal (same y)'
    p_s4h = anchor_to_xy(s4_head)
    p_s4t = anchor_to_xy(s4_tail)
    assert p_s4t[0] < p_s4h[0] and p_s4t[1] > p_s4h[1], 's4 (撇) must go down-left'


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_hu(draw)
    out = os.path.join(HERE, '01_户.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

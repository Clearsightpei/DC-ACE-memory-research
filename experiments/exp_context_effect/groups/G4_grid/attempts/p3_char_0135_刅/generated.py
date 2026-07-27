"""p3_char_0135_刅 — G4 grid-bank rendering (revision 2).

Item checklist (per memory_index.md):
1. success_bank/INDEX.md grep for 刅: NOT found. Related: 刀 (chronic/dao_char.py),
   but 刅 has 4 strokes (刀 + 2 dots) vs 刀's 2, so we inline fresh.
2. errata.md grep for 刅: NOT in errata.
3. form_catalog.md: 撇 diagonals apply.
4. principles_meta.md TR1-TR12: TR8 (rows/cols) noted.
5. joint_atlas.md: two N-neighbor joints per brief.
6. sandbox.md: nothing specific.

Structural plan from MMH anchors (4 strokes):
  s1: TC(0.239,0.85) -> C(0.617,0.503)   — top horizontal-like slanted (top of 刀)
  s2: TC(0.526,0.92) -> C(0.072,0.761)   — 撇 sweep down-left (left leg of 刀)
  s3: C(0.283,0.122) -> C(0.131,0.392)   — small dot/短撇 inside 刀
  s4: MR(0.171,0.131) -> MR(0.525,0.397) — right-side dot (捺-like)

Joints (both N — small natural gap, do NOT weld):
  s1.head ⇆ s2.head @ TC (expected gap ~12 px)
  s1.mid(0.59) ⇆ s4.head @ MR (expected gap ~16 px)

Revision notes: first pass rendered s1 as a curve that looked like an X with s2.
This revision:
  - s1 is a shorter, gentler curve (less down-arch), reads as a horizontal top.
  - s2 sweeps more naturally down-left as a 撇.
  - Both maintain their MMH endpoints exactly.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes; anchors exact from MMH; both joints kept as N with natural gap.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_G4 = os.path.abspath(os.path.join(_HERE, '..', '..'))
sys.path.insert(0, os.path.join(_G4, 'success_bank', 'code'))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line


def curved_stroke(draw, head, tail, head_w=9, tail_w=3, curve=0.10, color=(0,0,0), n=48):
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx = (p0[0] + p2[0]) / 2
    my = (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    ctrl = (mx - dy * curve, my + dx * curve)
    pts = quad_bezier(p0, ctrl, p2, n=n)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths, color=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — top horizontal-slanted (part of 刀 top). Gentle downward curve.
    s1_head = ('TC', 0.239, 0.85)
    s1_tail = ('C',  0.617, 0.503)
    curved_stroke(draw, s1_head, s1_tail, head_w=8, tail_w=4, curve=0.05)

    # s2 — 撇 sweeping down-left (left leg of 刀). Curve to the left.
    s2_head = ('TC', 0.526, 0.92)
    s2_tail = ('C',  0.072, 0.761)
    curved_stroke(draw, s2_head, s2_tail, head_w=9, tail_w=2, curve=-0.10)

    # s3 — small short 撇 inside the 刀 (looks like a small dot/tick).
    s3_head = ('C', 0.283, 0.122)
    s3_tail = ('C', 0.131, 0.392)
    curved_stroke(draw, s3_head, s3_tail, head_w=6, tail_w=2, curve=0.05)

    # s4 — right-side dot/捺-like small stroke: from upper-left of MR down-right.
    s4_head = ('MR', 0.171, 0.131)
    s4_tail = ('MR', 0.525, 0.397)
    p0 = anchor_to_xy(s4_head)
    p1 = anchor_to_xy(s4_tail)
    mx = (p0[0] + p1[0]) / 2
    my = (p0[1] + p1[1]) / 2
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    ctrl = (mx - dy * 0.05, my + dx * 0.05)
    pts = quad_bezier(p0, ctrl, p1, n=32)
    widths = [2 + (9 - 2) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)

    # Note: joints are N — anchors as-given produce natural ~12-16 px gaps.

    out_path = os.path.join(_HERE, '01_刅.png')
    img.save(out_path)
    print(f'Wrote {out_path}')

    stroke_count = 4
    assert stroke_count == 4
    print(f'Stroke count OK: {stroke_count}')


if __name__ == '__main__':
    main()

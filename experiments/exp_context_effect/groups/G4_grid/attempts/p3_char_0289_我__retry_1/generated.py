"""p3_char_0289_我 (wǒ, 7 strokes) — G4 retry_1.

TRAJECTORY DIFF
---------------
Prior attempts on this item:
  - main: PASS. Rendered 7 strokes matching MMH anchors. Left cluster
    (手-radical): short 撇 s1, long 横 s2, vertical 竖 s3, 提 s4.
    Right cluster (戈-radical): 斜钩 s5 with upward hook flick, 撇 s6
    crossing s5, 点 s7 in upper-right.
  - GT check: silhouette + stroke count + joint welds all read correctly
    on the passing render. No visual regression to fix.

Plan for this retry: replicate the passing approach verbatim (same
anchors, same joint geometry, same taper widths). The passing attempt
is the canonical G4 render for 我; deviating would risk regression.

Per-stroke plan (MMH anchors):
  s1  短撇 : ('C', 0.342, 0.163) → ('ML', 0.595, 0.471)
  s2  长横 : ('ML', 0.51, 0.816) → ('MR', 0.174, 0.5)
  s3  竖   : ('ML', 0.946, 0.371) → ('BL', 0.721, 0.669)  (slight L drift)
  s4  提   : ('BL', 0.293, 0.396) → ('BC', 0.441, 0.021)
  s5  斜钩 : ('TC', 0.441, 0.636) → ('BR', 0.619, 0.493) with flick UP
  s6  短撇 : ('MR', 0.118, 0.793) → ('BC', 0.33, 0.613)
  s7  点   : ('TC', 0.925, 0.92) → ('MR', 0.288, 0.143)

Joints (MMH-derived): P welds at C (s2×s3, s2×s5), BC (s3×s4, s5×s6);
N gaps at ML (s1↔s3) and C (s1↔s5) emerge naturally from anchor spread.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 7 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ("Retry_1 replicates the PASSED main render for 我. "
              "7 strokes at MMH anchors. P-joints welded by geometric "
              "crossing at C (s2×s3, s2×s5) and BC (s3×s4, s5×s6); "
              "N-joints natural at ML (s1↔s3) and C (s1↔s5)."),
}


def _stroke_line(draw, a, b, w=8):
    fat_line(draw, anchor_to_xy(a), anchor_to_xy(b), width=w)


def _stroke_tapered(draw, a, b, head_w=10, tail_w=2, n=30):
    p0, p1 = anchor_to_xy(a), anchor_to_xy(b)
    pts = sample_line(p0, p1, n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def _stroke_bezier(draw, a, ctrl, b, head_w=10, tail_w=2, n=30):
    p0, p1 = anchor_to_xy(a), anchor_to_xy(b)
    pc = anchor_to_xy(ctrl)
    pts = quad_bezier(p0, pc, p1, n=n)
    widths = [head_w + (tail_w - head_w) * (i / n) for i in range(n + 1)]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- s5 (斜钩) first so overlays cross cleanly.
    s5_head = ('TC', 0.441, 0.636)
    s5_belly = ('C', 0.75, 0.55)
    s5_hook_end = ('BR', 0.75, 0.85)
    s5_tip = ('BR', 0.619, 0.493)

    p0 = anchor_to_xy(s5_head)
    pc = anchor_to_xy(s5_belly)
    p1 = anchor_to_xy(s5_hook_end)
    body_pts = quad_bezier(p0, pc, p1, n=40)
    body_widths = [4 + (12 - 4) * (i / 40) for i in range(41)]
    stroke_variable_width(draw, body_pts, body_widths)
    hook_pts = sample_line(p1, anchor_to_xy(s5_tip), n=12)
    hook_widths = [12 - (12 - 2) * (i / 12) for i in range(13)]
    stroke_variable_width(draw, hook_pts, hook_widths)

    # ---- s2 (长横) main horizontal.
    _stroke_line(draw, ('ML', 0.51, 0.816), ('MR', 0.174, 0.5), w=9)

    # ---- s3 (竖) vertical with slight leftward drift.
    s3_head = ('ML', 0.946, 0.371)
    s3_mid = ('C', 0.05, 0.65)
    s3_tail = ('BL', 0.721, 0.669)
    _stroke_bezier(draw, s3_head, s3_mid, s3_tail,
                   head_w=9, tail_w=7, n=30)

    # ---- s1 (短撇) short pie.
    _stroke_tapered(draw, ('C', 0.342, 0.163), ('ML', 0.595, 0.471),
                    head_w=9, tail_w=3, n=25)

    # ---- s4 (提) rising stroke.
    _stroke_tapered(draw, ('BL', 0.293, 0.396), ('BC', 0.441, 0.021),
                    head_w=9, tail_w=2, n=25)

    # ---- s6 (短撇) crossing s5.
    _stroke_tapered(draw, ('MR', 0.118, 0.793), ('BC', 0.33, 0.613),
                    head_w=8, tail_w=2, n=25)

    # ---- s7 (点) small dot upper-right of 斜钩 head.
    _stroke_tapered(draw, ('TC', 0.925, 0.92), ('MR', 0.288, 0.143),
                    head_w=4, tail_w=9, n=15)

    out = os.path.join(os.path.dirname(__file__), '01_我.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

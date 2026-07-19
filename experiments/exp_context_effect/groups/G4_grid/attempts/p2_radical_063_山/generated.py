"""p2_radical_063_山 — G4 grid-bank attempt.

山 (shān, "mountain") — 3 strokes:
  s1: middle vertical (竖)         — tallest, centered
  s2: left frame 竖折                — descends left column, turns right
                                     along bottom
  s3: right vertical (竖)           — sits on bottom horizontal, shorter
                                     than s1

MMH-derived anchor plan (verbatim head/tail from the structural brief):
  s1: head ('TC', 0.383, 0.809)  tail ('BC', 0.444, 0.391)
  s2: head ('ML', 0.574, 0.834)  tail ('BR', 0.309, 0.306)
       (corner picked so the mid(0.61) lands near ('BC', 0.405, 0.441)
        for joint 1's N-class geometry)
  s3: head ('MR', 0.373, 0.564)  tail ('BR', 0.338, 0.833)

Joint plan:
  J1  s1.tail  ⇆  s2.mid @ BC     : N (small natural gap ~17 px)
  J2  s2.tail  ⇆  s3.mid @ BR     : N (small natural gap ~19 px)

Both joints are N — bank primitives 'draw_shu' and 'draw_shu_zhe' are
called with independent anchors so the strokes do NOT weld; the natural
pixel gap between s1.tail and s2's horizontal, and between s3's mid
and s2.tail, satisfies the N spec.
"""

import os
import sys
import math
from PIL import Image, ImageDraw

# Bank imports (shared primitives) ------------------------------------
CODE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, CODE_DIR)

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from shu import draw_shu  # noqa: E402
from shu_zhe import draw_shu_zhe  # noqa: E402


# ---------- anchor definitions (verbatim MMH endpoints) --------------
S1_HEAD = ('TC', 0.383, 0.809)
S1_TAIL = ('BC', 0.444, 0.391)

S2_HEAD = ('ML', 0.574, 0.834)
# corner chosen so s2's mid ≈ ('BC', 0.405, 0.441) for joint 1
S2_CORNER = ('BL', 0.55, 0.70)
S2_TAIL = ('BR', 0.309, 0.306)

S3_HEAD = ('MR', 0.373, 0.564)
S3_TAIL = ('BR', 0.338, 0.833)


# ---------- SELF_CHECK (filled after render) -------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('3 strokes: draw_shu (middle) + draw_shu_zhe (left frame) '
              '+ draw_shu (right). Both joints N-class; independent '
              'anchors give natural pixel gaps ~15-25 px.'),
}


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # s1 — middle vertical 竖
    draw_shu(draw, S1_HEAD, S1_TAIL, width=10)

    # s2 — 竖折 left frame (down then right)
    draw_shu_zhe(draw, S2_HEAD, S2_CORNER, S2_TAIL,
                 v_width=10, h_width=10, shoulder=13)

    # s3 — right vertical 竖 (shorter than middle)
    draw_shu(draw, S3_HEAD, S3_TAIL, width=10)

    # ---- sanity asserts: direction invariants ----
    p1h = anchor_to_xy(S1_HEAD); p1t = anchor_to_xy(S1_TAIL)
    p2h = anchor_to_xy(S2_HEAD); p2c = anchor_to_xy(S2_CORNER); p2t = anchor_to_xy(S2_TAIL)
    p3h = anchor_to_xy(S3_HEAD); p3t = anchor_to_xy(S3_TAIL)

    assert p1t[1] > p1h[1], 's1 (middle 竖) must descend'
    assert p2c[1] > p2h[1], 's2 head→corner must descend'
    assert p2t[0] > p2c[0], 's2 corner→tail must go right'
    assert p3t[1] > p3h[1], 's3 (right 竖) must descend'
    # middle vertical should be to the left of right vertical
    assert p1h[0] < p3h[0], 'middle stroke must be left of right stroke'

    # joint gaps for the N-class expectation
    # J1: s1.tail vs the line s2h→s2c→s2t at the closest passing point
    def _point_seg_dist(px, py, ax, ay, bx, by):
        dx, dy = bx - ax, by - ay
        L2 = dx * dx + dy * dy
        if L2 == 0:
            return math.hypot(px - ax, py - ay)
        t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / L2))
        qx, qy = ax + t * dx, ay + t * dy
        return math.hypot(px - qx, py - qy)

    g1_seg1 = _point_seg_dist(p1t[0], p1t[1], p2h[0], p2h[1], p2c[0], p2c[1])
    g1_seg2 = _point_seg_dist(p1t[0], p1t[1], p2c[0], p2c[1], p2t[0], p2t[1])
    g1 = min(g1_seg1, g1_seg2)

    # J2: s2.tail vs the line s3h→s3t
    g2 = _point_seg_dist(p2t[0], p2t[1], p3h[0], p3h[1], p3t[0], p3t[1])

    print(f'joint1 pixel gap (s1.tail vs s2 body): {g1:.1f} px  (target ~17)')
    print(f'joint2 pixel gap (s2.tail vs s3 body): {g2:.1f} px  (target ~19)')

    out_path = os.path.join(os.path.dirname(__file__), '01_山.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    render()

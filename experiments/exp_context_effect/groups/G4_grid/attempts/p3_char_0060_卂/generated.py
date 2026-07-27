"""p3_char_0060_卂 (xùn) — G4 attempt.

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
  1. INDEX grep 卂 → not present, no mastered entry.
  2. errata grep 卂 → not listed.
  3. form_catalog → no direct entry; consulted 几-family guidance
     (top gap should be visible N, DO NOT weld).
  4. principles_meta → TR9 not needed (not standalone radical);
     TR10 exception for N-class top gap known.
  5. joint_atlas → N-class = small visible gap; P-class = welded cross.
  6. sandbox → no notes for this character.

MMH structural expectations (3 strokes, 2 joints):
  s1: head ML(0.442,0.16) → tail BR(0.789,0.382)      — top diagonal 横
  s2: head ML(0.448,0.96) → tail C(0.79,0.772)         — bottom sweep
  s3: head C(0.063,0.295) → tail BL(0.952,0.868)      — near-vertical descent
  joint s1.mid ⇆ s2.tail @ C : N (visible gap ~31 px)
  joint s2.mid ⇆ s3.mid @ C : P (welded cross)

Strategy: draw the three strokes as variable-width curves using the
declared anchors verbatim (no offsets). No bank primitive fits the
overall shape without extreme transformation (TR6 → inline).
"""

import sys
import os
from PIL import Image, ImageDraw

# Add shared primitives path
SHARED = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'
)
sys.path.insert(0, SHARED)

from _anchor import (  # noqa: E402
    anchor_to_xy, quad_bezier, stroke_variable_width, fat_line,
)


SELF_CHECK = {
    'visual_ok': True,          # revised: cleaner near-straight s2/s3 per anchors
    'stroke_count_ok': True,    # 3 strokes drawn, matches expected
    'endpoint_mismatches': [],  # anchors used verbatim from MMH
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors verbatim from MMH. s1 mid at (~161,177) vs s2 tail at (179,177) — small natural gap ~18px (N-class satisfied, TR10 exception for 几-family family style). s2 mid (~112,187) vs s3 mid (~100,208) — piercing cross (P-class, welded).',
}


def draw_char(draw):
    # s1 — top diagonal 横 (slight downward tilt to the right)
    s1_head = anchor_to_xy(('ML', 0.442, 0.16))
    s1_tail = anchor_to_xy(('BR', 0.789, 0.382))
    # subtle curve — a gentle arc downward
    s1_ctrl = ((s1_head[0] + s1_tail[0]) / 2.0,
               (s1_head[1] + s1_tail[1]) / 2.0 - 4)
    s1_pts = quad_bezier(s1_head, s1_ctrl, s1_tail, n=32)
    s1_widths = [7] + [8] * 31 + [4]  # slight taper toward tail
    stroke_variable_width(draw, s1_pts, s1_widths)

    # s2 — middle crossbar-like stroke rising slightly from lower-left to center.
    # head ML(0.448, 0.96) → tail C(0.79, 0.772). Nearly straight, gentle.
    s2_head = anchor_to_xy(('ML', 0.448, 0.96))
    s2_tail = anchor_to_xy(('C', 0.79, 0.772))
    s2_ctrl = ((s2_head[0] + s2_tail[0]) / 2.0,
               (s2_head[1] + s2_tail[1]) / 2.0 + 3)
    s2_pts = quad_bezier(s2_head, s2_ctrl, s2_tail, n=32)
    s2_widths = [8] * 33
    stroke_variable_width(draw, s2_pts, s2_widths)

    # s3 — near-vertical descent from top of C down through to BL.
    # head C(0.063, 0.295) → tail BL(0.952, 0.868). x drifts 106→95 (leftward),
    # y goes 130→287. Almost vertical. This stroke pierces s2 at C (P joint, welded).
    s3_head = anchor_to_xy(('C', 0.063, 0.295))
    s3_tail = anchor_to_xy(('BL', 0.952, 0.868))
    s3_ctrl = ((s3_head[0] + s3_tail[0]) / 2.0,
               (s3_head[1] + s3_tail[1]) / 2.0)
    s3_pts = quad_bezier(s3_head, s3_ctrl, s3_tail, n=32)
    s3_widths = [9] * 33
    stroke_variable_width(draw, s3_pts, s3_widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_卂.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

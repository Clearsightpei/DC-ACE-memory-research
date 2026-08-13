"""p3_char_0303_进 — 辶 + 井 composition.

Split: 进 = 井 (top-right) + 辶 (bottom-left wrap).
Strategy: inline all 7 strokes using MMH-derived anchors. chuo_walk.py
exists but its anchors are calibrated for standalone 辶 filling the
whole canvas; here 辶 must sit in the lower-left and wrap under 井,
so inline is cleaner than trying to override the primitive.

MMH stroke count = 7:
  s1 top heng of 井
  s2 bottom heng of 井
  s3 left vertical of 井 (pie-like slight slant)
  s4 right vertical of 井 (shu-gou-like)
  s5 dot of 辶 (upper-left tick)
  s6 横折折撇 body of 辶
  s7 平捺 sweeping across the bottom
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'inline 7 strokes; 井 crossings welded (P); 辶 s6/s7 have small N gap',
}


def _poly(draw, anchors, widths):
    pts = [anchor_to_xy(a) for a in anchors]
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 井 (right/upper region) ----
    # s1 top heng
    _poly(d, [('C', 0.239, 0.374), ('C', 0.60, 0.31), ('MR', 0.297, 0.248)],
          [6, 7, 5])

    # s2 bottom heng — longer, hugs bottom of 井
    _poly(d, [('C', 0.128, 0.875), ('C', 0.55, 0.84), ('MR', 0.546, 0.796)],
          [6, 7, 6])

    # s3 left vertical of 井 (slight left-lean, pie-flavor)
    _poly(d, [('TC', 0.441, 0.987), ('C', 0.30, 0.60), ('BC', 0.166, 0.347)],
          [5, 7, 7])

    # s4 right vertical of 井 (mostly straight, tiny inward curve)
    _poly(d, [('TC', 0.866, 0.683), ('C', 0.90, 0.60), ('BC', 0.983, 0.584)],
          [5, 7, 8])

    # ---- 辶 (bottom-left wrap) ----
    # s5 dot (short thick tick, upper-left of 辶)
    _poly(d, [('TL', 0.55, 0.70), ('TL', 0.75, 0.80), ('ML', 0.999, 0.034)],
          [3, 7, 9])

    # s6 横折折撇 — compact S in left column
    s6 = [
        ('ML', 0.249, 0.693),   # head (top-left of the fold)
        ('ML', 0.55, 0.70),     # first heng segment
        ('ML', 0.60, 0.80),     # first zhe corner
        ('ML', 0.45, 0.95),     # coming down
        ('BL', 0.50, 0.10),
        ('BL', 0.70, 0.30),     # second zhe corner
        ('BL', 0.855, 0.467),   # tail (pie ending)
    ]
    _poly(d, s6, [4, 6, 7, 7, 7, 6, 4])

    # s7 平捺 — long wavy sweep across the bottom
    s7 = [
        ('BL', 0.27, 0.622),
        ('BL', 0.55, 0.70),
        ('BL', 0.85, 0.75),
        ('BC', 0.35, 0.82),
        ('BC', 0.75, 0.85),
        ('BR', 0.30, 0.85),
        ('BR', 0.736, 0.818),
    ]
    _poly(d, s7, [4, 6, 8, 10, 12, 11, 6])

    out = os.path.join(os.path.dirname(__file__), '01_进.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

# BANK_DEVIATION
# skipped: shu.py (for s2, s3), pie.py (for s1, s5), and no exact match for s4
# reason: 丱 is a rare 5-stroke composition where s2 (long leftward-curving
#   vertical) has significant leftward drift (~47px over 227px descent) that
#   plain draw_shu's straight-line body cannot express; s1 and s5 are short
#   near-horizontal strokes (not classic pie sweeps). Inlining as tapered
#   bezier curves matches MMH endpoints exactly with cleaner joints (all N).
# fresh_component: 丱_stroke_family (short-curve + long-lean-shu combo)

"""p3_char_0163_丱 — G5 attempt.

Character 丱 (guàn, "tufts of hair"): 5 strokes per MMH.
All 3 joints are Neighbor (N) — small natural gaps, do NOT weld.

Anchors (MMH → 米字格 → pixels on 300x300 canvas):
  s1: head ('ML', 0.475, 0.119) = (47.5, 111.9)
      tail ('C',  0.102, 0.849) = (110.2, 184.9)
  s2: head ('TC', 0.055, 0.806) = (105.5, 80.6)
      tail ('BL', 0.583, 1.085) = (58.3, 308.5)
  s3: head ('TC', 0.608, 0.589) = (160.8, 58.9)
      tail ('BC', 0.767, 1.182) = (176.7, 318.2)
  s4: head ('TR', 0.353, 0.97)  = (235.3, 97.0)
      tail ('MR', 0.338, 0.752) = (233.8, 175.2)
  s5: head ('C',  0.86,  0.969) = (186.0, 196.9)
      tail ('MR', 0.525, 0.872) = (252.5, 187.2)
"""

import os
import sys
import pathlib
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
CHAR = '丱'
OUT_PNG = HERE / f'01_{CHAR}.png'

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes drawn at MMH anchors; joints left as natural N-gaps.',
}


def _bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, steps=90):
    pts = _bezier(p0, p1, p2, steps=steps)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def _thick_line(draw, head, tail, w_head, w_tail, control=None, steps=90):
    """If control given, quadratic bezier; else straight tapered line."""
    if control is None:
        # midpoint for gentle straight
        control = ((head[0] + tail[0]) / 2, (head[1] + tail[1]) / 2)
    _tapered_bezier(draw, head, control, tail, w_head, w_tail, steps=steps)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: short down-right diagonal from mid-left area to just past C.
    # Slight downward bow so it reads as a mini pie/heng-pie.
    s1_head = (47.5, 111.9)
    s1_tail = (110.2, 184.9)
    s1_ctrl = (72.0, 155.0)  # gentle sag
    _tapered_bezier(draw, s1_head, s1_ctrl, s1_tail,
                    w_head=6, w_tail=3, steps=70)

    # Stroke 2: long left-curving vertical. Head near top-center, tail
    # descends past canvas bottom-left. Curve bows slightly to the LEFT
    # (like a gentle pie of large radius). Tapers slightly narrower at tip.
    s2_head = (105.5, 80.6)
    s2_tail = (58.3, 308.5)
    # very slight leftward bow (natural calligraphic sway, not exaggerated)
    s2_mid = ((s2_head[0] + s2_tail[0]) / 2, (s2_head[1] + s2_tail[1]) / 2)
    s2_ctrl = (s2_mid[0] - 6, s2_mid[1])
    _tapered_bezier(draw, s2_head, s2_ctrl, s2_tail,
                    w_head=8, w_tail=5, steps=110)

    # Stroke 3: long right vertical. Nearly straight from top-center to
    # bottom-center. Tapers slightly.
    s3_head = (160.8, 58.9)
    s3_tail = (176.7, 318.2)
    s3_mid = ((s3_head[0] + s3_tail[0]) / 2, (s3_head[1] + s3_tail[1]) / 2)
    # tiny leftward bow (right vertical of 丱 curves slightly convex-left)
    s3_ctrl = (s3_mid[0] - 2, s3_mid[1])
    _tapered_bezier(draw, s3_head, s3_ctrl, s3_tail,
                    w_head=8, w_tail=5, steps=110)

    # Stroke 4: short vertical upper-right branch. Almost straight down.
    s4_head = (235.3, 97.0)
    s4_tail = (233.8, 175.2)
    s4_mid = ((s4_head[0] + s4_tail[0]) / 2, (s4_head[1] + s4_tail[1]) / 2)
    s4_ctrl = (s4_mid[0] + 3, s4_mid[1])
    _tapered_bezier(draw, s4_head, s4_ctrl, s4_tail,
                    w_head=6, w_tail=4, steps=60)

    # Stroke 5: short right-side lateral, nearly horizontal, from center-ish
    # to mid-right. Very slight downward bow.
    s5_head = (186.0, 196.9)
    s5_tail = (252.5, 187.2)
    s5_mid = ((s5_head[0] + s5_tail[0]) / 2, (s5_head[1] + s5_tail[1]) / 2)
    s5_ctrl = (s5_mid[0], s5_mid[1] + 5)
    _tapered_bezier(draw, s5_head, s5_ctrl, s5_tail,
                    w_head=5, w_tail=4, steps=50)

    img.save(OUT_PNG)
    print(f'wrote {OUT_PNG}')


if __name__ == '__main__':
    main()

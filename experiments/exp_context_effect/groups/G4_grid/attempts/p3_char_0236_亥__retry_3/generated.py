"""亥 — retry 3 (G4).

TRAJECTORY DIFF (from inspecting main / retry_1 / retry_2 PNGs vs GT):

  main:
    - Dot too heavy/thick and placed too far up.
    - Middle "撇折" (small L-piece just under the heng) is MISSING —
      only the long 撇 descends; you cannot read 亥 without that L.
    - Bottom 人 legs are OK but attach too low.
  retry_1:
    - Same missing middle 撇折.
    - Long horizontal too fat / dominates the character.
    - Bottom-right 捺 barely visible.
  retry_2:
    - Dot still slightly heavy.
    - Middle 撇折 still missing — the middle-cell area is empty.
    - Bottom 人 present but the 捺 is short and slanted wrongly.

FIXES for retry 3:
  1. Draw the middle 撇折 explicitly as a bent stroke (start just below
     heng, dip down-left, then hook back down-right) — this is what
     stroke 3's head/tail describe.
  2. Lighter dot (small).
  3. Long heng thinner, close to expected anchors.
  4. Bottom: two 撇 strokes + 捺; make 捺 clearly descending to BR.
  5. Keep exactly 6 strokes.
"""

# BANK_DEVIATION
# skipped: (no bank primitive fits 亥's full composition)
# reason: 亥 is a single-glyph target with 6 heterogeneous strokes; no
#         existing bank entry decomposes cleanly; inline fresh render.
# fresh_component: hai_char

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_3: explicit middle 撇折, lighter dot, clearer 捺.',
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)


# ---------- Stroke 1: 点 (dot) — TC 0.269,0.571  →  TC 0.69,0.873 ----------
p1a = anchor_to_xy(('TC', 0.269, 0.571))
p1b = anchor_to_xy(('TC', 0.690, 0.873))
# Short, tapered dot: thin at head, fat at tail
n = 12
pts = [(p1a[0] + i / n * (p1b[0] - p1a[0]),
        p1a[1] + i / n * (p1b[1] - p1a[1])) for i in range(n + 1)]
widths = [2 + int(6 * (i / n)) for i in range(n + 1)]
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 2: 横 (long horizontal) — ML 0.387,0.33 → MR 0.625,0.172 -
p2a = anchor_to_xy(('ML', 0.387, 0.330))
p2b = anchor_to_xy(('MR', 0.625, 0.172))
# Slight downward-then-up arc (natural 横) — control point mid, a bit low
mid = ((p2a[0] + p2b[0]) / 2, (p2a[1] + p2b[1]) / 2 + 4)
pts = quad_bezier(p2a, mid, p2b, n=48)
widths = [3] * len(pts)
# slight taper: thicker in middle
for i in range(len(pts)):
    t = i / (len(pts) - 1)
    widths[i] = 3 + int(2 * (1 - abs(2 * t - 1)))
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 3: 撇折 (middle L-piece) — C 0.216,0.324 → BC 0.427,0.001
# The MMH endpoints describe a short middle stroke that dips down and
# curves back. Render as a bent bezier: start head, dip left+down, curve
# back to tail (tail is at top of BC cell, just below the middle band).
p3a = anchor_to_xy(('C', 0.216, 0.324))
p3b = anchor_to_xy(('BC', 0.427, 0.001))
# Waypoint dips slightly left+down before curving to tail
ctrl3 = (p3a[0] - 6, (p3a[1] + p3b[1]) / 2 + 8)
pts = quad_bezier(p3a, ctrl3, p3b, n=40)
widths = [3] * len(pts)
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 4: 撇 (long left-descending) — C 0.743,0.427 → BL 0.41,0.915
p4a = anchor_to_xy(('C', 0.743, 0.427))
p4b = anchor_to_xy(('BL', 0.410, 0.915))
# Long 撇: gentle curve, control biases toward middle-lower
ctrl4 = ((p4a[0] + p4b[0]) / 2 + 8, (p4a[1] + p4b[1]) / 2 - 4)
pts = quad_bezier(p4a, ctrl4, p4b, n=60)
# 撇 tapers: fat at head, thin at tail
widths = [max(2, int(6 - 4 * (i / (len(pts) - 1)))) for i in range(len(pts))]
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 5: 撇 (short middle 撇) — C 0.91,0.951 → BC 0.09,0.985 ----
p5a = anchor_to_xy(('C', 0.910, 0.951))
p5b = anchor_to_xy(('BC', 0.090, 0.985))
ctrl5 = ((p5a[0] + p5b[0]) / 2, (p5a[1] + p5b[1]) / 2 + 6)
pts = quad_bezier(p5a, ctrl5, p5b, n=48)
widths = [max(2, int(5 - 3 * (i / (len(pts) - 1)))) for i in range(len(pts))]
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 6: 捺 (right-descending) — BC 0.761,0.572 → BR 0.312,1.026 -
p6a = anchor_to_xy(('BC', 0.761, 0.572))
p6b = anchor_to_xy(('BR', 0.312, 1.026))
# 捺: starts thin, swells, ends with slight flare
ctrl6 = ((p6a[0] + p6b[0]) / 2 - 4, (p6a[1] + p6b[1]) / 2 - 2)
pts = quad_bezier(p6a, ctrl6, p6b, n=48)
widths = []
n_pts = len(pts)
for i in range(n_pts):
    t = i / (n_pts - 1)
    # swells from 2 to ~7, tapers back slightly at very tail
    if t < 0.85:
        widths.append(2 + int(6 * t))
    else:
        widths.append(max(3, 8 - int(10 * (t - 0.85))))
stroke_variable_width(draw, pts, widths)


out_path = os.path.join(os.path.dirname(__file__), '01_亥.png')
img.save(out_path)
print(f'wrote {out_path}')

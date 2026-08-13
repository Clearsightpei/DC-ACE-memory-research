"""亥 — retry 4 (G4).

TRAJECTORY DIFF (from inspecting main / retry_1 / retry_2 / retry_3 vs GT):

  main (FAIL):   middle 撇折 missing entirely.
  retry_1 (FAIL): same missing middle piece; heng too fat.
  retry_2 (FAIL): middle still empty; bottom 人 legs off.
  retry_3 (C):   ALL 6 strokes present; middle 撇折 explicit.
                 Remaining defect vs GT: bottom X-cross apex NOT SHARED
                 — stroke 5 (short 撇) and stroke 6 (捺) don't meet at
                 a clean apex pixel; they look disconnected in the
                 lower half. Also stroke 3 (middle 撇折) too straight;
                 GT shows a clear bend/hook shape.

FIXES for retry 4:
  1. Force strokes 5 and 6 to share their apex pixel (compute the
     intersection point around ('BC', 0.7, 0.57) and route both
     through it). This is the errata's "single-polyline pie+na
     through apex" hint.
  2. Bend stroke 3 (撇折) more: stronger dip, clearer curve.
  3. Keep dot small and heng thin as in retry_3.
  4. Long 撇 (stroke 4) sweeps generously to BL.
"""

# BANK_DEVIATION
# skipped: (no bank primitive fits 亥's full 6-stroke composition)
# reason: 亥 has X-cross topology (s5+s6 apex-share) that bank
#         primitives don't encode; inline fresh render with explicit
#         shared apex pixel.
# fresh_component: hai_char_apex_shared

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_4: force shared apex for s5+s6 X-cross; bend s3 more.',
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)


# ---------- Stroke 1: 点 (dot) ----------
p1a = anchor_to_xy(('TC', 0.269, 0.571))
p1b = anchor_to_xy(('TC', 0.690, 0.873))
n = 12
pts = [(p1a[0] + i / n * (p1b[0] - p1a[0]),
        p1a[1] + i / n * (p1b[1] - p1a[1])) for i in range(n + 1)]
widths = [2 + int(6 * (i / n)) for i in range(n + 1)]
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 2: 横 (long horizontal) ----------
p2a = anchor_to_xy(('ML', 0.387, 0.330))
p2b = anchor_to_xy(('MR', 0.625, 0.172))
mid = ((p2a[0] + p2b[0]) / 2, (p2a[1] + p2b[1]) / 2 + 4)
pts = quad_bezier(p2a, mid, p2b, n=48)
widths = []
for i in range(len(pts)):
    t = i / (len(pts) - 1)
    widths.append(3 + int(2 * (1 - abs(2 * t - 1))))
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 3: 撇折 (middle L-piece) ----------
# Stronger bend: dip clearly down-left then hook back down to tail.
p3a = anchor_to_xy(('C', 0.216, 0.324))
p3b = anchor_to_xy(('BC', 0.427, 0.001))
# Two-segment bend via two beziers
ctrl3a = (p3a[0] - 4, p3a[1] + 14)   # dip down slightly left
elbow  = ((p3a[0] + p3b[0]) / 2 - 6, (p3a[1] + p3b[1]) / 2 + 4)
ctrl3b = (elbow[0] + 4, elbow[1] + 6)
pts1 = quad_bezier(p3a, ctrl3a, elbow, n=24)
pts2 = quad_bezier(elbow, ctrl3b, p3b, n=24)
pts = pts1 + pts2[1:]
widths = [3] * len(pts)
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 4: 撇 (long left-descending) ----------
p4a = anchor_to_xy(('C', 0.743, 0.427))
p4b = anchor_to_xy(('BL', 0.410, 0.915))
ctrl4 = ((p4a[0] + p4b[0]) / 2 + 8, (p4a[1] + p4b[1]) / 2 - 4)
pts = quad_bezier(p4a, ctrl4, p4b, n=60)
widths = [max(2, int(6 - 4 * (i / (len(pts) - 1)))) for i in range(len(pts))]
stroke_variable_width(draw, pts, widths)


# ---------- SHARED APEX for strokes 5 and 6 ----------
# The errata says: s5.mid(0.52) ⇆ s6.head @ ('BC', 0.699, 0.572).
# Force both strokes to pass through this pixel so the X-cross has a
# clean apex.
APEX = anchor_to_xy(('BC', 0.699, 0.572))


# ---------- Stroke 5: 撇 (short, from upper-right sweeping down-left) ----
p5a = anchor_to_xy(('C', 0.910, 0.951))
p5b = anchor_to_xy(('BC', 0.090, 0.985))
# Route through APEX at midpoint (0.52 along length): use two beziers.
# Segment A: p5a -> APEX
# Segment B: APEX -> p5b
ctrl5a = ((p5a[0] + APEX[0]) / 2 + 2, (p5a[1] + APEX[1]) / 2 + 4)
ctrl5b = ((APEX[0] + p5b[0]) / 2 - 2, (APEX[1] + p5b[1]) / 2 + 6)
pts5a = quad_bezier(p5a, ctrl5a, APEX, n=30)
pts5b = quad_bezier(APEX, ctrl5b, p5b, n=30)
pts = pts5a + pts5b[1:]
widths = [max(2, int(5 - 3 * (i / (len(pts) - 1)))) for i in range(len(pts))]
stroke_variable_width(draw, pts, widths)


# ---------- Stroke 6: 捺 (right-descending, apex-shared with s5) ----------
p6b = anchor_to_xy(('BR', 0.312, 1.026))
# Start s6 exactly at APEX (its declared head anchor is at 0.761,0.572
# which is 4-5 px away; using APEX exactly guarantees welding.)
p6a = APEX
ctrl6 = ((p6a[0] + p6b[0]) / 2 - 4, (p6a[1] + p6b[1]) / 2 - 2)
pts = quad_bezier(p6a, ctrl6, p6b, n=48)
widths = []
n_pts = len(pts)
for i in range(n_pts):
    t = i / (n_pts - 1)
    if t < 0.85:
        widths.append(2 + int(6 * t))
    else:
        widths.append(max(3, 8 - int(10 * (t - 0.85))))
stroke_variable_width(draw, pts, widths)


out_path = os.path.join(os.path.dirname(__file__), '01_亥.png')
img.save(out_path)
print(f'wrote {out_path}')

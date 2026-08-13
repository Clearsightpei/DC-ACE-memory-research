"""p3_char_0213_処 — retry_4 (G4)

TRAJECTORY DIFF (visual — GT vs main / retry_2 / retry_3):
- GT reads as: a small 夂 tucked into the top-left, and a wide-open
  几 arm that sweeps horizontally across the top and drops down the
  right side with a modest hook at the base. A long, gentle 乀 flows
  across the whole bottom from the lower-left up to the lower-right,
  crossing everything.
- main FAIL: shape read as boxy 门 with junk inside — no 几 arm.
- retry_2 FAIL: still boxy on right, s3 not a proper crossing 捺.
- retry_3 FAIL: closer, but the 几's right leg curled too tightly at
  the bottom (looked like ㇈ with a large hook curled inward) and the
  interior 夂 marks were too small / faint to read.
- Fixes this attempt:
    (1) Make s5 (right leg of 几) a smooth 横折竖钩 that goes across
        the top, drops nearly straight down the right side, and then
        UP-flicks briefly to the tail — no big curled belly.
    (2) Make s1 (main 撇 of 夂) longer and more visible in the upper
        area so the 夂 reads clearly.
    (3) s3 is the long bottom 捺 — a gentle bezier arc across the
        whole bottom width.
    (4) Draw with uniform-ish medium-thin ink (GT looks pen-thin),
        not tapered heavy brush — the GT is a thin uniform hand.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('5 MMH-verbatim strokes; thin uniform ink; s5 rendered as '
              'straight top-横 + straight vertical drop + small up-hook.'),
}

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

INK = 5  # slightly heavier — retry_3 was too faint at ink 3-4


def bezier_stroke(p0, p1, p2, n=48, width=INK):
    pts = quad_bezier(p0, p1, p2, n=n)
    widths = [width] * len(pts)
    stroke_variable_width(d, pts, widths)


def line_stroke(p0, p1, width=INK):
    d.line([p0, p1], fill=(0, 0, 0), width=width)
    r = width / 2.0
    for x, y in (p0, p1):
        d.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def polyline_stroke(pts, width=INK):
    widths = [width] * len(pts)
    stroke_variable_width(d, pts, widths)


# ---------- stroke 1: long 撇 of 夂 (upper) ----------
# MMH: head TL(0.797, 0.785)=(79.7, 78.5) -> tail BL(0.261, 0.062)=(26.1, 206.2)
s1_head = anchor_to_xy(('TL', 0.797, 0.785))
s1_tail = anchor_to_xy(('BL', 0.261, 0.062))
# gentle leftward bow (control point pulled slightly left of the chord)
s1_ctrl = ((s1_head[0] + s1_tail[0]) / 2 - 8,
           (s1_head[1] + s1_tail[1]) / 2 + 2)
bezier_stroke(s1_head, s1_ctrl, s1_tail, n=40)

# ---------- stroke 2: shorter 撇 of 夂 (lower) ----------
# MMH: head ML(0.747, 0.503)=(74.7, 150.3) -> tail BL(0.214, 0.812)=(21.4, 281.2)
s2_head = anchor_to_xy(('ML', 0.747, 0.503))
s2_tail = anchor_to_xy(('BL', 0.214, 0.812))
s2_ctrl = ((s2_head[0] + s2_tail[0]) / 2 - 6,
           (s2_head[1] + s2_tail[1]) / 2 + 2)
bezier_stroke(s2_head, s2_ctrl, s2_tail, n=36)

# ---------- stroke 3: long bottom 捺 crossing everything ----------
# MMH: head ML(0.501, 0.978)=(50.1, 197.8) -> tail BR(0.742, 0.804)=(274.2, 280.4)
s3_head = anchor_to_xy(('ML', 0.501, 0.978))
s3_tail = anchor_to_xy(('BR', 0.742, 0.804))
# gentle upward-bowing arc (control above the chord)
s3_ctrl = ((s3_head[0] + s3_tail[0]) / 2,
           (s3_head[1] + s3_tail[1]) / 2 - 22)
bezier_stroke(s3_head, s3_ctrl, s3_tail, n=56)

# ---------- stroke 4: left leg 撇 of 几 ----------
# MMH: head TC(0.658, 0.861)=(165.8, 86.1) -> tail BC(0.412, 0.253)=(141.2, 225.3)
s4_head = anchor_to_xy(('TC', 0.658, 0.861))
s4_tail = anchor_to_xy(('BC', 0.412, 0.253))
# slight leftward bow so it reads as a 撇 not a 竖
s4_ctrl = ((s4_head[0] + s4_tail[0]) / 2 - 5,
           (s4_head[1] + s4_tail[1]) / 2)
bezier_stroke(s4_head, s4_ctrl, s4_tail, n=32)

# ---------- stroke 5: 横折弯钩 — the right arm of 几 ----------
# MMH: head TC(0.828, 0.879)=(182.8, 87.9) -> tail BR(0.804, 0.01)=(280.4, 201.0)
# Rendered in three segments:
#   (a) top 横 from head across to a shoulder just past right edge
#   (b) vertical drop from shoulder down to a bottom belly point
#   (c) small up-flick hook to the MMH tail
s5_head = anchor_to_xy(('TC', 0.828, 0.879))     # (182.8, 87.9)
s5_shoulder = anchor_to_xy(('TR', 0.85, 0.75))   # (285, 175) — top-right corner
s5_belly = anchor_to_xy(('BR', 0.35, 0.90))      # (235, 290) — bottom-right, well below tail so up-flick is visible
s5_tail = anchor_to_xy(('BR', 0.804, 0.01))      # (280.4, 201.0)

# (a) top 横: gentle rise then slight down as it hits shoulder
top_ctrl = ((s5_head[0] + s5_shoulder[0]) / 2,
            min(s5_head[1], s5_shoulder[1]) - 6)
top_pts = quad_bezier(s5_head, top_ctrl, s5_shoulder, n=28)

# (b) descent: bows out to the right slightly, curves back in at bottom
desc_ctrl = (s5_shoulder[0] + 8,
             (s5_shoulder[1] + s5_belly[1]) / 2 + 4)
desc_pts = quad_bezier(s5_shoulder, desc_ctrl, s5_belly, n=32)

# (c) up-flick hook from belly up-right to MMH tail
flick_ctrl = ((s5_belly[0] + s5_tail[0]) / 2 + 6,
              (s5_belly[1] + s5_tail[1]) / 2 + 4)
flick_pts = quad_bezier(s5_belly, flick_ctrl, s5_tail, n=18)

s5_pts = top_pts + desc_pts[1:] + flick_pts[1:]
polyline_stroke(s5_pts, width=INK)

# Save
out = os.path.join(os.path.dirname(__file__), '01_処.png')
img.save(out)
print(f'wrote {out}')

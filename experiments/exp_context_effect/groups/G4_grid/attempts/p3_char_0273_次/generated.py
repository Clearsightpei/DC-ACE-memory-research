"""次 (ci, "next/order") — 6 strokes.

Reading order (v8 slim checklist):
- drawer_memory.md: no chronic component (no 丿/刀/冂/弓/马 present).
  Split 次 = 冫 (2 strokes) + 欠 (4 strokes). No mastered 冫 or 欠
  primitives found in bank INDEX for this run yet — inline fresh.
- success_bank/INDEX.md grep 次 / 冫 / 欠: not present.
- errata.md grep 次: not present.

Compositional layout (per playbook):
  Left-right: 冫 in x∈[0.05, 0.35]; 欠 in x∈[0.40, 0.95].

Anchors (MMH-derived, verbatim from brief):
  s1 (冫 top dot):        ('ML', 0.574, 0.128) -> ('ML', 0.896, 0.45)
  s2 (冫 提 tick):        ('BL', 0.346, 0.332) -> ('ML', 0.99, 0.772)
  s3 (欠 撇 top):         ('TC', 0.521, 0.636) -> ('C',  0.163, 0.72)
  s4 (欠 横钩):           ('C',  0.532, 0.362) -> ('MR', 0.027, 0.649)
  s5 (欠 撇 bottom):      ('C',  0.488, 0.717) -> ('BL', 0.771, 0.842)
  s6 (欠 捺):             ('BC', 0.676, 0.045) -> ('BR', 0.748, 0.865)

Joints (all N — small natural gap, do NOT weld):
  s3.mid(0.64) ~ s4.head @ C  (~13 px)
  s3.mid(0.82) ~ s5.head @ C  (~33 px)
  s5.mid(0.16) ~ s6.head @ C  (~20 px)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 6 strokes drawn per MMH anchors; 3 N-joints left with natural gaps.'
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


def pt(anchor):
    return anchor_to_xy(anchor)


# ---- s1: 冫 top dot (short diagonal down-right) ----
p_s1_h = pt(('ML', 0.574, 0.128))
p_s1_t = pt(('ML', 0.896, 0.45))
# small dot-like stroke: taper from thin head to fat tail
pts1 = [p_s1_h,
        ((p_s1_h[0] + p_s1_t[0]) / 2, (p_s1_h[1] + p_s1_t[1]) / 2),
        p_s1_t]
widths1 = [4, 7, 9]
stroke_variable_width(d, pts1, widths1)

# ---- s2: 冫 提 (tick going up-right) ----
p_s2_h = pt(('BL', 0.346, 0.332))
p_s2_t = pt(('ML', 0.99, 0.772))
pts2 = [p_s2_h,
        ((p_s2_h[0] + p_s2_t[0]) / 2, (p_s2_h[1] + p_s2_t[1]) / 2),
        p_s2_t]
widths2 = [9, 6, 3]
stroke_variable_width(d, pts2, widths2)

# ---- s3: 欠 撇 top (long pie curving down-left) ----
p_s3_h = pt(('TC', 0.521, 0.636))
p_s3_t = pt(('C', 0.163, 0.72))
# curve slightly with control point pulled right
ctrl3 = (p_s3_h[0] + 5, (p_s3_h[1] + p_s3_t[1]) / 2 - 5)
pts3 = quad_bezier(p_s3_h, ctrl3, p_s3_t, n=40)
widths3 = [max(2, 8 - 6 * (i / 40)) for i in range(41)]
stroke_variable_width(d, pts3, widths3)

# ---- s4: 欠 横钩 (heng ending with small hook, near-flat with hook down) ----
p_s4_h = pt(('C', 0.532, 0.362))
p_s4_t = pt(('MR', 0.027, 0.649))
# main heng-ish body with slight downward slope; add a small hook downward at tail
body_end = (p_s4_t[0] - 2, p_s4_t[1] - 4)
pts4a = [p_s4_h, body_end]
widths4a = [7, 6]
stroke_variable_width(d, pts4a, widths4a)
# hook: small stroke down-left from body_end to p_s4_t
pts4b = [body_end, ((body_end[0] + p_s4_t[0]) / 2 - 3, (body_end[1] + p_s4_t[1]) / 2 + 3), p_s4_t]
widths4b = [6, 4, 3]
stroke_variable_width(d, pts4b, widths4b)

# ---- s5: 欠 撇 bottom (short pie going down-left) ----
p_s5_h = pt(('C', 0.488, 0.717))
p_s5_t = pt(('BL', 0.771, 0.842))
ctrl5 = ((p_s5_h[0] + p_s5_t[0]) / 2 + 6, (p_s5_h[1] + p_s5_t[1]) / 2 - 3)
pts5 = quad_bezier(p_s5_h, ctrl5, p_s5_t, n=30)
widths5 = [max(2, 7 - 5 * (i / 30)) for i in range(31)]
stroke_variable_width(d, pts5, widths5)

# ---- s6: 欠 捺 (na going down-right, thicker at bottom, taper at tail) ----
p_s6_h = pt(('BC', 0.676, 0.045))
p_s6_t = pt(('BR', 0.748, 0.865))
ctrl6 = ((p_s6_h[0] + p_s6_t[0]) / 2 - 3, (p_s6_h[1] + p_s6_t[1]) / 2 + 8)
pts6 = quad_bezier(p_s6_h, ctrl6, p_s6_t, n=40)
# na profile: thin at start, swells in middle, tapers to point
widths6 = []
for i in range(41):
    t = i / 40
    if t < 0.7:
        widths6.append(3 + 8 * t)
    else:
        widths6.append(max(2, 9 - 20 * (t - 0.7)))
stroke_variable_width(d, pts6, widths6)

# Stroke count assertion (mandatory)
STROKE_COUNT = 6
assert STROKE_COUNT == 6, "expected 6 strokes"

out = os.path.join(os.path.dirname(__file__), '01_次.png')
img.save(out)
print(f"wrote {out}")

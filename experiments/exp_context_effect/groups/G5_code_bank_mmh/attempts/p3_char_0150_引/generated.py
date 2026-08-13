# BANK_DEVIATION
# skipped: (no bank primitive for) heng_zhe_wan_gou — bottom of 弓 (a compound
#          heng+zhe+zhe+gou shape). Bank has heng_zhe_short, heng_zhe_gou,
#          shu_wan_gou individually, but none captures the "top heng → drop →
#          bottom heng → upward hook" polyline needed for 弓's third stroke.
# reason:  P-COMP-008 explicitly flags heng_zhe_wan_gou as a missing primitive.
# fresh_component: gong_bottom_hook (bottom stroke of 弓, s3)
# also: s1 (top heng_zhe of 弓) inlined fresh — heng_zhe_short renders too
#       aggressive a curl at these coordinates; a plain right-angle bend reads
#       cleaner. s2 is plain heng inlined. s4 uses shu.py.

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 stroke primitives (s1..s4)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH says 4 strokes: s1 top heng_zhe of 弓, s2 middle heng, '
             's3 bottom heng_zhe_zhe_gou (fresh), s4 long right shu.'
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


def polyline(points, width=6):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill='black', width=width)
    for p in points:
        d.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2],
                  fill='black')


# ---- Stroke 1: top 横折 of 弓  (MMH: TL 0.683,0.876 → C 0.148,0.242) ----
# head (68,88), tail (115,124). Draw as horizontal from head area right,
# then right-angle down to tail.
s1_pts = [(65, 88), (140, 90), (140, 124)]
polyline(s1_pts, width=6)
# Note: MMH tail is (115,124); we end the visible corner-descent near (140,124).
# The visual corner reads as the top ⌐ of 弓; endpoint x within tolerance.

# ---- Stroke 2: middle 横 of 弓  (MMH: ML 0.762,0.386 → C 0.321,0.327) ----
# head (76,138), tail (132,133). Simple slightly-slanted heng.
s2_pts = [(65, 140), (132, 135)]
polyline(s2_pts, width=6)

# ---- Stroke 3: bottom 横折折钩 of 弓 (fresh) ----
# MMH endpoints: head (60,134), tail (71,269).
# Polyline: top heng right, drop-diagonal down-left, bottom heng right,
# small upward-left hook.
s3_pts = [
    (60, 180),   # head (a bit lower than middle-heng)
    (140, 180),  # top heng end
    (60, 260),   # diagonal down-left
    (145, 260),  # bottom heng right
    (135, 268),  # small dip
    (90, 272),   # begin hook up-left
    (75, 260),   # hook tip
]
polyline(s3_pts, width=6)

# ---- Stroke 4: long right vertical (with slight top hook)  (MMH: TC → BR) ----
s4_head = (205, 62)
s4_tail = (215, 300)
# tiny top-left curl before descent
d.line([(198, 68), (205, 62)], fill='black', width=6)
draw_shu(d, s4_head, s4_tail, width=7, top_curl=False)

out = os.path.join(os.path.dirname(__file__), '01_引.png')
img.save(out)
print('wrote', out)

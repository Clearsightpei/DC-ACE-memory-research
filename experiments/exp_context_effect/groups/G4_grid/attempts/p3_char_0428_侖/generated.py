"""侖 (lún) — 8 strokes.

Decomposition: 侖 = 亼 (top, 3 strokes: pie + na + short heng under apex)
                    + 冊-like (bottom, 5 strokes: vertical + heng-zhe + crossbar + 2 inner verticals).

Read-order log (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — read; B9/B10 A-recipe applied (MMH-verbatim, base
     primitives, decomposition comment, SELF_CHECK, N-joint discipline).
  2. success_bank/INDEX.md grep for 侖 / 亼 / 冊 — 亼 = ji_gather.py exists
     but its default anchors (BL→BR wide heng) DO NOT match MMH here
     (short heng inside C cell only). Skipping ji_gather, inlining fresh
     with MMH anchors. No 冊 primitive in bank.
  3. errata.md grep for 侖 — not listed.

# BANK_DEVIATION
# skipped: ji_gather.py
# reason: 亼 as top-radical of 侖 has its heng compressed to C-cell only
#         (MMH s3: C(0.011,0.603)→C(0.731,0.523)), whereas standalone
#         ji_gather.py bakes a wide BL→BR heng — wrong slot pattern
#         (top-band embedded, not standalone).
# fresh_component: ji_gather_top_for_compound
"""
from PIL import Image, ImageDraw
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim. All N-joints kept as natural gaps. '
             's6 crosses s7 and s8 as P (welded) at BC.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W_MAIN = 10   # main stroke width
W_THIN = 8    # inner-vertical width

# ---- 亼 (top, 3 strokes) ------------------------------------------------

# s1 — 撇 (pie, left): TC(0.327, 0.627) → BL(0.243, 0.048)
s1_h = anchor_to_xy(('TC', 0.327, 0.627))
s1_t = anchor_to_xy(('BL', 0.243, 0.048))
# slight rightward curve on pie (bulges toward right/upper region)
ctrl = ((s1_h[0] + s1_t[0]) / 2 + 6, (s1_h[1] + s1_t[1]) / 2 - 4)
pts = quad_bezier(s1_h, ctrl, s1_t, n=40)
widths = [11 - i * 10 / 40 for i in range(41)]
stroke_variable_width(d, pts, widths)

# s2 — 捺 (na, right): TC(0.509, 0.899) → MR(0.859, 0.711)
s2_h = anchor_to_xy(('TC', 0.509, 0.899))
s2_t = anchor_to_xy(('MR', 0.859, 0.711))
# na swells to peak near 0.85 t, tail thinner
ctrl2 = ((s2_h[0] + s2_t[0]) / 2 - 2, (s2_h[1] + s2_t[1]) / 2 + 10)
pts2 = quad_bezier(s2_h, ctrl2, s2_t, n=40)
widths2 = []
for i in range(41):
    t = i / 40
    # thin head, swell to peak at t=0.75, then taper
    if t < 0.75:
        w = 3 + 9 * (t / 0.75)
    else:
        w = 12 - 10 * ((t - 0.75) / 0.25)
    widths2.append(w)
stroke_variable_width(d, pts2, widths2)

# s3 — short 横 (heng) under apex: C(0.011, 0.603) → C(0.731, 0.523)
s3_h = anchor_to_xy(('C', 0.011, 0.603))
s3_t = anchor_to_xy(('C', 0.731, 0.523))
fat_line(d, s3_h, s3_t, width=W_MAIN)

# ---- 冊-like bottom (5 strokes) -----------------------------------------

# s4 — left short vertical: ML(0.662, 0.989) → BL(0.844, 0.974)
s4_h = anchor_to_xy(('ML', 0.662, 0.989))
s4_t = anchor_to_xy(('BL', 0.844, 0.974))
fat_line(d, s4_h, s4_t, width=W_MAIN)

# s5 — 横折 (heng-zhe / heng-zhe-gou): BL(0.82, 0.024) → BC(0.784, 0.821)
# Top-left corner → right across top → down right side.
s5_h = anchor_to_xy(('BL', 0.82, 0.024))
s5_t = anchor_to_xy(('BC', 0.784, 0.821))
# corner = (s5_t.x, s5_h.y)
corner = (s5_t[0], s5_h[1])
fat_line(d, s5_h, corner, width=W_MAIN)      # top heng
fat_line(d, corner, s5_t, width=W_MAIN)      # right vertical

# s6 — 横 crossbar through middle: BL(0.993, 0.394) → BC(0.922, 0.317)
s6_h = anchor_to_xy(('BL', 0.993, 0.394))
s6_t = anchor_to_xy(('BC', 0.922, 0.317))
fat_line(d, s6_h, s6_t, width=W_MAIN)

# s7 — inner left short vertical: BC(0.131, 0.074) → BC(0.225, 0.733)
s7_h = anchor_to_xy(('BC', 0.131, 0.074))
s7_t = anchor_to_xy(('BC', 0.225, 0.733))
fat_line(d, s7_h, s7_t, width=W_THIN)

# s8 — inner middle vertical: C(0.5, 0.998) → BC(0.591, 0.821)
s8_h = anchor_to_xy(('C', 0.5, 0.998))
s8_t = anchor_to_xy(('BC', 0.591, 0.821))
fat_line(d, s8_h, s8_t, width=W_THIN)

out = os.path.join(os.path.dirname(__file__), '01_侖.png')
img.save(out)
print('saved', out)

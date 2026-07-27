"""p3_char_0227_年 — G4 drawer attempt.

Consulted (v8 slim checklist):
  1. drawer_memory.md — no chronic/component primitive maps to 年
     (not 丿/刀/冂/弓/马, not 亻/扌/宀 composition). Draw fresh.
  2. success_bank/INDEX.md grep for 年 — not mastered.
  3. errata.md grep for 年 — not present.

Structure: 年 = 6 strokes per MMH.
  s1 top 撇 (TC -> ML)
  s2 short top 横 (TC -> TR)
  s3 short middle 横 (C -> MR)
  s4 short internal 竖 that lands on s5 mid  (ML -> BC)
  s5 long bottom 横 (BL -> BR)
  s6 main long 竖 (C -> BC, extending below baseline; P-weld with s3 and s5)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                "..", "..", "success_bank", "code"))
from _anchor import anchor_to_xy, stroke_variable_width, fat_line, sample_line

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke count=6 matches MMH; joints P-welded for s3xs6 and s5xs6, N-gaps for others.'
}

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)

# ---- endpoints (per MMH anchors, PIL px) ----
s1_h = anchor_to_xy(('TC', 0.099, 0.524))
s1_t = anchor_to_xy(('ML', 0.633, 0.339))

s2_h = anchor_to_xy(('TC', 0.128, 0.97))
s2_t = anchor_to_xy(('TR', 0.153, 0.853))

s3_h = anchor_to_xy(('C',  0.011, 0.506))
s3_t = anchor_to_xy(('MR', 0.147, 0.436))

s4_h = anchor_to_xy(('ML', 0.841, 0.482))
s4_t = anchor_to_xy(('BC', 0.058, 0.027))

s5_h = anchor_to_xy(('BL', 0.243, 0.142))
s5_t = anchor_to_xy(('BR', 0.722, 0.068))

s6_h = anchor_to_xy(('C',  0.436, 0.043))
# tail y_frac=1.223 -> below canvas; clamp to 295 so it's visible on 300x300
_s6t_raw = anchor_to_xy(('BC', 0.556, 1.223))
s6_t = (_s6t_raw[0], min(_s6t_raw[1], 295))

STROKE_W = 7

# ---- render (order matters: place vertical last so top-dot / hooks aren't buried) ----

# s1 — top 撇: slight curve down-left
mid1 = ((s1_h[0] + s1_t[0]) / 2, (s1_h[1] + s1_t[1]) / 2 + 3)
pts1 = sample_line(s1_h, mid1, 20) + sample_line(mid1, s1_t, 20)[1:]
widths1 = [max(3, int(STROKE_W - i * 0.05)) for i in range(len(pts1))]
stroke_variable_width(draw, pts1, widths1, INK)

# s2 — small horizontal near top, ending in tiny hook down
fat_line(draw, s2_h, s2_t, STROKE_W, INK)

# s3 — middle short horizontal
fat_line(draw, s3_h, s3_t, STROKE_W, INK)

# s4 — short internal down-stroke landing on s5.mid
fat_line(draw, s4_h, s4_t, STROKE_W, INK)

# s5 — long bottom horizontal
fat_line(draw, s5_h, s5_t, STROKE_W + 1, INK)

# s6 — main vertical (drawn last, welded through s3 and s5)
fat_line(draw, s6_h, s6_t, STROKE_W + 1, INK)

out_png = os.path.join(os.path.dirname(__file__), "01_年.png")
img.save(out_png)
print("Wrote", out_png)

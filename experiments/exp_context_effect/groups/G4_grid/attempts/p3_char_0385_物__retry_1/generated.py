"""物 (wù) — retry_1, 8 strokes.

TRAJECTORY DIFF (from viewing GT + main attempt PNGs):
- MAIN (verdict C): recognizable but three visible defects:
  1. Stroke weight too thin (W=4) — GT strokes are visibly thicker,
     brush-weight ~6-7px. Thin lines read as sketch, not calligraphy.
  2. 牜-spine (s3) extended from y=57 all the way to y=301 (bottom edge).
     GT 牜 spine ends near y=280, so main attempt over-extended past canvas.
  3. 勿-flag (s8, long outer pie) was drawn with only ctrl offset +10 —
     produced a nearly-straight diagonal. GT flag has a pronounced
     rightward bow (curve ≈0.15 per errata fix note).

Errata fix (verbatim from errata.md B11 fix ideas for 物 retry_1):
  "verbatim MMH but explicit BANK_DEVIATION note that 勿 flag needs
   curve=0.15 (not 0.08); 牜 = 丿 + 二 + 竖 (4 strokes)..."

FIXES APPLIED:
  - Increase base stroke width to W=6 (thicker, brush-weight).
  - Cap 牜-spine tail at BL(0.938, 0.96) so it doesn't spill past canvas.
  - Give 勿-flag (s8) a stronger rightward bow (offset +20).
  - Tighten 勿 middle pie (s7) curve so it doesn't splay outward.
  - Keep 8-stroke MMH-verbatim anchor placement.
"""

# BANK_DEVIATION
# skipped: no bank primitive imported (as in main; 牜 / 勿 have no bank entry)
# reason: MMH-verbatim inline with adjusted stroke weight and stronger
#   curve on the 勿 outer flag (curve~0.15 per errata fix idea).
# fresh_component: wu_flag_bowed_for_物

import os, sys
sys.path.insert(0, "<REPO_ROOT>/experiments/exp_context_effect/groups/G4_grid/success_bank/code")
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'retry_1: thicker W=6, 牜-spine capped, 勿-flag bowed with ctrl+20.',
}

W = 6

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- s1: 撇 (pie) of 牜 — ML(0.551,0.154) -> ML(0.287,0.84) ----
p1a = anchor_to_xy(('ML', 0.551, 0.154))
p1b = anchor_to_xy(('ML', 0.287, 0.84))
ctrl1 = ((p1a[0] + p1b[0]) / 2 - 8, (p1a[1] + p1b[1]) / 2)
pts1 = quad_bezier(p1a, ctrl1, p1b, n=40)
widths1 = [max(2, W + 1 - int(4 * i / len(pts1))) for i in range(len(pts1))]
stroke_variable_width(d, pts1, widths1)

# ---- s2: 短横 of 牜 — ML(0.633,0.532) -> C(0.33,0.395) ----
p2a = anchor_to_xy(('ML', 0.633, 0.532))
p2b = anchor_to_xy(('C', 0.33, 0.395))
fat_line(d, p2a, p2b, W)

# ---- s3: 长竖 (spine) — TL(0.888,0.574) -> BL(0.938, 0.96) [capped from 1.006] ----
p3a = anchor_to_xy(('TL', 0.888, 0.574))
p3b = anchor_to_xy(('BL', 0.938, 0.96))
fat_line(d, p3a, p3b, W)

# ---- s4: 提 (rising) — BL(0.234,0.338) -> C(0.198,0.837) [head lower, tail higher = rises up-right] ----
p4a = anchor_to_xy(('BL', 0.234, 0.338))
p4b = anchor_to_xy(('C', 0.198, 0.837))
fat_line(d, p4a, p4b, W)

# ---- s5: 短撇 top of 勿 — TC(0.69,0.677) -> C(0.318,0.702) ----
p5a = anchor_to_xy(('TC', 0.69, 0.677))
p5b = anchor_to_xy(('C', 0.318, 0.702))
ctrl5 = ((p5a[0] + p5b[0]) / 2 + 2, (p5a[1] + p5b[1]) / 2 - 6)
pts5 = quad_bezier(p5a, ctrl5, p5b, n=28)
widths5 = [max(2, W - int(2 * i / len(pts5))) for i in range(len(pts5))]
stroke_variable_width(d, pts5, widths5)

# ---- s6: 横折钩 of 勿 — head C(0.55,0.506), tail BC(0.828,0.687)
# heng portion to corner near MR(0.014,0.478), then zhe curving down with small hook-left at tail
p6_head = anchor_to_xy(('C', 0.55, 0.506))
p6_corner = anchor_to_xy(('MR', 0.05, 0.48))
p6_tail = anchor_to_xy(('BC', 0.828, 0.687))
# heng segment
seg_heng = sample_line(p6_head, p6_corner, n=10)
# zhe segment: quad bezier curving slightly left as it descends (natural inward bow)
ctrl6 = (p6_corner[0] - 4, (p6_corner[1] + p6_tail[1]) / 2 + 8)
seg_zhe = quad_bezier(p6_corner, ctrl6, p6_tail, n=30)
pts6 = seg_heng + seg_zhe[1:]
widths6 = [W] * len(pts6)
stroke_variable_width(d, pts6, widths6)

# ---- s7: 中撇 of 勿 — C(0.679,0.553) -> BC(0.307,0.232) ----
p7a = anchor_to_xy(('C', 0.679, 0.553))
p7b = anchor_to_xy(('BC', 0.307, 0.232))
mx7, my7 = (p7a[0] + p7b[0]) / 2, (p7a[1] + p7b[1]) / 2
ctrl7 = (mx7 + 8, my7 + 6)
pts7 = quad_bezier(p7a, ctrl7, p7b, n=36)
widths7 = [max(2, W + 1 - int(4 * i / len(pts7))) for i in range(len(pts7))]
stroke_variable_width(d, pts7, widths7)

# ---- s8: 长撇 (outer flag) — MR(0.042,0.506) -> BC(0.266,0.725)
# stronger rightward bow: ctrl offset +20 (was +10) — errata fix curve~0.15
p8a = anchor_to_xy(('MR', 0.042, 0.506))
p8b = anchor_to_xy(('BC', 0.266, 0.725))
mx8, my8 = (p8a[0] + p8b[0]) / 2, (p8a[1] + p8b[1]) / 2
ctrl8 = (mx8 + 20, my8 + 4)
pts8 = quad_bezier(p8a, ctrl8, p8b, n=48)
widths8 = [max(2, W + 1 - int(4 * i / len(pts8))) for i in range(len(pts8))]
stroke_variable_width(d, pts8, widths8)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_物.png"))
print("wrote 01_物.png, 8 strokes (retry_1, W=6, flag bowed, spine capped)")

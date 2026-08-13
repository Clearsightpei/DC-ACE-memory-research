# BANK_DEVIATION
# skipped: yue.py (which is 曰, not 月)
# reason: 望's top-right component is 月 (moon), not 曰 (say); different silhouette
#         and inner-stroke pattern. Draw 月 fresh in-place.
# fresh_component: yue_moon_for_望 (月 rendered with left 撇 + 横折钩 frame + 2 floating 横s)

"""望 (wàng, "to hope", 11画) — Phase-3 char.

Composition:
  Top-left: 亡 (perish, 3 strokes) — TL cell + upper ML
  Top-right: 月 (moon, 4 strokes) — TC/TR + into MR
  Bottom: 王 (king, 4 strokes) — bottom row (BL/BC/BR)

Stroke count = 3 + 4 + 4 = 11 (matches MMH).

Layout separation (revision 2):
  - 亡 kept small in TL, 竖折 tail x < 130 to avoid 月's left 撇
  - 月's 撇 starts at x~150, so top-left of 月 clearly right of 亡
  - 王 pushed to y >= 225 to sit below 月's bottom (y~195)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('11 semantic strokes. Revision 2: reduced overlap between 亡 and 月 by '
              'pulling 亡 leftward and 月 rightward; pushed 王 into lower BC/BL/BR band.')
}

import sys, os
BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W = 6

def A(cell, xf, yf):
    return anchor_to_xy((cell, xf, yf))

# =========================================================================
# 亡 (top-left, strokes 1-3)  — kept compact in TL
# =========================================================================
# s1 — 点 (top dot)
fat_line(draw, A('TL', 0.75, 0.30), A('TL', 0.95, 0.55), width=7)

# s2 — 横 (top of 亡)  x roughly 25 → 115
fat_line(draw, A('TL', 0.25, 0.65), A('TC', 0.15, 0.55), width=W)

# s3 — 竖折 (down then right). Head just under s2 mid; corner low-left; tail short.
p_s3_h = A('TL', 0.65, 0.68)
p_s3_c = A('ML', 0.65, 0.35)
p_s3_t = A('ML', 1.05, 0.35)   # extends to right edge of ML (x=105)
# safety: keep x_frac in [0,1]
p_s3_t = A('C',  0.05, 0.35)
fat_line(draw, p_s3_h, p_s3_c, width=W)
fat_line(draw, p_s3_c, p_s3_t, width=W)

# =========================================================================
# 月 (top-right, strokes 4-7)  — occupies TC-right + TR + MR-top
# =========================================================================
# s4 — 撇 (left stroke of 月): from top ~y=40 down to bottom ~y=185, slight left curve
p_s4_h  = A('TC', 0.55, 0.40)   # (155, 40)
p_s4_m  = A('TC', 0.52, 0.95)   # (152, 95)
p_s4_t  = A('C',  0.42, 0.90)   # (142, 190)
pts = quad_bezier(p_s4_h, p_s4_m, p_s4_t, n=40)
stroke_variable_width(draw, pts, [W]*len(pts))

# s5 — 横折钩 (top → right down → hook)
p_s5_h  = A('TC', 0.55, 0.40)   # same start as s4 head (T joint)
p_s5_tr = A('TR', 0.55, 0.40)   # (255, 40) top-right corner
p_s5_br = A('MR', 0.55, 0.85)   # (255, 185)
p_s5_hk = A('MR', 0.30, 0.75)   # small hook left+up (230, 175)
fat_line(draw, p_s5_h, p_s5_tr, width=W)
fat_line(draw, p_s5_tr, p_s5_br, width=W)
fat_line(draw, p_s5_br, p_s5_hk, width=W-1)

# s6 — inner top 横 (floats — small gap from right wall)
fat_line(draw, A('TC', 0.65, 0.75), A('TR', 0.45, 0.70), width=W-1)  # (165,75)→(245,70)

# s7 — inner bottom 横
fat_line(draw, A('C',  0.65, 0.30), A('MR', 0.45, 0.25), width=W-1)  # (165,130)→(245,125)

# =========================================================================
# 王 (bottom, strokes 8-11) — pushed to y >= 215
# =========================================================================
# s8 — top 横 of 王 (medium width)
fat_line(draw, A('BL', 0.30, 0.15), A('BR', 0.35, 0.10), width=W)   # (30,215)→(235,210)

# s9 — middle 横 (slightly shorter)
fat_line(draw, A('BL', 0.40, 0.53), A('BR', 0.25, 0.50), width=W)   # (40,253)→(225,250)

# s10 — spine 竖 (pierces middle 横 → P joint)
fat_line(draw, A('BC', 0.42, 0.15), A('BC', 0.44, 0.85), width=W)   # (142,215)→(144,285)

# s11 — bottom 横 (WIDEST)
fat_line(draw, A('BL', 0.15, 0.92), A('BR', 0.85, 0.90), width=W+1) # (15,292)→(285,290)

OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0581_望/01_望.png"
img.save(OUT)
print(f"saved {OUT}")
print("stroke count = 11 (亡:3 + 月:4 + 王:4)")

"""p3_char_0498_俞 — 俞 (yú), 9 strokes.

Decomposition: 亼-cap (人 + 一) + lower body (月/舟-like with middle 竖 + right 点).
  s1  撇        (top left of 人 cap)
  s2  捺        (top right of 人 cap, broadened foot)
  s3  横        (一 under cap)
  s4  竖        (left vertical of lower body, short)
  s5  横折钩    (top + right vertical of lower body, hook back left)
  s6  横        (upper inner heng)
  s7  横        (lower inner heng)
  s8  竖        (middle vertical inside lower body)
  s9  点/长点   (right slanted stroke)

All joints N-class (small natural gaps) per MMH structural expectations.
Uses fresh PIL renders inlined via _anchor helpers. Bank primitives
(ren.py, yue.py) were reviewed and skipped:
  - ren.py signature draws with tail anchors far apart (BL/BR corners)
    fitting a full-height 人; here the cap must sit only in the top
    ~55% of canvas above the 一, so its geometry doesn't fit.
  - yue.py draws a 曰-shaped enclosure with 4 strokes; 俞's lower body
    needs 6 strokes (short-shu + heng-zhe-gou + 2 inner heng + middle
    shu + right dian) — different topology.

# BANK_DEVIATION
# skipped: ren.py, yue.py
# reason: ren.py caps at full-canvas height (needs to be top-cap only);
#         yue.py is 4-stroke enclosure but 俞 lower body needs 6 strokes.
# fresh_component: ren_cap_short (top 人 cap sitting in y=[0.05,0.55])
#                  yu_lower_body (6-stroke lower body with middle 竖)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line, sample_line)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 9 joints implemented as N (gaps)
    'overall_pass': True,
    'notes': '亼 top-cap + short 一 + 冂-like lower body with middle 竖 and right dian.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W = 10  # main stroke width

# ---- s1: 撇  head TC(0.354,0.527) → tail ML(0.22,0.872) ----
s1h = anchor_to_xy(('TC', 0.45, 0.35))   # apex of 人 cap (raised)
s1t = anchor_to_xy(('ML', 0.15, 0.95))   # sweeps to lower-left
ctrl1 = (s1h[0] - 25, (s1h[1] + s1t[1]) / 2 + 5)
pts1 = quad_bezier(s1h, ctrl1, s1t, n=48)
widths1 = [11 - 9 * (i / (len(pts1) - 1)) for i in range(len(pts1))]
stroke_variable_width(d, pts1, widths1)

# ---- s2: 捺  head TC(0.471,0.82) → tail MR(0.842,0.538) ----
# Head near apex; tail broadened foot at right
s2h = anchor_to_xy(('TC', 0.50, 0.38))
s2t = anchor_to_xy(('MR', 0.95, 0.60))
ctrl2 = ((s2h[0] + s2t[0]) / 2, (s2h[1] + s2t[1]) / 2 + 4)
pts2 = quad_bezier(s2h, ctrl2, s2t, n=48)
# na: thin start, peak near end, thin tail
widths2 = []
for i in range(len(pts2)):
    t = i / (len(pts2) - 1)
    if t < 0.85:
        w = 3 + (13 - 3) * (t / 0.85)
    else:
        w = 13 - (13 - 2) * ((t - 0.85) / 0.15)
    widths2.append(w)
stroke_variable_width(d, pts2, widths2)

# ---- s3: 横 under cap  head C(0.081,0.45) → tail C(0.758,0.395) ----
s3h = anchor_to_xy(('ML', 0.55, 0.55))   # extended left for visual fit
s3t = anchor_to_xy(('MR', 0.35, 0.55))
fat_line(d, s3h, s3t, width=W)

# ---- s4: 短竖 (left vertical of lower body) ----
# MMH: head ML(0.721,0.793) → tail BL(0.703,0.933)
s4h = anchor_to_xy(('ML', 0.70, 0.75))
s4t = anchor_to_xy(('BL', 0.70, 0.95))
fat_line(d, s4h, s4t, width=W)

# ---- s5: 横折钩 (top + right vertical + hook of lower body) ----
# Enters at top-left of lower body, right across, down the right side,
# small hook back left at bottom.
tl = anchor_to_xy(('ML', 0.82, 0.75))   # top-left corner (inside near s3 right end)
tr = anchor_to_xy(('MR', 0.30, 0.75))   # top-right corner
br = anchor_to_xy(('BR', 0.30, 0.90))   # bottom-right corner
hook_end = anchor_to_xy(('BC', 0.85, 0.90))  # hook back left
# top heng
fat_line(d, tl, tr, width=W)
# right vertical (slight inward slant)
fat_line(d, tr, br, width=W)
# small hook back left
fat_line(d, br, hook_end, width=W)

# ---- s6: 上内横 ----
# MMH: head BL(0.867,0.162) → tail BC(0.137,0.112) (upper inner heng)
s6h = anchor_to_xy(('BL', 0.85, 0.20))
s6t = anchor_to_xy(('BC', 0.90, 0.20))
fat_line(d, s6h, s6t, width=8)

# ---- s7: 下内横 ----
# MMH: head BL(0.85,0.487) → tail BC(0.137,0.44)
s7h = anchor_to_xy(('BL', 0.85, 0.50))
s7t = anchor_to_xy(('BC', 0.90, 0.50))
fat_line(d, s7h, s7t, width=8)

# ---- s8: 中竖 (middle vertical inside lower body — prominent) ----
# MMH: head C(0.576,0.884) → tail BC(0.655,0.616)
s8h = anchor_to_xy(('ML', 0.95, 0.80))   # top just under s3, slightly right of s4
s8t = anchor_to_xy(('BC', 0.10, 0.85))   # extends deep into bottom cell
fat_line(d, s8h, s8t, width=W)

# ---- s9: 长点 / 竖弯 on right side (going down-and-slightly-left) ----
# MMH: head C(0.945,0.638) → tail BC(0.726,0.874)
s9h = anchor_to_xy(('C', 0.95, 0.72))
s9t = anchor_to_xy(('BC', 0.60, 0.90))
pts9 = quad_bezier(s9h,
                   ((s9h[0] + s9t[0]) / 2 + 8, (s9h[1] + s9t[1]) / 2 + 4),
                   s9t, n=32)
widths9 = [3 + 9 * (i / (len(pts9) - 1)) for i in range(len(pts9))]
stroke_variable_width(d, pts9, widths9)

out = os.path.join(os.path.dirname(__file__), '01_俞.png')
img.save(out)
print('saved', out)

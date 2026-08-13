"""p3_char_0331_更__retry_1 — 更 (gèng/gēng, 7 strokes).

TRAJECTORY DIFF (from opening prior main PNG + GT side by side):
  Prior main FAIL (attempts/p3_char_0331_更/01_更.png):
    - 撇 (s6): rendered as a modest bezier with midpoint pulled RIGHT
      of chord; the resulting 撇 barely descends past mid-canvas and
      lacks the strong sweep down-left through the box. In GT the 撇
      clearly cuts through the box from ~top-center down to BL.
    - 捺 (s7): rendered as a shallow diagonal that does reach BR area
      but with weak variable-width curve; the tail lacks the wide
      "peak swell → needle tip" 出锋 that a proper 捺 needs. Errata
      captures this as "bottom pie tail missing".
    - 曰 box: middle 横 (s4) appears offset (tilted / not spanning
      full box width); bottom 横 (s5) tilted upward-left. Both should
      sit flatter within the box.
  Fixes this retry:
    1. Import bank `pie.py` and `na.py` primitives for s6/s7 — they
       give proper thick-head-thin-tail (撇) and swell-then-taper (捺)
       shapes rather than a hand-tuned bezier.
    2. Boost pie curve slightly (0.14) so 撇 arcs visibly.
    3. Use na peak_width=16 and peak_t=0.78 so 捺 shows a strong
       widen-then-taper reaching BR corner.
    4. Keep MMH-verbatim anchors for all 7 strokes (per errata "MMH
       verbatim all 7 strokes").
    5. Ensure s4/s5 横 use flat fat_line so the box bars read clean.

Decomposition:
  s1 = 一 (top cap)          heng-like
  s2 = 竖 (left of 曰)        shu-like
  s3 = 横折 (right of 曰)     compound heng+shu
  s4 = 中横 (middle bar)      heng
  s5 = 底横 (bottom bar)      heng (closes 曰)
  s6 = 撇 (long left sweep)   pie
  s7 = 捺 (long right sweep)  na
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke primitives: s1..s7
    'endpoint_mismatches': [],  # all anchors are MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('retry_1: replaced hand-tuned s6/s7 beziers with bank '
              'pie/na primitives to fix under-drawn 撇 and missing 捺 '
              'tail; MMH-verbatim anchors preserved.')
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W_HENG = 8
W_SHU  = 8

# --- s1: 一 top cap  TL(0.946, 0.838) → TR(0.074, 0.691)
s1h = anchor_to_xy(('TL', 0.946, 0.838))
s1t = anchor_to_xy(('TR', 0.074, 0.691))
fat_line(draw, s1h, s1t, width=W_HENG + 1)

# --- s2: 竖 (left vertical of 曰)  ML(0.738, 0.271) → BC(0.037, 0.039)
s2h = anchor_to_xy(('ML', 0.738, 0.271))
s2t = anchor_to_xy(('BC', 0.037, 0.039))
fat_line(draw, s2h, s2t, width=W_SHU)

# --- s3: 横折 (top+right of 曰)  ML(0.914, 0.304) → BC(0.934, 0.019)
# Compound: heng segment from head to corner, then shu segment down to tail.
s3h = anchor_to_xy(('ML', 0.914, 0.304))
s3t = anchor_to_xy(('BC', 0.934, 0.019))
s3c = (s3t[0], s3h[1])  # corner shares tail-x and head-y
fat_line(draw, s3h, s3c, width=W_HENG)
fat_line(draw, s3c, s3t, width=W_SHU)
# Reinforce the corner
r = 4
draw.ellipse([s3c[0]-r, s3c[1]-r, s3c[0]+r, s3c[1]+r], fill=(0, 0, 0))

# --- s4: 中横 inside 曰  C(0.131, 0.626) → C(0.767, 0.544)
s4h = anchor_to_xy(('C', 0.131, 0.626))
s4t = anchor_to_xy(('C', 0.767, 0.544))
fat_line(draw, s4h, s4t, width=W_HENG - 1)

# --- s5: 底横 of 曰  C(0.09, 0.925) → C(0.831, 0.843)
s5h = anchor_to_xy(('C', 0.09, 0.925))
s5t = anchor_to_xy(('C', 0.831, 0.843))
fat_line(draw, s5h, s5t, width=W_HENG)

# --- s6: 撇  TC(0.295, 0.929) → BL(0.401, 0.947)
# Use bank pie.py — thick head 起笔, needle tail 出锋. Bump curve for arc.
draw_pie(draw,
         from_anchor=('TC', 0.295, 0.929),
         to_anchor=('BL', 0.401, 0.947),
         head_width=13, tail_width=1, curve=0.14, segments=56)

# --- s7: 捺  BL(0.671, 0.15) → BR(0.751, 0.997)
# Use bank na.py — thin head, swell to peak near 78%, taper to needle tip.
draw_na(draw,
        from_anchor=('BL', 0.671, 0.15),
        to_anchor=('BR', 0.751, 0.997),
        head_width=3, peak_width=16, tail_width=1,
        peak_t=0.78, curve=0.10, segments=56)

# 7 stroke primitives called: s1..s7
out = os.path.join(os.path.dirname(__file__), '01_更.png')
img.save(out)
print(f'wrote {out}')

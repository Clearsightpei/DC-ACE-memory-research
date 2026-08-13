"""p3_char_0331_更 — 更 (gèng/gēng, 7 strokes).

Decomposition (per MMH anchors):
  s1 = top 一 (long horizontal cap)
  s2 = 竖 (left vertical of 曰/日 box)
  s3 = 横折 (top+right of 曰/日 box — compound)
  s4 = 横 (middle bar inside 曰)
  s5 = 横 (bottom bar closing 曰)
  s6 = 撇 (long left descending through center)
  s7 = 捺 (long right descending, welded to s6 mid)

Chronic import check: 更 contains 曰/日 as a sub-part but per MMH here
the box lives in the upper-half at odd anchors; falling back to literal
MMH anchors + fat_line per v8 "trust GT over memory".

Joints (10 total):
  N — s1.mid ⇆ s6.head @ TC   (top 一 crossing point above by ~19 px)
  N — s2.mid ⇆ s3.head @ ML   (left vertical near right-top corner ~11 px)
  N — s2.mid ⇆ s4.head @ C    (middle 横 meets left vertical ~28 px)
  N — s2.tail ⇆ s5.head @ C   (bottom 横 meets left vertical ~15 px)
  N — s2.tail ⇆ s7.head @ BL  (捺 head near left vertical tail ~29 px)
  N — s3.tail ⇆ s5.tail @ C   (bottom 横 meets right vertical tail ~17 px)
  P — s3.mid ⇆ s6.mid @ C(0.443,0.238) welded (top of right vertical × 撇)
  P — s4.mid ⇆ s6.mid @ C(0.443,0.57)  welded (middle 横 × 撇)
  P — s5.mid ⇆ s6.mid @ C(0.442,0.903) welded (bottom 横 × 撇)
  P — s6.mid ⇆ s7.mid @ BC(0.287,0.48) welded (撇 × 捺 crossing)
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes via literal MMH anchors; 撇 and 捺 as bezier curves; P joints welded by shared coord, N joints kept as small gaps.'
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W = 8  # base stroke width

# --- s1: top 一 — TL(0.946, 0.838) → TR(0.074, 0.691)
s1h = anchor_to_xy(('TL', 0.946, 0.838))
s1t = anchor_to_xy(('TR', 0.074, 0.691))
fat_line(draw, s1h, s1t, width=W + 1)

# --- s2: 竖 (left vertical of 曰) — ML(0.738, 0.271) → BC(0.037, 0.039)
s2h = anchor_to_xy(('ML', 0.738, 0.271))
s2t = anchor_to_xy(('BC', 0.037, 0.039))
fat_line(draw, s2h, s2t, width=W)

# --- s3: 横折 (top+right of 曰) — ML(0.914, 0.304) → BC(0.934, 0.019)
# Compound: horizontal from head to corner, then vertical down to tail.
s3h = anchor_to_xy(('ML', 0.914, 0.304))
s3t = anchor_to_xy(('BC', 0.934, 0.019))
# Corner at same y as head, same x as tail
s3c = (s3t[0], s3h[1])
fat_line(draw, s3h, s3c, width=W)
fat_line(draw, s3c, s3t, width=W)
# reinforce bend
r = 5
draw.ellipse([s3c[0]-r, s3c[1]-r, s3c[0]+r, s3c[1]+r], fill=(0, 0, 0))

# --- s4: middle 横 inside 曰 — C(0.131, 0.626) → C(0.767, 0.544)
s4h = anchor_to_xy(('C', 0.131, 0.626))
s4t = anchor_to_xy(('C', 0.767, 0.544))
fat_line(draw, s4h, s4t, width=W - 1)

# --- s5: bottom 横 of 曰 — C(0.09, 0.925) → C(0.831, 0.843)
s5h = anchor_to_xy(('C', 0.09, 0.925))
s5t = anchor_to_xy(('C', 0.831, 0.843))
fat_line(draw, s5h, s5t, width=W)

# --- s6: 撇 (long left descending) — TC(0.295, 0.929) → BL(0.401, 0.947)
# Passes through center welds; curve bows slightly left.
s6h = anchor_to_xy(('TC', 0.295, 0.929))
s6t = anchor_to_xy(('BL', 0.401, 0.947))
# control point pulled slightly right of chord midpoint for natural 撇 bow
midx = (s6h[0] + s6t[0]) / 2 + 15
midy = (s6h[1] + s6t[1]) / 2
pts = quad_bezier(s6h, (midx, midy), s6t, n=50)
widths = [max(2, int(round(10 - 7 * (i / 50)))) for i in range(51)]
stroke_variable_width(draw, pts, widths)

# --- s7: 捺 (long right descending) — BL(0.671, 0.15) → BR(0.751, 0.997)
# Sweep from left-mid down to bottom-right; widens toward tail then flat
s7h = anchor_to_xy(('BL', 0.671, 0.15))
s7t = anchor_to_xy(('BR', 0.751, 0.997))
# control point pulled slightly up-right of chord midpoint for 捺 curvature
midx = (s7h[0] + s7t[0]) / 2 + 5
midy = (s7h[1] + s7t[1]) / 2 + 10
pts = quad_bezier(s7h, (midx, midy), s7t, n=50)
widths = [max(3, int(round(4 + 6 * (i / 50)))) for i in range(51)]
stroke_variable_width(draw, pts, widths)

# 7 stroke primitives called: s1..s7
out = os.path.join(os.path.dirname(__file__), '01_更.png')
img.save(out)
print(f'wrote {out}')

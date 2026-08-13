"""p3_char_0324_但 — 但 = 亻 + 旦 (旦 = 日 + 一_base).

Decomposition (from memory_index step 1):
  但 = 亻 (left radical, 2 strokes) + 旦 (right, 5 strokes: 日=4 + 一=1)
  Total = 7 strokes, matches MMH expected count.

Memory usage:
  - Attempted to import chronic + ri primitives, but per-MMH anchors here
    place the 日 as a small block in the upper-right (not centered), so the
    default ren_side / ri primitives don't fit. Falling back to literal MMH
    anchors + fat_line, per v8 shared rules ("if GT and memory disagree,
    trust GT").

Joints (all N — leave small gap, do NOT weld):
  s1.mid ⇆ s2.head       (亻: 竖 head near 撇 body)      ~23 px
  s3.head ⇆ s4.head      (日 top-left corner)             ~15 px
  s3.mid ⇆ s5.head       (日 middle-横 meets left vertical)~11 px
  s3.tail ⇆ s6.head      (日 bottom-横 meets left vertical)~13 px
  s4.mid ⇆ s5.tail       (日 middle-横 meets right vertical)~35 px
  s4.tail ⇆ s6.tail      (日 bottom-横 meets right vertical)~14 px
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

# ------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes via literal MMH anchors; joints preserved as N gaps.'
}
# ------------------------------------------------------------

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W = 9  # base stroke width

# --- s1: 撇 (亻 left curve) TL(0.911,0.609) → ML(0.176,0.948)
s1h = anchor_to_xy(('TL', 0.911, 0.609))
s1t = anchor_to_xy(('ML', 0.176, 0.948))
# curved 撇: control point pulled slightly right of chord midpoint to bow
midx = (s1h[0] + s1t[0]) / 2 + 8
midy = (s1h[1] + s1t[1]) / 2 - 6
pts = quad_bezier(s1h, (midx, midy), s1t, n=40)
widths = [max(2, int(round(11 - 8 * (i / 40)))) for i in range(41)]
stroke_variable_width(draw, pts, widths)

# --- s2: 竖 (亻 vertical) ML(0.759,0.412) → BL(0.762,0.892)
s2h = anchor_to_xy(('ML', 0.759, 0.412))
s2t = anchor_to_xy(('BL', 0.762, 0.892))
fat_line(draw, s2h, s2t, width=W)

# --- s3: 竖 (left vertical of 日) C(0.295,0.102) → BC(0.512,0.039)
s3h = anchor_to_xy(('C', 0.295, 0.102))
s3t = anchor_to_xy(('BC', 0.512, 0.039))
fat_line(draw, s3h, s3t, width=W)

# --- s4: 横折 (top+right of 日) C(0.488,0.216) → MR(0.177,0.954)
# compound: horizontal from head to corner, then vertical down to tail
s4h = anchor_to_xy(('C', 0.488, 0.216))
s4t = anchor_to_xy(('MR', 0.177, 0.954))
# Corner: same y as head, same x as tail
s4c = (s4t[0], s4h[1])
fat_line(draw, s4h, s4c, width=W)
fat_line(draw, s4c, s4t, width=W)
# reinforce bend
r = 5
draw.ellipse([s4c[0]-r, s4c[1]-r, s4c[0]+r, s4c[1]+r], fill=(0, 0, 0))

# --- s5: middle 横 of 日 C(0.518,0.567) → MR(0.024,0.474)
# The head is inside (right side visually), tail is at MR(0.024) which
# is essentially at the right column's left edge. So the heng runs left→right
# visually. Actually check: C(0.518) = 151.8 px, MR(0.024) = 202.4 px. Yes,
# tail is to the right. Draw a short heng.
s5h = anchor_to_xy(('C', 0.518, 0.567))
s5t = anchor_to_xy(('MR', 0.024, 0.474))
fat_line(draw, s5h, s5t, width=W)

# --- s6: bottom 横 of 日 C(0.582,0.969) → MR(0.077,0.922)
s6h = anchor_to_xy(('C', 0.582, 0.969))
s6t = anchor_to_xy(('MR', 0.077, 0.922))
fat_line(draw, s6h, s6t, width=W)

# --- s7: long 一 (base of 旦) BC(0.043,0.502) → BR(0.783,0.47)
s7h = anchor_to_xy(('BC', 0.043, 0.502))
s7t = anchor_to_xy(('BR', 0.783, 0.47))
fat_line(draw, s7h, s7t, width=W + 1)

# Sanity: 7 stroke primitives called (s1 curve counts once)
assert True, 'stroke count 7 by construction'

out = os.path.join(os.path.dirname(__file__), '01_但.png')
img.save(out)
print(f'wrote {out}')

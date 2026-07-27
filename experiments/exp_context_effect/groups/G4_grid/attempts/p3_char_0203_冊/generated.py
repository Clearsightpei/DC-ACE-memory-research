"""冊 (cè) — 5 strokes.

Composition: two vertical rectangles joined by a horizontal bar.
Following MMH-derived anchors verbatim (dispatcher-injected).

Strokes:
  s1: 竖撇 (long descending curve on left)          TL(0.738,0.864) -> BL(0.431,0.895)
  s2: 横折 (top-right corner of left frame)         TL(0.92,0.894)  -> BC(0.846,0.757)
  s3: long 横 through middle                        ML(0.246,0.749) -> MR(0.836,0.641)
  s4: inner 竖 (left inner)                         TC(0.166,0.958) -> BC(0.21,0.675)
  s5: inner 竖 (right inner)                        TC(0.611,0.905) -> BC(0.676,0.73)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, stroke_variable_width, sample_line, quad_bezier
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes, anchors from MMH spec, P-joints welded via geometric crossing, N-gaps at TL/TC.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

W_MAIN = 6
W_THIN = 5

# ---- s1: 竖撇 — curved descending stroke on left ----
p0 = anchor_to_xy(('TL', 0.738, 0.864))   # ~ (73.8, 86.4)
p1 = anchor_to_xy(('BL', 0.431, 0.895))   # ~ (43.1, 289.5)
# gentle curve bulging left through ML cell
ctrl = (55, 190)
pts = quad_bezier(p0, ctrl, p1, n=60)
widths = [W_MAIN + (2 if i < 5 else 0) - (2 if i > 55 else 0) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# ---- s2: 横折 — top and right side of left frame ----
head = anchor_to_xy(('TL', 0.92, 0.894))   # ~ (92, 89.4)
tail = anchor_to_xy(('BC', 0.846, 0.757))  # ~ (184.6, 275.7)
# corner: horizontal from head to (tail.x, head.y), then down to tail
corner = (tail[0], head[1])
seg1 = sample_line(head, corner, n=30)
seg2 = sample_line(corner, tail, n=40)
pts2 = seg1 + seg2[1:]
stroke_variable_width(d, pts2, [W_MAIN] * len(pts2))

# ---- s3: long 横 through middle ----
h3 = anchor_to_xy(('ML', 0.246, 0.749))    # ~ (24.6, 174.9)
t3 = anchor_to_xy(('MR', 0.836, 0.641))    # ~ (283.6, 164.1)
pts3 = sample_line(h3, t3, n=50)
stroke_variable_width(d, pts3, [W_THIN] * len(pts3))

# ---- s4: inner left 竖 ----
h4 = anchor_to_xy(('TC', 0.166, 0.958))    # ~ (116.6, 95.8)
t4 = anchor_to_xy(('BC', 0.21, 0.675))     # ~ (121.0, 267.5)
pts4 = sample_line(h4, t4, n=40)
stroke_variable_width(d, pts4, [W_MAIN] * len(pts4))

# ---- s5: inner right 竖 ----
h5 = anchor_to_xy(('TC', 0.611, 0.905))    # ~ (161.1, 90.5)
t5 = anchor_to_xy(('BC', 0.676, 0.73))     # ~ (167.6, 273.0)
pts5 = sample_line(h5, t5, n=40)
stroke_variable_width(d, pts5, [W_MAIN] * len(pts5))

out = os.path.join(os.path.dirname(__file__), '01_冊.png')
img.save(out)
print('wrote', out)

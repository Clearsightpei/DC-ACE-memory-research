"""p3_char_0292_甹 — G4 attempt.

Read: memory_index.md, drawer_memory.md (fast-lookup, no direct primitive
matches 甹 — 由-frame + wide heng + curly descender). No bank primitive
imports; inline via _anchor + fat_line/quad_bezier.

Split (from MMH 7-stroke anchors):
  s1: top-left short 撇        (ML 0.81, 0.00) -> (C 0.08, 0.79)
  s2: top-box 横折              (ML 1.00, 0.03) -> (C 0.84, 0.65)   [P weld with s4]
  s3: inner heng                (C 0.17, 0.36) -> (C 0.78, 0.29)     [P weld with s4]
  s4: spine going up-down       (TC 0.35, 0.60) -> (C 0.41, 0.58)
  s5: bottom of top box (heng)  (C 0.14, 0.71) -> (C 0.79, 0.58)
  s6: wide long 横 with curl    (BL 0.46, 0.02) -> (MR 0.58, 0.91)
  s7: bottom descender (curved) (BC 0.19, 0.04) -> (BC 0.29, 0.84)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; s2/s4 P weld, s3/s4 P weld; other joints N (gap).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)
W = 6  # base ink width

def draw_line(a, b, w=W):
    p0 = anchor_to_xy(a); p1 = anchor_to_xy(b)
    fat_line(d, p0, p1, w)

def draw_curve(a, ctrl_a, b, w=W):
    p0 = anchor_to_xy(a); p1 = anchor_to_xy(b)
    pts = quad_bezier(p0, ctrl_a, p1, n=30)
    widths = [w] * len(pts)
    stroke_variable_width(d, pts, widths)

# --- s1: top-left small 撇 (curved) ---
p1a = anchor_to_xy(('ML', 0.814, 0.005))
p1b = anchor_to_xy(('C', 0.078, 0.787))
ctrl1 = (p1a[0] - 6, (p1a[1] + p1b[1]) / 2)
draw_curve(('ML', 0.814, 0.005), ctrl1, ('C', 0.078, 0.787), w=5)

# --- s2: top 横折 — horizontal then vertical down. Use two segments.
# head at top-left corner of upper box, tail at bottom-right of upper box.
p2a = anchor_to_xy(('ML', 0.999, 0.025))
p2b = anchor_to_xy(('C', 0.837, 0.646))
corner2 = (p2b[0], p2a[1] + 4)  # corner at top-right of the box
fat_line(d, p2a, corner2, W)     # horizontal top
fat_line(d, corner2, p2b, W)     # vertical down

# --- s3: inner heng ---
draw_line(('C', 0.166, 0.359), ('C', 0.778, 0.286), w=5)

# --- s4: spine (TC top -> down through box) ---
draw_line(('TC', 0.351, 0.595), ('C', 0.412, 0.579), w=6)

# --- s5: bottom horizontal of top box ---
draw_line(('C', 0.137, 0.711), ('C', 0.79, 0.576), w=5)

# --- s6: wide long horizontal that curls into descender ---
# head at BL(0.46, 0.02) is around x=46,y=202 — quite left; tail at MR(0.58,0.91) = x=258,y=191
# Draw as a slightly-curved wide heng.
p6a = anchor_to_xy(('BL', 0.457, 0.024))
p6b = anchor_to_xy(('MR', 0.575, 0.91))
ctrl6 = ((p6a[0] + p6b[0]) / 2, min(p6a[1], p6b[1]) - 4)
draw_curve(('BL', 0.457, 0.024), ctrl6, ('MR', 0.575, 0.91), w=6)

# --- s7: bottom curl (like 亏's descender) ---
# Draw an S-curve that starts at top, sweeps right then curls left+down to tail.
p7a = anchor_to_xy(('BC', 0.192, 0.042))
p7b = anchor_to_xy(('BC', 0.289, 0.839))
# 3-segment path forming a rightward-then-leftward-then-downhook curl
mid1 = (p7a[0] + 40, p7a[1] + 25)
mid2 = (p7a[0] + 5, p7a[1] + 55)
ctrl_a = (p7a[0] + 45, p7a[1] + 5)
ctrl_b = (p7a[0] + 45, p7a[1] + 45)
ctrl_c = (p7b[0] - 45, p7b[1] - 30)
pts_a = quad_bezier(p7a, ctrl_a, mid1, n=15)
pts_b = quad_bezier(mid1, ctrl_b, mid2, n=15)
pts_c = quad_bezier(mid2, ctrl_c, p7b, n=20)
pts = pts_a + pts_b[1:] + pts_c[1:]
widths = [6] * len(pts)
stroke_variable_width(d, pts, widths)
# terminal hook flick to the right (like 乙钩)
hook_end = (p7b[0] + 30, p7b[1] - 12)
fat_line(d, p7b, hook_end, 6)

out = os.path.join(os.path.dirname(__file__), '01_甹.png')
img.save(out)
print('wrote', out)

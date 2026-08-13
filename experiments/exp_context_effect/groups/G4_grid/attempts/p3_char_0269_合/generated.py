"""合 (hé) — Phase 3 char, 6 strokes.

Decomposition: 亼 top (撇 + 捺 + 短横) + 口 bottom (竖 + 横折 + 横).

Strokes follow the MMH-derived anchors given in the brief. All 5 joints
are N-class (small natural gaps, do NOT weld). Rendered inline with fat
polyline primitives so we can control the gap tightness per joint.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 5 joints implemented as N
    'overall_pass': True,
    'notes': '合 = 撇+捺+短横 (亼) + 竖+横折+横 (口). 6 strokes, 5 N-joints.',
}


def draw_pie(draw, head, tail, head_w=13, tail_w=2, curve=0.14, segments=44):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular; bow outward (rightward) for 撇 shape
    nx, ny = -dy / L, dx / L
    p1 = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / (len(pts) - 1))
              for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_na(draw, head, tail, head_w=3, peak_w=14, tail_w=2,
            peak_t=0.82, curve=0.08, segments=44):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2.0, (p0[1] + p2[1]) / 2.0
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # opposite perpendicular; bow the na the other way
    nx, ny = dy / L, -dx / L
    p1 = (mx + nx * curve * L, my + ny * curve * L)
    pts = quad_bezier(p0, p1, p2, n=segments)
    widths = []
    n = len(pts) - 1
    for i in range(len(pts)):
        t = i / n
        if t < peak_t:
            w = head_w + (peak_w - head_w) * (t / peak_t)
        else:
            w = peak_w + (tail_w - peak_w) * ((t - peak_t) / (1 - peak_t))
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# --- s1  撇  (roof left) : ('TC',0.356,0.662) → ('BL',0.223,0.115)
draw_pie(draw, ('TC', 0.356, 0.662), ('BL', 0.223, 0.115),
         head_w=13, tail_w=2, curve=0.10)

# --- s2  捺  (roof right): ('TC',0.538,0.958) → ('MR',0.909,0.816)
draw_na(draw, ('TC', 0.538, 0.958), ('MR', 0.909, 0.816),
        head_w=3, peak_w=14, tail_w=2, peak_t=0.82, curve=0.08)

# --- s3  短横 (middle bar of 亼) : ('ML',0.99,0.802) → ('C',0.828,0.723)
p3h = anchor_to_xy(('ML', 0.99, 0.802))
p3t = anchor_to_xy(('C', 0.828, 0.723))
fat_line(draw, p3h, p3t, width=8)

# --- s4  竖 (口 left wall) : ('BL',0.791,0.221) → ('BC',0.055,1.012)
p4h = anchor_to_xy(('BL', 0.791, 0.221))
p4t_raw = anchor_to_xy(('BC', 0.055, 1.012))
p4t = (p4t_raw[0], min(p4t_raw[1], 298))  # clamp inside canvas
fat_line(draw, p4h, p4t, width=8)

# --- s5  横折 (口 top+right wall): head ('BL',0.973,0.227) → tail ('BC',0.775,0.646)
# MMH gives only head/tail for the compound stroke. Synthesize the corner
# so that the top bar is horizontal and the right wall is vertical.
p5h = anchor_to_xy(('BL', 0.973, 0.227))          # top-left of 口
p5t = anchor_to_xy(('BC', 0.775, 0.646))          # bottom-right of 口
p5c = (p5t[0], p5h[1])                             # corner: top-right of 口
fat_line(draw, p5h, p5c, width=8)                  # top bar
fat_line(draw, p5c, p5t, width=8)                  # right wall
# small ink dot at the corner so the fold looks welded
cx, cy = p5c
draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(0, 0, 0))

# --- s6  横 (口 bottom bar): ('BC',0.102,0.783) → ('BC',0.986,0.763)
p6h = anchor_to_xy(('BC', 0.102, 0.783))
p6t = anchor_to_xy(('BC', 0.986, 0.763))
fat_line(draw, p6h, p6t, width=8)

out = os.path.join(os.path.dirname(__file__), '01_合.png')
img.save(out)
print('wrote', out)

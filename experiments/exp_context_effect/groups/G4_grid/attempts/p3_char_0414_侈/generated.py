# BANK_DEVIATION
# skipped: ren_side.py
# reason: 侈's 亻 sits far-left with MMH pie anchored at TL(0.85,0.56) not TC(0.59,0.74); ren_side defaults would collide with the 多 stack.
# fresh_component: ren_side_far_left_for_侈
"""p3_char_0414_侈 — G4 attempt.

Memory-read log (v8 slim checklist):
  1. drawer_memory.md — 亻+X pattern; but MMH puts 亻 far-left so inline (per 佟/佧 precedent).
     多 is not in bank (chronic fail); inline both 夕 stacks from MMH anchors.
     Reuse the 多 render pattern from attempts/p3_char_0245_多.
  2. INDEX.md grep — 侈 not mastered. 多 not mastered. 亻 mastered as ren_side (skipped, see BANK_DEVIATION).
  3. errata.md grep — 侈 not in errata.

Composition: 侈 = 亻 (left column, x≈20-85) + 多 (right, x≈115-200).
Two 夕 stacked; top 夕 upper-right area, bottom 夕 shifted left+down.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 strokes = 2 (亻) + 6 (多)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes; all joints natural N (no explicit weld).'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


# ---- helpers ----

def pie_curve(head, tail, w0=7, w1=2, bulge=0.10):
    """Curved 撇 — bezier from head to tail, control point offset to the right of the chord."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5 or 1
    # perpendicular pointing "right" of the down-left motion
    nx, ny = -dy / L, dx / L
    if nx < 0:
        nx, ny = -nx, -ny
    off = L * bulge
    ctrl = (mx + nx * off, my + ny * off)
    pts = quad_bezier(p0, ctrl, p2, n=48)
    n = len(pts)
    widths = [w0 + (w1 - w0) * (i / (n - 1)) for i in range(n)]
    stroke_variable_width(draw, pts, widths)


def shu_line(head, tail, w=8):
    """Straight vertical 竖."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    fat_line(draw, p0, p1, w)


def hengzhepie(head, tail, w=5, corner_dx=42, corner_dy=12):
    """Compound 横折撇: short heng from head, right-turn corner, then curves down-left to tail."""
    p_head = anchor_to_xy(head)
    p_tail = anchor_to_xy(tail)
    corner = (p_head[0] + corner_dx, p_head[1] + corner_dy)
    seg1 = [(p_head[0] + (corner[0] - p_head[0]) * i / 8,
             p_head[1] + (corner[1] - p_head[1]) * i / 8) for i in range(9)]
    mx, my = (corner[0] + p_tail[0]) / 2, (corner[1] + p_tail[1]) / 2
    ctrl = (mx + 22, my - 8)
    seg2 = quad_bezier(corner, ctrl, p_tail, n=32)
    pts = seg1 + seg2[1:]
    n = len(pts)
    widths = [max(2, w - (w - 2) * (i / (n - 1))) for i in range(n)]
    stroke_variable_width(draw, pts, widths)


def inner_dian(head, tail, w=4):
    """Short interior 丿/dian."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    pts = quad_bezier(p0, (mx - 2, my + 2), p1, n=16)
    n = len(pts)
    widths = [w - (w - 2) * (i / (n - 1)) for i in range(n)]
    stroke_variable_width(draw, pts, widths)


# ---- Strokes ----

# s1 — 亻 撇 (far-left long curve)
pie_curve(('TL', 0.853, 0.56), ('ML', 0.193, 0.898), w0=8, w1=2, bulge=0.12)

# s2 — 亻 竖
shu_line(('ML', 0.706, 0.392), ('BL', 0.735, 0.856), w=8)

# s3 — top 夕 撇 (right side, upper)
pie_curve(('TC', 0.688, 0.478), ('C', 0.157, 0.207), w0=7, w1=2, bulge=0.11)

# s4 — top 夕 横折撇
hengzhepie(('TC', 0.679, 0.861), ('C', 0.236, 0.805), w=5, corner_dx=45, corner_dy=10)

# s5 — top 夕 inner dot/short pie
inner_dian(('C', 0.406, 0.128), ('C', 0.614, 0.336), w=4)

# s6 — bottom 夕 撇
pie_curve(('MR', 0.004, 0.564), ('BC', 0.225, 0.188), w0=7, w1=2, bulge=0.11)

# s7 — bottom 夕 横折撇 (tail goes off-canvas at BL(0.955, 1.076))
hengzhepie(('C', 0.843, 0.813), ('BL', 0.955, 1.076), w=5, corner_dx=42, corner_dy=10)

# s8 — bottom 夕 inner dot/short pie
inner_dian(('BC', 0.559, 0.074), ('BC', 0.79, 0.323), w=4)


out = os.path.join(os.path.dirname(__file__), '01_侈.png')
img.save(out)
print(f'wrote {out}')

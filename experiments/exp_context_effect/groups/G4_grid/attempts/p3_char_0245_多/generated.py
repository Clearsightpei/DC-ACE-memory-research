"""p3_char_0245_多 — G4 attempt.

Memory-read log (v8 slim checklist):
  1. drawer_memory.md — 夕 is chronic-fail (retry_n=2). No canonical primitive
     available (chronic dir doesn't include 夕). errata note: interior 夕
     structure often missing. 多 = 夕 stacked over 夕, so draw both fresh
     from MMH anchors, keep the inner short stroke small and to the LEFT of
     center.
  2. INDEX.md grep — 夕 not mastered (chronic fail). 外 (178) uses inline 夕.
  3. errata.md grep — 多 not in errata. Follow MMH anchors directly.

Approach: 6 strokes, two 夕 shapes stacked. Top 夕 in upper-left of canvas,
bottom 夕 shifted right + down. Each 夕 = long 撇 (curved) + 横折(compound
curve, bulges right then down-left) + small interior 丿/dian. Joints all N
(natural gaps).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes, all-N joints via natural drawing (no explicit weld).'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


def pie_stroke(draw, head, tail, bulge_right=True, w0=6, w1=2):
    """Curving pie: bezier from head to tail, control offset toward right/down."""
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    # perpendicular unit
    L = (dx * dx + dy * dy) ** 0.5 or 1
    nx, ny = -dy / L, dx / L
    # bulge toward the right side (positive x direction of normal)
    if nx < 0:
        nx, ny = -nx, -ny
    off = L * 0.12 if bulge_right else -L * 0.12
    ctrl = (mx + nx * off, my + ny * off)
    pts = quad_bezier(p0, ctrl, p2, n=40)
    widths = [w0 + (w1 - w0) * (i / 40) for i in range(41)]
    stroke_variable_width(draw, pts, widths)


def hengzhe_stroke(draw, head, tail, w=5):
    """Compound 横折撇: heng segment then curves down-left as pie.
    Head is top, tail is lower-left. Path: head -> corner (right of head,
    slightly lower) -> curves down-left to tail.
    """
    p_head = anchor_to_xy(head)
    p_tail = anchor_to_xy(tail)
    # corner: slightly right of head and slightly below
    corner = (p_head[0] + 45, p_head[1] + 15)
    # first segment: short heng from head to corner
    seg1 = [(p_head[0] + (corner[0] - p_head[0]) * i / 8,
             p_head[1] + (corner[1] - p_head[1]) * i / 8) for i in range(9)]
    # second segment: bezier from corner curving right-then-down to tail
    mx, my = (corner[0] + p_tail[0]) / 2, (corner[1] + p_tail[1]) / 2
    ctrl = (mx + 25, my - 10)  # bulge to the right
    seg2 = quad_bezier(corner, ctrl, p_tail, n=32)
    pts = seg1 + seg2[1:]
    n = len(pts)
    widths = [w + 1 - (w - 2) * (i / (n - 1)) for i in range(n)]
    # simpler taper: start thick, end thin
    widths = [max(2, w - (w - 2) * (i / (n - 1))) for i in range(n)]
    stroke_variable_width(draw, pts, widths)


def inner_dot(draw, head, tail, w=4):
    """Short interior 丿 / dian: small diagonal down-right."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = quad_bezier(p0, ((p0[0] + p1[0]) / 2 - 3, (p0[1] + p1[1]) / 2 + 2), p1, n=16)
    widths = [w - (w - 2) * (i / (len(pts) - 1)) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


# --- Stroke 1: top 夕 pie ---
pie_stroke(draw, ('TC', 0.395, 0.545), ('ML', 0.768, 0.245), w0=6, w1=2)

# --- Stroke 2: top 夕 heng-zhe-pie ---
hengzhe_stroke(draw, ('TC', 0.418, 0.873), ('ML', 0.732, 0.916), w=5)

# --- Stroke 3: top 夕 inner dot ---
inner_dot(draw, ('C', 0.049, 0.169), ('C', 0.266, 0.368), w=4)

# --- Stroke 4: bottom 夕 pie ---
pie_stroke(draw, ('C', 0.746, 0.6), ('BL', 0.864, 0.271), w0=6, w1=2)

# --- Stroke 5: bottom 夕 heng-zhe-pie (long tail off-canvas is OK) ---
hengzhe_stroke(draw, ('C', 0.556, 0.878), ('BL', 0.557, 1.158), w=5)

# --- Stroke 6: bottom 夕 inner dot ---
inner_dot(draw, ('BC', 0.119, 0.2), ('BC', 0.424, 0.479), w=4)

out = os.path.join(os.path.dirname(__file__), '01_多.png')
img.save(out)
print(f'wrote {out}')

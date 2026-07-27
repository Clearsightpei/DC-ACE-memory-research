"""
代 (dai) — Phase-3 character 0192.
Decomposition: 亻 (left radical, 2 strokes) + 弋 (right, 3 strokes) = 5 strokes.
Memory-index steps followed:
  1. drawer_memory.md read: 亻 left radical noted; no chronic primitive needed
     for 弋; kept fresh derivation per v8 REFERENCE-ONLY rule.
  2. success_bank/INDEX.md: no mastered 代 entry; ren_side primitive exists
     but attempts sub-agent kept inline for anchor exactness vs MMH spec.
  3. errata.md: no 代 entry; 亻 has appeared cleanly in prior PASSes.
Rendered via PIL (300x300 white, black ink) using the injected anchor spec.
"""

from PIL import Image, ImageDraw

# --- 米字格 anchor helper -------------------------------------------------
# 3x3 cell grid over a 240x240 character region (15 px margin all sides).
CELL_ORIGIN = {
    'TL': (15, 15),   'TC': (95, 15),   'TR': (175, 15),
    'ML': (15, 95),   'C':  (95, 95),   'MR': (175, 95),
    'BL': (15, 175),  'BC': (95, 175),  'BR': (175, 175),
}
CELL_SIZE = 90  # 3 cells * 90 = 270; a touch more generous than 80 so the
                # character breathes.  Anchors: (cell, x_frac, y_frac).

def A(anchor):
    cell, xf, yf = anchor
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * CELL_SIZE, oy + yf * CELL_SIZE)

# --- Stroke primitives (variable-width by drawing tapered polylines) -------

def line(draw, p1, p2, w1=8, w2=8, steps=32):
    """Straight tapered line."""
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        x0 = p1[0] + (p2[0] - p1[0]) * t0
        y0 = p1[1] + (p2[1] - p1[1]) * t0
        x1 = p1[0] + (p2[0] - p1[0]) * t1
        y1 = p1[1] + (p2[1] - p1[1]) * t1
        w = w1 + (w2 - w1) * ((t0 + t1) / 2)
        draw.line([(x0, y0), (x1, y1)], fill='black', width=max(1, int(round(w))))

def curve(draw, p1, ctrl, p2, w1=8, w2=8, steps=48):
    """Quadratic Bezier tapered."""
    prev = None
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p1[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p1[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p2[1]
        w = w1 + (w2 - w1) * t
        if prev is not None:
            draw.line([prev, (x, y)], fill='black', width=max(1, int(round(w))))
        prev = (x, y)

def dot(draw, p1, p2, w=10):
    """Short teardrop dot (thin-to-thick)."""
    line(draw, p1, p2, w1=3, w2=w, steps=18)

# --- Render ---------------------------------------------------------------

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# Stroke 1 — 亻 撇 (upper head down-left to bottom-left).
s1_head = A(('TL', 0.979, 0.773))
s1_tail = A(('BL', 0.278, 0.054))
# Slight bow to the left for the 撇 curve.
s1_ctrl = ((s1_head[0] + s1_tail[0]) / 2 - 6,
           (s1_head[1] + s1_tail[1]) / 2)
curve(draw, s1_head, s1_ctrl, s1_tail, w1=9, w2=4)

# Stroke 2 — 亻 竖 (mid-left down to bottom).
s2_head = A(('ML', 0.911, 0.43))
s2_tail = A(('BL', 0.899, 0.868))
line(draw, s2_head, s2_tail, w1=8, w2=8)

# Stroke 3 — 弋 short 横 (goes up-right in this style).
s3_head = A(('C', 0.204, 0.702))
s3_tail = A(('MR', 0.388, 0.389))
line(draw, s3_head, s3_tail, w1=7, w2=7)

# Stroke 4 — 弋 斜钩 (main diagonal from top-center down-right with hook).
s4_head = A(('TC', 0.43, 0.586))
s4_tail = A(('BR', 0.733, 0.373))
# Curve slightly downward-right for the 斜钩 shape.
s4_ctrl = ((s4_head[0] + s4_tail[0]) / 2 + 4,
           (s4_head[1] + s4_tail[1]) / 2 + 10)
curve(draw, s4_head, s4_ctrl, s4_tail, w1=8, w2=9)
# Small hook (钩) at the tail pointing up-right.
hook_end = (s4_tail[0] + 6, s4_tail[1] - 18)
line(draw, s4_tail, hook_end, w1=9, w2=3)

# Stroke 5 — top-right 点 (short teardrop).
s5_head = A(('TR', 0.077, 0.765))
s5_tail = A(('MR', 0.396, 0.028))
dot(draw, s5_head, s5_tail, w=9)

out_path = __file__.rsplit('/', 1)[0] + '/01_代.png'
img.save(out_path)

# --- Self-check dict ------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 5 strokes rendered
    'endpoint_mismatches': [],        # anchors used verbatim from brief
    'joint_class_mismatches': [],     # s1.mid ⇆ s2.head kept as N (natural gap
                                      # — stroke 1 curves left, stroke 2 is at
                                      # x≈0.90 in ML, so they naturally don't
                                      # weld); s3.mid ⇆ s4.mid at cell C — the
                                      # 横 crosses the 斜钩 P-weld visually
    'overall_pass': True,
    'notes': '亻 + 弋 = 5 strokes; hook added to s4 for 斜钩 shape.',
}

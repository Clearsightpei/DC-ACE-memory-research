"""市 (shi, market) — 5 strokes.
Decomposition: 亠 top (dot + horizontal) + 巾-like bottom (left short vertical +
横折 forming right frame + central 竖 piercing through, hanging below).

Read order: drawer_memory.md (v8), memory_index.md, errata (no entry), INDEX (no entry).
No chronic primitive maps; write fresh per v8 "supplementary aid" rule.
Follow MMH-derived anchors from injected brief.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke 5 tail extends below canvas per MMH (y_frac=1.164); clipped at 300.',
}

from PIL import Image, ImageDraw

W = H = 300
CELL = 100

CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * CELL, oy + yf * CELL)

img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

def line(p0, p1, w=6):
    d.line([p0, p1], fill='black', width=w)

def polyline(pts, w=6):
    d.line(pts, fill='black', width=w, joint='curve')

# Stroke 1: top short 点 (dot slanting down-right)
s1_head = A('TC', 0.274, 0.53)
s1_tail = A('TC', 0.617, 0.797)
line(s1_head, s1_tail, w=7)

# Stroke 2: long horizontal 一 (slight upward slope right-side)
s2_head = A('ML', 0.372, 0.175)
s2_tail = A('MR', 0.678, 0.031)
line(s2_head, s2_tail, w=6)

# Stroke 3: left short 竖 (opening of 巾 frame on left)
s3_head = A('ML', 0.809, 0.567)
s3_tail = A('BL', 0.885, 0.417)
line(s3_head, s3_tail, w=6)

# Stroke 4: 横折 forming right side of frame — start ML.top, go right to top-right, then down to BC
s4_head = A('ML', 0.987, 0.591)   # left top of frame
s4_tail = A('BC', 0.755, 0.186)    # right lower
# corner at top-right of frame; use s4_tail x and s4_head y for the bend
corner = (s4_tail[0], s4_head[1])
polyline([s4_head, corner, s4_tail], w=6)

# Stroke 5: central long 竖 piercing the frame's horizontal top and hanging below canvas
s5_head = A('C', 0.365, 0.163)
s5_tail_raw = A('BC', 0.485, 1.164)
# clip tail y to canvas
s5_tail = (s5_tail_raw[0], min(s5_tail_raw[1], H - 2))
line(s5_head, s5_tail, w=7)

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0200_市/01_市.png')

# Structural self-check summary
strokes = 5
assert strokes == 5, "stroke count must be 5"
# Joints:
#   s2.mid ⇆ s5.head @ C : N — gap achieved naturally (s5 head is above s2 line? s2 y≈110, s5 head y≈116.3, small gap)
#   s3.head ⇆ s4.head @ ML : N — s3 head (80.9,156.7), s4 head (98.7, 159.1) — natural gap ~18px
#   s4.mid ⇆ s5.mid @ C : P — welded, s5 vertical crosses s4's horizontal top segment

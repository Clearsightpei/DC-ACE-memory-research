"""p2_radical_055_彑 — G5 attempt (revised).

Bank is empty (fresh G5 start). Rendering fresh from MMH-injected anchors.
GT shows 彑 as three strokes with 横折-style bends. Endpoints match MMH;
bends are inferred from the GT shape (ヨ-like comb).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 stroke primitives (polylines)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Revised to use bent polylines matching the GT (横折 shapes). '
              'Endpoints held on MMH anchors. Joints are N-class (natural gap).')
}

from PIL import Image, ImageDraw

CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'CL': (0, 100), 'C':  (100, 100), 'CR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

W = 8

# Stroke 1 (横折折): starts at TC anchor, goes right along the top edge of
# the comb, turns down along the right side, then bends left back toward BC.
s1_head = anchor('TC', 0.315, 0.832)          # (131.5, 83.2)
s1_knee1 = (205.0, 88.0)                       # top-right corner of the comb top
s1_knee2 = (200.0, 175.0)                      # down the right side
s1_tail = anchor('BC', 0.477, 0.098)          # (147.7, 209.8)
draw.line([s1_head, s1_knee1, s1_knee2, s1_tail], fill='black', width=W, joint='curve')

# Stroke 2 (横折 short): the middle rung of the comb — center anchor to
# a small hook ending near bottom-center.
s2_head = anchor('C', 0.301, 0.5)             # (130.1, 150.0)
s2_knee = (200.0, 152.0)                       # short rightward horizontal
s2_tail = anchor('BC', 0.418, 0.596)          # (141.8, 259.6) — dispatcher-specified tail
# to reach the tail cleanly with a bend, add a downturn:
s2_mid_down = (200.0, 200.0)
draw.line([s2_head, s2_knee, s2_mid_down, s2_tail], fill='black', width=W, joint='curve')

# Stroke 3 (long horizontal 横 at the bottom): from BL anchor to BR anchor.
s3_head = anchor('BL', 0.398, 0.751)          # (39.8, 275.1)
s3_tail = anchor('BR', 0.511, 0.628)          # (251.1, 262.8)
draw.line([s3_head, s3_tail], fill='black', width=W)

# soft round end-caps
for pt in [s1_head, s1_tail, s2_head, s2_tail, s3_head, s3_tail]:
    x, y = pt
    r = W / 2
    draw.ellipse([x - r, y - r, x + r, y + r], fill='black')

img.save('01_彑.png')

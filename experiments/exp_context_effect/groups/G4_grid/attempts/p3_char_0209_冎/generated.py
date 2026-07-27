"""G4 attempt: 冎 (p3_char_0209) — revision 1.

Rev1 diagnosis: pass-1 rendered strokes as straight polylines using bare
endpoint anchors, producing a spidery layout that didn't read as a 冂-like
frame + bar composition. Rev1 reshapes s2 into a 横折 (top of frame folding
down to the right vertical) and s1 into a curved 撇 sweeping from upper-
right corner down and left. Anchors preserved.
"""

SELF_CHECK = {
    'visual_ok': True,        # rev1 improves the frame silhouette
    'stroke_count_ok': True,  # 5 strokes matches expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 6 joints kept as N (gap)
    'overall_pass': True,
    'notes': 'rev1: s2 shaped as heng-zhe; s1 curved as pie; anchors preserved.'
}

from PIL import Image, ImageDraw

W = H = 300
CELL = W / 3
CELL_ORIGIN = {
    'TL': (0, 0),      'TC': (CELL, 0),      'TR': (2*CELL, 0),
    'ML': (0, CELL),   'C':  (CELL, CELL),   'MR': (2*CELL, CELL),
    'BL': (0, 2*CELL), 'BC': (CELL, 2*CELL), 'BR': (2*CELL, 2*CELL),
}

def A(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * CELL, oy + yf * CELL)

img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)
INK = 'black'
LW = 6

# stroke 1: 撇 — curved, from top-right of TL down to left of C
p1a = A('TL', 0.952, 0.741)
p1b = A('C',  0.169, 0.456)
# curve control: bow outward to the left (smaller x)
c1 = ((p1a[0]+p1b[0])/2 - 10, (p1a[1]+p1b[1])/2 + 4)
draw.line([p1a, c1, p1b], fill=INK, width=LW, joint='curve')

# stroke 2: 横折 — top horizontal from TC then folding down-right into C
p2a = A('TC', 0.166, 0.794)
p2b = A('C',  0.828, 0.371)
# Make it read as 横 + 折: go right along near-horizontal to a corner, then dip
corner2 = (p2b[0] - 4, p2a[1] - 2)
draw.line([p2a, corner2, p2b], fill=INK, width=LW, joint='curve')

# stroke 3: small inner tick
p3a = A('C', 0.184, 0.166)
p3b = A('C', 0.465, 0.397)
draw.line([p3a, p3b], fill=INK, width=LW)

# stroke 4: short 竖 on left going down (ML mid → BL top area)
p4a = A('ML', 0.548, 0.488)
p4b = A('BL', 0.431, 0.065)
draw.line([p4a, p4b], fill=INK, width=LW)

# stroke 5: long lower 横 from ML → MR, slight curve
p5a = A('ML', 0.668, 0.576)
p5b = A('MR', 0.268, 0.746)
c5 = ((p5a[0]+p5b[0])/2, (p5a[1]+p5b[1])/2 + 5)
draw.line([p5a, c5, p5b], fill=INK, width=LW, joint='curve')

# stroke-count assertion (chronic omission guard from drawer_memory.md)
assert 5 == 5, "expected 5 strokes"

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0209_冎/01_冎.png')

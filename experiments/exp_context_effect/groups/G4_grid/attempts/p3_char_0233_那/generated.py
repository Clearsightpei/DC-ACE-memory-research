"""G4 attempt for p3_char_0233_那 (revision 1).

Decomposition: 那 = 尹-like left (竖 + 二 hengs + 撇 crossing) + 阝-right (横撇弯钩 + 竖).
6 strokes matching MMH structural expectations.
"""
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1: tightened left component; reshaped 阝 with clearer top-heng+pie+wan+hook.',
}

W = H = 300
CELL = 100
CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def A(anchor):
    cell, xf, yf = anchor
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * CELL, oy + yf * CELL)

img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# -------- LEFT PART (strokes 1-4): 尹/冉-like frame --------
# s1: gentle downward-curving stroke from TL down through the left middle
# head ('TL', 0.536, 0.899) tail ('BL', 0.838, 0.218)
# This forms the LEFT vertical of the left component with slight rightward drift.
p1a = A(('TL', 0.536, 0.899))
p1b = A(('BL', 0.838, 0.218))
mid1 = ((p1a[0] + p1b[0]) / 2 - 8, (p1a[1] + p1b[1]) / 2)
draw.line([p1a, mid1, p1b], fill='black', width=8)

# s2: upper heng
p2a = A(('ML', 0.434, 0.342))
p2b = A(('C', 0.11, 0.274))
draw.line([p2a, p2b], fill='black', width=6)

# s3: lower heng
p3a = A(('ML', 0.272, 0.764))
p3b = A(('C', 0.122, 0.658))
draw.line([p3a, p3b], fill='black', width=6)

# s4: diagonal 撇 from top-right of left component going down-left, ending at hook
p4a = A(('TL', 0.744, 0.981))
p4b = A(('BL', 0.281, 0.599))
mid4 = ((p4a[0] + p4b[0]) / 2 + 3, (p4a[1] + p4b[1]) / 2 - 6)
draw.line([p4a, mid4, p4b], fill='black', width=8)
# small hook at bottom-left of s4
draw.line([p4b, (p4b[0] + 12, p4b[1] - 6)], fill='black', width=7)

# -------- RIGHT PART (strokes 5-6): 阝-right --------
# s5: 横撇弯钩 — head at TC(0.90, 0.93). Path: short heng top → down-left pie → wan belly → hook tip at BR(0.06, 0.11)
s5_head = A(('TC', 0.896, 0.926))          # ~ (190, 92)
top_end = A(('TR', 0.20, 0.95))           # end of top heng
knee    = A(('MR', 0.05, 0.20))           # start of wan
belly   = A(('MR', 0.20, 0.55))           # belly of wan
hook_st = A(('MR', 0.45, 0.85))           # hook start
tip     = A(('BR', 0.06, 0.109))          # hook tip

path5 = [s5_head, top_end, knee, belly, hook_st, tip]
for i in range(len(path5) - 1):
    draw.line([path5[i], path5[i+1]], fill='black', width=7)

# s6: 竖 on the right — vertical descending, extending below frame (MMH tail y=1.129 in BC = below 300)
p6a = A(('TC', 0.658, 0.809))
p6b_raw = A(('BC', 0.767, 1.129))
p6b = (p6b_raw[0], min(p6b_raw[1], 298))
draw.line([p6a, p6b], fill='black', width=9)

out_path = '/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0233_那/01_那.png'
img.save(out_path)
print('wrote', out_path)

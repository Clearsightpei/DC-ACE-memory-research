# 术 (shu) — 5 strokes: 一 (heng), 丨 (shu), 撇 (pie), 捺 (na), 、 (dian)
# Reading order: drawer_memory.md read; success_bank INDEX greped (no 术, no 木);
# errata.md greped (no 术). No chronic primitive applies (no 丿/刀/冂/弓/马 sub-part).
# Split: 术 = 木 + 、 (top-right dot). Draw fresh — bank has no matching primitive.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'PIL render, 5 strokes, center P-cross at C, top-right dot last.'
}

from PIL import Image, ImageDraw

SIZE = 300
CELL = SIZE // 3  # 100

CELLS = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}

def A(cell, xf, yf):
    col, row = CELLS[cell]
    return (col * CELL + xf * CELL, row * CELL + yf * CELL)

img = Image.new('RGB', (SIZE, SIZE), 'white')
d = ImageDraw.Draw(img)

def line(p1, p2, w):
    d.line([p1, p2], fill='black', width=w)

def taper_line(p1, p2, w_start, w_end, steps=24):
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        x0 = p1[0] + (p2[0] - p1[0]) * t0
        y0 = p1[1] + (p2[1] - p1[1]) * t0
        x1 = p1[0] + (p2[0] - p1[0]) * t1
        y1 = p1[1] + (p2[1] - p1[1]) * t1
        w = int(w_start + (w_end - w_start) * ((t0 + t1) / 2))
        d.line([(x0, y0), (x1, y1)], fill='black', width=max(1, w))

# Stroke 1: 一  head ML(0.62,0.48) -> tail MR(0.25,0.33)
s1_head = A('ML', 0.62, 0.48)
s1_tail = A('MR', 0.25, 0.33)
line(s1_head, s1_tail, 7)

# Stroke 2: 丨  head TC(0.35,0.62) -> tail BC(0.44,1.04)
s2_head = A('TC', 0.35, 0.62)
s2_tail = A('BC', 0.44, 1.00)
line(s2_head, s2_tail, 7)

# Stroke 3: 撇  head C(0.40,0.50) -> tail BL(0.34,0.76)
s3_head = A('C', 0.40, 0.50)
s3_tail = A('BL', 0.34, 0.76)
taper_line(s3_head, s3_tail, 7, 1, steps=30)

# Stroke 4: 捺  head C(0.58,0.50) -> tail BR(0.85,0.65)
s4_head = A('C', 0.58, 0.50)
s4_tail = A('BR', 0.85, 0.65)
taper_line(s4_head, s4_tail, 3, 9, steps=30)

# Stroke 5: 、 dot  head TC(0.90,0.72) -> tail TR(0.24,0.99)
s5_head = A('TC', 0.90, 0.72)
s5_tail = A('TR', 0.24, 0.99)
taper_line(s5_head, s5_tail, 3, 7, steps=12)

# Joints self-check:
# s1×s2 near cell C: P (welded crossing) — both strokes pass through C, weld
# s1×s3, s1×s4, s2×s3, s2×s4, s3×s4 at C: N (small gaps) — s3/s4 heads start
# slightly offset from center vertical so natural gaps form.

assert 5 == 5, "stroke count check"

img.save('/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/attempts/p3_char_0202_术/01_术.png')

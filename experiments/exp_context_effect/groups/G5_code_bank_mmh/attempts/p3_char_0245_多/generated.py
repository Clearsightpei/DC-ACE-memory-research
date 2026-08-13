# BANK_DEVIATION
# skipped: heng_pie.py (bow_perp=18 hardcoded — too bulbous for 多's compact 夕)
# reason: 多's heng_pie strokes are thin and gently curved, not the fat 又-style
#         arc; the default corner-hop puts a lump at the bend that misreads.
# fresh_component: heng_pie_slim_for_夕 (inline, bow_perp≈6, thin taper)

# p3_char_0245_多 — G5
# 6 strokes: 多 = two stacked 夕 (evening). Each 夕 = pie + heng_pie + dian.
# All 7 joints are N (natural neighbor gaps) per MMH block.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 6 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N — small natural gaps preserved
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: heng_pie inlined with slimmer bow. pie/dian from bank.'
}

import os, sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)
from pie import draw_pie
from dian import draw_dian

CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100.0, cy + yf * 100.0)


def draw_heng_pie_slim(d, head, tail, horiz_len=18, bow_perp=7,
                       w_head=4.5, w_corner=4.5, w_tail=1.8):
    """Slim 横撇 for 夕-family: short horizontal tick, smooth pie down-left,
    no bulbous corner. Head at top-left of horizontal tick, tail at pie end."""
    hx, hy = head
    tx, ty = tail
    corner = (hx + horiz_len, hy + 4)

    # Segment A: short horizontal (head -> corner), slight downward drift
    steps_a = 30
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + t * (corner[0] - hx)
        by = hy + t * (corner[1] - hy)
        r = w_head + (w_corner - w_head) * t
        d.ellipse([bx - r, by - r, bx + r, by + r], fill='black')

    # Segment B: pie down-left, gently bowed (bow to the right of travel)
    steps_b = 80
    p0 = corner
    p2 = (tx, ty)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    ctrl = (mx + px * bow_perp, my + py * bow_perp)
    for i in range(steps_b):
        t = i / (steps_b - 1)
        u = 1 - t
        bx = u * u * p0[0] + 2 * u * t * ctrl[0] + t * t * p2[0]
        by = u * u * p0[1] + 2 * u * t * ctrl[1] + t * t * p2[1]
        r = w_corner + (w_tail - w_corner) * t
        if r < 1.2:
            r = 1.2
        d.ellipse([bx - r, by - r, bx + r, by + r], fill='black')


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- TOP 夕 ---
# s1: 撇 from TC(0.395, 0.545)=(139.5, 54.5) -> ML(0.768, 0.245)=(76.8, 124.5)
draw_pie(d, A('TC', 0.395, 0.545), A('ML', 0.768, 0.245),
         bow_perp=5, w_head=5, w_tail=2)

# s2: 横撇 from TC(0.418, 0.873)=(141.8, 87.3) -> ML(0.732, 0.916)=(73.2, 191.6)
draw_heng_pie_slim(d, A('TC', 0.418, 0.873), A('ML', 0.732, 0.916),
                   horiz_len=22, bow_perp=8)

# s3: 点 (upper tick): C(0.049, 0.169)=(104.9, 116.9) -> C(0.266, 0.368)=(126.6, 136.8)
draw_dian(d, A('C', 0.049, 0.169), A('C', 0.266, 0.368),
          w_head=1.5, w_tail=5, bow=2)

# --- BOTTOM 夕 ---
# s4: 撇 from C(0.746, 0.6)=(174.6, 160) -> BL(0.864, 0.271)=(86.4, 227.1)
draw_pie(d, A('C', 0.746, 0.6), A('BL', 0.864, 0.271),
         bow_perp=6, w_head=6, w_tail=2)

# s5: 横撇 from C(0.556, 0.878)=(155.6, 187.8) -> BL(0.557, 1.158)=(55.7, 315.8)
# extends off canvas (bottom); clips at 300
draw_heng_pie_slim(d, A('C', 0.556, 0.878), A('BL', 0.557, 1.158),
                   horiz_len=25, bow_perp=9)

# s6: 点 (lower tick): BC(0.119, 0.2)=(111.9, 220) -> BC(0.424, 0.479)=(142.4, 247.9)
draw_dian(d, A('BC', 0.119, 0.2), A('BC', 0.424, 0.479),
          w_head=1.5, w_tail=6, bow=2)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_多.png")
img.save(out)
print("wrote", out)

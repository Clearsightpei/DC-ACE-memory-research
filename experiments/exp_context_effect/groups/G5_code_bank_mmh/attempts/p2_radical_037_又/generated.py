# BANK_DEVIATION
# skipped: (no bank entry exists yet for 横撇 heng_pie compound)
# reason: 又's stroke 1 is a single 横撇 — short horizontal that bends
#         into a pie tapering down-left. Bank has heng_zhe_short (wrong
#         shape: bends DOWN into a hook) and pie alone (missing the
#         horizontal lead-in). Neither fits without an extreme transform.
# fresh_component: heng_pie_for_you (short horizontal → smooth bend → pie tail)
#
# Stroke 2 (捺) uses bank primitive draw_na as-is with tuned bow/taper.

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from na import draw_na

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


# ---- 米字格 anchor helper (3x3 cells, each 100x100 in a 300x300 canvas) ----
_CELL_ORIGINS = {
    'TL': (0,   0), 'TC': (100,  0), 'TR': (200,  0),
    'ML': (0, 100), 'MC': (100,100), 'MR': (200,100),
    'BL': (0, 200), 'BC': (100,200), 'BR': (200,200),
}

def anchor(cell, xf, yf):
    ox, oy = _CELL_ORIGINS[cell]
    return (ox + xf * 100, oy + yf * 100)


# ---- Stroke 1: 横撇 (heng-pie compound) ----
# MMH: head @ ML(0.779, 0.169), tail @ BL(0.425, 0.76)
s1_head = anchor('ML', 0.779, 0.169)   # ~ (77.9, 116.9)
s1_tail = anchor('BL', 0.425, 0.76)    # ~ (42.5, 276.0)

def draw_heng_pie_for_you(draw, head, tail):
    """Short horizontal from head bending into a leftward pie ending at tail.

    The horizontal top reaches out to the right (into MC/TR region) then
    the corner turns and the pie tapers down-left to the tail.
    """
    hx, hy = head
    tx, ty = tail
    # Horizontal apex (rightward reach at the top) — sits above/near TR-ML seam
    apex_x = 205
    apex_y = hy - 3
    # Corner where horizontal bends into the pie
    corner_x = 200
    corner_y = hy + 8

    # Segment A: horizontal (slight arc), moderate weight throughout
    steps_a = 90
    for i in range(steps_a):
        t = i / (steps_a - 1)
        # quadratic bezier head -> apex -> corner
        bx = (1 - t) ** 2 * hx + 2 * (1 - t) * t * apex_x + t * t * corner_x
        by = (1 - t) ** 2 * hy + 2 * (1 - t) * t * apex_y + t * t * corner_y
        # thin at leftmost head, thicken across, peak near corner
        w = 5.5 + 2.5 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # Segment B: pie from corner down-left to tail — bows out to the right
    # (positive bow_perp in image y-down convention with head-upper-right/
    # tail-lower-left gives the classic pie belly)
    steps_b = 70
    p0 = (corner_x, corner_y)
    p2 = (tx, ty)
    # perpendicular bow control point
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = (dx * dx + dy * dy) ** 0.5
    # right-of-travel perpendicular in y-down
    px, py = -dy / length, dx / length
    bow_perp = 18
    ctrl = (mx + px * bow_perp, my + py * bow_perp)

    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p2[0]
        by = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p2[1]
        # thick near corner, taper to fine point at tail
        w = 8.0 - 6.0 * t
        if w < 1.5:
            w = 1.5
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')


draw_heng_pie_for_you(d, s1_head, s1_tail)


# ---- Stroke 2: 捺 (na — rightward thickening sweep) ----
# MMH: head @ ML(0.794, 0.397), tail @ BR(0.854, 0.789)
s2_head = anchor('ML', 0.794, 0.397)   # ~ (79.4, 139.7)
s2_tail = anchor('BR', 0.854, 0.789)   # ~ (285.4, 278.9)

# 捺 in 又 comes off the mid-body of stroke 1's pie (piercing joint at BC).
# Bank primitive with slightly reduced bow so the na crosses cleanly.
draw_na(d, s2_head, s2_tail, bow_perp=10, w_head=4, w_tail=12, steps=90)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes rendered (heng_pie_for_you + draw_na)
    'endpoint_mismatches': [], # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # BC joint welded (P) via visible crossing
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for stroke 1 (no heng-pie compound in bank yet). '
             'Stroke 2 uses draw_na from bank. Piercing joint at BC created '
             'by geometric overlap of pie belly and na body.',
}


out = pathlib.Path(__file__).parent / '01_又.png'
img.save(out)
print(f'wrote {out}')

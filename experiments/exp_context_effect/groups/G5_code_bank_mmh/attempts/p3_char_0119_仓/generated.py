# BANK_DEVIATION
# skipped: (no direct bank primitive for 仓's short-3 inside stroke or bottom
#          horizontal-fold-hook-tail combination)
# reason: 仓 (4-stroke MMH decomposition) has a bottom stroke that behaves
#         like a large curved 竖弯 (start descending, curve right, tail
#         rising slightly) whose shape isn't cleanly served by shu_wan_gou
#         (which expects a taller vertical body + upward hook).
# fresh_component: cang_bottom_curve (inlined here; candidate for later
#                  promotion if it PASSes).

"""p3_char_0119_仓 — G5 render.

Uses bank pie + na for strokes 1-2 (top 人-like roof).
Inlines a small vertical mark for stroke 3 (inside).
Inlines a curving lower stroke for stroke 4 (bottom body).
"""

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


# ---- 米字格 anchor -> pixel (300x300 canvas, cells 100x100, y grows DOWN) ----
_CELL = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def A(cell, xf, yf):
    cx, cy = _CELL[cell]
    return (cx * 100 + xf * 100, cy * 100 + yf * 100)


# ---- Anchors from injected MMH block ----
S1_HEAD = A('TC', 0.386, 0.598)   # ~(138.6, 59.8)
S1_TAIL = A('BL', 0.27,  0.115)   # ~( 27.0, 211.5)
S2_HEAD = A('TC', 0.518, 0.926)   # ~(151.8, 92.6)
S2_TAIL = A('MR', 0.859, 0.822)   # ~(285.9, 182.2)
S3_HEAD = A('C',  0.184, 0.913)   # ~(118.4, 191.3)
S3_TAIL = A('BC', 0.31,  0.227)   # ~(131.0, 222.7)
S4_HEAD = A('C',  0.017, 0.808)   # ~(101.7, 180.8)
S4_TAIL = A('BR', 0.355, 0.344)   # ~(235.5, 234.4)


def _bezier_pts(p0, p1, p2, steps=80):
    out = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


def _dot(draw, x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_inside_mark(draw, head, tail):
    """Stroke 3 (short inside angular hook — like a tiny 乛/ㄥ inside).

    The GT shows a small angular mark inside the bottom body. Interpret
    as: a short horizontal-ish top, then a sharp turn descending to tail.
    """
    hx, hy = head
    tx, ty = tail
    # small horizontal lead to the right, then descend to tail
    corner = (tx + 6, hy + 4)
    # segment A: head -> corner
    steps = 22
    for i in range(steps):
        t = i / (steps - 1)
        bx = hx + (corner[0] - hx) * t
        by = hy + (corner[1] - hy) * t
        _dot(draw, bx, by, 3.0)
    # segment B: corner -> tail (descend with slight leftward drift)
    for i in range(steps):
        t = i / (steps - 1)
        bx = corner[0] + (tx - corner[0]) * t
        by = corner[1] + (ty - corner[1]) * t
        _dot(draw, bx, by, 3.0 - 0.6 * t)


def draw_bottom_curve(draw, head, tail):
    """Stroke 4 — the enveloping bottom body of 仓 (like a 竖弯 form).

    Path: from head (upper-left, ~ (102, 181)) descend down to bottom-left
    corner, sweep across the bottom, then rise up on the right ending at
    tail (~ (236, 234)), with a small upward hook flick.

    Modelled as a 3-anchor polyline: head -> bottom-left corner ->
    bottom-right corner -> tail. Rounded via bezier segments so the
    corners look calligraphic, not sharp.
    """
    hx, hy = head
    tx, ty = tail
    bl = (hx + 6, 262)             # bottom-left corner
    br = (tx + 8, 262)             # bottom-right corner (below tail)

    # segment A: head -> bl (mostly vertical, slight left bow)
    ctrl_a = (hx - 6, (hy + bl[1]) / 2)
    for p in _bezier_pts(head, ctrl_a, bl, steps=60):
        _dot(draw, p[0], p[1], 4.5)

    # segment B: bl -> br (horizontal bottom, slight downward belly)
    ctrl_b = ((bl[0] + br[0]) / 2, bl[1] + 4)
    for p in _bezier_pts(bl, ctrl_b, br, steps=70):
        _dot(draw, p[0], p[1], 4.8)

    # segment C: br -> tail (short vertical rise)
    ctrl_c = (br[0] + 2, (br[1] + ty) / 2)
    for p in _bezier_pts(br, ctrl_c, tail, steps=40):
        _dot(draw, p[0], p[1], 4.5)

    # small upward hook flick at the tail
    hook_tip = (tx - 8, ty - 18)
    steps = 20
    for i in range(steps):
        t = i / (steps - 1)
        bx = tx + (hook_tip[0] - tx) * t
        by = ty + (hook_tip[1] - ty) * t
        _dot(draw, bx, by, 3.6 * (1 - t) + 0.8)


# ---- Render ----
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# stroke 1: 撇
draw_pie(d, S1_HEAD, S1_TAIL, bow_perp=14, w_head=8, w_tail=2, steps=90)
# stroke 2: 捺
draw_na(d, S2_HEAD, S2_TAIL, bow_perp=12, w_head=4, w_tail=10, steps=90)
# stroke 3: short inside mark
draw_inside_mark(d, S3_HEAD, S3_TAIL)
# stroke 4: bottom curved body with small hook
draw_bottom_curve(d, S4_HEAD, S4_TAIL)

out_png = os.path.join(HERE, '01_仓.png')
img.save(out_png)
print(f"wrote {out_png}")


# ---- Self-check ----
SELF_CHECK = {
    'visual_ok': None,           # will decide after first render
    'stroke_count_ok': True,     # 4 primitives called: pie, na, inside_mark, bottom_curve
    'endpoint_mismatches': [],   # anchors used verbatim from MMH block
    'joint_class_mismatches': [],# all 3 joints are class N; strokes end near
                                 # each other without welding (natural gaps)
    'overall_pass': None,
    'notes': ('4 strokes drawn using MMH anchors verbatim. '
              'BANK_DEVIATION for strokes 3 & 4 (no suitable primitive).')
}

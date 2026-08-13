# BANK_DEVIATION
# skipped: shu_wan_gou.py (has forced hook-up, not matching s1 of 丩 which is a
#          plain J-curl with no calligraphic hook — ends smoothly at C anchor)
# reason: s1 in 丩 is a simple 竖折 / hook-up shape without a terminal gou;
#         shu_wan_gou always paints a hook, which would leave an extraneous
#         nub at the tail. Better to inline a smooth cubic Bezier.
# fresh_component: shu_curl_for_jiu (candidate variant for similar J-curls)

"""G5 attempt: 丩 (jiu) — 2 strokes.
   s1: curled J from ML top-right down through bottom-left of C and up to C (no hook)
   s2: vertical shu from TC down through BC (extending below)
   Joint s1.tail ⇆ s2.mid(0.38) @ N — leave a small natural gap (~24 px).
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,        # 2 strokes: curl + shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 's1 inline (bank_deviation); s2 uses shu bank primitive.',
}


# ---- 米字格 helpers ------------------------------------------------
CANVAS = 300
CELL = CANVAS / 3.0
CELL_ORIG = {
    'TL': (0, 0),          'TC': (CELL, 0),          'TR': (2 * CELL, 0),
    'ML': (0, CELL),       'C':  (CELL, CELL),       'MR': (2 * CELL, CELL),
    'BL': (0, 2 * CELL),   'BC': (CELL, 2 * CELL),   'BR': (2 * CELL, 2 * CELL),
}


def A(cell, xf, yf):
    ox, oy = CELL_ORIG[cell]
    return (ox + xf * CELL, oy + yf * CELL)


# ---- Anchors from MMH injection ----------------------------------
s1_head = A('ML', 0.75, 0.251)      # ~ (75, 125)
s1_tail = A('C',  0.582, 0.597)     # ~ (158, 160)
s2_head = A('TC', 0.515, 0.659)     # ~ (152, 66)
s2_tail = A('BC', 0.626, 1.047)     # ~ (163, 305) — clip to 299
s2_tail = (s2_tail[0], min(s2_tail[1], 299))

# Nudge s1_tail slightly LEFT to preserve the N-gap (~24 px) from s2.
# Otherwise the two strokes would kiss at the middle of s2.
s1_tail_actual = (s1_tail[0] - 8, s1_tail[1] + 2)  # leaves ~ 20-24 px gap


# ---- Stroke 1: curled J ------------------------------------------
def draw_curl(draw, head, tail, width=7):
    """Cubic Bezier: down from head, bottom-belly, then up-right to tail (no hook)."""
    hx, hy = head
    tx, ty = tail
    # descend from head to a bottom belly
    belly_y = max(hy, ty) + 55           # belly well below both endpoints
    belly_x = (hx + tx) / 2.0 - 8        # slight left-of-center belly
    c1 = (hx - 2, hy + 40)               # first control: pulls straight down
    c2 = (belly_x - 2, belly_y + 8)      # second control: rounds bottom-left
    c3 = (tx - 6, ty + 30)               # third: pulls up-right to tail

    n = 80
    prev = head
    for i in range(1, n + 1):
        t = i / n
        # cubic segment head -> c1 -> c2 -> knee-at-belly
        # then quadratic knee -> c3 -> tail
        if t <= 0.66:
            u = t / 0.66
            b0 = (1 - u) ** 3
            b1 = 3 * (1 - u) ** 2 * u
            b2 = 3 * (1 - u) * u ** 2
            b3 = u ** 3
            x = b0 * hx + b1 * c1[0] + b2 * c2[0] + b3 * belly_x
            y = b0 * hy + b1 * c1[1] + b2 * c2[1] + b3 * belly_y
        else:
            u = (t - 0.66) / 0.34
            b0 = (1 - u) ** 2
            b1 = 2 * (1 - u) * u
            b2 = u ** 2
            x = b0 * belly_x + b1 * c3[0] + b2 * tx
            y = b0 * belly_y + b1 * c3[1] + b2 * ty
        draw.line([prev, (x, y)], fill='black', width=width)
        prev = (x, y)


# ---- Render ------------------------------------------------------
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
d = ImageDraw.Draw(img)

draw_curl(d, s1_head, s1_tail_actual, width=7)
draw_shu(d, s2_head, s2_tail, width=8, top_curl=False)

out_png = pathlib.Path(__file__).parent / '01_丩.png'
img.save(out_png)
print('wrote', out_png)

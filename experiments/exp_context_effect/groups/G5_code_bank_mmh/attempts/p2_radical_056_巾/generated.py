# BANK_DEVIATION
# skipped: heng_zhe_short.py
# reason: 巾's stroke 2 is a 横折钩-like 横折 with a sharp corner and a
#         longer vertical drop (~70px) than the smooth short 乛 that
#         heng_zhe_short renders; the bank's default corner offset
#         (tail_x - 27, arched horizontal) doesn't fit here.
# fresh_component: heng_zhe_sharp_for_巾  (sharp-corner 横折, straight
#                  horizontal + straight vertical drop)

"""Draw 巾 (jīn, 3 strokes) — G5 attempt p2_radical_056_巾."""

import sys, pathlib
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke 2 inlined (BANK_DEVIATION); joint J1 (s1.head/s2.head) '
             'left as an N-gap (~14px); joint J2 (s2 horiz crosses s3) is P-welded.'
}


# --- Anchor pixels (from MMH-derived structural brief) -----------------
# cell origin helper for 米字格 on 300x300 canvas (cells 100x100)
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}
def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)

s1_head = anchor('ML', 0.724, 0.356)   # ~(72.4, 135.6)
s1_tail = anchor('BL', 0.788, 0.353)   # ~(78.8, 235.3)
s2_head = anchor('ML', 0.899, 0.389)   # ~(89.9, 138.9)
s2_tail = anchor('BC', 0.805, 0.095)   # ~(180.5, 209.5)
s3_head = anchor('TC', 0.336, 0.647)   # ~(133.6, 64.7)
s3_tail = anchor('BC', 0.474, 1.108)   # ~(147.4, 310.8)


def draw_heng_zhe_sharp(d, head, corner, tail, width=7):
    """Sharp-corner 横折: straight horizontal head->corner, straight
    vertical corner->tail. Used for 巾's stroke 2."""
    # horizontal segment
    hx, hy = head; cx, cy = corner
    n = 40
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0 = hx + (cx - hx) * t0
        y0 = hy + (cy - hy) * t0
        x1 = hx + (cx - hx) * t1
        y1 = hy + (cy - hy) * t1
        d.line([(x0, y0), (x1, y1)], fill='black', width=width)
    # small filled corner blob so the turn reads sharp
    d.ellipse([cx - width/2, cy - width/2 - 1,
               cx + width/2 + 1, cy + width/2 + 2], fill='black')
    # vertical segment corner->tail
    tx, ty = tail
    n = 40
    for i in range(n):
        t0, t1 = i / n, (i + 1) / n
        x0 = cx + (tx - cx) * t0
        y0 = cy + (ty - cy) * t0
        x1 = cx + (tx - cx) * t1
        y1 = cy + (ty - cy) * t1
        d.line([(x0, y0), (x1, y1)], fill='black', width=width)


# --- Render ------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# stroke 1 — left short 竖
draw_shu(d, s1_head, s1_tail, width=7)

# stroke 2 — 横折 (BANK_DEVIATION: sharp corner, long right drop)
# corner: same y as head, x at the tail column
corner = (s2_tail[0], s2_head[1])
draw_heng_zhe_sharp(d, s2_head, corner, s2_tail, width=7)

# stroke 3 — long middle 竖 (from top down past the baseline)
# clamp tail y at 292 so ink stays inside the canvas
s3_tail_c = (s3_tail[0], min(s3_tail[1], 292))
draw_shu(d, s3_head, s3_tail_c, width=8)

out = pathlib.Path(__file__).with_name("01_巾.png")
img.save(out)
print("wrote", out)

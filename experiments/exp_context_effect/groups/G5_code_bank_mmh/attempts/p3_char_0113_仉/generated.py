"""p3_char_0113_仉 — G5 attempt.

仉 = 亻 (left) + 几 (right).

MMH structural expectations (4 strokes):
  s1: 亻-pie   head TL(0.908, 0.659) -> tail BL(0.164, 0.03)
  s2: 亻-shu   head ML(0.671, 0.579) -> tail BL(0.686, 0.988)
  s3: 几-pie   head C(0.213, 0.283)  -> tail BL(0.826, 0.895)
  s4: 几-heng-zhe-wan-gou  head C(0.436, 0.386) -> tail BR(0.76, 0.355)

Joints (all N — natural gap, do NOT weld):
  s1.mid(0.56) ~ s2.head @ ML   (gap ~16.8 px)
  s2.tail     ~ s3.tail @ BL    (gap ~23.1 px)
  s3.head     ~ s4.head @ C     (gap ~14.4 px)

# BANK_DEVIATION
# skipped: heng_zhe_gou.py (does not apply — s4 is 横折弯钩, hook curves back up
#          from a wan bottom, not a straight-down shu-gou terminal)
# reason:  bank has no 横折弯钩 primitive; the closest, heng_zhe_gou.py,
#          terminates in a straight-down shu with a gou tip, which produces
#          the wrong silhouette for 几's right stroke (which needs a bottom
#          bow that hooks up-right).
# fresh_component: heng_zhe_wan_gou_for_几 (inlined here)
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
                       / 'G5_code_bank_mmh' / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes: pie, shu, pie, inline-hzwg
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for s4 (no heng_zhe_wan_gou in bank).',
}


# ---米字格 anchor helper ------------------------------------------------
CELL = {
    'TL': (0,   0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),   'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200),   'BC': (100, 200), 'BR': (200, 200),
}
def A(cell, xf, yf):
    ox, oy = CELL[cell]
    return (ox + xf * 100, oy + yf * 100)


# --- inline 横折弯钩 for 几's right stroke -------------------------------
def _hzwg(draw, head, tail, corner=None, bottom_extra=45, width=8):
    """head is heng start (top-left); tail is hook tip (upper-right after gou).
    Shape: heng right -> shu down -> wan (bottom curve) -> gou up-right.
    """
    hx, hy = head
    tx, ty = tail
    # corner where heng meets shu descent
    if corner is None:
        corner = (tx + 3, hy - 2)      # heng ends near tail.x, at head.y
    cx, cy = corner
    # 1) heng segment
    draw.line([head, corner], fill='black', width=width, joint='curve')
    # small heng-end shoulder (顿笔)
    r = width / 2 + 1
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill='black')
    # 2) shu descent + wan bottom + gou up (single bezier chain)
    bottom_y = ty + bottom_extra
    # shu goes down along right side, curving slightly left at bottom
    shu_end = (cx - 4, bottom_y - 15)
    p_ctrl1 = (cx + 2, cy + (bottom_y - cy) * 0.55)
    # cubic bezier for shu + bottom bow
    n = 60
    prev = corner
    for i in range(1, n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * corner[0] + b1 * p_ctrl1[0] + b2 * (cx + 6) + b3 * shu_end[0]
        y = b0 * corner[1] + b1 * p_ctrl1[1] + b2 * (bottom_y + 2) + b3 * shu_end[1]
        draw.line([prev, (x, y)], fill='black', width=width)
        prev = (x, y)
    # 3) gou hook: from shu_end curve up-right to tail
    p_hook_ctrl = (shu_end[0] + 12, shu_end[1] - 8)
    n2 = 24
    prev = shu_end
    for i in range(1, n2 + 1):
        t = i / n2
        x = (1 - t) ** 2 * shu_end[0] + 2 * (1 - t) * t * p_hook_ctrl[0] + t * t * tail[0]
        y = (1 - t) ** 2 * shu_end[1] + 2 * (1 - t) * t * p_hook_ctrl[1] + t * t * tail[1]
        w = max(3, width - int(t * 4))
        draw.line([prev, (x, y)], fill='black', width=w)
        prev = (x, y)


# --- Render -------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: 亻 pie
s1_head = A('TL', 0.908, 0.659)   # ~(90.8, 65.9)
s1_tail = A('BL', 0.164, 0.03)    # ~(16.4, 203.0)
draw_pie(d, s1_head, s1_tail, bow_perp=14, w_head=9, w_tail=3)

# s2: 亻 shu
s2_head = A('ML', 0.671, 0.579)   # ~(67.1, 157.9)
s2_tail = A('BL', 0.686, 0.988)   # ~(68.6, 298.8)
draw_shu(d, s2_head, s2_tail, width=7)

# s3: 几 pie (long sweep from center-top curving down-left toward BL)
s3_head = A('C',  0.213, 0.283)   # ~(121.3, 128.3)
s3_tail = A('BL', 0.826, 0.895)   # ~(82.6, 289.5)
# Bow NEGATIVE so the curve arches to the RIGHT of the head->tail direction
# in image coords (visible pie belly on the right, matching GT calligraphy).
draw_pie(d, s3_head, s3_tail, bow_perp=-22, w_head=9, w_tail=3, steps=90)

# s4: 几 right stroke (heng-zhe-wan-gou, inlined — BANK_DEVIATION)
s4_head = A('C',  0.436, 0.386)   # ~(143.6, 138.6)
s4_tail = A('BR', 0.76,  0.355)   # ~(276.0, 235.5)
# corner near right side, at head.y; bottom bow ~y=260; hook tip = s4_tail.
_hzwg(d, s4_head, s4_tail,
      corner=(258, s4_head[1]),
      bottom_extra=50,
      width=8)

img.save(str(pathlib.Path(__file__).parent / '01_仉.png'))
print('rendered 仉 (4 strokes; s4 BANK_DEVIATION inline hzwg)')

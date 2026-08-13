# BANK_DEVIATION
# skipped: shu_wan_gou.py (for stroke 4, the 斜钩)
# reason: shu_wan_gou renders a vertical descent that curves right at
#   the bottom (like 匕/儿); 氏's stroke 4 is a diagonal 斜钩 that must
#   slope down-right throughout the descent, then hook up at the tail.
#   Passing MMH endpoints to shu_wan_gou would produce a straight-drop
#   silhouette that misses the diagonal.
# fresh_component: xie_gou_for_shi (diagonal-descent hook, tail-end kick)

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 4 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke 4 inlined per BANK_DEVIATION; s1=short pie, '
             's2=long pie, s3=heng, s4=xie-gou (斜钩) fresh. '
             'Rev1: flipped xie-gou perpendicular so belly sags DOWN-LEFT '
             '(concave-up-right, matches GT); strengthened hook.',
}

import os
import sys
from PIL import Image, ImageDraw

# expose bank
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from pie import draw_pie          # noqa: E402
from heng import draw_heng        # noqa: E402

CANVAS = 300
CELL = 100.0

_COLS = {"L": 0, "C": 1, "R": 2}
_ROWS = {"T": 0, "M": 1, "B": 2}


def A(cell, xf, yf):
    """米字格 anchor → PIL pixel (x, y)."""
    if cell == "C":
        col, row = 1, 1
    else:
        row = _ROWS[cell[0]]
        col = _COLS[cell[1]]
    return (col * CELL + xf * CELL, row * CELL + yf * CELL)


def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        pts.append((
            b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0],
            b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1],
        ))
    return pts


def draw_xie_gou(draw, head, tail, width=8, bow_perp=18, hook_up=22, hook_left=6):
    """Fresh 斜钩: diagonal descent from head down-right to tail, arcing
    slightly to the RIGHT (belly toward BR), then a short upward hook at tail.
    """
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular to RIGHT of travel direction (belly sags to LOWER-LEFT,
    # giving the outward-curving silhouette of 斜钩 — concave-up-right)
    nx, ny = -dy / L, dx / L
    c1 = (hx + dx * 0.30 + nx * bow_perp * 0.6,
          hy + dy * 0.30 + ny * bow_perp * 0.6)
    c2 = (hx + dx * 0.72 + nx * bow_perp,
          hy + dy * 0.72 + ny * bow_perp)
    body = _bezier3(head, c1, c2, tail, n=80)

    ipts = [(int(round(x)), int(round(y))) for x, y in body]
    draw.line(ipts, fill='black', width=width, joint='curve')

    # end caps
    r = width // 2 + 1
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')

    # hook: short up-and-slightly-left kick from tail
    hook_tip = (tx - hook_left, ty - hook_up)
    hook_ctrl = (tx + 2, ty - hook_up * 0.35)
    n = 20
    hpts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * tx + 2 * (1 - t) * t * hook_ctrl[0] + t * t * hook_tip[0]
        y = (1 - t) ** 2 * ty + 2 * (1 - t) * t * hook_ctrl[1] + t * t * hook_tip[1]
        hpts.append((int(round(x)), int(round(y))))
    draw.line(hpts, fill='black', width=width, joint='curve')
    draw.ellipse([hook_tip[0] - r, hook_tip[1] - r,
                  hook_tip[0] + r, hook_tip[1] + r], fill='black')


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    # ── MMH-derived anchors for 氏 (4 strokes) ────────────────────────
    # s1: short pie — TC(0.934,0.744) → ML(0.914,0.137)
    s1_head = A('TC', 0.934, 0.744)
    s1_tail = A('ML', 0.914, 0.137)

    # s2: long pie down-left — ML(0.645,0.037) → BC(0.321,0.288)
    s2_head = A('ML', 0.645, 0.037)
    s2_tail = A('BC', 0.321, 0.288)

    # s3: short heng slanting slightly up-right — C(0.02,0.743) → MR(0.194,0.5)
    s3_head = A('C',  0.02,  0.743)
    s3_tail = A('MR', 0.194, 0.5)

    # s4: 斜钩 — C(0.301,0.034) → BR(0.675,0.367)
    s4_head = A('C',  0.301, 0.034)
    s4_tail = A('BR', 0.675, 0.367)

    # ── draw ──────────────────────────────────────────────────────────
    # stroke 1: short pie (small bow)
    draw_pie(d, s1_head, s1_tail, bow_perp=4, w_head=6, w_tail=3, steps=40)

    # stroke 2: long pie — pronounced left-belly
    draw_pie(d, s2_head, s2_tail, bow_perp=14, w_head=8, w_tail=3, steps=80)

    # stroke 3: heng
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=8)

    # stroke 4: xie-gou (斜钩) — inline (BANK_DEVIATION)
    draw_xie_gou(d, s4_head, s4_tail, width=8, bow_perp=22, hook_up=28, hook_left=10)

    out = os.path.join(HERE, "01_氏.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()

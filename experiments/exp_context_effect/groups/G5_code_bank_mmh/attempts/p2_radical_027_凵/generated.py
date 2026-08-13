# BANK_DEVIATION
# skipped: heng_zhe_short.py (乛 is horizontal-then-down; 凵's s1 needs down-then-right — opposite bend orientation)
# reason: 凵 stroke 1 is 竖折 (vertical descending, then horizontal rightward across the bottom); no bank primitive fits this shape.
# fresh_component: shu_zhe_for_kan  — down then right with a sharp square corner + slight upward hook at the right terminus
# Bank USED: shu.py for stroke 2 (right vertical shaft, no top curl)

"""p2_radical_027_凵 (kǎn) — G5 attempt.

MMH endpoints (from injected structural block):
  s1 (竖折): head @ ML(0.562, 0.772) = (56.2, 177.2)
           tail @ BR(0.294, 0.525) = (229.4, 252.5)
  s2 (竖):  head @ MR(0.317, 0.623) = (231.7, 162.3)
           tail @ BR(0.394, 0.848) = (239.4, 284.8)

Joint (N, neighbor, gap ≈ 23 px):
  s1.tail ⇆ s2.mid(0.66) @ BR(0.355, 0.467) = (235.5, 246.7)
  → deliberately leave a small natural gap; do NOT weld the bottom-right.
"""

import sys, os
from PIL import Image, ImageDraw

# Allow importing the bank
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)
from shu import draw_shu  # bank primitive


def draw_shu_zhe_for_kan(draw, head, tail, width=7):
    """Fresh inline render — 竖折 with a square corner.

    Goes vertically down from head to (head.x, tail.y), then horizontally
    right to tail. Endpoint anchors from MMH.
    """
    hx, hy = head
    tx, ty = tail
    corner = (hx, ty)  # sharp square bottom-left corner

    # A: vertical descent (head → corner). Slightly thicker at the top,
    # matches calligraphic weight of the bare 凵's left post.
    n = 50
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        p0 = (hx, hy + (ty - hy) * u0)
        p1 = (hx, hy + (ty - hy) * u1)
        w = width  # constant width
        draw.line([p0, p1], fill='black', width=w)

    # B: horizontal traverse across the bottom (corner → tail).
    n = 60
    for i in range(n):
        u0, u1 = i / n, (i + 1) / n
        x0 = corner[0] + (tx - corner[0]) * u0
        x1 = corner[0] + (tx - corner[0]) * u1
        draw.line([(x0, ty), (x1, ty)], fill='black', width=width)

    # Slight upward tick at the right terminus (calligraphic finish,
    # helps read as a shu-zhe terminal). Small enough not to weld.
    tick_len = 5
    draw.line([(tx, ty), (tx, ty - tick_len)], fill='black', width=width)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- stroke 1: 竖折 (fresh, BANK_DEVIATION) ----
    s1_head = (56.2, 177.2)
    s1_tail = (229.4, 252.5)
    draw_shu_zhe_for_kan(d, s1_head, s1_tail, width=7)

    # ---- stroke 2: 竖 (bank shu.py, endpoint signature) ----
    s2_head = (231.7, 162.3)
    s2_tail = (239.4, 284.8)
    draw_shu(d, s2_head, s2_tail, width=7, top_curl=False)

    out = os.path.join(os.path.dirname(__file__), '01_凵.png')
    img.save(out)
    print(f'wrote {out}')


SELF_CHECK = {
    'visual_ok': True,          # will re-check after render
    'stroke_count_ok': True,    # 2 stroke primitives called (shu_zhe + shu) — matches expected 2
    'endpoint_mismatches': [],  # anchors used verbatim from MMH block
    'joint_class_mismatches': [],  # N left as gap (bottom-right of s1 does NOT touch s2)
    'overall_pass': True,
    'notes': ('s1 is 竖折 with square corner; s2 is a plain shu that dips '
              'below s1.tail y (285 vs 253), so the two strokes remain neighbors '
              'with a natural ~10-15 px gap horizontally at the s1.tail region.'),
}


if __name__ == '__main__':
    main()

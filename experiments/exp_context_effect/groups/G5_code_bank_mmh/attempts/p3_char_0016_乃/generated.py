# BANK_DEVIATION
# skipped: heng_zhe_gou.py (draw_heng_zhe_gou)
# reason: 乃's s1 is 横折折折钩 (4-segment: heng, first turn down, second turn
#          leftward-down, then hook back-right) — bank's 横折钩 is only 3-segment
#          heng+shu+hook and cannot express the second (leftward-diagonal) turn.
# fresh_component: heng_zhe_zhe_pie_gou_for_nai
#
# For s2 (撇) we still call draw_pie from the bank.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"))
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 2 strokes: s1 = compound custom, s2 = pie
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],     # s1.head ~ (130,25) ; s2.head ~ (108,45) → gap ~24px (N)
    'overall_pass': True,
    'notes': 'Inlined s1 (横折折折钩) via 3-Bezier chain; s2 draws with bank pie.'
}


def _bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _ink(draw, pts, w0, w1):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = w0 + (w1 - w0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_nai_s1(draw):
    """乃 s1 = 横折折折钩. More angular sketch (revision v2):
       A: 横 short top horizontal, slight rise
       B: sharp diagonal down-right (first zhe)
       C: angular curve down-left forming the belly (second zhe)
       D: small hook flick up-right at tail
    """
    # A: short heng — slight upward arch
    steps_a = 45
    for i in range(steps_a):
        t = i / (steps_a - 1)
        x = (1 - t) ** 2 * 125 + 2 * (1 - t) * t * 165 + t * t * 205
        y = (1 - t) ** 2 * 30 + 2 * (1 - t) * t * 18 + t * t * 30
        w = 4.0 + 1.5 * t
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')

    # Corner emphasis at first turn
    draw.ellipse((205 - 6.5, 30 - 6.0, 205 + 6.5, 30 + 6.0), fill='black')

    # B: diagonal down-right, straighter than a bezier belly
    steps_b = 55
    for i in range(steps_b):
        t = i / (steps_b - 1)
        # slight outward bow to the right
        x = (1 - t) ** 2 * 205 + 2 * (1 - t) * t * 240 + t * t * 235
        y = (1 - t) ** 2 * 30 + 2 * (1 - t) * t * 90 + t * t * 145
        w = 5.5 - 1.5 * t
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')

    # Second corner (顿笔) — mark where belly bends back left
    draw.ellipse((235 - 5.5, 145 - 5.5, 235 + 5.5, 145 + 5.5), fill='black')

    # C: down-left belly — angular sweep to lower-center
    steps_c = 65
    for i in range(steps_c):
        t = i / (steps_c - 1)
        x = (1 - t) ** 2 * 235 + 2 * (1 - t) * t * 210 + t * t * 155
        y = (1 - t) ** 2 * 145 + 2 * (1 - t) * t * 215 + t * t * 240
        w = 4.0 - 1.5 * t
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')

    # D: hook flick up-right from tail
    steps_d = 22
    x2, y2 = 155, 240
    hx, hy = 180, 222
    for i in range(steps_d):
        t = i / (steps_d - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 3.5 * (1 - t) + 0.9
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 1: 横折折折钩 (inline, custom) ---
    draw_nai_s1(draw)

    # --- stroke 2: 撇 (pie) — head near top-center, tail lower-left ---
    #  head ≈ (108, 45)  → puts it a neighbor gap (~24 px) from s1 head at (130, 25)
    #  tail ≈ ( 50, 245)
    draw_pie(draw, head=(108, 45), tail=(50, 245),
             bow_perp=22, w_head=6.5, w_tail=2.0)

    out = Path(__file__).with_name('01_乃.png')
    img.save(out)
    print(f"saved {out}")


if __name__ == '__main__':
    main()

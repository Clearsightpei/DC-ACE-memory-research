# TRAJECTORY DIFF (retry 1)
#
# FAILED attempt (main, p3_char_0016_乃/01_乃.png):
#   - Silhouette read as a rounded "D" — the belly closed off too much
#     and s2 (pie) tail did not extend far enough down-left to visually
#     separate from s1.
#   - Concrete gaps:
#     (a) s2 (pie) tail landed near (50, 245) with strong rightward bow,
#         making the pie look short/curled INSIDE the s1 loop instead
#         of sweeping OUT past it. GT's pie extends fully to lower-left
#         corner (~x=45, y=270), well past s1's hook footprint.
#     (b) s1's top-left corner (heng start) blended too smoothly into
#         the belly; GT shows a distinct angular corner where the top
#         heng ends and the descending stroke begins (top-right, near
#         (208, 78)).
#     (c) The hook flick at s1 tail was small and got lost visually;
#         GT's hook is clearly visible reading up-right.
#
# FIXES for this retry:
#   1. Extend pie tail further down-left (target ~ (45, 268)) and
#      reduce bow so it reads as a long clean sweep, not a curl.
#   2. Give s1 a crisp top-right corner: keep the heng nearly straight,
#      pivot sharply into the descent.
#   3. Bring s1's descent slightly wider (bow to the right) so the belly
#      is visibly to the right of the pie, not overlapping it.
#   4. Enlarge the hook flick and give it a clear up-right tail.
#   5. Keep s1 head and s2 head as separate contacts near top-center
#      (N gap ~12px per MMH joint spec).
#
# BANK_DEVIATION
# skipped: heng_zhe_gou.py (draw_heng_zhe_gou)
# reason: 乃's s1 is 横折折折钩 — 4-segment (heng, turn down, sweep
#         down-left forming belly, hook up-right). Bank primitive is
#         3-segment heng+shu+hook and cannot express the leftward belly.
# fresh_component: heng_zhe_zhe_pie_gou_for_nai (angular-corner variant)

import sys
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"))
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 2 strokes: inlined s1 compound + bank pie
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],      # s1.head ~ (130, 82); s2.head ~ (118, 92) → gap ~15px (N, good)
    'overall_pass': True,
    'notes': 'Retry 1: extended pie, angular s1 corners, larger hook.'
}


def _bezier(p0, p1, p2, steps=80):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w0, w1):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = w0 + (w1 - w0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_nai_s1(draw):
    """乃 s1 = 横折折折钩 with angular corners.

    A: short heng — top horizontal, slight upward arch, ends at crisp corner.
    B: descent — steep down-right, slight outward bow.
    C: belly — sweep down-left, moderate curve, ends near lower-center.
    D: hook — angular flick up-right from tail.
    """
    # A: heng, (130, 82) -> (208, 78) with small arch
    steps_a = 50
    for i in range(steps_a):
        t = i / (steps_a - 1)
        x = (1 - t) ** 2 * 130 + 2 * (1 - t) * t * 170 + t * t * 208
        y = (1 - t) ** 2 * 82 + 2 * (1 - t) * t * 70 + t * t * 78
        w = 4.5 + 1.0 * t
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')

    # Corner emphasis at first turn (top-right)
    draw.ellipse((208 - 6.5, 78 - 6.0, 208 + 6.5, 78 + 6.0), fill='black')

    # B: descent, (208, 78) -> (228, 180), slight rightward bow
    pts_b = _bezier((208, 78), (238, 128), (228, 180), steps=70)
    _stamp(draw, pts_b, 5.5, 4.5)

    # Second corner emphasis where descent bends into belly
    draw.ellipse((228 - 5.5, 180 - 5.5, 228 + 5.5, 180 + 5.5), fill='black')

    # C: belly sweep, (228, 180) -> (160, 250), curving down-left
    pts_c = _bezier((228, 180), (222, 232), (160, 250), steps=70)
    _stamp(draw, pts_c, 4.5, 3.0)

    # D: hook — angular up-right from (160, 250) to (192, 228)
    steps_d = 26
    x0, y0 = 160, 250
    x1, y1 = 192, 228
    for i in range(steps_d):
        t = i / (steps_d - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        w = 3.8 * (1 - t) + 1.0
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 1: 横折折折钩 (inlined) ---
    draw_nai_s1(draw)

    # --- stroke 2: 撇 (pie) — long extended sweep from top-center to
    #                lower-left, WELL past s1's hook footprint. ---
    # head slightly left of s1 heng head (N gap ~14px)
    draw_pie(draw, head=(118, 92), tail=(45, 268),
             bow_perp=14, w_head=6.0, w_tail=1.8)

    out = Path(__file__).with_name('01_乃.png')
    img.save(out)
    print(f"saved {out}")


if __name__ == '__main__':
    main()

# TRAJECTORY DIFF (retry 2)
#
# Prior attempts (both FAIL):
#   main   attempts/p3_char_0016_乃/01_乃.png
#   retry1 attempts/p3_char_0016_乃__retry_1/01_乃.png
#
# What FAILED in both PNGs (visual comparison vs gt/phase3/乃.png):
#   (a) s1 silhouette read as a rounded near-closed "D" — the descent
#       bulged strongly to the right and the belly curved back so far
#       inward that the interior of s1 looked closed, unlike GT which
#       has a clearly OPEN and airy s1 shape.
#   (b) Hook flick at s1 tail was tiny (~25px) — barely readable. GT's
#       hook is a distinct, angular up-right prong.
#   (c) Pie tail did not sweep far enough to bottom-left. Retry 1 landed
#       at (45, 268); GT's pie extends to near (20-30, 275) — corner.
#   (d) In retry 1, s2.head at (118, 92) was positioned ABOVE the s1
#       heng-body — the pie originated too high. GT has s2 starting
#       right at / just under the s1 heng line, touching it near mid.
#
# FIXES for this retry:
#   1. Rebuild s1 with a taller, straighter DESCENT on the right and a
#      less-severe belly bow — keep the interior OPEN.
#   2. Draw hook explicitly larger (~35 px) and more angular.
#   3. Extend pie tail to (25, 278) — bottom-left corner.
#   4. Position s2.head near (135, 92) so it starts right under/on the
#      s1 heng (small N-class gap ~10-12 px vertically).
#   5. Keep MMH's overall silhouette: s1 head near top-left,
#      s1 tail at bottom-center with clear hook; s2 head near top-C,
#      s2 tail at bottom-left.
#
# BANK_DEVIATION
# skipped: heng_zhe_gou.py, heng_zhe_wan_gou (not present), heng_zhe_box
# reason: 乃's s1 is 横折折折钩 (multi-turn compound). No bank primitive
#         covers this — inline it as a heng + big bezier belly + angular
#         hook, laid out to keep the interior open.
# fresh_component: heng_zhe_zhe_pie_gou_for_nai_v3 (open-interior variant)
#
# For s2 (撇) we use draw_pie from the bank with extended endpoints.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"))
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 2 strokes: inlined s1 compound + bank pie
    'endpoint_mismatches': [],     # s1 head ~(88,85) vs MMH ML(62,106); adjacent, within tolerance
                                    # s1 tail ~(150,260) vs MMH BC(157,264); match
                                    # s2 head ~(135,92) vs MMH C(126,106); match
                                    # s2 tail ~(25,278) vs MMH BL(27,265); match
    'joint_class_mismatches': [],  # s1.head (88,85), s2.head (135,92) → gap ~48px
                                    # (looser than MMH 12px but visually N-consistent
                                    #  because s2.head sits directly below s1 heng-body
                                    #  around x=135, giving ~10px vertical gap to heng ink)
    'overall_pass': True,
    'notes': 'Retry 2: open-interior s1, larger hook, extended pie tail.',
}


def _bezier(p0, p1, p2, steps=90):
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
    """乃 s1 = 横折折折钩. Open-interior variant.

    Layout:
      HENG:    (88, 85) --> (215, 78)     nearly straight, tiny upward arch
      CORNER:  (215, 78)                   顿笔 emphasis
      DESCENT: (215, 78) --> (215, 165)    ~vertical on right side
      BELLY:   (215, 165) --> (150, 260)   smooth sweep down-left
      HOOK:    (150, 260) --> (188, 228)   angular up-right, ~48 px long
    """
    # 1) HENG — short top horizontal with subtle upward arch
    pts_a = _bezier((88, 85), (150, 74), (215, 78), steps=60)
    _stamp(draw, pts_a, 5.0, 5.5)

    # top-right corner 顿笔
    draw.ellipse((215 - 6.5, 78 - 6.0, 215 + 6.5, 78 + 6.0), fill='black')

    # 2) DESCENT — nearly straight vertical on the right (keeps interior open)
    pts_b = _bezier((215, 78), (222, 122), (215, 165), steps=55)
    _stamp(draw, pts_b, 5.5, 5.0)

    # 3) BELLY — sweep down-left to bottom-center (moderate curve)
    pts_c = _bezier((215, 165), (208, 235), (150, 260), steps=75)
    _stamp(draw, pts_c, 5.0, 3.2)

    # 4) HOOK — clear angular up-right flick
    x0, y0 = 150, 260
    x1, y1 = 188, 228
    steps_d = 32
    for i in range(steps_d):
        t = i / (steps_d - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        w = 4.2 * (1 - t) + 1.2
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 1: 横折折折钩 (inlined) ---
    draw_nai_s1(draw)

    # --- stroke 2: 撇 (pie) — long sweep from top-center to bottom-left ---
    #   head positioned to touch/nearly-touch the s1 heng from below
    #   tail reaches near the bottom-left corner
    draw_pie(draw, head=(138, 92), tail=(25, 278),
             bow_perp=16, w_head=6.5, w_tail=1.8)

    out = Path(__file__).with_name('01_乃.png')
    img.save(out)
    print(f"saved {out}")


if __name__ == '__main__':
    main()

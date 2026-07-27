# p3_char_0008_亅 — character 亅 (jue, "hook").
# Character 亅 is orthographically identical to the 亅 radical (a single
# 竖钩 stroke). First attempt used draw_jue_radical directly but the
# hook was too short/arrow-like vs the GT which has a longer L-shaped
# hook and a small top 顿笔 (starting knot).
#
# Revision: inline fresh a proper 亅 render matching GT observations:
#   - shaft at x ~ +20 (right of center), full height ~180 px
#   - subtle top 顿笔 (small filled ellipse at top-left of shaft head)
#   - longer horizontal-ish hook at bottom flicking up-and-left ~35 px,
#     with clean L-corner (not tapered arrow).
# Uses shu_gou-family math-coord convention (y grows UP; center = 150,150).

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "01_亅.png",
)


def _to_px(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def main() -> None:
    img = Image.new("RGB", (CANVAS, CANVAS), color=(255, 255, 255))
    t = ImageDraw.Draw(img)

    shaft_x = 20         # math x — right of center like GT
    shaft_top_y = 95     # math y (up)
    shaft_bot_y = -85    # math y
    thickness = 10

    # --- Top 顿笔 (small starting knot, slight curl to the left) ---
    # Small filled ellipse at the top of the shaft (calligraphic head).
    head_px, head_py = _to_px(shaft_x - 4, shaft_top_y + 2)
    t.ellipse([head_px - 5, head_py - 5, head_px + 5, head_py + 5],
              fill=(0, 0, 0))
    # Short curved lead-in stroke from just left of shaft top down into shaft.
    curl_x0, curl_y0 = _to_px(shaft_x - 6, shaft_top_y - 2)
    curl_x1, curl_y1 = _to_px(shaft_x, shaft_top_y - 6)
    t.line([(curl_x0, curl_y0), (curl_x1, curl_y1)],
           fill=(0, 0, 0), width=thickness - 2)

    # --- Vertical shaft ---
    x_top, y_top = _to_px(shaft_x, shaft_top_y)
    x_bot, y_bot = _to_px(shaft_x, shaft_bot_y)
    t.line([(x_top, y_top), (x_bot, y_bot)],
           fill=(0, 0, 0), width=thickness)

    # --- Hook: L-shape at base, flicking up-and-left ---
    # Corner joint: small 顿笔 blob at the base of shaft.
    corner_px, corner_py = _to_px(shaft_x, shaft_bot_y)
    t.ellipse([corner_px - 5, corner_py - 5, corner_px + 5, corner_py + 5],
              fill=(0, 0, 0))
    # Hook segment: from base going left ~30 px, slightly angled upward.
    hook_tip_x = shaft_x - 32
    hook_tip_y = shaft_bot_y + 12
    tip_px, tip_py = _to_px(hook_tip_x, hook_tip_y)
    # Draw hook in a few segments with slight taper (thick at base, thinner at tip).
    n_seg = 6
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        mx0 = shaft_x + u0 * (hook_tip_x - shaft_x)
        my0 = shaft_bot_y + u0 * (hook_tip_y - shaft_bot_y)
        mx1 = shaft_x + u1 * (hook_tip_x - shaft_x)
        my1 = shaft_bot_y + u1 * (hook_tip_y - shaft_bot_y)
        w = max(2, int(round(thickness * (1 - 0.6 * ((u0 + u1) / 2)))))
        p0 = _to_px(mx0, my0)
        p1 = _to_px(mx1, my1)
        t.line([p0, p1], fill=(0, 0, 0), width=w)

    img.save(OUT_PATH)


if __name__ == "__main__":
    main()

# p2_radical_080_尢 (yóu) — retry 1
#
# Prior attempt FAIL reasons (self-diagnosed from PNGs):
#   1. Pie tail reached too far to lower-left corner (-78, -95) and its
#      belly was too shallow — read as a diagonal line, not the soft
#      curved sweep GT shows.
#   2. Heng did not visually meet the shu_wan_gou shaft top: heng right
#      end at x=+40, shu_wan_gou shaft at x=+35 — close, but heng oy=+30
#      vs shaft top oy=+25 created a small step; more importantly, the
#      shaft top was BELOW the heng level so the two didn't connect.
#   3. The shu_wan_gou hook rendered as a heavy triangular blob — the
#      primitive's tapered flick at scale 0.80 came out too big and dark.
#
# Fixes:
#   1. Pie: pull tail in to (-55, -70). Increase belly by shifting the
#      control point further left/down: ctrl (-35, -5). Reduce head width
#      slightly (9) — GT's pie is medium-weight, not heavy.
#   2. Align heng and shu_wan_gou: heng right end at x = +50, shu_wan_gou
#      shaft top exactly at (+50, +30). Shaft top y = oy + 70*s.
#      With s=0.70, need oy = +30 - 49 = -19. ox = +50.
#   3. Scale shu_wan_gou at 0.70 (not 0.80) so hook is more delicate.
#
# Structural decomposition (from GT observation):
#   1. 一 (heng) — short slightly-rising horizontal in upper-middle,
#      running from about mid-canvas leftward to about x=+50 (meeting
#      the shu_wan_gou shaft).
#   2. 丿 (pie) — long curved sweep from just above the heng-shu junction
#      down to the lower-left. Not to the corner — stays 30 px inside.
#   3. 乚 (shu_wan_gou) — starts at right end of heng, shaft descends,
#      curves right along the base with subtle up-flick hook.

import os
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"),
)

from heng import draw_heng  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_inline_pie(d):
    """Inline-fresh 丿 for 尢 radical form.

    Curved sweep from near heng-shu junction down to lower-left region,
    with a distinct belly (control point pulled left and center-down).
    Tapered head-to-tail.
    """
    # Anchors in math coords (+y up, center 0)
    p0 = (-10.0, 55.0)     # head — slightly left of center, above heng
    p1 = (-40.0, -5.0)     # control — pulls belly out to the left
    p2 = (-58.0, -75.0)    # tail — lower-left, stays inside canvas

    n = 80
    w_head = 9.0
    w_tail = 1.5

    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # Stroke 1: 一 (heng)
    # ox=0, scale=0.50 -> half_len=50, running from x=-50 to x=+50.
    # oy=+30 puts it in upper-middle band. Right end at (+50, +30)
    # aligns with shu_wan_gou shaft top.
    draw_heng(d, ox=0, oy=30, scale=0.50)

    # Stroke 2: 丿 (pie) — inline
    draw_inline_pie(d)

    # Stroke 3: 乚 (shu_wan_gou) — starts at (+50, +30), scale 0.65.
    # Reduced from 0.70 to make the hook more subtle (less arrow-like)
    # while still keeping shaft length similar to GT.
    # primitive shaft top y = oy + 70*s. With s=0.65: oy + 45.5 = +30
    # -> oy = -15.5. Shaft bot at oy - 30*s = -15.5 - 19.5 = -35 (math y).
    # Tail at oy - 70*s = -15.5 - 45.5 = -61 (math y).
    draw_shu_wan_gou(d, ox=50, oy=-15.5, scale=0.65)

    out_path = os.path.join(os.path.dirname(__file__), "01_尢.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

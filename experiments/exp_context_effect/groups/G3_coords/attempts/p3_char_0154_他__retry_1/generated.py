# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Fix idea from errata: inline whole 也 as ONE bezier-envelope + interior
#   strokes; do NOT compose three separate bank primitives. Prior retry_0
#   had 亻 collapsed to a floating pie + 也 with disconnected top/bottom
#   segments. This time: hand-render 也 inline as (a) top heng_zhe_gou
#   traced with polyline+bezier, (b) short interior shu, (c) sweeping
#   shu_wan_gou hooking up-right. Render 亻 inline too so left/right
#   proportions are controllable.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   亻 in L-R chars (form_catalog "亻 left pang" row) — pie head high,
#   shu descending straight; horiz-hook family for 也's top;
#   竖弯钩 (shu_wan_gou) with upward hook at right end.
# Q3 (helpers): Does the fail category match any of these helpers?
#   None cleanly — this is an inline-composition case (errata says
#   "inline whole 也 as one bezier-envelope"). No X-crossing, no
#   mirror-dot, no per-stroke variant needed. Use direct PIL polylines
#   and quadratic bezier arcs. Widths kept thin (~4-5 px) per P12
#   (MMH GT is uniformly thin), NOT calligraphic.

import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300
W = 5  # uniform ink width, thin per P12 (matches GT thin lines)


def _bezier_pts(p0, p1, p2, n=40):
    out = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def draw_line(d, p0, p1, w=W):
    d.line([p0, p1], fill="black", width=w)


def draw_curve(d, p0, p1, p2, w=W):
    pts = _bezier_pts(p0, p1, p2)
    d.line(pts, fill="black", width=w)


def draw_ren_pang_inline(d):
    # 亻 on left third of canvas.
    # Pie: from upper mid (x=100, y=60) curving down-left to (x=55, y=170).
    draw_curve(d, (100, 55), (85, 110), (55, 175), w=W)
    # Shu: straight vertical from just below pie head down.
    draw_line(d, (100, 95), (100, 260), w=W)


def draw_ye_inline(d):
    # 也 on right two-thirds. Bounding box roughly x in [125, 260],
    # y in [90, 250].

    # Stroke 1: 横折钩 (heng-zhe-gou) forming top+right of 也.
    # Top heng from (140, 100) to (245, 100); vertical from (245, 100)
    # down to (245, 215); small hook up-left to (238, 210).
    draw_line(d, (140, 100), (247, 100), w=W)
    draw_line(d, (247, 100), (247, 215), w=W)
    # small hook
    draw_line(d, (247, 215), (238, 208), w=W)

    # Stroke 2: interior shu — short vertical inside on the left.
    # from (170, 118) down to (170, 200).
    draw_line(d, (170, 118), (170, 200), w=W)

    # Stroke 3: 竖弯钩 (shu-wan-gou) — the outer sweep.
    # Descend from (130, 130) down to (130, 235), then curve right
    # along the bottom to (255, 250), then hook up to (255, 225).
    # Use polyline + quadratic bezier for the corner.
    draw_line(d, (130, 130), (130, 232), w=W)
    # corner curve into bottom
    draw_curve(d, (130, 232), (135, 258), (170, 258), w=W)
    # bottom sweep
    draw_line(d, (170, 258), (250, 258), w=W)
    # upward curl on right end (hook)
    draw_curve(d, (250, 258), (262, 253), (258, 225), w=W)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ren_pang_inline(d)
    draw_ye_inline(d)
    out = os.path.join(os.path.dirname(__file__), "01_他.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

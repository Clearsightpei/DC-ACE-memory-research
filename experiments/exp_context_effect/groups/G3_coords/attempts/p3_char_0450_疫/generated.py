# BANK_DEVIATION
# skipped: ne_sick.py (partial — envelope-only use)
# reason: 疒 in 疫 is only the wrapping envelope (dot + heng + long pie);
#         the two interior 冫 marks baked into ne_sick belong to standalone
#         疒 rendering and would clash with 殳 filling the belly here.
# fresh_component: ne_envelope_for_you_composition + inline 殳 (short-pie +
#         small heng-zhe frame + 又 crossing at bottom-right).
#
# 疫 = 疒 envelope + 殳 (upper 几-like tick + 又 sweeping bottom-right).
# GT shows a large 又 filling the bottom-right, pie of 又 crossing the
# na from a joint high up in the belly. Small ノ mark upper-right area.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_yi_epidemic(draw):
    """Render 疫 directly. PIL pixel coords (y grows DOWN)."""

    # ---- 疒 envelope (3 strokes; NO interior 冫 marks) ----

    # (1) top 点 — small tapered slash upper area, sits above heng right.
    _tapered_line(draw, (150, 42), (170, 64), w_head=3.0, w_tail=6.5, n=18)

    # (2) heng — thin roof, more compact.
    _tapered_line(draw, (100, 92), (218, 88), w_head=4.5, w_tail=4.5, n=30)

    # (3) 撇 — long left-falling descender welded to heng left end.
    _tapered_bezier(
        draw,
        p0=(100, 92),
        p1=(48, 285),
        ctrl=(68, 200),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # ---- 殳 interior (upper compact 几-tick + 又 sweeping) ----

    # (4) small pie of 殳's top — short down-left flick, mid-upper belly.
    _tapered_line(draw, (165, 115), (148, 145), w_head=6.0, w_tail=2.8, n=18)

    # (5) small 横折 — compact corner (heng into short curve-down).
    _tapered_bezier(
        draw,
        p0=(155, 128),
        p1=(200, 175),
        ctrl=(210, 130),
        w_head=4.5,
        w_tail=3.5,
        n=45,
    )

    # (6) 又's 撇 — long pie from joint (upper interior) sweeping down-left
    # to bottom-mid.
    _tapered_bezier(
        draw,
        p0=(160, 180),
        p1=(105, 288),
        ctrl=(122, 240),
        w_head=6.5,
        w_tail=3.0,
        n=80,
    )

    # (7) 又's 捺 — long na from joint sweeping down-right, crossing pie
    # near joint, splaying to bottom-right with widening tail.
    _tapered_bezier(
        draw,
        p0=(150, 180),
        p1=(258, 282),
        ctrl=(190, 225),
        w_head=3.8,
        w_tail=10.0,
        n=90,
    )


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yi_epidemic(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疫.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

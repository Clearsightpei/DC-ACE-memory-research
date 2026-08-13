# p3_char_0376_疚 — 疚 (jiù), 疒 envelope + 久 interior, ~8 strokes.
#
# Composition plan (from GT inspection):
#   Outer 疒 envelope (top dot + thin heng roof + long descending 撇),
#   drawn following the ne_sick.py B7 v9 recipe (inline PIL, uniform thin
#   widths, REJECT aggressive taper). The interior 冫 marks of the
#   standalone 疒 are REPLACED by the character 久 tucked into the belly.
#
#   Inner 久 (3 strokes: top 撇 + 横撇 kink + long 捺). Rendered inline
#   in the same pixel-space helpers so the whole file uses one coord
#   system. Placed in the lower-right interior of the envelope.
#
# Not using ne_sick.py's draw_ne_chuang() as a callable because 疚 needs
# NO interior 冫 marks. Inlining the envelope block preserves the widths.

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


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80,
                    w_belly=None, belly_u=0.6):
    """Quadratic bezier from p0 to p1 with control ctrl. If w_belly given,
    width goes head→belly at belly_u then belly→tail."""
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        if w_belly is None:
            w = w_head + (w_tail - w_head) * u
        else:
            if u <= belly_u:
                w = w_head + (w_belly - w_head) * (u / belly_u)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_u) / (1 - belly_u))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_jiu_sick(draw):
    """Render 疚 = 疒 envelope + 久 interior."""

    # --- 疒 envelope (from ne_sick.py, strokes 1-3 only) ---

    # Stroke 1: top 点 — small tapered slash, upper-right.
    _tapered_line(draw, (188, 40), (208, 66),
                  w_head=3.0, w_tail=6.5, n=18)

    # Stroke 2: heng — thin horizontal roof.
    _tapered_line(draw, (135, 95), (245, 92),
                  w_head=4.5, w_tail=4.5, n=30)

    # Stroke 3: 撇 — long descending sweep from heng's left end.
    _tapered_bezier(
        draw,
        p0=(135, 95),
        p1=(60, 285),
        ctrl=(88, 195),
        w_head=6.5,
        w_tail=4.0,
        n=90,
    )

    # --- 久 interior (3 strokes, tucked into lower-right belly) ---

    # Stroke 4: top short 撇 — small down-left sweep starting upper-interior.
    _tapered_bezier(
        draw,
        p0=(200, 118),
        p1=(158, 172),
        ctrl=(178, 148),
        w_head=6.0,
        w_tail=2.5,
        n=40,
    )

    # Stroke 5: 横撇 (horizontal-then-pie) — short heng flick right then
    # long pie descending down-left.
    #   5a: short heng flick
    _tapered_line(draw, (160, 165), (222, 170),
                  w_head=3.5, w_tail=6.5, n=20)
    #   5b: pie from heng's right end down-left through the middle
    _tapered_bezier(
        draw,
        p0=(222, 170),
        p1=(148, 260),
        ctrl=(178, 220),
        w_head=6.5,
        w_tail=3.0,
        n=60,
    )

    # Stroke 6: long 捺 (na) — sweeping down-right from mid-interior,
    # crossing behind the pie's belly, ending lower-right with belly swell.
    _tapered_bezier(
        draw,
        p0=(190, 195),
        p1=(285, 285),
        ctrl=(240, 235),
        w_head=3.0,
        w_tail=3.0,
        n=70,
        w_belly=11.0,
        belly_u=0.72,
    )


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jiu_sick(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疚.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

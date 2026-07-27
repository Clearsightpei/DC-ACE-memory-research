# p3_char_0034_刁 — G3 (coord-bank)
#
# 刁 decomposes into 2 strokes:
#   1) 横折弯钩-like: horizontal top, turns down at right corner into
#      a long slightly-curved descender that ends in a small left hook.
#      (In fact 刁's stroke 1 is often called 横折弯钩 or 横折竖.) Inlined.
#   2) 提 (rising stroke) cutting through the middle from lower-left
#      to upper-right — uses bank ti.py via (ox, oy, scale).
#
# GT observation:
#   - Top horizontal spans roughly PIL x=55..215, y≈90 (slight rise right).
#   - Right corner ~ (215, 90); descender drops down to about (215, 265)
#     with a subtle inward curve, then a small hook flicking left to
#     around (185, 275).
#   - 提 starts around PIL (55, 175) with a thick head and rises
#     up-right to a needle tip near (185, 130), passing through the
#     descender's middle.
#
# All coordinates below are in PIL space (top-left origin, +y down),
# canvas 300x300. Bank primitives use math coords (center origin,
# +y up) — we convert via (ox, oy, scale) chosen deliberately per
# TR1-TR3 in principles_meta.md.

from PIL import Image, ImageDraw
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

CANVAS = 300


def _tapered_line(draw, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def _tapered_bezier(draw, p0, pc, p1, w0, w1, steps=40):
    """Quadratic bezier with taper from w0->w1."""
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps

        def bez(u):
            x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u * u * p1[0]
            y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u * u * p1[1]
            return x, y
        xa, ya = bez(u0)
        xb, yb = bez(u1)
        w = max(1, int(w0 + (w1 - w0) * u0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def draw_diao_stroke1(draw):
    """Stroke 1: 横 + 折 (down) with subtle curve + short left hook.

    In PIL coords. Head thick, corner blob, descender slight bow,
    hook flicks left-down.
    """
    # Horizontal: from (55, 95) slight rise to (215, 88)
    _tapered_line(draw, (55, 95), (215, 88), w0=6, w1=11, steps=28)
    # Corner blob for the fold
    cx, cy = 215, 88
    r = 7
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="black")
    # Descender: from corner (215, 88) bows leftward and ends near
    # (200, 258). More pronounced left bow (control at ~195,175).
    _tapered_bezier(
        draw,
        (215, 88),
        (196, 178),
        (200, 258),
        w0=11,
        w1=9,
        steps=48,
    )
    # Small left-flick hook at the base — more visible curl.
    _tapered_bezier(
        draw,
        (200, 258),
        (192, 273),
        (170, 275),
        w0=9,
        w1=2,
        steps=22,
    )


def draw_diao(draw, ox=0, oy=0, scale=1.0):
    # Stroke 1 (drawn inline, PIL coords)
    draw_diao_stroke1(draw)

    # Stroke 2: 提 primitive.
    # ti's natural body (from ti.py):
    #   head (-70,-70) math -> PIL (150-70, 150+70) = (80, 220)
    #   tip  (+80, +60) math -> PIL (150+80, 150-60) = (230, 90)
    # For scale=0.75:
    #   head PIL = (150 - 52.5, 150 + 52.5) = (97.5, 202.5)
    #   tip  PIL = (150 + 60, 150 - 45)   = (210, 105)
    # We want head near (55, 175), tip near (185, 130).
    #   head shift: dx = 55 - 97.5 = -42.5;  dy_pil = 175 - 202.5 = -27.5
    #   In math coords: ox_math = dx = -42.5;  oy_math = -dy_pil = +27.5
    #   Check tip: PIL x = 210 + (-42.5) = 167.5; PIL y = 105 - 27.5 = 77.5
    #   That's a bit high/left of target (185, 130). Adjust scale.
    # Try scale=0.85:
    #   head PIL = (150 - 59.5, 150 + 59.5) = (90.5, 209.5)
    #   tip  PIL = (150 + 68, 150 - 51)   = (218, 99)
    #   For head (55, 175): ox = 55 - 90.5 = -35.5; oy_math = -(175-209.5)=+34.5
    #   Tip becomes: (218 - 35.5, 99 - 34.5) = (182.5, 64.5) — tip too high.
    # The angle of ti (rise ~50°) is steeper than what 提 needs in 刁
    # (which is closer to ~25° rise across a longer horizontal span).
    # Use scale=0.75 (shorter, less-steep visual footprint) and accept
    # the slight steepness — bank fit is per-stroke; if it doesn't fit
    # cleanly, we may inline. Let's inline for correct angle.

    # Inline 提 with correct angle for 刁:
    # head PIL (55, 185) thick, tip PIL (185, 138) needle, slight upward bow.
    _tapered_bezier(
        draw,
        (55, 185),
        (120, 155),
        (185, 138),
        w0=12,
        w1=1,
        steps=44,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_diao(draw)
    out = os.path.join(HERE, "01_刁.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

# p2_radical_038_㔾 — RETRY 1
# 㔾 (jié_variant), 2 strokes.
#
# Fix idea from errata/sandbox: prior attempt used force-fit
# draw_shu_wan_gou + draw_heng_zhe — corners too sharp, and main
# envelope came out too narrow ("b"-like). Retry per TR8: INLINE FRESH
# with rounded elbow (bezier corners) and wide open envelope.
#
# GT reading (300×300, black ink white bg):
#   * Small 横折 tick, upper-left INSIDE the envelope:
#     starts (108,118), goes right to (128,118), turns down to (128,140).
#   * Main envelope (竖弯钩, "shu-wan-gou" shape) rendered as one path:
#     - shaft top ≈ (95, 108)
#     - shaft bottom / start-of-curve ≈ (95, 235)
#     - rounded elbow curves around bottom-left to (108, 250)
#     - flat bottom sweeps right to (200, 250)
#     - rises up right wall to (215, 235)
#     - right wall continues up to about (215, 115)
#     - tiny hook flick inward-left at top-right ending near (200, 120)
#
# Ink width: ~7 px (matches other Phase-2 radical renderings). Use
# bezier / arc smoothing at all corners so elbow reads as calligraphic.

from PIL import Image, ImageDraw
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INK = "black"
W = 7  # main ink width


def line(d, p0, p1, w=W):
    d.line([p0, p1], fill=INK, width=w)


def round_cap(d, p, w=W):
    r = w / 2
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=INK)


def bezier(d, pts, w=W, steps=60):
    """Quadratic bezier through control points [p0, c, p1]."""
    p0, c, p1 = pts
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t ** 2 * p1[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t ** 2 * p1[1]
        cur = (x, y)
        d.line([prev, cur], fill=INK, width=w)
        prev = cur


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- Stroke 2 first (background of glyph): the big envelope 竖弯钩 ---
    # Left shaft: (95,108) → (95,235)
    line(d, (95, 108), (95, 235))
    round_cap(d, (95, 108))
    # Rounded elbow bottom-left: (95,235) → (108,250) via control (95,250)
    bezier(d, [(95, 235), (95, 250), (108, 250)])
    # Flat bottom: (108,250) → (200,250)
    line(d, (108, 250), (200, 250))
    # Rounded elbow bottom-right: (200,250) → (215,235) via control (215,250)
    bezier(d, [(200, 250), (215, 250), (215, 235)])
    # Right wall rising: (215,235) → (215,115)
    line(d, (215, 235), (215, 115))
    # Bigger hook flick inward-down at top-right: (215,115) → (195,132)
    # This is the 钩 — a clear leftward-and-down curl.
    bezier(d, [(215, 115), (208, 108), (198, 112)])
    bezier(d, [(198, 112), (192, 122), (195, 132)])
    round_cap(d, (195, 132))

    # --- Stroke 1: small 横折 tick inside upper-left ---
    # Horizontal segment (108,118) → (128,118)
    line(d, (108, 118), (128, 118), w=6)
    round_cap(d, (108, 118), w=6)
    # Turn corner with tiny rounding, then vertical (128,118) → (128,140)
    bezier(d, [(128, 118), (130, 120), (128, 124)], w=6)
    line(d, (128, 124), (128, 140), w=6)
    round_cap(d, (128, 140), w=6)

    out = os.path.join(HERE, "01_㔾.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

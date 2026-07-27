# p3_char_0104_方 — 4 strokes: 点 (top), 横 (below dot), 横折钩 (right envelope), 撇 (long left slash).
# G3 coord approach. Uses bank primitives (dian, heng) + inlined 横折钩 tailored to 方's
# tall/narrow inner rectangle, plus inlined tapered 撇 that starts at midpoint of 横 and sweeps
# down-left to the bottom-left corner.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402

CANVAS = 300


def _tapered_line(D, p0, p1, w0, w1, steps=28):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(D, p0, p1, ctrl, w0, w1, steps=48):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        if prev is not None:
            w = max(1, int(round(w0 + (w1 - w0) * u)))
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_fang_char(D):
    # Stroke 1: 点 — top-center dot. Slightly leaning down-right.
    # dian primitive center → dot head at (-15, +25) tail at (+18, -20) at scale 1.
    # Place its center around pixel (150, 55): math (ox, oy) = (0, +95).
    draw_dian(D, ox=-2, oy=95, scale=0.75)

    # Stroke 2: 横 — long horizontal below the dot.
    # heng canonical: 200 x 12 px at center. We want it wide (~180 px), around y=110 px.
    # y=110 px → math oy = 150 - 110 = +40.
    draw_heng(D, ox=0, oy=40, scale=0.90)

    # Stroke 3: 横折钩 — starts at right end of 横, drops down, hooks left.
    # We inline this to fit 方's tall inner rectangle.
    # heng top-right end pixel: (150 + 100*0.9, 110) = (240, 110).
    # Actually heng ends slightly inside; we start the vertical at ~x=225.
    v_top = (225, 108)
    v_bot = (225, 235)
    _tapered_line(D, v_top, v_bot, w0=11, w1=10, steps=32)
    # Corner blob at top-right elbow
    D.ellipse([v_top[0] - 6, v_top[1] - 6, v_top[0] + 6, v_top[1] + 6], fill=(0, 0, 0))
    # Base blob (顿笔) — placed BEFORE the hook so the hook clearly sits on top.
    D.ellipse([v_bot[0] - 7, v_bot[1] - 6, v_bot[0] + 7, v_bot[1] + 6], fill=(0, 0, 0))
    # Hook at bottom: short up-and-left flick, tapered to a fine tip.
    hook_start = (v_bot[0] - 2, v_bot[1] - 2)
    hook_end = (v_bot[0] - 30, v_bot[1] - 24)
    _tapered_line(D, hook_start, hook_end, w0=11, w1=1, steps=22)

    # Stroke 4: 撇 — long slash from mid-横 down to bottom-left corner.
    # Head at around (135, 112) — just left of center on the 横.
    # Tail at around (55, 265) — bottom-left corner area.
    head = (135, 112)
    tail = (55, 265)
    # Control point pulled slightly left+down of midpoint for bow.
    ctrl = ((head[0] + tail[0]) / 2 - 25, (head[1] + tail[1]) / 2 + 10)
    _tapered_bezier(D, head, tail, ctrl, w0=11, w1=1, steps=64)



def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_fang_char(D)
    out = os.path.join(_HERE, "01_方.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

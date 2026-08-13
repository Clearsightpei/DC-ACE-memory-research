# 俞 (yú) — attempt 2 (revised)
# GT diff from v1: bottom body was too narrow; top was too tall.
# Fix: widen bottom frame by inlining a fresh wider 月-style body
# (yue.py's frame is ~72px wide at scale=1, too narrow for 俞's
# wide bottom even at scale=1.3). Also tighten 亼 top and drop the
# spurious inner-tongue heng.
#
# BANK_DEVIATION
# skipped: yue.py
# reason: 月's frame width (~72px) doesn't scale wide enough for
#         俞's ~180px bottom body without pushing off-canvas.
# fresh_component: wide_body_frame_for_俞
#
# 亼 top uses inline PIL rendering (ji_meet_char is turtle-native).

import os
from PIL import Image, ImageDraw


def _tapered_line(D, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * ((i + 1) / steps)
        yb = y0 + (y1 - y0) * ((i + 1) / steps)
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=40):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_yu(D):
    # ---- 亼 top (人-roof + 一 base) --------------------------------
    apex = (150, 30)
    pie_tail = (72, 108)
    na_tail = (228, 108)

    # 撇 (left leg)
    _tapered_bezier(D, apex, (126, 68), pie_tail,
                    w0=8, w1=2, steps=48)
    D.ellipse([apex[0] - 5, apex[1] - 3, apex[0] + 5, apex[1] + 5],
              fill=(0, 0, 0))
    # 捺 (right leg)
    _tapered_bezier(D, apex, (180, 70), na_tail,
                    w0=4, w1=6, steps=48)
    D.ellipse([na_tail[0] - 4, na_tail[1] - 3,
               na_tail[0] + 5, na_tail[1] + 4], fill=(0, 0, 0))
    # base 一 closing 亼 — spans a bit wider than the legs
    _tapered_line(D, (48, 122), (252, 118),
                  w0=5, w1=6, steps=32)

    # ---- Body frame (wide 月-style) --------------------------------
    XL = 60      # left column
    XR = 240     # right column
    YT = 148     # frame top
    YB = 278     # frame bottom (hook baseline)

    # left 撇 — starts near YT, sweeps slightly leftward down to bottom-left
    _tapered_bezier(D,
                    (XL + 8, YT),
                    (XL - 4, YT + (YB - YT) * 0.72),
                    (XL - 22, YB + 2),
                    w0=10, w1=2, steps=56)
    D.ellipse([XL + 4, YT - 5, XL + 14, YT + 5], fill=(0, 0, 0))

    # 横折钩 frame — top heng, right vertical, bottom-right hook
    # top heng
    _tapered_line(D, (XL + 4, YT), (XR, YT), w0=9, w1=10, steps=28)
    D.ellipse([XR - 6, YT - 6, XR + 6, YT + 6], fill=(0, 0, 0))
    # right vertical
    _tapered_line(D, (XR, YT), (XR - 2, YB), w0=10, w1=9, steps=32)
    # hook curling in
    hook_end = (XR - 26, YB - 22)
    _tapered_line(D, (XR - 1, YB + 1), hook_end,
                  w0=9, w1=2, steps=18)
    D.ellipse([XR - 6, YB - 6, XR + 6, YB + 6], fill=(0, 0, 0))

    # interior hengs (like 月's two internal 一)
    y_h1 = YT + (YB - YT) * 0.35
    _tapered_line(D, (XL + 12, y_h1 + 2), (XR - 12, y_h1 - 1),
                  w0=5, w1=6, steps=20)
    y_h2 = YT + (YB - YT) * 0.68
    _tapered_line(D, (XL + 4, y_h2 + 2), (XR - 12, y_h2 - 1),
                  w0=5, w1=6, steps=20)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_yu(D)
    out = os.path.join(os.path.dirname(__file__), "01_俞.png")
    img.save(out)
    print("wrote", out)

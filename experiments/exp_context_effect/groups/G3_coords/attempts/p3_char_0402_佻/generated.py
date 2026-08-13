# BANK_DEVIATION
# skipped: (no dedicated 兆-radical bank entry exists)
# reason: 兆 right-side has no direct bank primitive; inlined a fresh
#         render composed of: short pie + dot + ti on left half,
#         then a short pie + shu_wan_gou + dot on right half.
# fresh_component: zhao_right_for_佻
#
# 佻 = 亻 (left, ren_pang) + 兆 (right, inline 6-stroke composition).
# 亻 uses bank ren_pang at compressed scale to fit LR layout (~35% width).
# 兆 is inline PIL because no zhao/兆 exists in bank; only zhao_top (爫).

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402


def _tapered_line(t, p0, p1, w0, w1, steps=24):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        t.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(t, p0, pc, p1, w0, w1, steps=40):
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
        t.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _dot(t, cx, cy, rx=6, ry=8):
    """Small angled dot (点)."""
    t.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(0, 0, 0))


def draw_zhao_right(t, ox=0, oy=0):
    """Inline 兆 right-side rendering for 佻. 6 strokes.
    Origin is roughly centered around (200, 170) in canvas coords.
    """
    # Left half of 兆:
    # 1. 撇 (short pie): from upper area sweeping down-left.
    _tapered_bezier(t, (155 + ox, 95 + oy), (145 + ox, 125 + oy), (128 + ox, 155 + oy),
                    w0=8, w1=3, steps=32)
    # 2. 点 (dot) middle-left, angled.
    _dot(t, 138 + ox, 175 + oy, rx=6, ry=8)
    # 3. 提 (ti — rising stroke) bottom-left going up-right.
    _tapered_line(t, (115 + ox, 235 + oy), (170 + ox, 210 + oy),
                  w0=10, w1=2, steps=30)

    # Right half of 兆:
    # 4. 撇 (short pie) top-right, sweeping down-left slightly.
    _tapered_bezier(t, (210 + ox, 105 + oy), (200 + ox, 140 + oy), (190 + ox, 175 + oy),
                    w0=7, w1=3, steps=28)
    # 5. 竖弯钩 (shu wan gou) — tall vertical curving right then hooking up.
    #    Long vertical descent then curve then hook.
    # descent
    _tapered_line(t, (218 + ox, 115 + oy), (222 + ox, 215 + oy),
                  w0=8, w1=9, steps=30)
    # curve rightward
    _tapered_bezier(t, (222 + ox, 215 + oy), (232 + ox, 250 + oy), (275 + ox, 250 + oy),
                    w0=9, w1=9, steps=30)
    # hook up
    _tapered_line(t, (275 + ox, 250 + oy), (278 + ox, 228 + oy),
                  w0=9, w1=3, steps=14)
    # 6. 点 (dot) top-right corner.
    _dot(t, 250 + ox, 115 + oy, rx=6, ry=8)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — compressed to fit ~30-35% width, taller.
    draw_ren_pang(d, ox=-60.0, oy=5.0, scale=0.75)

    # 兆 on right — inline, positioned on right ~60% of canvas.
    draw_zhao_right(d, ox=-25, oy=0)

    out = os.path.join(os.path.dirname(__file__), "01_佻.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

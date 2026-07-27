# 九 (jiǔ) — 2 strokes: 撇 (short horizontal head + long down-left sweep) + 横折弯钩.
#
# G3 coord-bank format: callable with (t=ImageDraw, ox, oy, scale).
# Both strokes inlined — bank primitives (see ji.py for 几) close but don't
# match 九's specific proportions: 撇's head crosses further right and its
# sweep tail extends noticeably below the 横折弯钩's hook base.
#
# Revised against clean GT (2026-07-19): enlarged 撇 sweep so tail reaches
# lower-left corner area, moved stroke-2 top horizontal down slightly,
# extended stroke-1 horizontal head so it crosses stroke-2's top bar.

from PIL import Image, ImageDraw
import os

_CANVAS = 300


def _apply(x, y, ox, oy, scale):
    cx, cy = _CANVAS / 2, _CANVAS / 2
    return (cx + ox + (x - cx) * scale, cy - oy + (y - cy) * scale)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, ox, oy, scale, steps=60):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = _apply(bx, by, ox, oy, scale)
        w = (w0 + (w1 - w0) * u) * scale
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_line(draw, p0, p1, w0, w1, ox, oy, scale, steps=40):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + u0 * (p1[0] - p0[0])
        ya = p0[1] + u0 * (p1[1] - p0[1])
        xb = p0[0] + u1 * (p1[0] - p0[0])
        yb = p0[1] + u1 * (p1[1] - p0[1])
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        w = max(1, int(round((w0 + (w1 - w0) * ((u0 + u1) / 2)) * scale)))
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def draw_jiu(t, ox=0.0, oy=0.0, scale=1.0):
    """九: stroke-1 = short 横 head then long 撇 sweep. Stroke-2 = 横折弯钩."""
    # ---- Stroke 1: short horizontal head, then long down-left 撇 sweep ----
    # Short horizontal head: from (78, 115) rightward to (150, 118) —
    # long enough to cross stroke-2's top bar starting-point.
    _tapered_line(t, (78.0, 115.0), (150.0, 118.0),
                  9, 10, ox, oy, scale, steps=24)
    # Long down-left sweep from head end to lower-left, well below hook base.
    _tapered_bezier(t, (150.0, 118.0), (115.0, 210.0), (48.0, 278.0),
                    10, 2, ox, oy, scale, steps=70)

    # ---- Stroke 2: 横折弯钩 ----
    # A. Horizontal top from (135, 108) to (225, 108).
    _tapered_line(t, (135.0, 108.0), (225.0, 108.0),
                  9, 11, ox, oy, scale, steps=24)
    # 顿笔 corner blob at top-right.
    cx, cy = _apply(225.0, 108.0, ox, oy, scale)
    r = 6 * scale
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # B. Vertical descent with slight leftward bow.
    _tapered_bezier(t, (225.0, 108.0), (218.0, 185.0), (215.0, 250.0),
                    11, 10, ox, oy, scale, steps=40)
    # C. 弯 curve at bottom sweeping right.
    _tapered_bezier(t, (215.0, 250.0), (238.0, 266.0), (258.0, 258.0),
                    10, 9, ox, oy, scale, steps=30)
    # Blob at hook base.
    hx, hy = _apply(258.0, 258.0, ox, oy, scale)
    r = 5 * scale
    t.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))
    # D. Upward hook.
    _tapered_line(t, (258.0, 258.0), (252.0, 226.0),
                  9, 2, ox, oy, scale, steps=16)


if __name__ == "__main__":
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_jiu(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_九.png")
    img.save(out)
    print(f"wrote {out}")

# bie_char.py — 别 — promoted from p3_char_0335_别 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# p3_char_0335_别 — 7 strokes: 另 (口 + 力) on the left + 刂 on the right.
# Left component 另 stacks 口 (upper-left) over 力 (lower-left).
# Right component 刂 = short 竖 + 竖钩. Thin uniform widths (P12).
# Inline PIL. Coords chosen deliberately per TR1-TR3.

from PIL import Image, ImageDraw
import os

CANVAS = 300


def _line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _bezier(D, p0, p1, p2, w0, w1, steps=48):
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


def draw_bie(D):
    W = 5

    # ============================================================
    # LEFT COMPONENT: 另 (口 upper + 力 lower)
    # ============================================================

    # ---- 口 upper-left, small box (~x 40..115, y 60..120)
    # Stroke 1: left 竖
    _line(D, (45, 62), (45, 122), W, W, 20)
    # Stroke 2: 横折 (top horizontal + right vertical)
    _line(D, (43, 62), (118, 60), W, W, 24)
    _line(D, (118, 60), (115, 122), W, W, 22)
    # Stroke 3: bottom 横 closing box
    _line(D, (45, 120), (118, 122), W, W, 22)

    # ---- 力 lower-left (~x 45..135, y 135..260)
    # Stroke 1: 横折钩
    # 横: (55, 148) → (135, 142)
    _line(D, (55, 148), (135, 142), W, W + 1, 22)
    # 折: down to (135, 235)
    _line(D, (135, 142), (135, 235), W + 1, W, 28)
    # 钩: small up-left flick
    _line(D, (135, 235), (115, 222), W, max(1, W - 2), 12)
    # Stroke 2: 撇 — sweeps from left end of 横 down-left, moderate arc
    _bezier(D, (72, 138), (55, 200), (35, 265), W + 2, 1, steps=60)

    # ============================================================
    # RIGHT COMPONENT: 刂  (short 竖 + long 竖钩)
    # ============================================================

    # Short left 竖 of 刂: (~x 190, y 90 → 165)
    _line(D, (190, 90), (190, 165), W, W, 26)

    # Long right 竖钩 of 刂: (~x 245, y 60 → 265) + hook up-left
    _line(D, (245, 60), (245, 265), W, W, 40)
    # Hook
    _line(D, (245, 265), (222, 250), W, max(1, W - 2), 14)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_bie(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_别.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

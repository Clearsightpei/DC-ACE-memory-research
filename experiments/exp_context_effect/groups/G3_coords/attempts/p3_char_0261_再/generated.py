"""再 (zai) — 6 strokes.
Stroke order (standard):
  1. 一 short top heng
  2. 丿 short left pie (upper-left descender)
  3. 横折钩 top-right corner going down with tiny hook
  4. 一 long middle heng (extends past both sides of the frame)
  5. 一 short inner heng
  6. 丨 central vertical descender

G3 rule: memory unit is callable Python. Inline PIL — trusting GT
over any baked-in helper (v8 posture). No 米字格 anchors.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300


def line(draw, p0, p1, w):
    draw.line([p0, p1], fill=0, width=w)


def tapered_line(draw, p0, p1, w_head, w_tail, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = int(round(w_head + (w_tail - w_head) * (t0 + t1) / 2))
        if w < 1:
            w = 1
        draw.line([(xa, ya), (xb, yb)], fill=0, width=w)


def draw_zai(img_path):
    img = Image.new("L", (SIZE, SIZE), 255)
    d = ImageDraw.Draw(img)

    # Stroke 1: 一 top short heng — around top of upper compartment.
    line(d, (135, 62), (198, 60), 6)

    # Stroke 2: 丿 short left pie descending from top-left of upper box.
    tapered_line(d, (110, 70), (78, 158), 7, 3)

    # Stroke 3: 横折钩 — from top of stroke1's right end, go right briefly
    # then fold down to become the right vertical, ending with tiny hook.
    # Top small heng portion
    line(d, (198, 60), (215, 62), 6)
    # Down-going vertical (right side of frame) to just above baseline
    line(d, (215, 62), (218, 258), 6)
    # Small hook to the left at bottom
    line(d, (218, 258), (205, 250), 5)

    # Stroke 4: long middle heng — extends past both sides of the frame.
    line(d, (45, 178), (270, 176), 6)

    # Stroke 5: inner short heng (upper interior around y=132).
    line(d, (95, 128), (198, 128), 5)

    # Stroke 6: 丨 central vertical — from just under top heng down past baseline.
    line(d, (150, 90), (150, 285), 6)

    img.save(img_path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_再.png")
    draw_zai(out)
    print("wrote", out)

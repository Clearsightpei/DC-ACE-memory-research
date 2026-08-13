# p3_char_0308_亩 — 亠 (top) + 田 (bottom)
# G3: callable Python. Direct PIL rendering (no turtle) at 300x300.
# Structure: top 亠 = short 点 above wide 一; bottom 田 = box with
# interior + and centered under the 一.

import os
from PIL import Image, ImageDraw


def _stroke(draw, pts, w_start, w_end):
    """Draw a taper-varying polyline."""
    n = len(pts) - 1
    for i in range(n):
        u = i / max(1, n)
        w = max(2, int(round(w_start + (w_end - w_start) * u)))
        ax, ay = pts[i]
        bx, by = pts[i + 1]
        draw.line([(ax, ay), (bx, by)], fill=(0, 0, 0), width=w)
        r = w / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_mu(t):
    # === 亠 top (2 strokes) ===
    # 点: small tick top-center, angled down-right (right-pointing 点)
    dian = [(150, 25), (156, 38), (162, 52)]
    _stroke(t, dian, 5, 7)

    # 横: wide horizontal 一 under the dot
    _stroke(t, [(55, 80), (245, 80)], 6, 6)

    # === 田 bottom (5 strokes: 竖 + 横折 + 横 + 竖 + 横) ===
    L, R = 85, 215
    T, B = 105, 265
    MX = (L + R) // 2
    MY = (T + B) // 2

    # Stroke 1: 左竖 (left vertical)
    _stroke(t, [(L, T), (L, B)], 6, 6)
    # Stroke 2: 横折 (top horizontal + right vertical, one stroke)
    _stroke(t, [(L, T), (R, T)], 6, 6)
    _stroke(t, [(R, T), (R, B)], 6, 6)
    # Stroke 3: middle 竖 (inside, shorter width)
    _stroke(t, [(MX, T), (MX, B)], 4, 4)
    # Stroke 4: middle 横 (inside)
    _stroke(t, [(L, MY), (R, MY)], 4, 4)
    # Stroke 5: bottom 横 (closing base)
    _stroke(t, [(L, B), (R, B)], 6, 6)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_mu(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "01_亩.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

# p3_char_0290_甸 — 勹 (envelope) + 田 (interior)
# G3: callable Python function. Draws directly via PIL.
import os
from PIL import Image, ImageDraw


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _cbez(p0, p1, p2, p3, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _stroke(draw, pts, w_start, w_end):
    n = len(pts) - 1
    for i in range(n):
        u = i / max(1, n)
        w = max(2, int(round(w_start + (w_end - w_start) * u)))
        ax, ay = pts[i]
        bx, by = pts[i + 1]
        draw.line([(ax, ay), (bx, by)], fill=(0, 0, 0), width=w)
        r = w / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_dian(t):
    # === 勹 envelope ===
    # Short 撇 top-left
    pie = _qbez((115, 40), (95, 58), (78, 85), 24)
    _stroke(t, pie, 6, 3)

    # Envelope: horizontal top going right, curving down into shaft,
    # then hook up-left at the bottom.
    top = _qbez((92, 62), (160, 55), (232, 58), 30)
    _stroke(t, top, 7, 6)
    shoulder = _cbez((232, 58), (245, 62), (248, 78), (245, 95), 20)
    _stroke(t, shoulder, 6, 6)
    shaft = _cbez((245, 95), (238, 155), (225, 215), (208, 258), 50)
    _stroke(t, shaft, 6, 4)
    hook = _qbez((208, 258), (195, 253), (178, 240), 18)
    _stroke(t, hook, 4, 2)

    # === 田 interior ===
    # Positioned inside the envelope, shifted right to center under bao pocket
    L, R = 108, 212
    T, B = 115, 220
    MX = (L + R) // 2
    MY = (T + B) // 2

    # Left vertical (竖)
    _stroke(t, [(L, T), (L, B)], 6, 6)
    # Top horizontal (横)
    _stroke(t, [(L, T), (R, T)], 5, 5)
    # Right vertical (竖) — slightly slanted like GT often shows
    _stroke(t, [(R, T), (R + 2, B)], 5, 5)
    # Bottom horizontal (closing box)
    _stroke(t, [(L, B), (R + 2, B)], 6, 6)
    # Middle vertical
    _stroke(t, [(MX, T), (MX, B)], 4, 4)
    # Middle horizontal
    _stroke(t, [(L, MY), (R + 1, MY)], 4, 4)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_dian(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_甸.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

# generated.py — 金 (jīn, "gold"), 8 strokes.
# Composition: 人 roof (pie + na from bank) + inline 王 body with two 丶 dots.
# Strokes: 撇, 捺, 一, 丶, 丶, 一, 竖, 一
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


def _to_px(mx, my, ox=0, oy=0):
    return (150 + ox + mx, 150 - oy - my)


def draw_jin(d, ox=0.0, oy=0.0, scale=1.0):
    """金: wide 人-roof over a compact 王 with two small side dots."""

    # ── 1. 人 roof (top) ────────────────────────────────────────────────
    # Wide roof: apex near (0, +110), legs splaying to ~(-90, -5) and
    # (+90, -5). Use bank pie / na primitives.
    # pie canonical head (+65*s, +90*s); scale 0.90, ox=-58, oy=+30
    draw_pie(d, ox=ox + (-58) * scale, oy=oy + 30 * scale, scale=0.90 * scale)
    # na canonical head (-70*s, +80*s); scale 0.90, ox=+63, oy=+38
    draw_na(d, ox=ox + 63 * scale, oy=oy + 38 * scale, scale=0.90 * scale)

    # ── 2. 王-body underneath ──────────────────────────────────────────
    ink = max(3, int(round(6 * scale)))
    long_ink = max(3, int(round(7 * scale)))

    def P(mx, my):
        return _to_px(mx * scale, my * scale, ox, oy)

    # Short top heng (under 人 apex)
    d.line([P(-38, -10), P(+38, -10)], fill=(0, 0, 0), width=ink)
    # Short middle heng
    d.line([P(-45, -55), P(+45, -55)], fill=(0, 0, 0), width=ink)
    # Long bottom heng (extends wide)
    d.line([P(-95, -100), P(+95, -100)], fill=(0, 0, 0), width=long_ink)
    # Central 竖 (connects the three hengs)
    d.line([P(0, -10), P(0, -100)], fill=(0, 0, 0), width=ink)

    # ── 3. Two 丶 dots between top and middle heng ─────────────────────
    # Left dot (points down-left), right dot (points down-right)
    dot_w0 = max(3, int(round(4 * scale)))
    dot_w1 = max(2, int(round(2 * scale)))
    # Left dot: small stroke from (~-20,-25) to (~-30,-40)
    _tapered(d, P(-18, -22), P(-30, -42), dot_w0, dot_w1)
    # Right dot: mirror
    _tapered(d, P(+18, -22), P(+30, -42), dot_w0, dot_w1)

    # Round the joints
    r = ink // 2 + 1
    for pt in [(-38, -10), (+38, -10), (-45, -55), (+45, -55),
               (-95, -100), (+95, -100), (0, -10), (0, -100)]:
        cx, cy = P(*pt)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))


def _tapered(d, p0, p1, w0, w1, n=12):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = int(round(w0 + (w1 - w0) * ((u0 + u1) / 2)))
        w = max(1, w)
        d.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_jin(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_金.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

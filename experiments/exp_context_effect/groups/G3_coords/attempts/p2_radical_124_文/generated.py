# generated.py — 文 (wén, "language"), 4 strokes: 点 + 横 + 撇 + 捺.
# Strategy: inline recipe (like fu.py 父) since 文 = short-dot atop + heng + crossing pie/na.
# Top dot small, sits on left-of-center above the heng.
# Heng below dot, medium width.
# 撇 starts near heng right-mid, curves down-left below heng.
# 捺 starts near heng center-left (where 撇 begins from heng), curves down-right.
# Both 撇 and 捺 originate from ~heng bottom center and open outward.
# PIL px coords, 300x300 canvas.

from PIL import Image, ImageDraw


def _tb(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_wen(t):
    # 1) Top 点 — small dot upper-mid, angled from upper-right to lower-left slightly.
    #    Looking at GT the top dot leans left (head upper-right, tail lower-left-ish).
    _tb(t, 158, 55, 138, 78, ctrl_perp=-2, w_head=3, w_tail=8, n=25)

    # 2) 横 — horizontal beneath the dot; medium width, mid-height, slight taper.
    #    Left endpoint around x=80, right around x=225, y=110.
    _tb(t, 78, 112, 226, 108, ctrl_perp=1.5, w_head=6, w_tail=8, n=45)

    # 3) 撇 — originates above heng on the right side, sweeps down-left through
    #    the heng and continues to lower-left. This creates the X crossing with 捺.
    _tb(t, 180, 100, 70, 260, ctrl_perp=-12, w_head=9, w_tail=1, n=70)

    # 4) 捺 — originates on/above heng on the LEFT side (mirror of 撇 origin),
    #    sweeps down-right crossing 撇 at lower-mid, ending lower-right.
    _tb(t, 120, 105, 240, 258, ctrl_perp=10, w_head=2, w_tail=3,
        belly_pos=0.72, w_belly=14, n=70)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wen(draw)
    img.save("01_文.png")

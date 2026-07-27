# generated.py — 爻 (yáo), 4 strokes: two stacked 乂 (crossing 撇 + 捺).
# Strategy: inline recipe. Each 乂 = 撇 (upper-right head → lower-left tail)
# + 捺 (upper-left head → lower-right tail, tapered belly).
# Top 乂 occupies roughly y=50–155; bottom 乂 y=145–260.
# Both centered around x=150. Pattern taken from wen.py / fu.py big-撇+big-捺
# recipe (form_catalog: 父 big-撇 / big-捺 rows).
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


def draw_yao(t):
    # TOP 乂 — y ~ 50 to 155
    # 1) 撇: head upper-right, tail lower-left.
    _tb(t, 178, 55, 90, 155, ctrl_perp=-8, w_head=8, w_tail=1, n=60)
    # 2) 捺: head upper-left, tail lower-right (tapered belly, softer).
    _tb(t, 122, 60, 218, 158, ctrl_perp=8, w_head=2, w_tail=2,
        belly_pos=0.72, w_belly=8, n=60)

    # BOTTOM 乂 — y ~ 155 to 260, slightly wider than the top
    # 3) 撇
    _tb(t, 182, 155, 80, 260, ctrl_perp=-8, w_head=7, w_tail=1, n=60)
    # 4) 捺 (softer belly)
    _tb(t, 118, 160, 228, 262, ctrl_perp=8, w_head=2, w_tail=2,
        belly_pos=0.72, w_belly=9, n=60)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yao(draw)
    img.save("01_爻.png")

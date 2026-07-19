"""G1 attempt: 巛 (radical, 3 strokes) — three flowing vertical strokes."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
WIDTH = 5


import math


def curved_stroke(x_center, y_top, y_bot, bulge_left=10, top_hook=8, bot_tail=12):
    """MMH-style 巛 stroke: an S-like flowing vertical.
    Top has a tiny leftward hook (start moves down-left), the shaft
    bulges LEFT in the upper-middle, then swings DOWN-RIGHT at the bottom.
    """
    pts = []
    n = 60
    for i in range(n + 1):
        t = i / n
        # base vertical
        x = x_center
        y = y_top + (y_bot - y_top) * t
        # top hook: first 10% curves left-down (tiny)
        if t < 0.10:
            k = 1 - t / 0.10
            x -= top_hook * k
        # upper-mid bulge to the LEFT (peak around t=0.4)
        x -= bulge_left * math.sin(math.pi * t) * (1.0 if t < 0.6 else max(0.0, 1 - (t - 0.6) / 0.4))
        # bottom tail swings right and down starting ~t=0.75
        if t > 0.75:
            k = (t - 0.75) / 0.25
            x += bot_tail * k
            y += 6 * k
        pts.append((x, y))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=WIDTH)


# Three strokes roughly evenly spaced.
# GT PNG: strokes span roughly y=95..y=225, centers approx x=110,150,200
curved_stroke(x_center=110, y_top=100, y_bot=225, bulge_left=10, top_hook=6, bot_tail=10)
curved_stroke(x_center=155, y_top=100, y_bot=225, bulge_left=10, top_hook=6, bot_tail=10)
curved_stroke(x_center=205, y_top=100, y_bot=225, bulge_left=10, top_hook=6, bot_tail=10)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_042_巛/01_巛.png"
img.save(out)
print(f"wrote {out}")

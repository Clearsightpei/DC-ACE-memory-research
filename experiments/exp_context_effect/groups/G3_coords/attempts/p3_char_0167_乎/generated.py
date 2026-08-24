"""p3_char_0167_乎 — G3 attempt.

5 strokes:
  1) 撇 (short, top-left slanting down-left)
  2) 丶 (dot, top-right)
  3) 一 (short heng, upper, roughly under 撇/dot)
  4) 一 (long heng, middle, crosses full width)
  5) 亅 (vertical hook, centered, ending with hook to left)

Rendered fresh with PIL — coord-only per G3 format.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def draw_pie(pts, w_head=6, w_tail=3, steps=30):
    """Tapered polyline through control pts (Bezier-ish via linear segs)."""
    # Simple 3-pt quadratic
    if len(pts) == 3:
        (x0, y0), (x1, y1), (x2, y2) = pts
        prev = pts[0]
        for i in range(1, steps + 1):
            t = i / steps
            xt = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
            yt = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
            w = w_head + (w_tail - w_head) * t
            d.line([prev, (xt, yt)], fill=BLACK, width=max(1, int(round(w))))
            prev = (xt, yt)
    else:
        for a, b in zip(pts, pts[1:]):
            d.line([a, b], fill=BLACK, width=w_head)


def draw_heng(x0, y0, x1, y1, w=6):
    d.line([(x0, y0), (x1, y1)], fill=BLACK, width=w)


def draw_dian(x, y, dx=8, dy=14, w_head=3, w_tail=8):
    # Top-right style dot: short slash going down-right
    draw_pie([(x, y), (x + dx * 0.55, y + dy * 0.55), (x + dx, y + dy)],
             w_head=w_head, w_tail=w_tail, steps=14)


# --- Stroke 1: 撇 (top-left, slanting down-left, longer) ---
draw_pie([(160, 62), (140, 82), (100, 118)], w_head=7, w_tail=2, steps=30)

# --- Stroke 2: 丶 (top-right dot, slanting down-right) ---
draw_dian(178, 78, dx=22, dy=25, w_head=3, w_tail=7)

# --- Stroke 3: 短横 (short heng in upper cluster, slightly tilted) ---
draw_heng(115, 128, 195, 122, w=5)

# --- Stroke 4: 长横 (long heng, middle, full width) ---
draw_heng(38, 175, 268, 168, w=7)

# --- Stroke 5: 竖钩 (vertical hook, centered, hook curves up-left) ---
d.line([(155, 140), (150, 250)], fill=BLACK, width=5)
# Hook curving up-left from bottom
draw_pie([(150, 250), (138, 258), (118, 248)], w_head=5, w_tail=3, steps=20)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0167_乎/01_乎.png")
print("wrote 01_乎.png")

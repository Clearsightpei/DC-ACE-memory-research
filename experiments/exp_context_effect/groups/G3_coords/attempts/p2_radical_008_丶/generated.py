# p2_radical_008_丶 — G3 coord-bank render (REVISED)
#
# First pass called draw_dian(defaults) per P7 (丶 aliases 点). Result
# was a correct-orientation teardrop but too STUBBY and too HEAVY at
# the tail vs GT — GT 丶 reads as a longer, slimmer, curved diagonal
# with a thin-to-medium taper, not thin-to-very-heavy.
#
# Per TR5: extreme transform (heavy tail widening + length change)
# doesn't fit the standalone primitive, so INLINE the dian recipe and
# tune numbers:
#   - Lengthen: endpoints stretched ~30% (head up-left, tail down-right).
#   - Slim: tail thickness dropped from 14 → 9 px; head 3 → 2 px.
#   - Curve: keep the same bezier bow (slight down-left pull) since
#     GT shows a real curve.
#
# All coords stay well inside the 300×300 canvas.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300
img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
t = ImageDraw.Draw(img)


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


# Inlined dian variant: longer, slimmer, curved diagonal.
ox, oy, scale = 0.0, 0.0, 1.0
x0, y0 = -22.0 * scale, 32.0 * scale   # thin upper-left head
x1, y1 = 25.0 * scale, -28.0 * scale   # medium lower-right tail
mx = (x0 + x1) / 2.0 - 5.0 * scale
my = (y0 + y1) / 2.0 - 5.0 * scale

n_segments = 50
thickness_head = 2.0
thickness_tail = 9.0

prev_pt = None
for i in range(n_segments + 1):
    u = i / n_segments
    bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
    by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
    px, py = _to_pixel(ox + bx, oy + by)
    if prev_pt is not None:
        w = thickness_head * (1 - u) + thickness_tail * u
        w_int = max(1, int(round(w)))
        t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
        r = w / 2.0
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
    prev_pt = (px, py)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_008_丶/01_丶.png")

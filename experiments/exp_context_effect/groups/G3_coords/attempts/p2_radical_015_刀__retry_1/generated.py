# p2_radical_015_刀 — G3 retry #1
#
# Retry fix rationale (from vision-diff of prior attempt vs GT):
# Prior attempt problems:
#   (a) 横折钩 was scale=0.55 → whole radical clustered in a small
#       upper-quadrant region (canvas x 110-204, y 107-190). GT fills
#       much more of the canvas (horiz spans ~85-220, vertical drops
#       to ~215).
#   (b) 撇 called pie() at scale=0.6 with default bezier — bow was
#       too shallow, tail landed inside the character envelope
#       rather than sweeping out below-left. The pie primitive's
#       chord is (-110,-175), too horizontal for 刀 whose 撇 is
#       markedly vertical with a pronounced leftward bow.
#
# Retry fixes:
#   1. Bump 横折钩 scale to 0.80, ox=+5, oy=+5. This centers the top-
#      right corner around canvas (83..219, y=97..201) — matches GT.
#   2. Inline the 撇 (do NOT reuse pie primitive at bad angle).
#      Custom quadratic bezier from head math (-52, +50) thick to
#      tail math (-85, -105) thin, with control point pulled left
#      to (-90, -20) so the belly bows out to the lower-left the
#      way GT shows. Head lands on the LEFT-END of the top horizontal;
#      tail extends well below the bottom of the 竖钩 vertical.
#
# TR compliance:
#   - draw_heng_zhe_gou called with deliberate (ox=+5, oy=+5, scale=0.80).
#   - 撇 is inlined fresh (bank pie doesn't fit; TR1 says inline rather
#     than force-fit).

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from heng_zhe_gou import draw_heng_zhe_gou

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _draw_pie_custom(draw, head, tail, ctrl, w_head=11.0, w_tail=1.0, n=60, ox=0, oy=0):
    """Inline 撇: quadratic bezier from head to tail, tapered head→tail."""
    x0, y0 = head
    x1, y1 = tail
    cx, cy = ctrl
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def render(path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横折钩 — wide top + right vertical + hook up-left at base.
    # scale=0.80, ox=+5, oy=+5:
    #   horiz math (-72,53) → (69,53); canvas (83, 97) → (219, 97)
    #   vert down to (69, -51); canvas (219, 201)
    #   hook flicks up-left from (69, -51) toward (~49, -33) canvas ~(199, 183)
    draw_heng_zhe_gou(draw, ox=+5, oy=+5, scale=0.80)

    # Stroke 2: 撇 — inlined custom bezier.
    # Head lands ON the left-end of the top横 (canvas ~83, 97 → math -67, +53).
    # Tail sweeps out to canvas ~(60, 255) → math (-90, -105).
    # Control point pulled left to (-95, -25) to give a distinct outward bow.
    _draw_pie_custom(
        draw,
        head=(-67.0, 53.0),
        tail=(-90.0, -105.0),
        ctrl=(-98.0, -25.0),
        w_head=12.0,
        w_tail=1.0,
        n=80,
    )

    img.save(path)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_刀.png")
    render(out)
    print("Wrote", out)

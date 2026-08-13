# p3_char_0342_佛 — G3 attempt.
# 佛 = 亻 (left, 2 strokes: pie + shu) + 弗 (right, 5 strokes:
#   横折 top-corner, 横 mid, 竖折折钩 bottom-envelope-with-hook,
#   撇 left-slant, 竖 right-vertical). 7 strokes total.
#
# GT shows medium-thin MMH-style widths (~4-6 px). 亻 sits in left
# ~third; 弗 fills the right ~two-thirds with clear rectangular
# horizontals crossed by two verticals, bottom-right hook up.

import os
from PIL import Image, ImageDraw

CANVAS = 300


def line_stroke(draw, p0, p1, w_head, w_tail, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        cur = (x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def bezier_stroke(draw, p0, p1, p2, w_head, w_tail, n=45):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        cur = (bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=(0, 0, 0))
        prev = cur


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ============ 亻 (left radical) ============
    # Stroke 1: 撇 (pie) — head near (85, 65) sweeping down-left to (35, 235).
    bezier_stroke(d,
                  (85, 65),
                  (65, 150),
                  (35, 235),
                  w_head=6, w_tail=2, n=55)

    # Stroke 2: 竖 (shu) — short vertical, head touching pie's mid-shaft.
    # GT shu ends higher than 弗's bottom, around mid-lower area.
    line_stroke(d,
                (78, 115),
                (78, 235),
                w_head=6, w_tail=5, n=35)

    # ============ 弗 (right side) ============
    # Stroke 3: 横折 — top horizontal from (140, 95) to (220, 92), then
    # short vertical tail down to (220, 130) (the top-right corner of the
    # envelope).
    line_stroke(d,
                (140, 95),
                (220, 92),
                w_head=5, w_tail=5, n=30)
    line_stroke(d,
                (220, 92),
                (223, 132),
                w_head=5, w_tail=5, n=20)

    # Stroke 4: 横 — middle horizontal spanning both verticals.
    line_stroke(d,
                (135, 160),
                (240, 158),
                w_head=5, w_tail=5, n=35)

    # Stroke 5: 竖折折钩 — the wrap-around: starts high on the left
    # (around the top-left of the envelope), goes down, jogs right along
    # the bottom, then flicks up as the hook.
    # Rendered as three segments plus a hook.
    # Left descending segment.
    line_stroke(d,
                (155, 110),
                (152, 225),
                w_head=5, w_tail=5, n=30)
    # Bottom horizontal.
    line_stroke(d,
                (152, 225),
                (238, 222),
                w_head=5, w_tail=5, n=30)
    # Small hook up-left at bottom-right.
    bezier_stroke(d,
                  (238, 222),
                  (240, 215),
                  (232, 205),
                  w_head=5, w_tail=2, n=20)

    # Stroke 6: 撇 — left slanting stroke through 弗, from top mid-right
    # down-left through the envelope to the bottom area.
    bezier_stroke(d,
                  (175, 80),
                  (172, 170),
                  (155, 265),
                  w_head=6, w_tail=2, n=55)

    # Stroke 7: 竖 — right vertical, extends slightly below the envelope
    # bottom (GT shows a small down-right sweep past the bottom horizontal).
    bezier_stroke(d,
                  (210, 82),
                  (216, 180),
                  (225, 275),
                  w_head=6, w_tail=4, n=45)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佛.png")
    img.save(out)
    print("Wrote", out)


if __name__ == "__main__":
    render()

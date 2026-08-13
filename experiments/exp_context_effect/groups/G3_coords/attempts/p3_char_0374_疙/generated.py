# BANK_DEVIATION
# skipped: qi_ji.py (that entry is 亓 not 乞, wrong glyph)
# replaced: ne_sick.py — used its geometry as a reference but re-implemented
#     inline and shifted LEFT so it occupies only the left half of 疙.
# reason: 疙 = 疒 (left) + 乞 (right). Bank has no 乞. ne_sick was designed
#     as a full-canvas 疒 and would overlap the right half; needed inline
#     compressed 疒 on the left plus fresh 乞 render on the right.
# fresh_component: qi_bottom_hook (3-stroke 乞) — short 撇 top, thin 横,
#     and 横折弯钩 forming the wan-hook tail.

# p3_char_0374_疙 — 疙 (gē), 疒 (5 strokes) + 乞 (3 strokes) = 8 strokes.
# Layout: 疒 on left (compact), 乞 tucked into 疒's belly on the right.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _tapered_line(draw, p0, p1, w_head, w_tail, n=28):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def _tapered_bezier(draw, p0, p1, ctrl, w_head, w_tail, n=80):
    prev = None
    for i in range(n + 1):
        u = i / n
        omu = 1 - u
        x = omu * omu * p0[0] + 2 * omu * u * ctrl[0] + u * u * p1[0]
        y = omu * omu * p0[1] + 2 * omu * u * ctrl[1] + u * u * p1[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_ne_left(draw):
    """Compressed 疒 on the LEFT half of the canvas (x roughly 30..150)."""
    # Stroke 1: top 点 — small tapered slash above heng, upper-right of 疒
    _tapered_line(draw, (118, 55), (132, 78), w_head=3.0, w_tail=6.0, n=18)

    # Stroke 2: heng — thin horizontal roof, spans left-of-center
    _tapered_line(draw, (80, 105), (150, 102), w_head=4.5, w_tail=4.5, n=30)

    # Stroke 3: 撇 — long left-falling sweep from heng's left end
    _tapered_bezier(
        draw,
        p0=(80, 105),
        p1=(35, 275),
        ctrl=(50, 200),
        w_head=6.0,
        w_tail=4.0,
        n=90,
    )

    # Stroke 4: 冫 upper 点 (short slash) — inside belly, upper
    _tapered_line(draw, (35, 135), (55, 155), w_head=3.0, w_tail=5.5, n=18)

    # Stroke 5: 冫 lower 提 (rising flick) — inside belly, lower
    _tapered_line(draw, (18, 210), (55, 195), w_head=7.0, w_tail=2.5, n=20)


def draw_qi_right(draw):
    """乞 (qi) on the RIGHT half, tucked into 疒's belly.
    3 strokes: 撇 (top short slash), 横 (thin), 横折弯钩 (wan hook)."""

    # Stroke 1: top 撇 — short slanting stroke, top-right area
    _tapered_line(draw, (200, 90), (170, 120), w_head=6.0, w_tail=2.5, n=20)

    # Stroke 2: 横 — a thin horizontal, right side
    _tapered_line(draw, (140, 145), (250, 140), w_head=4.5, w_tail=5.0, n=30)

    # Stroke 3: 横折弯钩 — starts with a short 横, bends down, then curves
    # right at the bottom into a hook. Draw as three connected segments.
    # segment A: short heng along top of the hook
    _tapered_line(draw, (170, 170), (235, 168), w_head=4.5, w_tail=4.5, n=25)
    # segment B: down-then-right curve (bezier)
    _tapered_bezier(
        draw,
        p0=(235, 168),
        p1=(255, 265),
        ctrl=(180, 240),   # bows down and to the left, then right
        w_head=5.0,
        w_tail=5.0,
        n=80,
    )
    # segment C: the hook tail — small upward flick at the right end
    _tapered_line(draw, (255, 265), (263, 245), w_head=5.0, w_tail=2.5, n=15)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ne_left(draw)
    draw_qi_right(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_疙.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

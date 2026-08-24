"""p3_char_0233_那 — G3 coord-bank drawer attempt.

那 (nà) — 7 strokes, L-R composition:
  Left component (冄-like, ~55% width):
    S1 heng (top)
    S2 heng-zhe (short vertical down on the right side of left component)
    S3 heng (middle)
    S4 heng (bottom, shorter)
    S5 long 撇 sweeping down-left through the middle-bottom
  Right component 阝 (~45% width):
    S6 横撇弯钩 (ear-curl loop)
    S7 竖 (long descender)

Right-ear recipe transferred (with shift) from bank attempt
p2_radical_020_阝/generated.py — pattern kept: two cubic beziers +
tapered vertical shu. Loop shifted +130 in math-x and tightened
horizontally to make room for the left component.

L-R scale posture (drawer_memory.md): left component gets ~55% width,
right ear ~45%, per typical L-R char scaling.
"""

from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _tapered_line(draw, p0, p1, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _cubic_taper(draw, p0, p1, c1, c2, w0, w1, steps=140):
    for i in range(steps + 1):
        u = i / steps
        omu = 1 - u
        bx = (omu ** 3 * p0[0] + 3 * omu ** 2 * u * c1[0]
              + 3 * omu * u ** 2 * c2[0] + u ** 3 * p1[0])
        by = (omu ** 3 * p0[1] + 3 * omu ** 2 * u * c1[1]
              + 3 * omu * u ** 2 * c2[1] + u ** 3 * p1[1])
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_left_component(draw):
    """Left component of 那 — 冄-like: top-heng + short down + two hengs + long pie.

    Math coords (center-origin, +y up). Left panel roughly x∈[-110,-10].
    """
    # S1 top heng: from upper-left to upper-right of left panel
    p0 = _to_pixel(-110, 90)
    p1 = _to_pixel(-25, 90)
    _tapered_line(draw, p0, p1, 6.0, 6.0)

    # S2 short vertical drop (heng-zhe corner completion) on right side of left panel
    # From end of S1 down to bottom of left panel
    p0 = _to_pixel(-25, 90)
    p1 = _to_pixel(-25, -60)
    _tapered_line(draw, p0, p1, 6.0, 6.0)

    # S3 middle heng
    p0 = _to_pixel(-100, 30)
    p1 = _to_pixel(-25, 30)
    _tapered_line(draw, p0, p1, 6.0, 6.0)

    # S4 bottom heng (closing bar for the boxy top part)
    p0 = _to_pixel(-95, -30)
    p1 = _to_pixel(-25, -30)
    _tapered_line(draw, p0, p1, 6.0, 6.0)

    # S5 long 撇 — sweep from top of left panel down-left to lower-left
    # Start above top heng, sweep through middle, tail well below bottom
    p0 = _to_pixel(-70, 120)          # head near top-center of left panel
    p1 = _to_pixel(-135, -130)        # tail lower-left
    c1 = _to_pixel(-75, 50)
    c2 = _to_pixel(-115, -60)
    _cubic_taper(draw, p0, p1, c1, c2, 9.0, 3.0, steps=140)


def draw_right_ear(draw):
    """阝 (right-ear) — transferred from bank attempt p2_radical_020_阝.

    Original centered at math x ≈ -50; shift by +130 → centered near math x=+80.
    """
    # Segment A: top hump — upper-left start, sweep right and down to waist
    p0 = _to_pixel(45, 120)
    p1 = _to_pixel(80, 60)
    c1 = _to_pixel(135, 150)
    c2 = _to_pixel(150, 80)
    _cubic_taper(draw, p0, p1, c1, c2, 7.0, 8.0, steps=120)

    # Segment B: bottom hump + hook
    p0 = _to_pixel(80, 60)
    p1 = _to_pixel(60, 0)
    c1 = _to_pixel(150, 25)
    c2 = _to_pixel(135, -15)
    _cubic_taper(draw, p0, p1, c1, c2, 8.0, 4.0, steps=120)

    # S7 shu — long vertical descender for the ear (long, reaches near bottom)
    top = _to_pixel(55, 0)
    bot = _to_pixel(55, -140)
    _tapered_line(draw, top, bot, 9.0, 9.0, steps=120)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    draw_left_component(draw)
    draw_right_ear(draw)

    out_path = ("<REPO_ROOT>/experiments/"
                "exp_context_effect/groups/G3_coords/attempts/"
                "p3_char_0233_那/01_那.png")
    img.save(out_path)
    print(f"saved {out_path}")


if __name__ == "__main__":
    main()

# p3_char_0085_马 — G3 attempt
# 马 has 3 strokes:
#   1. 横折 (top: short horizontal then down) forming the upper-right box
#   2. 竖折折钩 (left vertical down, then right, then down with a hook)
#   3. 横 (bottom long horizontal crossing through)
# Thin uniform lines to match MMH GT (per P12: thin, not calligraphic).

from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def line(t, p1, p2, w):
    t.line([_to_pixel(*p1), _to_pixel(*p2)], fill=(0, 0, 0), width=w)


def draw_ma(t, ox=0, oy=0, scale=1.0):
    w = max(1, int(4 * scale))  # thin lines to match GT

    # Stroke 1: 横折 — small box on upper-left. Horizontal top, then down.
    #   From upper-left of box to upper-right, then down to mid-height.
    s1_a = (ox + -55 * scale, oy + 75 * scale)
    s1_b = (ox + 25 * scale, oy + 75 * scale)
    s1_c = (ox + 25 * scale, oy + 15 * scale)
    line(t, s1_a, s1_b, w)
    line(t, s1_b, s1_c, w)

    # Stroke 2: 竖折折钩 — starts at upper-left (aligned with s1_a),
    # goes down, then right (forming the middle horizontal ~mid),
    # then down (right side of horse), then hooks up-left at bottom.
    s2_a = (ox + -55 * scale, oy + 75 * scale)   # top-left (aligned w/ s1_a)
    s2_b = (ox + -55 * scale, oy + 15 * scale)   # down to mid
    s2_c = (ox + 55 * scale, oy + 15 * scale)    # right across middle
    s2_d = (ox + 55 * scale, oy + -70 * scale)   # down to bottom-right
    s2_e = (ox + 10 * scale, oy + -60 * scale)   # hook up-left
    line(t, s2_a, s2_b, w)
    line(t, s2_b, s2_c, w)
    line(t, s2_c, s2_d, w)
    line(t, s2_d, s2_e, w)

    # Stroke 3: 横 — long horizontal across the bottom, crossing through
    # the right vertical of stroke 2.
    s3_a = (ox + -95 * scale, oy + -65 * scale)
    s3_b = (ox + 80 * scale, oy + -65 * scale)
    line(t, s3_a, s3_b, w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ma(t, ox=0, oy=0, scale=1.0)
    out_path = __file__.rsplit("/", 1)[0] + "/01_马.png"
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

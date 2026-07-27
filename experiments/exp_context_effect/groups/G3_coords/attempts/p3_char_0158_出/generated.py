# p3_char_0158_出 — 出 (chū, "to go out"), 5 strokes.
# Structure: two stacked 屮-like forms sharing central vertical shaft.
# Stroke order (per MMH/standard):
#   1) short central 竖 (upper shaft segment, top part of 屮-top)
#   2) 竖折 of top part (left descending stroke turning right into crossbar)
#   3) short right 竖 (upper right arm)
#   4) 竖折 of bottom part (bigger, left descending + bottom crossbar)
#   5) short right 竖 (bottom right arm, longer than top)
#
# Uniform thin ~5px lines per P12 (MMH GT convention).
# Inline PIL rendering — this is closer to chu_radical_char.py recipe
# extended by adding a lower ⼑-like bowl below.

from PIL import Image, ImageDraw


def draw_chu_char(t, ox=0, oy=0, scale=1.0):
    ink = (0, 0, 0)
    lw = max(1, int(round(5 * scale)))

    def P(mx, my):
        return (150 + ox + mx * scale, 150 - oy - my * scale)

    # 1) Central vertical shaft — from very top down through both bowls.
    t.line([P(0, 105), P(0, -105)], fill=ink, width=lw)

    # 2) Top 竖折: left arm dropping into small crossbar.
    t.line([P(-32, 55), P(-32, 5)], fill=ink, width=lw)
    t.line([P(-32, 5), P(0, 5)], fill=ink, width=lw)

    # 3) Top right vertical arm (extends above crossbar & slightly below).
    t.line([P(32, 65), P(32, 5)], fill=ink, width=lw)

    # 4) Bottom 竖折: bigger — left vertical descending, then long crossbar.
    t.line([P(-75, 30), P(-75, -100)], fill=ink, width=lw)
    t.line([P(-75, -100), P(75, -100)], fill=ink, width=lw)

    # 5) Bottom right vertical arm (taller than top-right).
    t.line([P(75, 40), P(75, -100)], fill=ink, width=lw)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_chu_char(d)
    img.save("01_出.png")


if __name__ == "__main__":
    main()

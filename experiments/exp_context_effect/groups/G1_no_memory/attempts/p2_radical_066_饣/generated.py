"""G1 render of radical 饣 (3画)."""
import os
from PIL import Image, ImageDraw

SIZE = 300
OUT = os.path.join(os.path.dirname(__file__), "01_饣.png")


def smooth_curve(draw, pts, width=4):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        draw.ellipse([p[0] - width / 2, p[1] - width / 2,
                      p[0] + width / 2, p[1] + width / 2], fill="black")


def main():
    img = Image.new("RGB", (SIZE, SIZE), "white")
    draw = ImageDraw.Draw(img)

    W = 4

    # Stroke 1: 撇 — top diagonal, from ~(165, 78) sweeping down-left to (125, 135)
    stroke1 = [
        (168, 80),
        (160, 92),
        (150, 105),
        (140, 118),
        (130, 132),
        (124, 142),
    ]
    smooth_curve(draw, stroke1, width=W)

    # Stroke 2: 横钩 — starts where pie ends, short horizontal right to (185, 128),
    # then hooks down-left ending near (168, 148).
    stroke2 = [
        (138, 128),
        (152, 126),
        (170, 126),
        (185, 128),
        (182, 135),
        (176, 143),
        (168, 150),
    ]
    smooth_curve(draw, stroke2, width=W)

    # Stroke 3: 竖弯钩 / bowl — starts from just below the 横钩 endpoint area,
    # descends as a bowl-like curve, then hooks up-right at the bottom.
    stroke3 = [
        (152, 150),
        (150, 168),
        (152, 188),
        (158, 208),
        (168, 224),
        (182, 234),
        (196, 236),
        (208, 232),
        (216, 224),
    ]
    smooth_curve(draw, stroke3, width=W)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

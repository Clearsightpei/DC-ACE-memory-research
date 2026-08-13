"""p3_char_0283_传 — 传 (chuán). 6 strokes.
Left: 亻 (撇 + 竖). Right: 专 (横, 横折, 竖折撇 = one continuous stroke, 点).
Revision 1: merged the mid-vertical INTO the 竖折撇 (it's a single stroke,
not two); moved 亻 rightward and made 竖 attach to 撇 midpoint; positioned
the dot as short 点 in upper-right.
"""
from PIL import Image, ImageDraw
import os


def draw_chuan(img_size=300):
    W = H = img_size
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    ink = "black"
    w = 4

    # === LEFT: 亻 (person radical) ===
    # 撇 — from head near (95, 60) slanting down-left to tail (72, 165)
    pie_pts = []
    for i in range(41):
        t = i / 40
        x = 95 + (72 - 95) * t
        y = 60 + (165 - 60) * t
        bow = 5 * (t * (1 - t) * 4)
        x -= bow * 0.5
        pie_pts.append((x, y))
    for i in range(len(pie_pts) - 1):
        d.line([pie_pts[i], pie_pts[i + 1]], fill=ink, width=w)

    # 竖 — vertical from midpoint of 撇 going down to bottom
    d.line([(85, 118), (85, 260)], fill=ink, width=w)

    # === RIGHT: 专 ===
    # 1) 一 (top short horizontal), slight rightward tilt up
    d.line([(150, 82), (240, 72)], fill=ink, width=w)

    # 2) 横折 — longer horizontal then short down-turn on the right
    d.line([(135, 128), (258, 118)], fill=ink, width=w)
    d.line([(258, 118), (253, 148)], fill=ink, width=w)

    # 3) 竖折撇 — single continuous stroke:
    #    start near top center (~185, 55), go DOWN as vertical crossing
    #    both horizontals, reach ~(180, 195), then curl left-down as
    #    a long 撇 to (110, 275)
    curl = []
    # vertical portion
    for i in range(41):
        t = i / 40
        x = 190 + (180 - 190) * t
        y = 55 + (195 - 55) * t
        curl.append((x, y))
    # curl portion — long 撇 to lower-left
    for i in range(1, 51):
        t = i / 50
        x = 180 + (110 - 180) * t
        y = 195 + (275 - 195) * t
        # slight downward bow
        bow = 6 * (t * (1 - t) * 4)
        y += bow * 0.3
        x -= bow * 0.2
        curl.append((x, y))
    for i in range(len(curl) - 1):
        d.line([curl[i], curl[i + 1]], fill=ink, width=w)

    # 4) 点 (dot) upper-right of 专, short stroke slanting down-right
    dot_pts = [(240, 55), (255, 72), (250, 78), (236, 65)]
    d.polygon(dot_pts, fill=ink)

    return img


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    img = draw_chuan(300)
    img.save(os.path.join(out_dir, "01_传.png"))
    print("wrote", os.path.join(out_dir, "01_传.png"))

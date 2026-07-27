# 仟 (qian) = 亻 (left, tall) + 千 (right).
# G3 v8: inline PIL, treating bank as reference only. GT shows thin/moderate
# strokes with a slight brush feel. Composition matches the 亻+X left-radical
# recipe (see 付 in bank #182).

from PIL import Image, ImageDraw
import os

W = H = 300


def line(draw, p0, p1, width=6):
    draw.line([p0, p1], fill="black", width=width)


def curve(draw, pts, width=6):
    # simple polyline
    for i in range(len(pts) - 1):
        line(draw, pts[i], pts[i + 1], width=width)


def draw_ren_pang(draw):
    # 撇 (top pie of 亻): sweep from upper-mid down-left, with slight curve.
    pts = [(95, 70), (82, 105), (68, 145), (52, 200)]
    curve(draw, pts, width=6)
    # 丨/竖 of 亻: vertical starts on the pie mid-shaft, descends straight.
    line(draw, (80, 128), (95, 260), width=6)


def draw_qian(draw):
    # 撇 (short top pie of 千): from upper right down-left across vertical top.
    pts = [(230, 65), (210, 85), (185, 100), (155, 110)]
    curve(draw, pts, width=6)
    # 横 (heng): long horizontal.
    line(draw, (140, 130), (272, 124), width=6)
    # 丨 (vertical of 千): starts just under the pie, through heng, straight down.
    line(draw, (198, 95), (198, 278), width=6)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_ren_pang(draw)
    draw_qian(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_仟.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()

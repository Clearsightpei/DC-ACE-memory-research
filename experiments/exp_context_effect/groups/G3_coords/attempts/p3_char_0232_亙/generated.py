"""亙 (gèn) — top 一, middle rounded/curved body, bottom 一.
G3 v8: inline fresh, matching GT visually. Callable Python unit preserved.
"""
from PIL import Image, ImageDraw
import os

W = H = 300


def draw_heng(d, x0, y0, x1, y1, w=6):
    d.line([(x0, y0), (x1, y1)], fill=0, width=w)


def draw_middle_body(d):
    # A rounded/pill shape approximating the middle of 亙 as seen in GT
    # Left curve down, bottom, right curve up, small inner strokes
    # outer left arc/stroke: 撇-like going down-left
    d.line([(115, 105), (95, 200)], fill=0, width=6)
    # bottom horizontal of the middle body
    d.line([(95, 200), (200, 200)], fill=0, width=6)
    # right side: vertical-ish going up from bottom-right to top-right
    d.line([(200, 200), (200, 105)], fill=0, width=6)
    # top short cap of middle body (small horizontal joining left-top to right-top)
    d.line([(115, 105), (200, 105)], fill=0, width=6)
    # inner detail: two short diagonals like 口/日 inside marker
    d.line([(130, 145), (170, 145)], fill=0, width=5)
    d.line([(150, 160), (185, 195)], fill=0, width=5)


def draw_gen(img_path):
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    # top 一
    draw_heng(d, 55, 70, 240, 68, w=6)
    # middle body
    draw_middle_body(d)
    # bottom 一 (wider, sitting near baseline)
    draw_heng(d, 40, 255, 260, 253, w=6)
    img.save(img_path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_亙.png")
    draw_gen(out)
    print("wrote", out)

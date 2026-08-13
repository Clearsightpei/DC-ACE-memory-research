# p3_char_0266_伥 — 伥 = 亻 (left) + 长 (right)
# G3 drawer. Uses inline PIL rendering with function-callable form.
# Bank has ren_pang but no 长; render both fresh at appropriate L-R scale
# per drawer_memory L-R table (亻 narrow left third, 长 wider right two-thirds).

from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = 0
BG = 255


def draw_line(d, p1, p2, width):
    d.line([p1, p2], fill=INK, width=width)


def draw_curve(d, points, width):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=INK, width=width)


def draw_ren_pang(d):
    """Left 亻 radical: pie + short shu."""
    # pie: sweep down-left from ~(85, 70) to (40, 210)
    pie_pts = [(85, 70), (78, 105), (68, 140), (56, 175), (40, 215)]
    draw_curve(d, pie_pts, 5)
    # shu: short vertical starting from mid-shaft of pie down to ~245
    draw_line(d, (76, 115), (76, 250), 5)


def draw_chang(d):
    """Right 长 (cháng): small top pie + top heng + long stem + cross heng + big na."""
    # small pie top-left
    draw_curve(d, [(155, 75), (145, 95), (135, 115)], 5)
    # top heng from top of stem going right
    draw_line(d, (150, 100), (225, 95), 5)
    # main vertical stem (long)
    draw_line(d, (152, 100), (150, 215), 5)
    # crossing middle heng
    draw_line(d, (135, 150), (215, 148), 5)
    # left-bottom pie going down-left from stem end
    draw_curve(d, [(150, 210), (125, 235), (95, 265)], 5)
    # long na sweep (bottom-right, extends far)
    na_pts = [(150, 210), (175, 225), (205, 245), (240, 265), (275, 275)]
    draw_curve(d, na_pts, 6)


def draw_xiang(path):
    img = Image.new("L", (W, H), BG)
    d = ImageDraw.Draw(img)
    draw_ren_pang(d)
    draw_chang(d)
    img.save(path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伥.png")
    draw_xiang(out)
    print(f"wrote {out}")

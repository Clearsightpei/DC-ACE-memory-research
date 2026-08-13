# BANK_DEVIATION
# skipped: ren_pang.py (turtle-based; scale-composition would clash with PIL inline right side)
# reason: right side of 侯 has 9 strokes and needs precise inline PIL control; mixing turtle+PIL awkward
# fresh_component: hou_ren_left (thin PIL 亻 sized to leave room for dense right)
#
# 侯 (hou) = 亻 (left, tall thin) + 侯-right (top heng cap + small hanging pie + short heng + 矢-like base)
# GT shows: thin brush weight (~5-6px), tall aspect. Follows qian_thousand's inline pattern.

from PIL import Image, ImageDraw
import os

W = H = 300


def line(draw, p0, p1, width=6):
    draw.line([p0, p1], fill="black", width=width)


def curve(draw, pts, width=6):
    for i in range(len(pts) - 1):
        line(draw, pts[i], pts[i + 1], width=width)


def draw_ren_left(draw):
    # 撇 of 亻: broader sweep from upper-mid down-left
    pts = [(85, 70), (75, 110), (62, 155), (48, 210)]
    curve(draw, pts, width=6)
    # 丨 of 亻: vertical starts on the pie mid-shaft, descends
    line(draw, (74, 130), (88, 285), width=6)


def draw_hou_right(draw):
    # Top heng (cap over right structure) - wide
    line(draw, (135, 65), (270, 67), width=6)
    # Small hanging pie under left end of top heng (short 亅-like drop)
    pts = [(155, 70), (148, 90), (140, 112)]
    curve(draw, pts, width=6)
    # Short interior heng (亠-below crossbar)
    line(draw, (160, 128), (258, 126), width=6)
    # === 矢-like base (大 with a small pie above) ===
    # Small pie above the main crossbar (arrow-body top)
    pts = [(205, 150), (188, 172), (172, 190)]
    curve(draw, pts, width=5)
    # Main heng (crossbar of 大)
    line(draw, (140, 200), (275, 198), width=6)
    # Long pie sweeping down-left, crossing the heng from above-center
    pts = [(220, 165), (205, 200), (180, 240), (145, 292)]
    curve(draw, pts, width=6)
    # Long na sweeping down-right, starting from crossbar intersection
    pts = [(215, 200), (238, 235), (262, 265), (288, 292)]
    curve(draw, pts, width=7)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_ren_left(draw)
    draw_hou_right(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_侯.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()

# BANK_DEVIATION
# skipped: ren_pang.py
# reason: ren_pang bank primitive uses turtle-style bezier calls; inlining PIL
#   for 亻 gives consistent stroke style with the fresh-inlined 求 body on right.
# fresh_component: ren_pang_inline_for_qiu_LR

# 俅 (qiú) = 亻 (left) + 求 (right). 7-stroke right component with no bank entry.
# G3 v13: inline PIL, using the 亻+X L-R recipe (see qian_thousand.py template).
# L compressed 亻 at ~x=45-95, R 求 at ~x=110-280.

from PIL import Image, ImageDraw
import os

W = H = 300


def line(draw, p0, p1, width=6):
    draw.line([p0, p1], fill="black", width=width)


def curve(draw, pts, width=6):
    for i in range(len(pts) - 1):
        line(draw, pts[i], pts[i + 1], width=width)


def draw_ren_pang_inline(draw):
    # 撇 (top pie of 亻): sweep from upper-mid down-left, slight curve.
    # Tightened so tail stays in frame.
    pts = [(85, 80), (75, 120), (65, 160), (55, 215)]
    curve(draw, pts, width=6)
    # 丨/竖 of 亻: vertical starts on the pie mid-shaft, descends straight.
    line(draw, (78, 138), (92, 275), width=6)


def draw_qiu_inline(draw):
    # Stroke 1: 横 top horizontal.
    line(draw, (130, 115), (265, 110), width=6)
    # Stroke 2: 竖钩 central vertical with small hook at bottom.
    line(draw, (198, 85), (198, 240), width=6)
    curve(draw, [(198, 240), (190, 250), (178, 253)], width=6)
    # Stroke 3: 点 top-left dot on top of heng (small tick).
    curve(draw, [(152, 88), (158, 98), (164, 108)], width=5)
    # Stroke 4: 提 short rising stroke on left of shaft (below heng).
    curve(draw, [(142, 165), (158, 158), (175, 152)], width=5)
    # Stroke 5: 撇 pie — sweeps from mid-shaft down-left to bottom-left.
    pts = [(193, 148), (175, 185), (150, 220), (125, 265)]
    curve(draw, pts, width=6)
    # Stroke 6: 捺 na — sweeps from near mid-shaft down-right, thickening.
    pts_na = [(203, 158), (220, 195), (240, 230), (265, 268)]
    curve(draw, pts_na, width=6)
    # Stroke 7: 点 bottom-right dot (small tick, off shaft).
    curve(draw, [(232, 158), (245, 172), (253, 185)], width=5)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_ren_pang_inline(draw)
    draw_qiu_inline(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_俅.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()

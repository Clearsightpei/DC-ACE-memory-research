# BANK_DEVIATION
# skipped: (no bank entry for 欠 or 次 exists)
# reason: right side 次 (冫+欠) has no bank primitive; ren_pang alone
#   covers only the left 亻. Inline the entire right composition fresh.
# fresh_component: ci_right_for_佽 (冫 top-left dots + 欠 pie/heng-hook/pie/na)

# 佽 (cì) = 亻 (left) + 次 (right, 冫 upper-left + 欠 body).
# GT shows thin uniform strokes (MMH style). Follow the qian_thousand
# pattern: inline PIL, ~5-6px uniform width, no calligraphic taper.

from PIL import Image, ImageDraw
import os

W = H = 300


def line(draw, p0, p1, width=5):
    draw.line([p0, p1], fill="black", width=width)


def curve(draw, pts, width=5):
    for i in range(len(pts) - 1):
        line(draw, pts[i], pts[i + 1], width=width)


def draw_ren_pang(draw):
    # 撇 of 亻: shorter, less steep sweep from upper-mid down-left.
    pts = [(85, 80), (72, 115), (58, 155), (45, 205)]
    curve(draw, pts, width=5)
    # 丨 of 亻: vertical starts on the pie mid-shaft, ends around lower-mid.
    line(draw, (75, 138), (85, 265), width=5)


def draw_ci_right(draw):
    # --- 冫 (upper-left of right region) — 2 short strokes stacked ---
    # upper 点: short slanted stroke (top-left dot).
    pts_dot1 = [(140, 78), (152, 100)]
    curve(draw, pts_dot1, width=5)
    # lower 提: short slant going up-right (raise stroke).
    pts_dot2 = [(140, 132), (162, 122)]
    curve(draw, pts_dot2, width=5)

    # --- 欠 (right/lower body) ---
    # top short 撇 at upper-right.
    pts_top_pie = [(220, 60), (205, 78), (188, 92)]
    curve(draw, pts_top_pie, width=5)
    # 横钩 (short heng ending with tiny hook down-left).
    pts_heng_gou = [(185, 108), (245, 105), (238, 122)]
    curve(draw, pts_heng_gou, width=5)
    # main 撇: long left-falling sweep from below the heng-hook down to lower-left.
    pts_pie = [(210, 140), (185, 175), (155, 215), (118, 268)]
    curve(draw, pts_pie, width=5)
    # main 捺: right-falling sweep from near pie head down to lower-right.
    pts_na = [(215, 155), (238, 195), (260, 232), (285, 272)]
    curve(draw, pts_na, width=5)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_ren_pang(draw)
    draw_ci_right(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佽.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()

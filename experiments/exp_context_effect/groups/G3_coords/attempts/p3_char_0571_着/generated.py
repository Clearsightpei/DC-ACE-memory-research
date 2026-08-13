# BANK_DEVIATION
# skipped: mu.py, zhao_top.py
# reason: 着 is 羊-top (丷 + 3 hengs + long 撇) over 目 at bottom-right;
#   neither mu.py (木 tree) nor zhao_top.py (爫) matches this composition.
# fresh_component: zhao_ye_top_yang (羊-top with long descender + inline 目_eye)
#
# 着 (zhāo/zháo) — 11 strokes. Top: 丷 (2 dots) + 3 stacked 横 + long 撇
# descending to lower-left. Bottom-right: 目 (eye, 5 strokes) as in 相.

import os
from PIL import Image, ImageDraw

CANVAS = 300


def draw_dian(t, x0, y0, x1, y1, w=8):
    """Simple dian: line from (x0,y0) to (x1,y1) with width w."""
    t.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=w)


def draw_heng(t, x0, x1, y, w=6):
    t.line([(x0, y), (x1, y)], fill=(0, 0, 0), width=w)


def draw_pie(t, x0, y0, x1, y1, w=7):
    """Straight-ish 撇, approximated as one line for MMH-thin style."""
    t.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=w)


def draw_mu_eye(t, x_left, x_right, y_top, y_bot, w=6):
    """目 rectangle with 2 inner hengs. Bottom-right small eye."""
    w_inner = max(1, w - 1)
    # left 竖
    t.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # 横折 (top + right)
    t.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    t.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # two inner hengs
    h = (y_bot - y_top) / 3.0
    y_mid_up = y_top + h
    y_mid_lo = y_top + 2 * h
    t.line([(x_left + 1, y_mid_up), (x_right - 2, y_mid_up)],
           fill=(0, 0, 0), width=w_inner)
    t.line([(x_left + 1, y_mid_lo), (x_right - 2, y_mid_lo)],
           fill=(0, 0, 0), width=w_inner)
    # bottom heng
    t.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # --- 羊-top block (occupies upper portion, center) ---

    # Two dots (丷) at top: left dot slopes down-right, right dot down-left.
    # 1. left 点
    draw_dian(t, 118, 25, 135, 55, w=8)
    # 2. right 撇 (short)
    draw_dian(t, 198, 25, 182, 55, w=8)

    # 3. upper 横 (top bar of 羊-body)
    draw_heng(t, 108, 215, 78, w=6)
    # 4. middle 横 (slightly wider, close under upper)
    draw_heng(t, 105, 225, 108, w=6)
    # 5. lower 横 (base bar of 羊 — the widest, extends past pie on right)
    draw_heng(t, 55, 265, 145, w=7)

    # 6. long 撇 — from top of 羊 body, slicing down-left to lower-left.
    # Starts near right side of the upper heng band, descends to bottom-left.
    draw_pie(t, 192, 60, 45, 285, w=7)

    # --- 目 (eye) at lower-right ---
    # Rectangle roughly x 180..248, y 160..278 — slightly narrower, taller
    draw_mu_eye(t, x_left=180, x_right=248,
                y_top=163, y_bot=278, w=6)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_着.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

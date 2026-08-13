# BANK_DEVIATION
# skipped: jia_first.py (full-canvas 甲) — needs LR-left compression for 鸭
# reason: 甲 must occupy left ~40% for L-R layout; jia_first fills full canvas
# fresh_component: jia_compressed_for_LR_left (甲 inline compressed to left band)
#
# Also: no bank entry for 鸟 (bird); inline fresh — niao_bird_for_LR_right
# 鸭 = 甲 (left) + 鸟 (right), L-R layout.

import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_鸭.png")


def draw_jia_compressed(canvas):
    """甲 compressed for LR-left slot. Box in upper region, long shu extends down."""
    x_left, x_right = 35, 115
    y_top, y_bot = 65, 160
    y_mid = 115
    x_center = (x_left + x_right) // 2
    y_extend = 250
    w = 6
    # left shu
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # top heng
    canvas.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    # right shu
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # middle heng
    canvas.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=w)
    # bottom heng
    canvas.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)
    # long central shu (extends below box)
    canvas.line([(x_center, y_top + 6), (x_center, y_extend)], fill=(0, 0, 0), width=w + 1)


def draw_niao_bird(canvas):
    """鸟 for LR-right slot. Head box (top-right) + slanted 撇 + eye dot +
    zigzag body + long bottom heng."""
    w = 6
    # Stroke 1: 撇 (short slant top of head), from ~(180, 55) down-left
    canvas.line([(190, 55), (160, 90)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折钩 — top heng of head, then right shu with small hook
    # top heng
    canvas.line([(160, 90), (240, 90)], fill=(0, 0, 0), width=w)
    # right shu
    canvas.line([(240, 90), (240, 135)], fill=(0, 0, 0), width=w)
    # small hook (left-pointing)
    canvas.line([(240, 135), (228, 128)], fill=(0, 0, 0), width=w)
    # Stroke 3: bottom of head (short heng closing head under)
    canvas.line([(175, 135), (240, 135)], fill=(0, 0, 0), width=w)
    # Stroke 4: eye dot inside head
    canvas.ellipse([(205, 108), (218, 121)], fill=(0, 0, 0))
    # Stroke 5: 竖折折钩 body — shu going down from head-left,
    # then heng right, then shu down with hook
    # descending shu from head bottom-left
    canvas.line([(175, 135), (175, 180)], fill=(0, 0, 0), width=w)
    # heng across
    canvas.line([(175, 180), (245, 180)], fill=(0, 0, 0), width=w)
    # small right shu with hook back left
    canvas.line([(245, 180), (245, 210)], fill=(0, 0, 0), width=w)
    canvas.line([(245, 210), (230, 205)], fill=(0, 0, 0), width=w)
    # Stroke 6: long 横 across bottom
    canvas.line([(140, 245), (285, 245)], fill=(0, 0, 0), width=w + 1)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_jia_compressed(d)
    draw_niao_bird(d)
    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()

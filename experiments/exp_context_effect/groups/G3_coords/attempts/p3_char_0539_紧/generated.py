# BANK_DEVIATION
# skipped: you.py (bank 又 primitive)
# reason: 紧's top-right 又 must sit in the upper-right corner as a compact
#   partner to 臣; bank 又 is scaled for standalone. Inlining gives tighter
#   control over the joint area between 臣 and 又.
# fresh_component: you_compact_top_right_for_jin
#
# 紧 (jin) — top: 臣 (left, simplified) + 又 (right); bottom: 糸.
# Rendered fresh with PIL. GT is thin-line MMH; use uniform ~3-4 px widths.

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
WM = 4   # main
WT = 3   # thin


def line(p0, p1, w=WM):
    d.line([p0, p1], fill=INK, width=w)


def polyline(pts, w=WM):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)


# =========================================================================
# TOP HALF (y 40..145): 臣 (left) + 又 (right)
# =========================================================================

# --- 臣 (simplified as a small 巨-like shape) ---
# Top horizontal
line((60, 55), (135, 55), w=WT)
# Left vertical (long)
line((60, 55), (60, 148), w=WM)
# Right vertical (short)
line((135, 55), (135, 100), w=WT)
# Inner middle heng
line((85, 92), (135, 92), w=WT)
# Small inner heng
line((85, 118), (115, 118), w=WT)
# Bottom horizontal closing
line((60, 148), (135, 148), w=WT)

# --- 又 (top-right): 横撇 + 捺 ---
# 横撇 — short heng then long pie down-left
polyline([(158, 55), (218, 58), (168, 148)], w=WM)
# 捺 — from mid-shaft of 撇 heading down-right
polyline([(180, 82), (250, 150)], w=WM)


# =========================================================================
# BOTTOM HALF (y 155..280): 糸 (silk)
# =========================================================================
# 糸 layout:
#   top: small 幺 (two little loops) at center-top of bottom half
#   middle: broad 一 horizontal
#   bottom: 小 (three descending strokes)

# --- 幺: two 撇折 stacked ---
# First 撇折 (top)
polyline([(155, 160), (140, 178), (162, 186)], w=WT)
# Second 撇折 (below)
polyline([(162, 188), (145, 208), (170, 218)], w=WT)

# --- Broad 一 horizontal (main crossbar of 糸) ---
line((75, 232), (240, 232), w=WM)

# --- 小 bottom: 竖 + 撇 + 点 ---
# Center vertical (main descender)
line((158, 234), (158, 285), w=WM)
# Left 撇 (curving down-left)
polyline([(120, 240), (100, 280)], w=WT)
# Right 点/捺 (down-right)
polyline([(200, 240), (225, 280)], w=WT)


out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_紧.png")
img.save(out_path)
print(f"Saved {out_path}")

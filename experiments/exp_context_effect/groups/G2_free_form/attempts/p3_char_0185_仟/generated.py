"""
仟 = 亻 (left) + 千 (right)

# SIGNATURE CHECK (from sibling_signature_checklist.md, pasted verbatim
#   because 千 appears as a component of 仟):
#   千 | 撇-LID top + straight through-竖 (no hook) | 干, 于
#
# Compound-character sibling protocol (memory_index D):
#   The 千 sub-glyph must show:
#     - a 撇 lid on top (short flick)
#     - a horizontal 一
#     - a straight through-竖, NO HOOK at the bottom
#
# Layout for 仟 (left-right compound, 亻 narrow on left ~30%, 千 wider ~70%):
#   Left 亻: 撇 (short flick top) + long 竖 down through midline
#   Right 千: 撇-lid at top-center, 一 crossing under it, 丨 straight down
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

def brush_line(p0, p1, w0, w1, steps=40):
    """taper-capable line via stacked disks"""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w0 + (w1 - w0) * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---------- LEFT: 亻 (person radical) ----------
# 撇 from top-right of the radical zone flicking down-left
brush_line((85, 70), (55, 165), 8, 5)
# 竖 (straight vertical) starting where 撇 meets the body
brush_line((78, 110), (78, 245), 7, 7)

# ---------- RIGHT: 千 ----------
# 撇 lid at top (short flick from upper-right down to upper-left)
brush_line((215, 70), (170, 105), 8, 5)
# 一 horizontal crossbar (long, spans most of right side)
brush_line((140, 135), (255, 130), 6, 6)
# 丨 through-竖 STRAIGHT (NO HOOK) — from top of 千 body down
brush_line((198, 100), (198, 265), 7, 7)

img.save("01_仟.png")

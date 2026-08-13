"""p3_char_0298_丽 — G3 attempt.

Decomposition of 丽 (per GT):
  1. Long top horizontal stroke (一).
  2. Left box: 冂 with an inner short vertical dot ~ (like a small 月-like box).
  3. Right box: mirror of left box.

Both boxes sit under the horizontal. Each box has:
  - a left vertical stroke that hooks slightly at the bottom-left (or is a
    plain vertical — GT shows plain-ish),
  - a top-right corner that turns down (横折),
  - a small inner short vertical stroke inside the box.

Widths per P4/P12 (MMH GT thin lines): use ~4-5 px ink; calligraphic
end-thickening slight.

Format: inline PIL rendering. Callable function form retained (G3
constraint). No reliance on frozen bank primitives (v8 UNLOCKED — GT
governs).
"""
from PIL import Image, ImageDraw


def draw_li(img_path):
    W = H = 300
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)

    ink = "black"
    lw = 5  # main stroke width

    # 1) Top horizontal 一, slight sag/lift, spanning most of canvas.
    # left tail slightly thin, right tail with tiny down-hook end.
    # Draw as a slightly curved polyline.
    top_y = 70
    pts = [(38, top_y + 3), (90, top_y - 2), (150, top_y - 4),
           (210, top_y - 2), (262, top_y + 4)]
    d.line(pts, fill=ink, width=lw)
    # small right-end downward tick (顿笔)
    d.line([(262, top_y + 4), (265, top_y + 12)], fill=ink, width=lw)

    # ---- Left box ----
    # Left vertical (long, extends further down than the frame top)
    lx = 68
    top_box = 110
    bot_box = 255
    # left vertical stroke — slight leftward lean at bottom (calligraphic)
    d.line([(lx, top_box - 5), (lx - 4, bot_box)], fill=ink, width=lw)

    # top-right corner of left box: short horizontal then long vertical (横折)
    # horizontal top of left box
    top_h_y = top_box
    d.line([(lx - 2, top_h_y), (138, top_h_y + 2)], fill=ink, width=lw)
    # vertical down from right end
    d.line([(138, top_h_y + 2), (135, bot_box - 8)], fill=ink, width=lw)

    # inner short vertical dot inside left box
    d.line([(100, top_h_y + 30), (100, top_h_y + 65)], fill=ink, width=lw)

    # ---- Right box (mirror) ----
    rx_left = 165  # left vertical of right box
    rx_right = 240  # right vertical of right box (from 横折)
    # left vertical of right box
    d.line([(rx_left, top_box - 5), (rx_left - 3, bot_box)], fill=ink, width=lw)
    # top horizontal
    d.line([(rx_left - 2, top_h_y), (rx_right, top_h_y + 2)], fill=ink, width=lw)
    # right vertical from the 横折 corner
    d.line([(rx_right, top_h_y + 2), (rx_right - 3, bot_box - 8)], fill=ink, width=lw)
    # inner short vertical
    d.line([(200, top_h_y + 30), (200, top_h_y + 65)], fill=ink, width=lw)

    img.save(img_path)


if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    draw_li(os.path.join(here, "01_丽.png"))

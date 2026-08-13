# p3_char_0319_听 — 听 (ting, "listen") = 口 (left) + 斤 (right)
# G3 attempt. Inline PIL thin uniform ink (P12 posture, B8-style
# recipe like tong_char/hui_char). L on left ~40% width, R on right ~60%.
# GT read:
#   - 口 sits mid-left, small compact box.
#   - 斤 on right: short 撇 top-left, long 撇 sweeping down-left,
#     short 横 mid, long 竖 descending on right.
# Callable-function unit preserved (G3's constraint).

from PIL import Image, ImageDraw


W_INK = 5  # thin uniform (P12, MMH GT is thin)


def _line(draw, p0, p1, w=W_INK):
    draw.line([p0, p1], fill=(0, 0, 0), width=w)


def _poly(draw, pts, w=W_INK):
    for i in range(len(pts) - 1):
        _line(draw, pts[i], pts[i + 1], w=w)


def draw_kou_inline(draw, left, top, right, bot, w=W_INK):
    """口 as 3-stroke thin box: left 竖, top+right 横折, bottom 横."""
    # Left 竖 (slightly slanted like GT)
    _line(draw, (left, top + 5), (left + 3, bot), w=w)
    # Top 横 + right 竖 (横折)
    _poly(draw, [(left, top), (right, top - 2), (right + 2, bot - 5)], w=w)
    # Bottom 横 closing
    _line(draw, (left - 2, bot), (right + 4, bot - 3), w=w)


def draw_jin_inline(draw, cx, top, bot, w=W_INK):
    """斤: 4 strokes — short 撇, long 撇 (starts nearly horizontal), 横, 竖."""
    # Stroke 1: short 撇 top-left (little slanted tick)
    _line(draw, (cx - 5, top + 5), (cx - 22, top + 30), w=w)
    # Stroke 2: long 撇 — starts near horizontal at top going right,
    # then curves down and sweeps to lower-left (this is the top+left
    # frame of 斤 in one MMH stroke).
    _poly(draw, [(cx - 15, top + 20),
                 (cx + 20, top + 15),
                 (cx + 45, top + 30),
                 (cx + 10, top + 90),
                 (cx - 25, top + 160),
                 (cx - 45, bot - 5)], w=w)
    # Stroke 3: short 横 across middle (attaching interior to right shu)
    _line(draw, (cx - 10, top + 105), (cx + 55, top + 95), w=w)
    # Stroke 4: long 竖 (right vertical, descending to bottom)
    _line(draw, (cx + 52, top + 30), (cx + 55, bot + 10), w=w)


def draw_ting(canvas_size=300):
    img = Image.new("RGB", (canvas_size, canvas_size), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Left 口: mid-left band, roomier
    draw_kou_inline(d, left=40, top=115, right=115, bot=195)

    # Right 斤: taller, offset right
    draw_jin_inline(d, cx=190, top=70, bot=270)

    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_听.png")
    draw_ting().save(out)
    print("wrote", out)

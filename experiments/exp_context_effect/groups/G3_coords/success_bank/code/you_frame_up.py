# you_frame_up.py — 由 frame variant (central 竖 extends ABOVE box top)
# Promoted from p3_char_0409_油 (B11 main PASS, BANK_DEVIATION).
# Curator B11 (2026-08-03, position 550).
#
# CONTEXT (v13 variant policy). Bank has `jia_first.py` (甲: central shu
# extends BELOW box) but nothing for 由 (central shu extends ABOVE box).
# The two shapes are visually mirror-related but cannot be produced by
# uniform-scaling jia_first — the shu extends the OPPOSITE direction.
#
# This entry captures the 由-frame recipe: rectangular 3-stroke box +
# middle heng + central 竖 whose top extends above the top heng.
#
# Use for 由 char itself (0409_油 right side), 甲/申 family cousins
# where the shu direction differs, and any compound with a 由-shape.
#
# Related bank entries (do NOT edit those):
#   - jia_first.py           (甲, shu-below)
#   - shen_extend.py         (申, shu-both-directions)
#   - ri.py                  (日, no central shu)

from PIL import Image, ImageDraw


def draw_you_frame_up(canvas, x_left=130, x_right=250,
                      y_top=95, y_bot=240, y_extend_top=55):
    """Draw 由-shaped 5-stroke frame into a PIL ImageDraw canvas.

    Defaults are the exact values that PASSed for 油's right side.
    Override x_left/x_right to slide left or right; override y_top/y_bot
    and y_extend_top to grow/shrink vertically. The visual property that
    matters is that y_extend_top < y_top (central 竖 starts ABOVE box).

    5 strokes: left 竖, 横折 (top+right), middle 横, central 竖 (extends up),
    bottom 横. All uniform thin ink (P12).
    """
    y_mid = (y_top + y_bot) // 2
    x_center = (x_left + x_right) // 2

    w = 8
    w_mid = 6
    w_vert = 8

    # Stroke 1: left 竖
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top heng + right shu, drawn as two segments)
    canvas.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle heng
    canvas.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom heng (drawn before central shu so shu paints over the joint)
    canvas.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 5: central 竖 — extends from ABOVE top of box to bottom.
    canvas.line([(x_center, y_extend_top), (x_center, y_bot - 2)],
                fill=(0, 0, 0), width=w_vert)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_you_frame_up(d)
    img.save("you_frame_up_preview.png")

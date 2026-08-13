# 身 (shēn, "body") — 7 strokes.
# Composition inline (v8 fresh render, GT-driven):
#   Body is a narrow-ish tilted rectangle with 2 internal 横 + 1 bottom 横.
#   Top-left small 撇 kisses the top of the body.
#   Big 撇 sweeps from the bottom-right corner down and across to lower-left.
from PIL import Image, ImageDraw


def draw_shen(canvas):
    # Body rectangle geometry (slight tilt right side downward, per GT)
    x_left = 115
    x_right = 195
    y_top = 90
    y_bot = 210
    y_mid_up = 130
    y_mid_lo = 170
    w = 7      # body strokes
    w_thin = 5 # internal horizontals

    # Stroke 1: top 撇 — short pie from above body head down-left, kissing top-left
    canvas.line([(165, 50), (x_left - 2, y_top - 2)], fill=(0, 0, 0), width=6)

    # Stroke 2: 竖 — left vertical
    canvas.line([(x_left, y_top + 2), (x_left + 4, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 3: 横折钩 — top horizontal, right vertical, small hook
    canvas.line([(x_left, y_top + 2), (x_right, y_top + 6)], fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 6), (x_right + 3, y_bot + 4)], fill=(0, 0, 0), width=w)
    # small hook at bottom-right (upward-leftward)
    canvas.line([(x_right + 3, y_bot + 4), (x_right - 8, y_bot - 2)], fill=(0, 0, 0), width=6)

    # Stroke 4: middle 横 (upper)
    canvas.line([(x_left + 5, y_mid_up), (x_right - 3, y_mid_up + 2)], fill=(0, 0, 0), width=w_thin)

    # Stroke 5: middle 横 (lower)
    canvas.line([(x_left + 5, y_mid_lo), (x_right - 3, y_mid_lo + 2)], fill=(0, 0, 0), width=w_thin)

    # Stroke 6: bottom 横 (closes body, extends further right past body)
    canvas.line([(x_left + 3, y_bot + 2), (x_right + 20, y_bot + 6)], fill=(0, 0, 0), width=w_thin)

    # Stroke 7: big 撇 — from upper-right area sweeping down-left curved
    # Three segments approximate the smooth diagonal curve
    canvas.line([(230, 75), (215, 130)], fill=(0, 0, 0), width=7)
    canvas.line([(215, 130), (180, 200)], fill=(0, 0, 0), width=7)
    canvas.line([(180, 200), (50, 280)], fill=(0, 0, 0), width=7)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shen(d)
    img.save("01_身.png")

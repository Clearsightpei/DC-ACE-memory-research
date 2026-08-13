# 白 (bái) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0206_白/generated.py
# Note: 5 (short top pie + rectangular ri-body with middle heng)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

# 白 (bái, "white") — 5 strokes.
# Composition: short 撇 on top + 日-like rectangle body with middle 横.
# Adapts ri.py body scheme (tall rectangle, inline fresh) but shifted
# down to leave room for the top 撇. Under v8: bank is REFERENCE ONLY,
# so I inline the whole render for control.
from PIL import Image, ImageDraw


def draw_bai(canvas):
    """5-stroke 白 into a PIL ImageDraw canvas."""
    # Body geometry (日-like tall rectangle, shifted down for 撇 room)
    x_left = 95
    x_right = 215
    y_top = 95
    y_bot = 265
    y_mid = 180
    w = 10        # main strokes
    w_mid = 8     # middle 横 slightly lighter

    # Stroke 1: 撇 (short pie, from top-right of body up-and-right, tail down-left)
    # Tail ends at (x_left+8, y_top+2) so it "kisses" the top-left corner area.
    canvas.line([(155, 45), (x_left + 8, y_top + 2)],
                fill=(0, 0, 0), width=8)

    # Stroke 2: 竖 (left vertical of body)
    canvas.line([(x_left, y_top), (x_left + 3, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 3: 横折 (top 横 + right 竖)
    canvas.line([(x_left, y_top), (x_right, y_top + 4)],
                fill=(0, 0, 0), width=w)
    canvas.line([(x_right, y_top + 4), (x_right + 2, y_bot)],
                fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横 (small right gap, per 日 convention)
    canvas.line([(x_left + 4, y_mid), (x_right - 6, y_mid)],
                fill=(0, 0, 0), width=w_mid)

    # Stroke 5: bottom 横 (closes body)
    canvas.line([(x_left + 2, y_bot), (x_right + 2, y_bot + 2)],
                fill=(0, 0, 0), width=w)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_bai(d)
    img.save("01_白.png")

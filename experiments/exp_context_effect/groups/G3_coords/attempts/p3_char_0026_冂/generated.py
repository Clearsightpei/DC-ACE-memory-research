"""冂 (jiong) — 'down box' radical.
Two strokes:
  1. Left vertical (丨) — short vertical on the left.
  2. Top horizontal + right vertical (横折) — one continuous stroke,
     turns down at the top-right corner.
Rendered inline with PIL. Callable form preserved per G3 constraint.
"""
from PIL import Image, ImageDraw


def draw_jiong(draw, ox=0, oy=0, scale=1.0):
    # Coordinates in image pixels (top-left origin).
    # Center around (150, 150), roughly 180 wide x 200 tall.
    W = 8  # stroke width
    # Left vertical: slight lean-out at bottom
    x_left_top = int(60 + ox)
    y_left_top = int(85 + oy)
    x_left_bot = int(58 + ox)
    y_left_bot = int(245 + oy)
    draw.line([(x_left_top, y_left_top), (x_left_bot, y_left_bot)], fill="black", width=W)

    # Top horizontal (starts a bit right of left vertical top; slight upward arc)
    x_top_l = int(70 + ox)
    y_top_l = int(80 + oy)
    x_top_r = int(235 + ox)
    y_top_r = int(78 + oy)
    draw.line([(x_top_l, y_top_l), (x_top_r, y_top_r)], fill="black", width=W)

    # Right vertical (continues from top-right corner down)
    x_right_top = int(238 + ox)
    y_right_top = int(80 + oy)
    x_right_bot = int(232 + ox)
    y_right_bot = int(240 + oy)
    draw.line([(x_right_top, y_right_top), (x_right_bot, y_right_bot)], fill="black", width=W)

    # Small hook / lift at bottom right (subtle upturn)
    draw.line([(x_right_bot, y_right_bot), (int(225 + ox), int(232 + oy))], fill="black", width=W)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_jiong(draw)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0026_冂/01_冂.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

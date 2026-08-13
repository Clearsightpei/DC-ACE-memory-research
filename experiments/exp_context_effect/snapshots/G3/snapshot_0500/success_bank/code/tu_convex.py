# 凸 (tū) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0215_凸/generated.py
# Note: 5 (stepped rectangle: PIL polyline)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

"""凸 (tū) — 'convex'. 5 strokes forming the classic stepped outline.

Under v8: signature freedom. This character is a pure geometric outline,
so the cleanest form is inlined PIL segments. No bank primitive fits
without extreme transformation (凸 is a unique silhouette).

Stroke decomposition (per GT PNG):
  1. left vertical of the top bump      (top-left corner going down)
  2. top horizontal of the top bump     (across the top)
  3. right vertical of the top bump + right shelf + right vertical of base
     — this reads in the GT as three connected segments; drawn as one path
  4. bottom horizontal of the base
  5. left vertical of the base + left shelf back up under the bump
     — also drawn as one connected path

Rendered as callable function (G3 core constraint).
"""

from PIL import Image, ImageDraw


def draw_tu(canvas_size=300, stroke_w=11):
    img = Image.new("RGB", (canvas_size, canvas_size), "white")
    d = ImageDraw.Draw(img)

    # Top bump outline (upside-down U): left-vert, top-horiz, right-vert-then-shelf-right
    top_left_x = 115
    top_right_x = 190
    top_y = 60          # top edge of bump
    shelf_y = 165       # where bump meets base shelf

    # Base rectangle outline
    base_left_x = 45
    base_right_x = 255
    base_bot_y = 255

    # Points that trace the full silhouette (start bottom-left, clockwise):
    path = [
        (base_left_x, base_bot_y),   # bottom-left
        (base_left_x, shelf_y),      # up left side of base
        (top_left_x, shelf_y),       # right along left shelf
        (top_left_x, top_y),         # up left side of bump
        (top_right_x, top_y),        # across top of bump
        (top_right_x, shelf_y),      # down right side of bump
        (base_right_x, shelf_y),     # right along right shelf
        (base_right_x, base_bot_y),  # down right side of base
        (base_left_x, base_bot_y),   # back across the bottom
    ]

    for a, b in zip(path[:-1], path[1:]):
        d.line([a, b], fill="black", width=stroke_w)

    # Round the joints so the corners don't look pixel-scarred
    for p in path:
        r = stroke_w // 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")

    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__), "01_凸.png")
    draw_tu().save(out)
    print(f"wrote {out}")

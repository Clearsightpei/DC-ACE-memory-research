"""Draw 册 (ce, "book/volume") — 5 strokes.

Structure (v8 free-form G3, callable Python unit):
  Two mirror 冂-like frames joined by a middle horizontal.
  - Left frame:  竖 (short outer) + 横折钩 (top + right-down + hook)
  - Right frame: 竖 (short outer) + 横折钩 (top + right-down + hook)
  - Cross horizontal running through both frames' middle bars

Looking at GT: the two "gates" have thin uniform ink and the crossbar
juts slightly past the outer edges. Bottoms of the inner verticals
curve/hook leftward like a soft 竖钩.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5  # thin uniform width, matches GT

def line(p0, p1, w=LW):
    d.line([p0, p1], fill=INK, width=w)

def curve_hook(p0, p1, ctrl, w=LW, steps=30):
    """Quadratic bezier from p0 to p1 with control ctrl."""
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p1[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p1[1]
        d.line([prev, (x, y)], fill=INK, width=w)
        prev = (x, y)

def draw_frame(left_x, right_x, top_y, bottom_y, hook_left=True):
    """One 冂-like gate: outer vertical (long, slight left bow, tiny hook),
    top horizontal with right-angle turn into inner vertical + hook."""
    # Outer vertical: long, slight leftward bow (撇-flavored 竖)
    curve_hook((left_x + 3, top_y + 6), (left_x - 6, bottom_y),
               (left_x - 2, (top_y + bottom_y) / 2 + 20))
    # Top horizontal
    line((left_x - 1, top_y), (right_x, top_y))
    # Right vertical (down the inner side) — straight
    line((right_x, top_y), (right_x, bottom_y - 5))
    # Hook at bottom pointing left (calligraphic upward-tick)
    hook_end_x = right_x - 14 if hook_left else right_x + 14
    curve_hook((right_x, bottom_y - 5), (hook_end_x, bottom_y - 20),
               (right_x - 2, bottom_y - 2) if hook_left else (right_x + 2, bottom_y - 2))

# Character bounds — center it
# Left frame
LF_L = 70
LF_R = 135
# Right frame
RF_L = 165
RF_R = 230
TOP = 90
BOT = 250

draw_frame(LF_L, LF_R, TOP, BOT, hook_left=True)
draw_frame(RF_L, RF_R, TOP, BOT, hook_left=True)

# Cross horizontal — running through both frames' middle area
# Slightly slants up, extends past outer edges
CROSS_Y = 160
line((LF_L - 8, CROSS_Y + 4), (RF_R + 12, CROSS_Y - 6))

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0207_册/01_册.png"
img.save(out)
print("saved", out)

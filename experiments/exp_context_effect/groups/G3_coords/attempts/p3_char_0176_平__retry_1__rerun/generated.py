# VISUAL DIFF (prior retry_1 vs GT) — STEP 0
# =========================================
# Read: groups/G3_coords/attempts/p3_char_0176_平__retry_1/01_平.png
# Read: gt/phase3/平.png
#
# Concrete visual gaps between prior attempt and GT:
#
# 1. TOP-ORNAMENT SHAPE IS WRONG. Prior rendered the two side dots
#    as an inverted-V ("^") tent joined at an apex ABOVE a small heng.
#    GT shows a 丷-style mirror pair (left 点 slanting down-right,
#    right 撇 slanting down-left) that DO NOT touch each other and
#    sit BETWEEN a top short heng (above them) and the main heng
#    (below them). Prior's apex+tent has no equivalent in the GT.
#
# 2. TOP SHORT HENG POSITION. In prior it sits just below the tent
#    apex (very small, ~30px wide) and BELOW the two side strokes.
#    In GT the top short heng is the highest element (y ~ 60px from
#    top), roughly the width of the 丷 pair beneath it (~80–90px),
#    and the two dots hang below it, not above.
#
# 3. VERTICAL SHU ORIGIN. Prior's vertical starts at the tent apex
#    and runs continuously downward through the main heng. GT's
#    vertical begins AT the crossing point of the main heng (mid-
#    canvas) and extends only downward from there — the shu does
#    NOT extend above the main heng.
#
# 4. MAIN HENG WIDTH / TILT. Prior main heng is ~90% canvas width,
#    dead flat. GT main heng is ~85% width with a slight upward
#    tilt from left to right (calligraphic rise).
#
# Fix plan:
#   - Draw the top short heng first (short, high, centered).
#   - Draw a 丷-pair BELOW that heng, ABOVE the main heng
#     (left 点 slanting down-right; right 撇 slanting down-left,
#     mirror). Both are short (~25 px), do NOT touch, and stay
#     within the horizontal span of the top short heng.
#   - Draw the wide main heng, slight upward tilt.
#   - Draw the vertical shu starting AT the crossing of the main
#     heng, running straight down to near the bottom.
#
# G3 constraint: everything below is expressed as callable Python
# functions taking pixel coordinates. No 米字格 anchors. Bank primitives
# are REFERENCE ONLY (v8) — since 平's exact composition is not in the
# bank, I inline fresh with per-stroke functions.

from PIL import Image, ImageDraw
import os

W = H = 300
INK = 0

def _line(draw, p0, p1, width):
    draw.line([p0, p1], fill=INK, width=width)

def draw_top_heng(draw, cx=150, cy=60, half_w=42, width=6):
    """Short top heng, slight upward tilt L->R."""
    x0 = cx - half_w
    x1 = cx + half_w
    y0 = cy + 3          # left end sits a touch lower
    y1 = cy - 3          # right end lifts (calligraphic rise)
    _line(draw, (x0, y0), (x1, y1), width)

def draw_left_dian(draw, x_top=125, y_top=78, dx=-8, dy=22, width=6):
    """Left 点: short stroke slanting from upper-right down to lower-left.
    Visually in GT the left ornament goes from lower-left up to
    upper-right; we render it as a short slanted line, mirror of the
    right 撇."""
    x1 = x_top + dx      # 117
    y1 = y_top + dy      # 100
    _line(draw, (x_top, y_top), (x1, y1), width)

def draw_right_pie(draw, x_top=175, y_top=78, dx=+8, dy=22, width=6):
    """Right 撇: short stroke slanting from upper-left down to lower-right.
    Mirror of the left dian across cx=150."""
    x1 = x_top + dx      # 183
    y1 = y_top + dy      # 100
    _line(draw, (x_top, y_top), (x1, y1), width)

def draw_main_heng(draw, cx=150, cy=155, half_w=115, width=7):
    """Wide main heng, slight upward tilt L->R."""
    x0 = cx - half_w
    x1 = cx + half_w
    y0 = cy + 5          # left end slightly lower
    y1 = cy - 5          # right end lifted
    _line(draw, (x0, y0), (x1, y1), width)

def draw_shu(draw, cx=150, cy_top=152, y_bot=270, width=7):
    """Vertical shu starting AT the main heng crossing, running down."""
    _line(draw, (cx, cy_top), (cx, y_bot), width)

def draw_ping(img_path):
    img = Image.new("L", (W, H), 255)
    draw = ImageDraw.Draw(img)

    # Stroke order (MMH-typical): 1 top-heng, 2 left-dian,
    # 3 right-pie, 4 main-heng, 5 shu.
    draw_top_heng(draw)
    draw_left_dian(draw)
    draw_right_pie(draw)
    draw_main_heng(draw)
    draw_shu(draw)

    img.save(img_path)


if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    draw_ping(os.path.join(out_dir, "01_平.png"))

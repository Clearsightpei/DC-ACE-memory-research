"""p3_char_0174_主 — 主 (5 strokes: dot + 龶 (3 hengs + piercing shu)).

Composition:
  - top 丶 (short diagonal dot) above the top heng
  - 龶 (zhu_top) below — from success_bank/code/zhu_top.py
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Allow importing from bank
BANK = Path("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code")
sys.path.insert(0, str(BANK))

from zhu_top import draw_zhu_top  # noqa: E402

CANVAS = 300


def _to_pixel(mx, my, size=CANVAS):
    return size / 2 + mx, size / 2 - my


def draw_top_dot(t, ox=0.0, oy=0.0, scale=1.0):
    """Small diagonal dot 丶 — thin (~4 px), tilts down-right, short (~12 units)."""
    ink = max(2, int(round(4.0 * scale)))
    # Short diagonal segment in math coords
    x0, y0 = -6.0 * scale, 6.0 * scale
    x1, y1 = 6.0 * scale, -6.0 * scale
    p0 = _to_pixel(ox + x0, oy + y0)
    p1 = _to_pixel(ox + x1, oy + y1)
    t.line([p0, p1], fill=(0, 0, 0), width=ink)


def draw_zhu(t):
    """主 = 丶 on top + 龶 (zhu_top) below.

    zhu_top has top-heng at math y=55, bottom-heng at y=-20, shu from
    y=70 to y=-35 (all centered at x=0).
    Shift zhu_top down (oy = -20) so top-heng lands ~y=35, giving room
    for the dot above at ~y=75.
    """
    # zhu_top shifted down slightly to leave headroom for the dot
    draw_zhu_top(t, ox=0.0, oy=-20.0, scale=1.0)
    # dot placed above the (shifted) top heng
    draw_top_dot(t, ox=0.0, oy=75.0, scale=1.0)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_zhu(t)
    out = Path("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0174_主/01_主.png")
    img.save(out)
    print(f"wrote {out}")

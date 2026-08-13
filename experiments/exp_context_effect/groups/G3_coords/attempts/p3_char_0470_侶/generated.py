# p3_char_0470_侶 — 侶 (lǚ, "companion"): 亻 (left) + 呂 (right, two stacked 口).
#
# Recipe:
# - Left: bank `ren_pang` — placed at ox=-60, scale=0.65. Per drawer_memory
#   L-R table the proven anchor is ox=-45 scale=0.55; nudged slightly bigger
#   and further left because 呂 (right) is a two-box stack that dominates.
# - Right: two stacked bank `kou` boxes (like chuan_char but WITHOUT the
#   piercing shu). Both centered around x=+40. Top box slightly smaller and
#   higher; bottom box slightly larger and lower — matches GT proportion.
#
# No BANK_DEVIATION needed — ren_pang and kou fit cleanly for this L-R form.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from kou import draw_kou            # noqa: E402


CANVAS = 300


def draw_lu_companion(d):
    """侶: 亻 (left) + 呂 (two stacked 口 on right).

    REVISION 1: first pass had 亻 too small/high and boxes too far apart.
    - Bigger 亻 (scale 0.95) that spans nearly full canvas height.
    - Bring the two 呂 boxes closer together (oy=+40 / oy=-45) so they
      read as one connected unit, not two isolated squares.
    - Nudge boxes slightly further right (ox=+50) so 亻 has room.
    """
    # Left: 亻 — tall, dominates left half.
    draw_ren_pang(d, ox=-55, oy=-5, scale=0.95)

    # Right: 呂 — two stacked 口 boxes, close together.
    # Top 口 — slightly smaller.
    draw_kou(d, ox=50, oy=45, scale=0.48)
    # Bottom 口 — slightly larger.
    draw_kou(d, ox=50, oy=-50, scale=0.55)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_lu_companion(d)
    out = os.path.join(os.path.dirname(__file__), "01_侶.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

# p3_char_0138_水 — main attempt (G3 coord bank)
#
# Decomposition (4 strokes standard):
#   1. 竖钩 (shu_gou) center vertical with left-flick hook at bottom
#   2. 横撇 (heng_pie) top-left: short heng then pie down-left
#      (looking at GT: it's really a small ~horizontal-to-pie mark
#      upper-left of the shaft, ending well left of shaft mid)
#   3. 撇 upper-right — short pie from near shaft going up-right
#   4. 捺 (na) — from near shaft mid going down-right
#
# GT shows uniformly thin lines (MMH reference). Per P12: use thin
# widths, not calligraphic.
#
# Read memory_index: shu_gou primitive fits the center stroke well.
# Left arm (heng_pie) and right pie+na don't fit a single primitive
# nicely — I'll inline with variant_pie / variant_na for control,
# plus a straight thin line for the small heng segment on the left.

import sys
import os
from PIL import Image, ImageDraw

# Import shared helpers from the success bank.
SB = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, SB)
from _shared_helpers import variant_pie, variant_na, to_px, tapered_line  # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402


CANVAS = 300
OUT = os.path.join(os.path.dirname(__file__), "01_水.png")


def draw():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 1. 竖钩 (center) — draw INLINE thin, not bank primitive.
    # Bank shu_gou is 12px calligraphic; GT is thin uniform. Per P12,
    # override to thin. Shaft from top (~+95) to bottom (~-95), hook
    # at bottom flicks up-left ~20px.
    d.line([to_px(0, +95), to_px(0, -95)], fill=(0, 0, 0), width=4)
    # Hook: from (0, -95) up-left to (-22, -78)
    d.line([to_px(0, -95), to_px(-22, -78)], fill=(0, 0, 0), width=4)

    # ---- 2. Left 横撇 arm ------------------------------------------
    # Two segments meeting at a corner: short heng at top-left meeting
    # shaft around y=+35, then a pie going down-left.
    # Heng: from (-55, +55) to (-8, +40)  (slightly rising toward shaft)
    d.line([to_px(-55, +55), to_px(-8, +40)], fill=(0, 0, 0), width=4)
    # Pie: from corner (-55, +55) down-left curving to (-75, -35)
    variant_pie(
        d,
        head=(-52.0, +52.0),
        tail=(-78.0, -45.0),
        bow_perp=-8.0,
        w_head=4.0,
        w_tail=2.0,
        n=48,
    )

    # ---- 3. Right upper 撇 (short, going up-right from shaft) ------
    # Short thin stroke from shaft (~ +12, +35) up-right to (~+55, +60)
    # actually in 水 it's a small pie that STARTS upper-right and comes
    # down-left toward shaft. So head at (+55, +60), tail near (+15, +25).
    variant_pie(
        d,
        head=(+55.0, +60.0),
        tail=(+15.0, +28.0),
        bow_perp=+3.0,
        w_head=4.0,
        w_tail=2.5,
        n=32,
    )

    # ---- 4. Right 捺 -----------------------------------------------
    # From near shaft (slightly above middle) down-right, mildly curved.
    variant_na(
        d,
        head=(+15.0, +20.0),
        tail=(+80.0, -55.0),
        bow_perp=+4.0,
        w_head=2.5,
        w_belly=5.0,
        w_tail=3.0,
        belly_u=0.65,
        n=60,
    )

    img.save(OUT)
    return OUT


if __name__ == "__main__":
    p = draw()
    print(f"wrote {p}")

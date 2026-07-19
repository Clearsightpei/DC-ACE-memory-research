# p2_radical_082_子 — G3 coord-bank attempt
# 子 has 3 strokes:
#   1. 横撇 (heng_pie) at the top — short horizontal ending in a down-left pie
#   2. 弯钩 (wan_gou) — long curved vertical hook from top-center down, hook at bottom
#   3. 一 (heng) — long horizontal crossing the vertical in the middle
#
# TR-compliance analysis (INLINE-FRESH TEST):
# - heng_pie primitive: standalone is short heng + down-left pie with 顿笔. This
#   matches the top of 子 in silhouette (a horizontal that turns down-left at
#   the right end). Use with scale reduced for top-of-character placement.
# - wan_gou primitive: standalone is exactly the curved-vertical-with-left-hook
#   we need. Use at near-full scale, centered.
# - heng primitive: standalone is a straight horizontal. Fits the crossing 一
#   perfectly; scale ~0.8 for a long crossbar.
# All three primitives are TR8-clean (their standalone geometry matches 子's
# required geometry after simple uniform scaling).

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Add success_bank/code to sys.path so we can import the primitives.
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng_pie import draw_heng_pie   # noqa: E402
from wan_gou import draw_wan_gou     # noqa: E402
from heng import draw_heng           # noqa: E402


CANVAS = 300
OUT = Path(__file__).with_name("01_子.png")


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # ---- Stroke 1: 横撇 (top hook) ----
    # heng_pie's standalone at scale 0.55: heng from (-80*0.55,+40*0.55) =
    # (-44,+22) to (+65*0.55,+50*0.55) = (+35.75,+27.5); corner at (+37.4,+25.85);
    # pie tail at (-15*0.55,-85*0.55) = (-8.25,-46.75).
    # Add (ox=-15, oy=+55): heng_start_world (-59,+77), heng_end_world (+20.75,+82.5),
    # corner_world (+22.4,+80.85), pie_tail_world (-23.25,+8.25).
    # We want the pie tail to weld to the head of 弯钩 (see below). The wan_gou
    # head (at its own scale 0.95) is at world (+2+5*0.95, oy_w+110*0.95) —
    # solve so the wan_gou head lands near the pie tail exit.
    draw_heng_pie(t, ox=-15, oy=+55, scale=0.55)

    # ---- Stroke 2: 弯钩 (curved vertical hook) ----
    # wan_gou standalone at scale 0.9: p_start(+4.5,+99), p_end(-9,-85.5),
    # hook tip (-34.2,-67.5).
    # Add offset (ox=-8, oy=-30): head lands at world (-3.5, +69); tail world
    # (-17, -115.5); hook tip world (-42.2, -97.5).
    # This puts the head just below the 横撇's corner (at world +22 x, +81 y)
    # — not welded, but visually connected as the 弯钩 emerges from under
    # the top corner. Slightly-left ox brings the shaft under the pie tail
    # rather than under the corner, matching the GT proportion.
    draw_wan_gou(t, ox=-8, oy=-30, scale=0.9)

    # ---- Stroke 3: 一 (crossing horizontal) ----
    # heng standalone: length 200 px scaled → 200*0.85 = 170 px bar.
    # ox = -5 shifts slightly left to visually cross the wan_gou shaft
    # (which is at world x ≈ -5 to -10 mid-shaft).
    # oy = -5: slightly below true center (matches GT crossbar position).
    draw_heng(t, ox=-5, oy=-5, scale=0.85)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    render()

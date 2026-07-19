# p2_radical_037_又 — G3 coord-format render.
# 又 = 横撇 (heng_pie) + 捺 (na). The 捺 crosses the 撇 partway down.
#
# Bank composition (TR6 transform log):
#   heng_pie: standalone span in math coords is approx heng from (-80,+40) to
#     (+65,+50) then pie tail (-15,-85). For 又 we want the top-horizontal
#     centered slightly above middle and shorter, so scale=0.85. No offset —
#     the primitive already sits at canvas-center-ish.
#     Transform: ox=+0, oy=+10, scale=0.85.
#     Post-transform pie tail lands near (-13, -62): the 撇 sweeps to
#     lower-left, ending clear of the bottom margin.
#   na: standalone runs (-70,+80) -> (+80,-90). For 又 the 捺 must
#     START from HIGH on the 撇 (near the corner region) and sweep
#     down-right past the canvas center. We want the 捺 head near
#     (-25, +30) (on the 撇) and belly-tail at (+70, -75).
#     na default head is (-70, +80); target head (-25, +30):
#       ox = -25 - (-70*0.85) = -25 + 59.5 = +34.5 -> use +32.
#       oy = +30 - (+80*0.85) = +30 - 68 = -38 -> use -38.
#     scale = 0.85.
#     Post-transform tail: (+80*0.85 + 32, -90*0.85 - 38) = (+100, -114.5) —
#     that overshoots canvas. Better: reduce scale a bit AND accept the
#     tail will land near the lower-right corner. Use scale=0.75 with
#     ox=+22, oy=-28 → head (-30.5,+32), tail (+82,-95.5). Head is close
#     to the 撇's mid section, tail lands within margin.
#
# Eyeball sanity (TR7):
#   heng_pie top-horiz: from (-80*.85+0,+40*.85+10)=(-68,+44) to (+55,+52.5).
#     -> pixel (82,106) to (205,97). OK, inside 300 canvas.
#   heng_pie pie tail: (-15*.85+0,-85*.85+10) = (-13,-62) -> pixel (137,212).
#     OK, well inside canvas.
#   na head: (-70*.75+22,+80*.75-28) = (-30.5,+32) -> pixel (119.5,118).
#     Sits on the 撇 shaft near its upper-mid — the two strokes CROSS
#     here. Good.
#   na tail: (+80*.75+22,-90*.75-28) = (+82,-95.5) -> pixel (232,245.5).
#     Inside 10-px margin.
#
# All strokes fit; the two strokes cross where the 撇 descends and the 捺
# swoops through. This is the 又 X-shape signature.

import sys
import os

CODE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, CODE_DIR)

from PIL import Image, ImageDraw

from heng_pie import draw_heng_pie
from na import draw_na


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Stroke 1: 横撇 (top-horizontal + down-left 撇)
    # Transform: ox=0, oy=+10, scale=0.85
    draw_heng_pie(d, ox=0, oy=10, scale=0.85)

    # Stroke 2: 捺 (crossing sweep down-right through the 撇)
    # Transform: ox=+22, oy=-28, scale=0.75
    # Head lands at (-30.5, +32) — on the 撇 shaft, upper-mid — creating
    # the crossing "X" that defines 又.
    draw_na(d, ox=22, oy=-28, scale=0.75)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "01_又.png",
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

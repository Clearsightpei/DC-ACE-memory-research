# p2_radical_064_彡 — 彡 radical, 3 strokes (three cascading pie sweeps).
#
# Analysis of GT: three short-to-medium 撇 strokes stacked diagonally,
# each starting to the upper-right, sweeping down-left. Each successive
# pie starts further down and slightly further left. Bottom pie is the
# longest with the deepest sweep. Overall composition sits slightly right
# of center in the canvas.
#
# TR1: every draw_pie call gets deliberate (ox, oy, scale).
# TR2: standalone radical — components ~0.35-0.55 scale (small strokes).
# TR3: origin picks each pie's own center offset.
# TR5: inline is fine here since we need 3 different small pies with
#      different curvatures — but pie primitive with tuned scales still
#      matches per-stroke shape well. Use bank primitive with adjusted
#      (ox, oy, scale) per stroke.

import os
import sys
from PIL import Image, ImageDraw

# Allow importing the shared primitive
BANK_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, BANK_DIR)

from pie import draw_pie  # noqa: E402

CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Pie primitive default (math coords, center origin):
    #   head at (+65, +90), tail at (-45, -85). At scale=1 the stroke spans
    #   ~110 x ~175. We want much smaller sub-strokes.
    #
    # GT layout (approx math coords, +y up, canvas center 0,0):
    #   canvas center (0,0). Character sits roughly x ∈ [-30, +60], y ∈ [-90, +75].
    #
    # Stroke 1 (top pie): short, upper region.
    #   Target center ≈ (+30, +60). Scale 0.35 -> spans ~38 x ~61.
    #
    # Stroke 2 (middle pie): slightly larger, offset down-left of stroke 1.
    #   Target center ≈ (+10, +5). Scale 0.42.
    #
    # Stroke 3 (bottom pie): longest, further down-left.
    #   Target center ≈ (-10, -55). Scale 0.55.

    # Revision after visual self-check (v1 -> v2):
    # v1 strokes appeared too spread vertically and too near-vertical.
    # GT strokes are tightly clustered, each shifting left as it descends,
    # with a clear diagonal slant. Reduce vertical spacing, keep small
    # scales (pie primitive is naturally quite slanted at any scale),
    # shift top pie left so composition doesn't lean too far right.

    # Stroke 1 — top short pie (upper region, slightly right of center)
    draw_pie(t, ox=+20, oy=+40, scale=0.32)

    # Stroke 2 — middle pie (slightly left, slightly larger)
    draw_pie(t, ox=+5, oy=-5, scale=0.38)

    # Stroke 3 — bottom long pie (further left, longest sweep)
    draw_pie(t, ox=-10, oy=-45, scale=0.48)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_彡.png"
    )
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

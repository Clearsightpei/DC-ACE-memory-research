# p2_radical_028_人 — 人 radical (2 strokes: 撇 + 捺 meeting at top apex).
#
# Compositional plan (deliberate TR1/TR3 placement):
#   - Unlike 八 (splayed, V-notch gap at top), 人's two strokes MEET at
#     the top-center apex and splay outward-downward.
#   - Apex placed at ~(150, 90) in PIL coords (top-center of canvas).
#   - Pie primitive: standalone head is at math-coord (+65, +90). To land
#     that head near the apex (math coord (0, +60)), pass ox=-65, oy=-30.
#     scale=0.75 so the stroke spans roughly the full character height.
#   - Na primitive: standalone head is at math-coord (-70, +80). To land
#     that head near the apex too, pass ox=+70, oy=-20 (and scale=0.75).
#   - Small horizontal nudge inward so heads truly touch/kiss at top.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # 人: apex at top-center. Both stroke-heads converge near (0, +60) in
    # math coords (i.e. PIL pixel (150, 90)).
    # scale 0.75 -> pie/na occupy ~character size (not full canvas).

    # Revised: scale up to 0.90 so tails reach near bottom edges of canvas,
    # matching GT's wide splayed silhouette. Apex still at math (0, +75).
    #
    # Pie: head standalone at (+65*s, +90*s) = (+58.5, +81). Push head to
    # (~ -3, +75). ox = -3 - 58.5 = -61.5, oy = 75 - 81 = -6.
    draw_pie(t, ox=-61.5, oy=-6.0, scale=0.90)

    # Na: head standalone at (-70*s, +80*s) = (-63, +72). Push head to
    # (~ +3, +75). ox = 3 - (-63) = +66, oy = 75 - 72 = +3.
    draw_na(t,  ox=+66.0, oy=+3.0,  scale=0.90)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_人.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

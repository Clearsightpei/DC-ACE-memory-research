# hua_char.py — 花 — promoted from p3_char_0357_花 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# generated.py — p3_char_0357_花 (huā, "flower") — 7 strokes
# Composition: 艹 (top, 3 strokes) + 化 (bottom, 4 strokes: 亻 + 匕).
# Use bank cao_zi_tou for top, bank ren_pang for left 亻, and inline
# the right 匕 (bank has no clean 匕 primitive; bi_char has a similar
# right-side 匕 recipe we adapt here).
#
# Uniform thin lines (W=5) per P12 to match MMH GT rendering style.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from cao_zi_tou import draw_cao_zi_tou  # noqa: E402
from ren_pang import draw_ren_pang  # noqa: E402

CANVAS = 300
W = 5

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# ---- TOP: 艹 radical (upper third, compressed vertically) ----
# cao_zi_tou uses math coords centered at canvas midpoint (150, 150).
# Push up (oy=+95) and use scale 0.55 → thickness ≈ 5-6 (matches thin
# MMH GT style, and prior heavy version overweighted the top).
draw_cao_zi_tou(d, ox=0, oy=95, scale=0.55)

# ---- BOTTOM LEFT: 亻 ----
# Shift further left (ox=-75) so its short shu clears the 匕 column;
# ren_pang shu sits at ox+20*scale ≈ -60 → canvas x ≈ 90 (well left).
draw_ren_pang(d, ox=-75, oy=-45, scale=0.85)

# ---- BOTTOM RIGHT: 匕 (inlined; 2 strokes) ----
# Stroke A: 撇 — starts upper-right (~215, 130), sweeps down-left,
# landing on the 竖弯钩 shaft.
line((215, 130), (155, 200))

# Stroke B: 竖弯钩 — vertical from top (~180, 140) down to ~180, 240,
# then curves right along the bottom and hooks up.
line((180, 140), (180, 240))
polyline([(180, 240), (188, 255), (205, 263), (230, 260), (250, 245)])
# hook up
line((250, 245), (250, 225))

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0357_花/01_花.png"
)

# BANK_DEVIATION
# skipped: shi_ceremony_pang.py
# reason: 被's left radical is 衤 (5 strokes, clothing) not 礻 (4 strokes);
#   needs extra left dot below the heng-pie corner — 礻 primitive lacks it.
# fresh_component: yi_cloth_pang (5-stroke 衤 inline)
#
# BANK_DEVIATION
# skipped: (no 皮 primitive exists)
# reason: 皮 has no bank entry; inline fresh.
# fresh_component: pi_skin (5-stroke 皮 inline)

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import to_px, tapered_bezier, tapered_line  # noqa: E402

CANVAS = 300


def draw_yi_cloth_pang(d, ox=0.0, oy=0.0, scale=1.0):
    """衤 (clothing side-radical), 5 strokes. Math coords y-up, origin=canvas center."""
    def T(p): return (p[0] * scale + ox, p[1] * scale + oy)
    # Stroke 1: top 点
    tapered_bezier(d, T((0, 95)), T((7, 85)), T((16, 72)),
                   2 * scale, 7 * scale, n=25)
    # Stroke 2: 横撇 — short heng + corner blob + descending pie
    tapered_line(d, T((-38, 52)), T((18, 55)), 5 * scale, 8 * scale, n=20)
    bx, by = to_px(*T((18, 55)))
    d.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(0, 0, 0))
    tapered_bezier(d, T((18, 55)), T((-8, 25)), T((-38, -18)),
                   8 * scale, 2 * scale, n=30)
    # Stroke 3: long shu (central vertical)
    tapered_line(d, T((-2, 35)), T((-4, -110)), 6 * scale, 6 * scale, n=30)
    # Stroke 4: left dian (below the heng-pie, left of shu)
    tapered_bezier(d, T((-20, -5)), T((-28, -20)), T((-38, -40)),
                   2 * scale, 8 * scale, n=25)
    # Stroke 5: right dian (below the shu-mid, right side)
    tapered_bezier(d, T((10, -10)), T((22, -25)), T((36, -48)),
                   2 * scale, 8 * scale, n=25)


def draw_pi_skin(d, ox=0.0, oy=0.0, scale=1.0):
    """皮 (skin), 5 strokes. Math coords y-up, origin=canvas center."""
    def T(p): return (p[0] * scale + ox, p[1] * scale + oy)
    # Stroke 1: top short heng, slight arch, from mid to upper-right corner
    tapered_line(d, T((-15, 90)), T((30, 88)), 4 * scale, 6 * scale, n=20)
    # Stroke 2: long descending 撇 — starts at top-left area (from stroke1 head),
    #           sweeps down through the interior to bottom-left
    tapered_bezier(d, T((-15, 90)), T((-40, 20)), T((-75, -110)),
                   9 * scale, 2 * scale, n=40)
    # Stroke 3: 横折钩 — heng across top of the box, then hook down at right
    tapered_line(d, T((-25, 45)), T((55, 48)), 5 * scale, 6 * scale, n=25)
    # small corner blob
    bx, by = to_px(*T((55, 48)))
    d.ellipse([bx - 4, by - 4, bx + 4, by + 4], fill=(0, 0, 0))
    tapered_bezier(d, T((55, 48)), T((50, 25)), T((38, 0)),
                   6 * scale, 5 * scale, n=25)
    # small hook tip
    tapered_bezier(d, T((38, 0)), T((30, 5)), T((22, 3)),
                   5 * scale, 2 * scale, n=15)
    # Stroke 4: inner short 撇 (pie) inside the 又
    tapered_bezier(d, T((-5, 20)), T((-12, -5)), T((-25, -35)),
                   6 * scale, 2 * scale, n=25)
    # Stroke 5: 捺 na — sweeps down-right to bottom-right
    tapered_bezier(d, T((-8, 20)), T((25, -45)), T((78, -110)),
                   3 * scale, 13 * scale, n=40)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Left: 衤 (clothing pang)
    draw_yi_cloth_pang(d, ox=-58.0, oy=5.0, scale=0.75)
    # Right: 皮
    draw_pi_skin(d, ox=65.0, oy=5.0, scale=0.80)
    img.save(os.path.join(os.path.dirname(__file__), "01_被.png"))


if __name__ == "__main__":
    main()

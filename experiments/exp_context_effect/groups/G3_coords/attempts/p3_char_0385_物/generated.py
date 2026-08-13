# BANK_DEVIATION
# skipped: niu.py (牛 is full-width symmetric; 物's left is 牜, a compressed
#          left-side variant with a rising ti replacing the bottom heng and
#          a shortened vertical) and wu_neg.py (a full render() script, not
#          ox/oy/scale composable — coords baked to center 150,150).
# reason: 物 = 牜 (left, compressed) + 勿 (right, dominant). Bank primitives
#         don't compose at the required side-by-side sub-canvases without
#         extreme rewrite. Cleaner to inline both halves fresh.
# fresh_component: niu_left_variant_for_LR (牜 in left position) and
#                  wu_neg_for_LR (勿 rendered as right-side component).
#
# p3_char_0385_物 — cow (牜) + wu (勿), left-right composition.
# Left side ~x:30-125 in PIL; right side ~x:130-275.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie, tapered_line, tapered_bezier, to_px


def draw_niu_left(d):
    """牜 in left position of 物. Math coords: center=(150,150), +y up.
    Left-half sub-canvas centered around math (-75, 0)."""
    # (1) top pie — short down-left sweep from upper-right of top area
    #     into upper-left. Head at math (-55, 75), tail at (-90, 40).
    variant_pie(d, head=(-55, 75), tail=(-95, 30),
                bow_perp=6.0, w_head=8.0, w_tail=2.0, n=36)

    # (2) short heng — a shoulder crossing to the right of the pie's tail
    #     top area. Math from (-70, 55) to (-30, 55).
    tapered_line(d, (-72, 55), (-32, 55), 5.0, 5.0, n=24)

    # (3) long vertical (shu) — the main stem of 牜. Slightly right of the
    #     pie-tail area, extending far down but not to the very bottom
    #     (in 牜 the vertical is a bit shortened vs 牛). Math (-45, 60) to
    #     (-45, -95).
    tapered_line(d, (-45, 65), (-45, -105), 6.0, 6.0, n=32)

    # (4) rising ti (提) — bottom-left area rising up-right, crossing the
    #     shu. Math from (-95, -30) to (-25, -5).
    tapered_line(d, (-95, -30), (-22, -3), 7.0, 3.0, n=32)


def draw_wu_right(d):
    """勿 in right position of 物. Larger — dominant right side.
    Sub-canvas centered around math (+60, 0)."""
    # (1) short top pie — clearly ABOVE the envelope. Sweeps down-left.
    variant_pie(d, head=(45, 110), tail=(15, 78),
                bow_perp=4.0, w_head=7.0, w_tail=2.0, n=32)

    # (2) 横折钩 envelope — top horizontal (heng), then vertical down
    #     with a mild leftward drift and small hook at end.
    #     Top heng starts a bit inside from where top pie ended.
    tapered_line(d, (15, 65), (100, 65), 5.0, 5.0, n=28)
    # Right vertical: gentler curve, ends slightly left-and-down for hook.
    tapered_bezier(d,
                   p0=(100, 65),
                   p1=(95, -20),
                   p2=(60, -100),
                   w_head=6.0, w_tail=5.0, n=48)
    # Hook flick at bottom — small up-left tick.
    tapered_line(d, (60, -100), (40, -85), 5.0, 2.0, n=12)

    # (3) inner long pie #1 — from just under envelope-top, sweeps
    #     down-left crossing the envelope's bottom-left area.
    variant_pie(d, head=(35, 45), tail=(-5, -105),
                bow_perp=9.0, w_head=8.0, w_tail=2.0, n=48)

    # (4) inner long pie #2 — parallel, further right.
    variant_pie(d, head=(70, 45), tail=(35, -110),
                bow_perp=9.0, w_head=8.0, w_tail=2.0, n=48)


def render(out_path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_niu_left(d)
    draw_wu_right(d)
    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_物.png")
    render(out)
    print("wrote", out)

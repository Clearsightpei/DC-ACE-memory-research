# p2_radical_100_见 — RETRY 1 — 见 (jiàn), 4-stroke radical.
#
# Prior failure (retry_0):
#   - Box was too tall/thin (heng_zhe forced into non-native aspect).
#   - 撇 started INSIDE the box at the top-right and cut down-left across
#     the interior — should instead start near the box bottom-left and
#     descend BELOW the box.
#   - 竖弯钩 also floated inside instead of welding to the box floor.
#
# Errata fix idea: "inline the box (like ri.py but square), then hand-
# place the two descenders welding to bottom."
#
# Correct structure (from GT visual):
#   Top box: roughly square, occupies upper 55% of canvas.
#     Box left x ~= -50, right x ~= +40, top y ~= +85, bottom y ~= -5.
#   Stroke order:
#     1. 竖   — left wall of box (goes from top y=+85 down to bottom y=-5)
#     2. 横折 — top horizontal (top-left to top-right) + right wall down
#              (top-right → bottom-right)
#     3. 撇   — starts at box's inner bottom-left (~(-45, -5)) sweeps down
#              and left, exiting at about (-90, -110). This is the LEFT
#              descender.
#     4. 竖弯钩 — starts at box's inner bottom-right (~(+35, -5)) drops
#              down to ~(+35, -85), curves right to ~(+80, -110), then
#              hooks UP to about (+70, -80). This is the RIGHT descender.
#
# Coord math convention (P5): center origin, +y up. Convert via to_px.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from _shared_helpers import to_px, tapered_line, tapered_bezier, variant_pie  # noqa: E402


CANVAS_SIZE = 300


def draw():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ============================================================
    # Box parameters (inlined per errata fix — do NOT force kou/heng_zhe)
    # REVISION 1: widened box (was -50..+40, now -65..+55) and shifted
    # top slightly higher; the previous render was too narrow relative
    # to the GT which shows a nearly-square box.
    # ============================================================
    BOX_LEFT   = -65
    BOX_RIGHT  = +55
    BOX_TOP    = +90
    BOX_BOTTOM = -5
    BOX_INK    = 8   # uniform ink thickness for box walls

    # Stroke 1: 竖 — left wall (top-to-bottom)
    tapered_line(d,
                 (BOX_LEFT, BOX_TOP),
                 (BOX_LEFT, BOX_BOTTOM),
                 w0=BOX_INK, w1=BOX_INK, n=32)

    # Stroke 2: 横折 — top horizontal from (BOX_LEFT, BOX_TOP) to
    # (BOX_RIGHT, BOX_TOP), then vertical down to (BOX_RIGHT, BOX_BOTTOM).
    # Draw as two connected tapered segments; add a small 顿笔 corner blob.
    tapered_line(d,
                 (BOX_LEFT, BOX_TOP),
                 (BOX_RIGHT, BOX_TOP),
                 w0=BOX_INK, w1=BOX_INK, n=32)
    # Corner blob at (BOX_RIGHT, BOX_TOP)
    cx, cy = to_px(BOX_RIGHT, BOX_TOP)
    r = 5
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # Right wall (top-to-bottom)
    tapered_line(d,
                 (BOX_RIGHT, BOX_TOP),
                 (BOX_RIGHT, BOX_BOTTOM),
                 w0=BOX_INK, w1=BOX_INK, n=32)

    # ============================================================
    # Descenders — MUST weld to the box floor
    # ============================================================

    # Stroke 3: 撇 — long left-falling sweep from box's inner bottom-left
    # HEAD is welded to the box floor just inside the left wall.
    # TAIL exits well below and to the left.
    variant_pie(d,
                head=(-55, -5),        # welded to box floor near left wall
                tail=(-100, -120),     # deep down-left exit
                bow_perp=-8.0,         # outward bow (belly to the left)
                w_head=10.0, w_tail=1.5,
                n=52)

    # Stroke 4: 竖弯钩 — starts inside box near bottom-right, drops down,
    # curves right along the base, then hooks UP-and-slightly-left.
    # Inline as three phases:
    #   (a) tapered shaft from (+30, -5) down to (+30, -85)
    #   (b) quarter-arc curve from (+30, -85) sweeping right to (+80, -115)
    #   (c) hook up from (+80, -115) to (+70, -85) — points up-and-left,
    #       classic 竖弯钩 hook direction.

    # (a) shaft — slight taper (heavier at top, thinner as it curves)
    tapered_line(d,
                 (+40, -5),
                 (+40, -85),
                 w0=10.0, w1=9.0, n=32)

    # (b) curved base — quadratic bezier from shaft bottom, through control
    # point at bottom-right corner, to arc end. Keep width consistent.
    tapered_bezier(d,
                   p0=(+40, -85),
                   p1=(+70, -118),      # corner control point (down-right)
                   p2=(+95, -110),
                   w_head=9.0, w_tail=7.0, n=40)

    # (c) hook up-and-slightly-left — tapered flick, thicker at base,
    # thinning as it rises. Direction: from (+95, -110) up to (+82, -82).
    # In math coords tail.y > head.y ⇒ genuinely points UP (P1 compliant).
    tapered_line(d,
                 (+95, -110),
                 (+82, -82),
                 w0=8.0, w1=2.0, n=24)

    out_path = os.path.join(_HERE, "01_见.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    draw()

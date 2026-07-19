# p2_radical_083_丬 — G3 coord-format attempt.
#
# 丬 (3 strokes): a left-side "half" of 爿, three strokes total.
#   1) short 点/短撇 (upper-left, going down-left, slight arc)
#   2) short 提 (middle-left, rising to the right meeting the vertical)
#   3) long 竖 (right side spine, dominant vertical)
#
# Coord convention (P5): math coords, center origin, +y up.
# Canvas 300x300 -> center (150,150). All ox/oy below are math coords.
#
# TR8/TR9 INLINE-FRESH TEST:
#   - Stroke 3 (long right 竖): shape matches shu primitive after uniform
#     scale, role identical to standalone shu (straight, uniform width),
#     placement is a pure translation. -> USE draw_shu with (ox, oy, scale).
#   - Stroke 2 (short 提): shape matches ti primitive after scaling; it's
#     a rising stroke, role identical to standalone. -> USE draw_ti with
#     small scale and left offset.
#   - Stroke 1 (short upper 撇/点): only ~40px long, curved. draw_pie is
#     tuned as a long diagonal sweep, and draw_dian's dot is heavier at the
#     tail whereas here head-at-top is thicker than the tail. INLINE FRESH
#     as a short tapered curve.
#
# Placement (in PIL 300x300 pixel targets from GT visual):
#   Stroke 3 spine: top ~(195, 55), bottom ~(195, 275).
#     -> vertical center pixel (195, 165); length 220 px.
#     shu default: length 200 px, centered at (150,150).
#     Scale = 220/200 = 1.10; ox_math = 195-150 = +45; oy_math = 150-165 = -15.
#   Stroke 2 短提: head ~(75, 195), tip ~(150, 160).
#     ti default: head (-70,-70)*scale -> (80,220) pixel (scale=1);
#                 tip  (+80,+60)*scale -> (230, 90) pixel.
#     Choose scale=0.55: head-to-tip chord (75-80)=~5 wide, so
#       head at ox+(-70*0.55, -70*0.55) = ox+(-38.5, -38.5) math
#       tip at ox+(+80*0.55, +60*0.55) = ox+(+44, +33) math
#     Chord center math = ox+(2.75, -2.75).
#     Target chord center pixel = ((75+150)/2, (195+160)/2) = (112.5, 177.5)
#       -> math (112.5-150, 150-177.5) = (-37.5, -27.5)
#     So ox = -37.5 - 2.75 = -40.25; oy = -27.5 + 2.75 = -24.75
#     Round: ox=-40, oy=-25, scale=0.55.
#   Stroke 1 (upper-left short 撇): head ~(145, 80), tail ~(105, 145).
#     Inline fresh as tapered bezier: head thicker (~9 px), tail thinner (~2 px).
#     Slight left-bow control point.

from PIL import Image, ImageDraw
import os, sys

CANVAS_SIZE = 300

# import bank primitives
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)
from shu import draw_shu  # noqa: E402 (kept for reference; inline-fresh used below)
from ti import draw_ti    # noqa: E402 (kept for reference; inline-fresh used below)


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_upper_pie(t, ox=0.0, oy=0.0, scale=1.0):
    """Inline short 撇-like stroke: tapered curve from upper-right to lower-left.

    Head (thicker) at (+18, +33); tail (needle) at (-22, -32).
    Slight left-bow control point. Revision: lighter (GT is thin-line).
    """
    x0, y0 = 18.0 * scale, 33.0 * scale      # thick head
    x1, y1 = -22.0 * scale, -32.0 * scale    # thin tail
    mx = (x0 + x1) / 2.0 - 6.0 * scale       # bow slightly left
    my = (y0 + y1) / 2.0 - 2.0 * scale

    n_segments = 40
    thickness_head = 5.0 * scale
    thickness_tail = 2.0 * scale

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
        w = thickness_head * (1 - u) + thickness_tail * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_thin_shu_spine(t, top_pixel, bottom_pixel, width=5):
    """Inline thin vertical spine matching GT's line-thin aesthetic.

    GT's 丬 spine is a slim line, not the bank shu's 12-px block.
    """
    t.line([top_pixel, bottom_pixel], fill=(0, 0, 0), width=width)


def draw_thin_ti(t, head_pixel, tip_pixel, width_head=5, width_tip=1):
    """Inline thin 提 (rising stroke) using tapered bezier.

    GT's 丬 middle 提 is a slim rising line, not the bank ti's 16-px pressed head.
    """
    x0, y0 = head_pixel
    x1, y1 = tip_pixel
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0 - 4.0  # slight upward bow (pixel coords)

    n = 40
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = width_head * (1 - u) + width_tip * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 3: long right 竖 (spine). Inline thin per GT.
    # top (195, 55), bottom (195, 275). Width 5 px.
    draw_thin_shu_spine(t, (195, 55), (195, 275), width=5)

    # Stroke 2: short 提 middle-left. head thick at (75, 195), tip at (150, 160).
    # Thin (width_head=5, width_tip=1) to match GT.
    draw_thin_ti(t, head_pixel=(78, 195), tip_pixel=(150, 158),
                 width_head=5, width_tip=1)

    # Stroke 1: inline upper-left short 撇.
    # Center pixel target ~(125, 112). math (-25, +38). scale 1.0.
    draw_upper_pie(t, ox=-25, oy=38, scale=1.0)

    out_path = os.path.join(_HERE, "01_丬.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

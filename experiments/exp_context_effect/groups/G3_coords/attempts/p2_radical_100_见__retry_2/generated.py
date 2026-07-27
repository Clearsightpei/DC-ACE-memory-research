# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata p2_radical_100 (retry_1 SHIFTED): "box aspect still wrong,
#   interior proportions off". Original fix idea: "inline the box (like
#   ri.py but square), then hand-place the two descenders welding to
#   bottom." Additionally B4 P12 lesson: this GT is MMH thin ink (~3-4px),
#   NOT calligraphic ~8-10px. Retry_1 used BOX_INK=8 — too heavy.
#   New fix: (a) thin uniform ink ~4px per P12; (b) more-square box
#   with proper aspect (~85 wide x 100 tall, upper 55% of canvas);
#   (c) descenders START from the bottom-inside corners of the box
#   (welded) and both extend well below; (d) the 撇 sweeps down-left
#   with a shallow bow; (e) 竖弯钩 shaft drops straight then curves
#   right along a base then hooks UP.
#
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   Box family: ri.py / kou.py aspects. For 见 the box is roughly
#   square, more like kou but with tall aspect closer to 目. Descenders
#   are 撇 + 竖弯钩 pair (er_ren-like). Char version p3_char_0114_见
#   used bank composition (shu + heng_zhe + er_ren) and drew a
#   recognisable 见 — but box was very small and descenders too long.
#   Radical version needs a larger box occupying the upper half and
#   descenders that are shorter/tighter and welded to the box floor.
#
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing → NO
#   - Mirror-dot pair → NO
#   - Per-stroke form (angle/taper/bow) → YES for the 撇: variant_pie
#   - Uniform thin lines (MMH GT) → YES per P12; use tapered_line with
#     w0=w1=4 for the box walls (uniform thin ink). This is the
#     critical fix vs retry_1.
#   Will import: tapered_line, tapered_bezier, variant_pie, to_px.
#   Rendering approach: fully inline (per errata fix idea; not force-
#   fit kou/heng_zhe primitives which caused retry_0 box aspect fail).

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
    # Box parameters — P12 compliance: THIN ink (~4 px) not calligraphic.
    # Roughly square box in the upper half of canvas.
    # Coords are math (center origin, +y up); to_px converts.
    # ============================================================
    # REVISION 1: box slightly larger + descenders longer/wider to
    # match GT (which shows a longer 竖弯钩 sweep + more visible hook).
    BOX_LEFT   = -50
    BOX_RIGHT  = +50
    BOX_TOP    = +100
    BOX_BOTTOM = +10
    BOX_INK    = 4     # THIN uniform ink per P12

    # Stroke 1: 竖 — left wall of the box (top to bottom).
    tapered_line(d,
                 (BOX_LEFT, BOX_TOP),
                 (BOX_LEFT, BOX_BOTTOM),
                 w0=BOX_INK, w1=BOX_INK, n=36)

    # Stroke 2: 横折 — top bar then right wall (single continuous stroke).
    # Top bar.
    tapered_line(d,
                 (BOX_LEFT, BOX_TOP),
                 (BOX_RIGHT, BOX_TOP),
                 w0=BOX_INK, w1=BOX_INK, n=36)
    # Small subtle 顿笔 corner (kept small to not dominate at thin ink).
    cx, cy = to_px(BOX_RIGHT, BOX_TOP)
    r = 3
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # Right wall.
    tapered_line(d,
                 (BOX_RIGHT, BOX_TOP),
                 (BOX_RIGHT, BOX_BOTTOM),
                 w0=BOX_INK, w1=BOX_INK, n=36)

    # ============================================================
    # Descenders — welded to the box floor at the INSIDE corners.
    # These are the two 儿-like legs.
    # ============================================================

    # Stroke 3: 撇 — starts at box's inner bottom-left (~BOX_LEFT, BOX_BOTTOM)
    # and sweeps down-left, exiting near lower-left of canvas.
    # Thin at head, tapering thinner at tail (classic 撇 taper).
    variant_pie(d,
                head=(BOX_LEFT + 3, BOX_BOTTOM + 2),  # welded just inside floor
                tail=(-105, -115),                    # deeper down-left exit
                bow_perp=-9.0,                        # more pronounced outward bow
                w_head=5.0, w_tail=1.5,
                n=52)

    # Stroke 4: 竖弯钩 — starts inside box near bottom-right, drops
    # straight, curves right along a base, then hooks UP.
    # Inline three phases:
    #   (a) vertical shaft from just inside box bottom-right down
    #   (b) quarter-arc curve right to arc end
    #   (c) hook up (P1: hook_tip.y > hook_base.y in math coords)

    # (a) shaft — thin uniform to match box weight. Longer shaft.
    tapered_line(d,
                 (BOX_RIGHT - 6, BOX_BOTTOM + 2),
                 (BOX_RIGHT - 6, -90),
                 w0=5.0, w1=4.5, n=36)

    # (b) curved base — bezier sweeping right further and lower.
    tapered_bezier(d,
                   p0=(BOX_RIGHT - 6, -90),
                   p1=(BOX_RIGHT + 20, -125),    # corner control
                   p2=(BOX_RIGHT + 55, -120),    # arc end (rightmost)
                   w_head=4.5, w_tail=4.0, n=40)

    # (c) hook up — tapered flick, base at arc end, tip up-and-slightly-
    # left. In math coords tail.y > head.y ⇒ genuinely UP (P1 compliant).
    tapered_line(d,
                 (BOX_RIGHT + 55, -120),
                 (BOX_RIGHT + 42, -85),
                 w0=4.5, w1=1.5, n=24)

    out_path = os.path.join(_HERE, "01_见.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    draw()

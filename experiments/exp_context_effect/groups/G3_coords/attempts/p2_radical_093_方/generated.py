"""方 (fāng) — p2_radical_093 — 4 strokes.

Composition analysis (from GT PNG):
  Stroke 1: 点 — small slanted dot near top-center (slightly right of center).
  Stroke 2: 横 — long horizontal below the dot, spanning most of canvas width.
  Stroke 3: 横折钩 (feels like an inlined 横折弯钩 in 方's shape) — starts at
            right end of the 横 (or slightly to the right of it), descends
            with a slight leftward bow, and terminates in a short up-and-left
            hook. It forms the right frame + hook of 方's enclosed lower box.
  Stroke 4: 撇 — from the left portion of the 横 (near center), sweeps
            down-left, tapering to a fine tail. Forms the left frame.

Bank use decisions (per TR1-TR9 in principle_bank.md):
  - draw_dian: PRIMITIVE FITS. Stroke 1 is a canonical 点 (thin head,
    heavier rounded tail) — just needs (ox, oy, scale) to place it near
    top of canvas. Bank primitive is TR8-compliant use.
  - draw_heng: PRIMITIVE FITS. Stroke 2 is a plain uniform horizontal.
    Bank primitive suits — set scale to fit 方's horizontal.
  - draw_heng_zhe_gou: INLINE-FRESH instead. Per TR8, this primitive was
    tuned for STANDALONE 横折钩 with sharp right-angle corner. 方's stroke 3
    is subtly different: the vertical portion bows LEFTWARD (curved, not
    straight), and the terminal hook is short. Force-fitting the primitive
    at compressed scale flattened this in past B1 fails. Inline as a
    tapered bezier that starts at the 横's right end, curves down with
    leftward bow, ends in an explicit tapered hook segment.
  - draw_pie: INLINE-FRESH instead. Per TR8/TR9 + sandbox B1 diagnosis
    (see 大/彳/巛/etc. fails), the pie primitive's default diagonal chord
    doesn't match 方's stroke-4: which needs a shorter, more vertical
    sweep starting mid-heng, ending at lower-left. Inline a fresh bezier.

Canvas: 300x300 white, black ink. Math coords, +y up, center origin.
"""

import os
import sys

from PIL import Image, ImageDraw

# Make bank primitives importable BEFORE the from-imports.
_BANK_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "success_bank", "code",
    )
)
if _BANK_DIR not in sys.path:
    sys.path.insert(0, _BANK_DIR)

# Bank primitives (deliberate placements per TR1)
from heng import draw_heng  # noqa: E402
from dian import draw_dian  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _tapered_bezier(draw, p0, p1, p2, w0, w1, n=60):
    """Quadratic bezier tapered from w0 to w1, in math coords.
    p0=start, p1=control, p2=end. Widths linear along u."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        px, py = _to_pixel(bx, by)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_line(draw, p0, p1, w0, w1, n=24):
    """Straight tapered segment from p0 to p1 (math coords)."""
    x0, y0 = p0
    x1, y1 = p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        px, py = _to_pixel(x, y)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 点 (top dot)
    # dian's canonical unit spans ~40 px, thick tail at lower-right.
    # For 方 the top dot sits slightly right of center, near canvas top.
    # Target center approx math (5, +100). dian default center is (0,0).
    # ox=+5, oy=+100, scale=0.55 puts a small dot near top.
    draw_dian(d, ox=+5, oy=+100, scale=0.55)

    # ---- Stroke 2: 横 (long horizontal below the dot)
    # heng canonical is 200 px long, centered. For 方 the horizontal spans
    # most of the width but sits slightly above center. Length ~180 px.
    # ox=+5 (nudge right to match GT slight asymmetry), oy=+55, scale=0.90
    draw_heng(d, ox=+5, oy=+55, scale=0.90)

    # ---- Stroke 3: 横折钩 (right frame + hook) — INLINE-FRESH per TR8
    # Starts at the RIGHT end of the horizontal (math ~(+95, +55)),
    # brief small horizontal head (already there via heng — the "折" corner
    # is where the vertical begins), then curves DOWN with a slight
    # LEFTWARD bow, ending in a short up-and-left hook (per P1, P9).
    #
    # Geometry:
    #   corner_top   at (+95, +55)   — sits on top of heng's right end
    #   shaft_bottom at (+55, -95)   — the vertical bows LEFT (from +95 to +55)
    #   hook_tip     at (+30, -70)   — flick UP-LEFT from shaft base (P1)
    #
    # Use a quadratic bezier for the shaft (curve, not straight) with
    # a control point pulled slightly LEFT of the chord to bow.
    corner_top = (95.0, 55.0)
    shaft_ctrl = (95.0, -20.0)   # keep close to vertical near top, curve down-left
    shaft_bot = (55.0, -95.0)
    _tapered_bezier(d, corner_top, shaft_ctrl, shaft_bot, w0=12, w1=10, n=48)

    # Small corner "顿笔" blob at the top-right corner where 横 meets shaft
    cx, cy = _to_pixel(*corner_top)
    r = 6
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # Hook: tapered flick from shaft bottom UP-and-LEFT (P1, P9)
    hook_base = shaft_bot
    hook_tip = (30.0, -70.0)  # UP (y higher) and LEFT (x smaller)
    _tapered_line(d, hook_base, hook_tip, w0=10, w1=2, n=18)

    # ---- Stroke 4: 撇 (left-falling sweep from left-mid of 横) — INLINE-FRESH per TR8
    # Revision: on first pass I placed pie head at (-5, +55) — too far right
    # (center of heng). GT shows pie head starting from LEFT PORTION of the
    # horizontal (roughly 1/4 to 1/3 from left end), then sweeping down and
    # to the lower-left with pronounced curve. Move head to (-35, +55) and
    # extend tail farther for stronger sweep, with stronger left-bow control.
    pie_head = (-35.0, 55.0)
    pie_ctrl = (-55.0, -20.0)  # pull left of chord midpoint to bow
    pie_tail = (-85.0, -95.0)
    _tapered_bezier(d, pie_head, pie_ctrl, pie_tail, w0=11, w1=1, n=60)

    out = "01_方.png"
    img.save(out)
    print(f"saved {out}")


if __name__ == "__main__":
    main()

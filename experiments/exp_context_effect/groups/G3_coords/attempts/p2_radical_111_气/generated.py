"""气 (qì) — 4-stroke radical.

Decomposition (from GT observation):
  1. 撇 (pie) at the top-left: starts high (upper area, slightly right
     of center), sweeps down-left ending near mid-height on the left.
     Fairly straight with a shallow bow.
  2. 横 (short, upper): a shorter horizontal near the top, sitting to
     the right of the pie's head. Slightly rising to the right.
  3. 横 (medium, middle): a horizontal below stroke 2, on the right
     side, roughly in the middle of the canvas.
  4. 横斜钩 (heng-xie-gou): a distinctive compound stroke starting at
     the left below the previous hengs. Runs right briefly, then sweeps
     DOWN AND RIGHT diagonally with a smooth curve, ending with a small
     upward-flicking hook at the bottom-right.

INLINE-FRESH decisions (TR8/TR9):
- Stroke 1 (撇): the bank's `draw_pie` primitive is tuned as a wide
  diagonal sweep from upper-right to lower-left. 气's pie is shorter
  and starts more centrally, tilted more vertically. Using bank pie
  at extreme scale would flatten it (TR8 category A failure). INLINE
  as a fresh tapered bezier tuned to this composition.
- Strokes 2, 3 (横): plain short horizontals — draw_heng primitive is a
  pure horizontal, easy pure-translation reuse. USE BANK (TR8 pass).
- Stroke 4 (横斜钩): NO primitive matches this compound. Bank has
  heng_xie_gou-family but they were tuned for other radicals. Also
  TR8: this is a distinctive compound curl and force-fitting a bank
  compound at compressed scale would flatten the hook (B1 failure
  mode 飞). INLINE as ONE tapered polyline: short flat opening, then
  smooth diagonal sweep down-right, terminating in a small up-flicking
  hook (P9: hook belongs on the shaft, not the corner).
"""

import sys
from pathlib import Path
import math

from PIL import Image, ImageDraw

# Import G3 bank primitives from the group's success_bank
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from heng import draw_heng  # noqa: E402


CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _tapered_bezier(t, p0, pc, p1, w_head, w_tail, n=50):
    """Draw a quadratic bezier from p0->p1 through control pc with a
    linearly-tapering width from w_head to w_tail. Points in math coords."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_qi_radical(t):
    # --- Stroke 1: 撇 (pie) top-left ---
    # Inline-fresh (TR8). Head at (-15, +85), tail at (-75, -10).
    # Longer, extending further down-left. Slight bow to the left.
    # GT shows a tiny curl/顿笔 at the top of the pie head — add a small
    # starting blob to mimic 起笔.
    p0 = (-15, 85)
    p1 = (-78, -12)
    pc = ((p0[0] + p1[0]) / 2 - 8, (p0[1] + p1[1]) / 2 - 2)
    _tapered_bezier(t, p0, pc, p1, w_head=9, w_tail=1, n=60)
    # 起笔 blob at head — small filled circle
    hx, hy = _to_pixel(-15, 85)
    r = 4
    t.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))

    # --- Stroke 2: upper 横 (short) ---
    # Center around (+30, +60). Length ~90 px → scale = 0.45.
    draw_heng(t, ox=30, oy=60, scale=0.45)

    # --- Stroke 3: middle 横 (medium) ---
    # Center around (+25, +20). Length ~110 px → scale = 0.55.
    draw_heng(t, ox=25, oy=20, scale=0.55)

    # --- Stroke 4: 横斜钩 (inline as tapered polyline) ---
    # GT observation: this stroke is a distinct compound with LONG
    # descending tail. It starts at left as a short flat opening, then
    # sweeps down-right with strong curvature (increasingly vertical),
    # ending deep at the bottom of the canvas with a clear upward hook.
    #
    # Structure:
    #   A. Short flat opening from (-80, -30) to (-40, -30).
    #   B. Long curved sweep from (-40, -30) through control point
    #      (+30, -55) — pulled to make the top part more horizontal —
    #      to end at (+60, -130). The end is near-vertical.
    #   C. Prominent hook flicking UP-AND-LEFT from (+60, -130)
    #      to (+45, -108). Longer and thicker than before (P1, P9).
    ink_w = 7

    # A. flat opening — short heng segment
    ax0, ay0 = _to_pixel(-82, -30)
    ax1, ay1 = _to_pixel(-40, -30)
    t.line([(ax0, ay0), (ax1, ay1)], fill=(0, 0, 0), width=ink_w)

    # B. long curved sweep via tapered bezier
    b0 = (-40, -30)
    b1 = (60, -130)
    bc = (30, -55)  # control point pulled to bend sweep: flatter at start,
                    # then more vertical toward the end
    _tapered_bezier(t, b0, bc, b1, w_head=ink_w, w_tail=7, n=70)

    # 顿笔 blob at the elbow (A→B junction) to hide the miter (P6)
    ex, ey = _to_pixel(-40, -30)
    r = 4
    t.ellipse([ex - r, ey - r, ex + r, ey + r], fill=(0, 0, 0))

    # C. hook — tapered stroke flicking UP-AND-LEFT from stroke end.
    # Made longer + thicker than v1 for clear visibility (GT hook is
    # prominent).
    hx0, hy0 = _to_pixel(60, -130)
    hx1, hy1 = _to_pixel(42, -105)
    steps = 12
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        px0 = hx0 + (hx1 - hx0) * u0
        py0 = hy0 + (hy1 - hy0) * u0
        px1 = hx0 + (hx1 - hx0) * u1
        py1 = hy0 + (hy1 - hy0) * u1
        w = max(1, int(round(8 * (1 - u0) + 2 * u0)))
        t.line([(px0, py0), (px1, py1)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_qi_radical(t)
    out = Path(__file__).parent / "01_气.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

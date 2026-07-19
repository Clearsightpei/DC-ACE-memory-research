# p2_radical_044_辶 (chuo) — G3 coord-format render.
#
# Composition (per TR6, deliberate placement):
#   Stroke 1: 点 (top-left dot)                           — reuse dian primitive
#   Stroke 2: 横折折撇 (small zig-zag under the dot)      — INLINE (bank primitive is too big
#              for the compact radical form; scale would drop <0.4, hitting TR5).
#   Stroke 3: 平捺 (long flat rightward sweep at bottom)  — INLINE (na primitive is a
#              diagonal sweep starting upper-left; 平捺 is nearly horizontal with
#              a low-belly curve. Structurally different, TR5 says inline.)
#
# GT observations (300x300):
#   - dian sits around (100, 60) in PIL coords (upper-left area).
#   - zig-zag sits around (75, 130)-(115, 195) — small, roughly under dot.
#   - flat 捺 spans from about (75, 210) rightward to (245, 250), belly dips a bit.
#
# Math coords (center origin, +y up): PIL (x, y) = (150 + mx, 150 - my).
# So PIL 100 -> mx=-50; PIL 60 -> my=90 etc.

from PIL import Image, ImageDraw
import os
import sys

# Make the G3 success_bank/code available for primitive imports (dian).
_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_bezier(t, x0, y0, mx, my, x1, y1, w_head, w_tail,
                    n=40, belly=None, w_belly=None):
    """Draw a quadratic bezier with a width profile.

    If belly + w_belly given, width goes head->belly->tail (piecewise).
    Otherwise linear head->tail.
    """
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        if belly is not None and w_belly is not None:
            if u <= belly:
                w = w_head + (w_belly - w_head) * (u / belly)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly) / (1 - belly))
        else:
            w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_segment(t, x0, y0, x1, y1, w0, w1, n=20):
    """Straight tapered segment."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel(bx, by)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_chuo(t):
    # --- Stroke 1: 点 (top-left dot) ---
    # GT dot around PIL (100, 60) -> math (mx=-50, my=+90). Reuse dian primitive.
    # dian's "canonical center" is roughly (0, 0) in its local math coords.
    # Place dian at (ox=-50, oy=+90), scale=0.7 (slightly smaller — this dot in
    # 辶 is smaller than the standalone 点 stroke; TR2 not strictly a radical
    # slot but similar shrink).
    from dian import draw_dian
    draw_dian(t, ox=-50, oy=90, scale=0.7)

    # --- Stroke 2: 横折折撇 (compact S/2-shape wiggle) ---
    # Revised: GT reads as a rounded "2"-like curl, not a sharp N.
    # Segments composed as three linked beziers with rounded corners:
    #   (a) Small 横 tilting slightly down-right at top: A -> B.
    #   (b) 折 curling down-and-left (rounded corner): B -> C via bezier.
    #   (c) 撇 sweeping down-right from C to D via bezier.
    # Math coords (PIL x = 150+mx, PIL y = 150 - my).
    # GT the wiggle sits roughly under the dot, spanning ~PIL(70..115, 130..200).
    A = (-80.0, 20.0)    # PIL (70, 130) — start of small 横
    B = (-40.0, 15.0)    # PIL (110, 135) — top-right shoulder
    C = (-75.0, -20.0)   # PIL (75, 170) — bottom-left of the fold
    D = (-40.0, -55.0)   # PIL (110, 205) — 撇 tail bottom-right
    # (a) small tilted 横 A -> B
    _tapered_segment(t, A[0], A[1], B[0], B[1], 5, 6, n=18)
    # (b) rounded 折 B -> C — control point pulled right-ish so it bulges
    #     outward like the top curl of a "2".
    _tapered_bezier(t,
                    B[0], B[1],
                    B[0] + 5, (B[1] + C[1]) / 2 + 4,   # right-of-chord bulge
                    C[0], C[1],
                    6, 7, n=30)
    # (c) 撇 C -> D — smooth downward-right sweep with a shallow leftward
    #     belly so it echoes the "tail" of the 2.
    _tapered_bezier(t,
                    C[0], C[1],
                    (C[0] + D[0]) / 2 - 6, (C[1] + D[1]) / 2 - 2,
                    D[0], D[1],
                    7, 3, n=30)

    # --- Stroke 3: 平捺 (long thin rightward sweep) ---
    # Revised: GT is thinner and longer than the first attempt. Extend
    # left-start further left, right-end further right, drop the max belly
    # width so the sweep reads slim like a boat's underside.
    #  Start head ~ PIL (55, 205) -> math (-95, -55).
    #  End tail  ~ PIL (255, 250) -> math (105, -100).
    x0, y0 = -95.0, -55.0
    x1, y1 = 105.0, -100.0
    # Belly control point sits slightly below chord for gentle downward bow.
    mx = (x0 + x1) / 2.0 + 5
    my = (y0 + y1) / 2.0 - 12
    _tapered_bezier(t,
                    x0, y0, mx, my, x1, y1,
                    w_head=3, w_tail=2,
                    n=70, belly=0.6, w_belly=10)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_chuo(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_辶.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

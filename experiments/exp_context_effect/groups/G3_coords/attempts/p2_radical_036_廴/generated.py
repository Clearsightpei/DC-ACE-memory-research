# p2_radical_036_廴 (yǐn) — 2-stroke radical: 横折折撇 + 平捺.
#
# Decomposition per GT:
#   Stroke 1: a small z/S shape in the upper-left area (横折折撇 style).
#     A short 横 to the right, then a hook down-left, then another
#     small horizontal segment. In practice the primitive
#     heng_zhe_zhe_pie captures this exact 4-segment idiom.
#   Stroke 2: a 平捺 (flat/horizontal 捺) — starts at the tail end of
#     stroke 1's pie, dips slightly down, then sweeps far right with
#     a long flat swelling foot. This is NOT the standalone 捺
#     (which is steep down-right); it is nearly horizontal, so we
#     INLINE it fresh rather than call draw_na (TR5 — 捺's default
#     is a steep sweep; using it would give the wrong slope).
#
# Placement (300x300 canvas, math coords center-origin +y-up):
#   Stroke 1 (heng_zhe_zhe_pie) — occupies upper-left quadrant.
#     Primitive default extends roughly x in [-80, +55], y in [+80, -90]
#     (i.e. -170 wide, +170 tall in math). We scale it DOWN to ~0.45
#     so the S sits in the upper-left ~third of the canvas, and offset
#     so its pie tail ends near (-40, -10) in math coords.
#     After scale=0.45 the pie tail lands at approximately
#     ox + (-75)*0.45 = ox - 33.75, oy + (-90)*0.45 = oy - 40.5.
#     Target tail (-40, -10) → ox = -40 + 33.75 = -6.25 ≈ -6,
#                                oy = -10 + 40.5 = +30.5 ≈ +30.
#     So call draw_heng_zhe_zhe_pie(t, ox=-25, oy=+40, scale=0.45)
#     — tune ox left by ~-19 so the top S sits toward left edge.
#     Empirical shift: ox=-25, oy=+40, scale=0.45.
#   Stroke 2 (平捺, inlined) — starts near stroke 1's pie tail
#     (~ -55, -25), dips slightly through belly at (+10, -50),
#     sweeps out to (+115, -30) with a long flat foot.

from PIL import Image, ImageDraw
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                 "success_bank", "code"))

from heng_zhe_zhe_pie import draw_heng_zhe_zhe_pie

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _bezier_taper(t, p0_math, p1_math, ctrl_math, w0, w_belly, w_tail,
                  belly_u=0.7, steps=100):
    """Quadratic bezier with thin head → belly → tapered foot (捺 profile)."""
    p0 = _to_pixel(*p0_math)
    p1 = _to_pixel(*p1_math)
    ctrl = _to_pixel(*ctrl_math)
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        if u <= belly_u:
            w = w0 + (w_belly - w0) * (u / belly_u)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - belly_u) / (1 - belly_u))
        r = max(0.5, w / 2.0)
        t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # ---- Stroke 1: 横折折撇 (z-shape in upper area).
    # First render was too small/centered; enlarge and shift left+up.
    # scale=0.55 → primitive spans ~74 px (heng) + ~28 (折) + ~72 (pie).
    # ox=-40 puts left edge near canvas left third; oy=+45 raises to
    # upper third; the pie tail lands near (-40 + 55*0.55, 45 + 10*0.55)
    # ≈ (-10, +50) for the S's mid, and pie sweeps to
    # (-40 + -75*0.55, 45 + -90*0.55) ≈ (-81, -5). That gives room for
    # the 平捺 to start left and sweep right.
    draw_heng_zhe_zhe_pie(t, ox=-40, oy=+45, scale=0.55)

    # ---- Stroke 2: 平捺 (flat 捺, inlined — na primitive is too steep).
    # Head lands near pie tail region ~(-70, -25); dips only slightly
    # through belly at (+15, -45); tail continues nearly flat to
    # (+115, -35). Ctrl point set closer to the chord to keep it flat.
    # Width profile: thin head (2) → thick belly (18) → tapered tail (2).
    _bezier_taper(
        t,
        p0_math=(-75, -20),
        p1_math=(+118, -35),
        ctrl_math=(+25, -55),  # only slightly below chord midpoint
        w0=2.0,
        w_belly=18.0,
        w_tail=2.0,
        belly_u=0.72,
        steps=120,
    )

    out_path = os.path.join(os.path.dirname(__file__), "01_廴.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()

# p2_radical_060_宀 — 宀 (baogaitou, "roof radical"), 3 strokes.
#
# Structural decomposition (from GT viewing):
#   S1. 点 (dian)   — small dot at top-center, slightly right of the vertical
#                     axis. This is the "chimney" tip of the roof.
#   S2. 竖 (shu) short — a short vertical/point on the LEFT end of the roof
#                     body, descending from where the horizontal begins.
#                     Looks in GT like a short slanted stroke.
#   S3. 横钩 (heng_gou) — the roof itself: a long horizontal spanning most
#                     of the canvas width, ending with a downward hook on the
#                     right. This is the wide "cap".
#
# Placement (300x300, PIL top-left origin):
#   - The roof is a TOP RADICAL, so per TR2 it sits in the upper 60% of the
#     canvas, wider than tall.
#   - 点 tip at approximately (150, 90).
#   - Roof horizontal from (~55, 130) to (~245, 130) with hook down to
#     (~230, 165). This matches the bank's heng_gou default range but pulled
#     upward (oy = -30 px to shift the whole heng_gou up).
#   - Short left 竖 vertical from (~62, 135) down to (~72, 175). Just a short
#     slanted line — will inline rather than call draw_shu (per TR5: scale
#     would be < 0.4 of the bank's 200px canonical shu).
#
# Bank primitive calls (per TR1/TR6 — deliberate placement):
#   - draw_dian (bank): default endpoints span math-coords (-15,+25) to
#     (+18,-20). Its center-of-mass in math coords is about (0, 0). To place
#     the tip at PIL (150, 90) → math (0, +60), pass ox=0, oy=+60, scale=0.55
#     (shrink so it reads as small chimney dot).
#   - draw_henggou (bank): uses raw PIL coords, horizontal at y≈120→130, hook
#     tail at (~x1-20, y1+38). Default span x0=55, y0=120 to x1=245, y1=130.
#     Move up ~10 px (oy=-10) so the roof line lands at y=~120, and stretch
#     via scale=1.0 (default width already fits 300 canvas nicely).
#     Actually: prefer oy=0 keeping y=120-130 which is where the GT roof is.
#
# Left short 竖: inline (TR5 — too small to reuse shu). Draw a short slanted
# line from (60, 135) to (72, 175). Tapered, thick head → thinner tail.

from PIL import Image, ImageDraw
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from dian import draw_dian
from heng_gou import draw_henggou


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)

    # --- S3 first (background layer): 横钩 as the roof cap ---
    # heng_gou uses raw PIL coords. Its natural span is x=55..245, y≈120..130,
    # with hook ending at (~225, ~168). This lands the roof in the upper half
    # of the canvas — perfect for a top radical. Use ox=0, oy=0, scale=1.0.
    # (TR6: default (0,0,1.0) IS a deliberate choice here because the
    # primitive's coord range already matches the target position.)
    draw_henggou(t, ox=0, oy=0, scale=1.0)

    # --- S1: 点 chimney tip at top-center ---
    # dian uses math coords. To place the tail at PIL (~152, ~90) → math
    # (+2, +60). dian's tail is at (+18, -20) in local math coords; pass
    # ox=-16, oy=+80 with scale=0.55 to shrink and land tip near (150, 92).
    # Rationally: dian default local range (-15,+25) to (+18,-20). Scaled 0.55
    # gives (-8,+14) to (+10,-11). Add ox=-8, oy=+95 → head at PIL
    # (150-8+(-8), 150-(95+14)) = (134, 41), tail at (150-8+10, 150-(95-11))
    # = (152, 66). Hmm, this puts it above the roof by ~55 px, which reads
    # as chimney. Actually GT shows chimney closer to roof — let's target
    # head at (135, 75) tail at (152, 100). That's math head (-15, +75), tail
    # (+2, +50). Local (unscaled) head (-15,+25) tail (+18,-20). Need scale
    # matching Δx=17→17 (scale=1.0? no, then dot too big). Try scale=0.6:
    # local head (-9,+15) tail (+11,-12). Pass ox=-6, oy=+60 → head at math
    # (-15,+75) = PIL (135, 75), tail at math (+5,+48) = PIL (155, 102).
    # Good — chimney tip touches roof at ~ (155, 102) which is just above
    # roof line at y=120.
    draw_dian(t, ox=-10, oy=+55, scale=0.5)

    # --- S2: left short 竖/点 (inlined, TR5: too small for bank shu) ---
    # In GT this reads as a short down-left slanted point (more 点-ish than
    # 竖). From PIL (68, 135) to (58, 175). Tapered: thin head → thicker tail
    # (opposite of a typical 竖), because it functions more like a 点 in this
    # radical.
    steps = 24
    x_head, y_head = 68, 135
    x_tail, y_tail = 58, 175
    w_head, w_tail = 5, 9
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x_head + (x_tail - x_head) * u0
        ya = y_head + (y_tail - y_head) * u0
        xb = x_head + (x_tail - x_head) * u1
        yb = y_head + (y_tail - y_head) * u1
        w = max(1, int(round(w_head + (w_tail - w_head) * u0)))
        t.line([(xa, ya), (xb, yb)], fill="black", width=w)

    out = os.path.join(HERE, "01_宀.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

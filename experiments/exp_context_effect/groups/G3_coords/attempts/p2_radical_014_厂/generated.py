# 厂 (chang) — 2-stroke radical: 一 (top heng) + 丿 (long left-falling pie).
#
# TR-compliant reuse plan (from principle_bank TR1–TR7):
#   Stroke 1 (heng): scale ~0.75 (radical horizontal ~150 px wide — GT shows
#     the top-heng spanning most of upper-right canvas). Placed high, right of
#     center so its left end welds to the top of the 撇. Target center (math
#     coords): (+35, +60). Standalone center is (0, 0), so ox=+35, oy=+60,
#     scale=0.75.
#   Stroke 2 (pie): inline a softer, longer, less-diagonal 丿 (per P10 —
#     bank's pie is too diagonal for radical 丿). Head shares pixel with the
#     LEFT end of heng, then a shallow-at-top / steeper-toward-bottom curl
#     down-left ending near lower-left. Head at (~-30, +60), tail at (~-70, -100).
#
# Weld math for heng LEFT end (math coords):
#   heng half_len = 100 * scale = 100 * 0.75 = 75
#   left end = center - (half_len, 0) = (+35 - 75, +60) = (-40, +60)
#   Pie head placed at (-40, +60) → welded.

from PIL import Image, ImageDraw
import os, sys

REPO = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect"
sys.path.insert(0, os.path.join(REPO, "groups/G3_coords/success_bank/code"))

from heng import draw_heng

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_radical_pie(t, x0, y0, x1, y1):
    """Inlined 丿 for radical: gentle scoop from (x0,y0) to (x1,y1).
    Head thick (~11 px), tail needle (~1 px). Control point pulled to make
    the top nearly horizontal then curling down-left toward the tail.
    """
    # Bezier control point: pull hard toward upper-left of chord so the top
    # is shallow and the bottom steepens (that's the 丿 curl).
    mx = x0 - 40.0   # left of head
    my = y0 - 10.0   # slightly below head
    # (This yields shallow start, then bending down.)

    n = 80
    w_head = 11.0
    w_tail = 1.0
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 1: heng, radical-width (0.75 * standalone), placed high & right
    # ox=+35 → center at math x=+35; oy=+60 → high on canvas
    draw_heng(t, ox=+35, oy=+60, scale=0.75)

    # Stroke 2: inlined 丿 radical.
    # Head at heng's left end (-40, +60); tail lower-left (-75, -105).
    draw_radical_pie(t, x0=-40, y0=+60, x1=-75, y1=-105)

    out = os.path.join(
        REPO, "groups/G3_coords/attempts/p2_radical_014_厂/01_厂.png"
    )
    img.save(out)
    print("saved:", out)


if __name__ == "__main__":
    main()

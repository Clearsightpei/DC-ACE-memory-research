# p2_radical_079_弋 — 弋 (yi, "arrow tie / dart") 3-stroke radical
#
# GT analysis (viewed from /gt/phase2/弋.png):
#   - Stroke 1: 横 (heng) — short horizontal, positioned slightly below
#     center, spanning left-of-center to just past center-right.
#   - Stroke 2: 斜钩 (xie gou) — starts upper-left (above the heng's
#     left end), sweeps diagonally down-and-right (with a rightward
#     belly bulge in the lower half), ends at lower-right where a
#     short hook flicks UP-AND-slightly-LEFT (P1).
#   - Stroke 3: 点 (dian) — small dot in the upper-right area, above
#     where the 斜钩 crosses the 横 line's y-level.
#
# Bank check (per TR1, TR8 INLINE-FRESH TEST, and TR9):
#   - No 斜钩 primitive exists in the bank (斜钩 remains in errata since
#     Phase-1 batch-1). So the main stroke MUST be inlined fresh.
#   - Bank has `heng.py` (a clean 200x12 straight tapered-uniform line);
#     for 弋's short cross-bar it fits with scale ~0.55–0.60 (TR2:
#     internal element of a small radical). Use draw_heng.
#   - Bank has `dian.py` — the canonical 点 primitive. Fits the small
#     upper-right dot with scale ~0.45. Use draw_dian.
#
# Coord convention (P5): math coords, center origin, +y up. Canvas 300.
#
# Stroke geometry (math coords):
#   heng: center at (ox=-5, oy=-5), scale=0.55  (half_len 55, thickness 7)
#         → spans roughly x=[-60, +50] at y=-5.
#   xie_gou body: bezier from head (-30, +65) down-right to tail
#         (+55, -90). Control point pulled to the RIGHT of chord midpoint
#         to create the characteristic outward belly bulge on the right
#         (斜钩's rightward arc — see errata's failed-斜钩 diagnosis,
#         attempt lost the belly).
#         Width: 6 → 10 (belly, u=0.6) → 4 (tail before hook).
#   xie_gou hook: short flick from tail (+55, -90) up-and-slightly-left
#         to (+47, -75). Tapered 8 → 2.
#   dian: bank primitive with ox=+55, oy=+55, scale=0.45.

from PIL import Image, ImageDraw
import sys, os

# Bank primitive imports (per TR6, deliberate transforms below)
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
from heng import draw_heng  # noqa: E402
from dian import draw_dian  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) → PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_xie_gou_inline(t, ox=0.0, oy=0.0):
    """Inline-fresh 斜钩 for 弋 (per TR5/TR8): the bank has no 斜钩,
    and force-fitting shu_wan_gou would flatten the diagonal.

    Recipe: tapered-bezier body from upper-left head to lower-right
    tail with a rightward belly, then a short tapered flick UP-LEFT
    for the hook (per P1 hook direction rules and P9 shaft-hook weld).
    """
    # Body endpoints (math coords) relative to (ox, oy)
    x0, y0 = -35.0 + ox, 70.0 + oy       # upper-left head
    x1, y1 =  55.0 + ox, -90.0 + oy      # lower-right tail (hook base)
    # Control point: chord midpoint is (10, -10). Push STRONGLY RIGHT
    # and slightly DOWN to bulge the arc outward on the right side
    # (revision 1: pushed from +22 to +40 for a much more pronounced
    # belly matching GT's outward-bowing arc — 斜钩 errata note said
    # "distinct rightward BULGE" is the pass criterion).
    cx = (x0 + x1) / 2.0 + 40.0
    cy = (y0 + y1) / 2.0 - 10.0

    n = 60
    w_head, w_belly, w_tail = 6.0, 10.0, 4.0
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        # Width profile: rises from head → belly (u=0.6) → tapers to tail
        if u <= 0.6:
            w = w_head + (w_belly - w_head) * (u / 0.6)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - 0.6) / 0.4)
        w_int = max(1, int(round(w)))
        px, py = _to_pixel(bx, by)
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)

    # 顿笔 blob at tail (small anchor before hook) — P6
    tx, ty = _to_pixel(x1, y1)
    t.ellipse([tx - 4, ty - 4, tx + 4, ty + 4], fill=(0, 0, 0))

    # Hook: short flick from tail up-and-slightly-left (P1). Revision 1:
    # lengthened and steepened hook so it reads clearly (GT hook is a
    # visible tapered flick, not a mere blob).
    # From (x1, y1) → (x1 - 12, y1 + 28) in math coords (+y = up).
    hx0, hy0 = x1, y1
    hx1, hy1 = x1 - 12.0, y1 + 28.0
    n_h = 20
    w_h_head, w_h_tail = 8.0, 2.0
    prev = None
    for i in range(n_h + 1):
        u = i / n_h
        hx = hx0 + (hx1 - hx0) * u
        hy = hy0 + (hy1 - hy0) * u
        w = w_h_head + (w_h_tail - w_h_head) * u
        w_int = max(1, int(round(w)))
        px, py = _to_pixel(hx, hy)
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    t = ImageDraw.Draw(img)

    # Stroke 1: 横 — bank primitive, deliberate transform per TR1/TR6.
    # Standalone heng is 200x12 centered at (0,0). We want a short cross-
    # bar spanning approx x=[-60, +50] at y=-5 → center (-5, -5), scale
    # (110/200) = 0.55.
    # Target role: internal cross-bar of small 3-stroke radical
    # (TR2 top-radical range 0.55-0.75, chose lower for compactness).
    draw_heng(t, ox=-5, oy=-5, scale=0.55)

    # Stroke 2: 斜钩 — inline fresh (no bank primitive; TR8 inline test).
    draw_xie_gou_inline(t, ox=0, oy=0)

    # Stroke 3: 点 — bank primitive at upper-right of composition.
    # Standalone dian's canonical center ≈ (0,0) with head (-15,+25) and
    # tail (+18,-20). Scaled 0.45 the dot is ~15px across. Place its
    # center at math (+55, +55) so it sits upper-right, above the heng
    # and to the right of the xie_gou's head.
    # TR3: origin picked to place dot center at target (55, 55).
    draw_dian(t, ox=55, oy=55, scale=0.45)

    out_path = os.path.join(os.path.dirname(__file__), "01_弋.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()

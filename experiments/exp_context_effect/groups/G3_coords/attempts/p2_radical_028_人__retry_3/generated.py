# p2_radical_028_人 (retry 3) — 人 radical, 2 strokes (撇 + 捺).
#
# Prior attempts' failure mode (from errata + retry_1 PNG inspection):
#   - retry_1 had BOTH strokes bowing outward convexly — pie curved
#     leftward too much AND na curved rightward too much, producing a
#     rounded ^ / gothic-arch shape instead of the natural 人.
#   - Widths peaked mid-stroke (w0=3.5, w_mid=6.0, w1=1.5) so the
#     pie's head was too THIN — GT's pie is heavier at the head with
#     a mild 顿笔 and tapers to a wispy tail.
#   - Kissing point rendered fine but overall silhouette too big/round.
#
# Fix idea (v7): Use the fu.py X-crossing recipe (bank #, PASSed) as
# template. Its `_tb` inline bezier helper handles taper + perp bow
# correctly. 人 is just the "big 撇 + big 捺" pair of 父 without the top
# dot/pie — copy those two lines and shift so heads kiss near top-center.
#
# GT anatomy (verified from gt/phase2/人.png):
#   - Apex near PIL (150, 90). Two strokes MEET at apex (no gap).
#   - 撇: starts at apex with a small 顿笔 blob (thick head), sweeps
#     down-LEFT with mild leftward bow, tapers to thin tail at bottom-
#     left ~PIL (78, 250).
#   - 捺: head KISSES the pie just below-right of apex ~PIL (155, 100),
#     sweeps down-right through a belly maximum around 70% along, tapers
#     to a small foot tail at bottom-right ~PIL (240, 245).
#   - Character occupies most of canvas height but is centered horizontally.

import os
from PIL import Image, ImageDraw


CANVAS = 300


def _tb(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    """fu.py-style tapered bezier: endpoints in PIL px, control offset
    from midpoint by ctrl_perp (perpendicular) + ctrl_along (along chord).
    Width lerps head->tail unless belly_pos<1 and w_belly given, in which
    case width peaks at belly_pos."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # --- Revision 1 vs pass 1: pass 1 head was too fat (w_head=9 fu-style
    # blob visible at apex), silhouette a touch narrow, na belly too heavy.
    # Fixes: pie w_head 9->7 (softer 顿笔), widen tails (pie tail x 78->65,
    # na tail x 240->248), reduce na w_belly 13->11, extend na tail slightly
    # to hint at foot lift.
    #
    # --- 撇 (pie): apex -> lower-left, mild leftward bow.
    _tb(d, 150, 90, 65, 252,
        ctrl_perp=-9, w_head=7, w_tail=1, n=70)

    # --- 捺 (na): head kisses just below-right of pie apex, sweeps
    # down-right with belly at 70% along, thin foot tail.
    _tb(d, 155, 100, 248, 250,
        ctrl_perp=7, w_head=2, w_tail=3,
        belly_pos=0.72, w_belly=11, n=70)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_人.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

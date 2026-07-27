"""p2_radical_046_大 (dà) — retry #5

# RETRY MEMORY CHECKLIST (v8)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Retry_4 failed (apex too HIGH -> reads as 'A' with a bar). Root
#   cause: pie head y=58, na kiss point y=108 -> apex ~y=100 while
#   heng at y=140 gave 40px of vertical space above heng and put the
#   crossing legs entirely below. GT: apex only ~15-20px above heng.
#   Also: retry_4 separate-tick segment at top of pie read as a
#   distinct protrusion. GT hook is a smooth curl integrated into
#   the pie head.
# Q2 (form_catalog): X-crossing family — 大 wants pie head modestly
#   above heng (~15-25px), na starts on pie shaft just above heng
#   crossing (small kiss window), both legs sweep to lower corners.
#   Widths: MMH-thin uniform ~5px.
# Q3 (helpers): Under v8, bank is REFERENCE. Trust GT. Inline PIL
#   with smooth head curl (single bezier), lower apex than retry_4.
#   No separate tick segment.
"""
from PIL import Image, ImageDraw


W, H = 300, 300


def _tapered_bezier(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
                    w_head=5, w_tail=5, belly_pos=1.0, w_belly=None, n=80):
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


def draw_da(draw):
    # ---- 1. 横 (heng): thin, spans wide, y=138
    _tapered_bezier(draw, 62, 140, 232, 138,
                    ctrl_perp=0.0, w_head=5, w_tail=5, n=40)

    # ---- 2. 撇 (pie): small integrated head curl, then long sweep
    # down-left through/near heng midpoint to lower-left tail.
    # Apex only ~20px above heng (y~120), NOT 80px (retry_4's mistake).
    #
    # Head curl: tiny arc from (168, 92) to (162, 106) with small
    # left bow, mimicking the calligraphic entry.
    _tapered_bezier(draw, 168, 92, 161, 105,
                    ctrl_perp=-2, w_head=4, w_tail=5, n=15)

    # Main body: from (161, 105) — just above heng — sweeping
    # down-left through heng at ~(150, 140) to tail (55, 268).
    # Gentle left bow.
    _tapered_bezier(draw, 161, 105, 55, 268,
                    ctrl_perp=-8, w_head=5, w_tail=3, n=90)

    # ---- 3. 捺 (na): apex-kiss on pie shaft just above heng.
    # Head at (158, 118) — the "kiss" point on the pie shaft ~20px
    # above heng crossing. Sweeps down-right with gentle belly bow.
    _tapered_bezier(draw, 158, 118, 245, 258,
                    ctrl_perp=7, w_head=3, w_tail=5, n=80)

    # Small foot flick at 捺 tail
    _tapered_bezier(draw, 245, 258, 262, 254,
                    ctrl_perp=0, w_head=5, w_tail=2, n=15)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_da(draw)
    out = "01_大.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

# p2_radical_082_子 retry_1 — G3 coord-bank inline-fresh attempt
#
# Errata fix idea (from errata.md p2_radical_082_子):
#   "横撇 primitive at scale + wan_gou primitive; the wan_gou hook came out
#    detached. Fix: inline whole 弯钩 fresh with matched taper."
#
# Prior attempt problems:
#   1. wan_gou hook was tiny/subtle
#   2. crossing 一 was too thick, dominating the visual
#   3. 横撇 corner was detached from the vertical shaft
#
# This retry inlines all three strokes with hand-tuned coords, ensuring:
#   - The 横撇 top ends near where the 弯钩 head begins (weld point)
#   - The 弯钩 shows a clear hook flick at the bottom (not a blob)
#   - The crossing 一 is thinner (~5px) matching GT thin ink

from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300
CX = CANVAS // 2
CY = CANVAS // 2
OUT = Path(__file__).with_name("01_子.png")


def to_px(mx, my):
    """math coords (+y up) -> pixel coords."""
    return (CX + mx, CY - my)


def qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def stroke_line(draw, pts, w_head, w_tail):
    """draw a tapered polyline (math coords), width interpolated head->tail."""
    n = len(pts)
    for i in range(n - 1):
        u = i / (n - 1) if n > 1 else 0
        w = w_head + (w_tail - w_head) * u
        w_int = max(2, int(round(w)))
        p1 = to_px(*pts[i])
        p2 = to_px(*pts[i + 1])
        draw.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        draw.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 横撇 (top) ----
    # GT shows a horizontal from upper-left arcing slightly, then a downward-left
    # short pie at the right end (like a hooked corner).
    # heng portion: from (-60, +60) to (+30, +70)  (slight up-arc)
    # pie portion: from (+30, +70) down-left to (0, +30)
    heng_pts = [(-60, 60), (-30, 66), (0, 70), (+30, 70)]
    stroke_line(d, heng_pts, w_head=3, w_tail=5)
    # corner "dun" (顿笔) — slight ink weight at bend
    cx1, cy1 = to_px(+30, 70)
    d.ellipse([cx1 - 4, cy1 - 4, cx1 + 4, cy1 + 4], fill=(0, 0, 0))
    # pie down-left from corner
    pie_pts = qbez((30, 70), (22, 55), (5, 35), 20)
    stroke_line(d, pie_pts, w_head=6, w_tail=3)

    # ---- Stroke 2: 弯钩 (long curved vertical with hook at bottom) ----
    # Starts near the pie tail (~(5, 35)) — welds visually to top stroke.
    # Curves gently right then swings back left descending, ending in a small
    # up-left hook flick at the bottom.
    body = qbez((5, 35), (15, -30), (-8, -90), 60)
    n = len(body)
    for i in range(n - 1):
        u = i / (n - 1)
        # taper: thin at head, thicker mid, thin at tail
        if u < 0.5:
            w = 4 + (7 - 4) * (u / 0.5)
        else:
            w = 7 - (7 - 4) * ((u - 0.5) / 0.5)
        w_int = max(3, int(round(w)))
        p1 = to_px(*body[i])
        p2 = to_px(*body[i + 1])
        d.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))

    # Hook: from tail (-8, -90) flick up-and-left with clear taper
    hook_pts = qbez((-8, -90), (-20, -85), (-32, -70), 20)
    stroke_line(d, hook_pts, w_head=5, w_tail=2)

    # ---- Stroke 3: 一 (crossing horizontal) ----
    # Long crossbar through middle. GT shows it thin & long, extending well
    # past both sides of the wan_gou shaft. Slight up-arc, tapered ends.
    heng2_pts = [(-95, -5), (-60, -3), (-20, -2), (+20, -2), (+60, -3), (+95, -5)]
    stroke_line(d, heng2_pts, w_head=3, w_tail=3)
    # slight thickening at center
    for i in range(len(heng2_pts) - 1):
        p1 = to_px(*heng2_pts[i])
        p2 = to_px(*heng2_pts[i + 1])
        d.line([p1, p2], fill=(0, 0, 0), width=4)

    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    render()

# p2_radical_070_纟 (sī, silk radical) — 3 strokes.
# Structure per GT: two small angular 撇折 (pie-then-横) hooks stacked
# (upper smaller, middle slightly larger), then a long 提 (rising) at
# the bottom. All three sit slightly right-of-center-column.
#
# TR8 inline-fresh test applied: pie_zhe primitive is tuned to be WIDE
# (chord ~100px each seg) and standalone-centered — it would be too big
# and its angular shape uniform. GT shows two compact tight hooks with
# distinct sizes and a longer 提 spanning bottom. Ti primitive is
# tuned to span (-70,-70) to (80,60) — also too wide. INLINE all three
# as tapered beziers hand-tuned to the target proportions.

from PIL import Image, ImageDraw
import os

CANVAS = 300
CX = CANVAS / 2
CY = CANVAS / 2


def to_px(x, y):
    return (CX + x, CY - y)


def tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    """Draw a quadratic bezier with tapered width from w_head to w_tail."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def draw_pie_zhe_hook(draw, cx, cy, size, ink=7):
    """撇折 hook: 撇 (down-left diagonal) then 提/横 (up-right).
    The corner (cx, cy) is the joint (bottom of the 撇, start of the 提).
    - 撇 segment: from upper-right head DOWN-LEFT to (cx, cy).
    - 提 segment: from (cx, cy) sweeps UP-RIGHT to give the "L" shape.
    """
    # 撇 segment — steep diagonal, head up-right, tail at corner
    p0 = (cx + size * 0.55, cy + size * 1.15)  # head, upper-right
    p2 = (cx, cy)                              # tail, at corner
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)   # slight rightward bow
    tapered_bezier(draw, p0, p1, p2, w_head=ink, w_tail=max(2, ink - 2), n=30)
    # 提 segment (upward-slanting horizontal-ish), longer to give L feel
    h0 = (cx, cy)
    h2 = (cx + size * 1.7, cy + size * 0.55)  # tip well up-right
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.1)  # slight downward belly
    tapered_bezier(draw, h0, h1, h2, w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)
    # 顿笔 blob at the corner
    r = ink * 0.75
    px, py = to_px(cx, cy)
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Stroke 1: upper 撇折 — smaller, upper region
    # Corner around (x=-15, y=+55), size ~22
    draw_pie_zhe_hook(draw, cx=-15, cy=55, size=22, ink=6)

    # Stroke 2: middle 撇折 — slightly larger, positioned below first
    # Corner at (x=-20, y=+5), size ~26
    draw_pie_zhe_hook(draw, cx=-20, cy=5, size=26, ink=7)

    # Stroke 3: 提 (long rising) — from lower-left to lower-right, sweep up
    p0 = (-65, -70)
    p2 = (60, -45)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 6)
    tapered_bezier(draw, p0, p1, p2, w_head=14, w_tail=1.5, n=60, head_ramp=0.08)

    out = os.path.join(os.path.dirname(__file__), "01_纟.png")
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

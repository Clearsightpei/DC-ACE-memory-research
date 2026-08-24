"""
p2_radical_118_殳 (shū, 4 strokes) — G3 coord-format Drawer attempt.

REVISION 1: first attempt had (a) too-compact top structure, (b)
descending 几-like curve too straight with a small forward-flick that
didn't match GT's downward curl-tail, (c) upper-left short pie too
detached, (d) bottom 又 pie head sitting too high (starting inside
the top structure). GT shows a bigger, sweepier top with a clearly
curled tail on the descender, and a lower-slung 又 filling the
bottom-third of the canvas.

Applying TR8/TR9: fully inline every stroke; no bank primitives.

Stroke plan (4 strokes):
  1. 撇 (upper-left, small-to-medium) — head near top-mid, sweeps
     down-left. Thick head → needle tip.
  2. 横折弯 (top-right shape like a 几 right side): horizontal top,
     hard shoulder (顿笔), descending shaft with mild leftward bow,
     curling down-and-right at the tail (short flick, distinctive).
  3. 又's 横撇 (long, from upper-mid-canvas down to bottom-left):
     wide sweep, thick head, needle tail.
  4. 又's 捺 (starts crossing stroke-3 mid-shaft, sweeps to bottom-
     right): thin head → belly at u~0.7 → tapered foot.
"""

from PIL import Image, ImageDraw

W = H = 300
CX, CY = W // 2, H // 2  # (150, 150)


def to_px(mx, my):
    return (CX + mx, CY - my)


def tapered_line(draw, p0, p1, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def tapered_bezier(draw, p0, p1, p2, w0, w1, steps=80):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        omu = 1 - u
        x = omu * omu * x0 + 2 * omu * u * x1 + u * u * x2
        y = omu * omu * y0 + 2 * omu * u * y1 + u * u * y2
        w = w0 + (w1 - w0) * u
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def tapered_bezier_wprofile(draw, p0, p1, p2, wprofile, steps=100):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        omu = 1 - u
        x = omu * omu * x0 + 2 * omu * u * x1 + u * u * x2
        y = omu * omu * y0 + 2 * omu * u * y1 + u * u * y2
        w = wprofile(u)
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def cubic_bezier(draw, p0, p1, p2, p3, wprofile, steps=120):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    for i in range(steps + 1):
        u = i / steps
        omu = 1 - u
        x = (omu ** 3) * x0 + 3 * (omu ** 2) * u * x1 + 3 * omu * (u ** 2) * x2 + (u ** 3) * x3
        y = (omu ** 3) * y0 + 3 * (omu ** 2) * u * y1 + 3 * omu * (u ** 2) * y2 + (u ** 3) * y3
        w = wprofile(u)
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def draw_shu(canvas):
    draw = ImageDraw.Draw(canvas)

    # --- Stroke 1: upper-left 撇 ---
    # Larger than v1, sweep from near top-mid down-left.
    # Head at math (-8, +70), tail at math (-50, +25).
    p0 = to_px(-8, 70)
    p1 = to_px(-25, 50)
    p2 = to_px(-50, 25)
    tapered_bezier(draw, p0, p1, p2, w0=8, w1=2, steps=70)

    # --- Stroke 2: 几-like top-right (横折弯 with tail curl) ---
    # Horizontal head from (-5, +75) to (+55, +72).
    hh_l = to_px(-5, 75)
    hh_r = to_px(55, 72)
    tapered_line(draw, hh_l, hh_r, w0=5, w1=7, steps=40)

    # 顿笔 blob at shoulder (P6).
    sx, sy = hh_r
    draw.ellipse([sx - 5, sy - 5, sx + 5, sy + 5], fill="black")

    # Descending shaft with mild leftward bow ending in a downward
    # curl-flick (matches GT's tail going down-right then hooking
    # back). Model as cubic bezier for the S-shape.
    # Anchors: start (55, 72), c1 (48, 30), c2 (28, 0), end (55, -5).
    d0 = to_px(55, 72)
    d1 = to_px(48, 30)
    d2 = to_px(28, 0)
    d3 = to_px(55, -5)

    def desc_w(u):
        # 6 → 8 → 5 profile.
        if u < 0.5:
            return 7 + (8 - 7) * (u / 0.5)
        else:
            return 8 + (5 - 8) * ((u - 0.5) / 0.5)

    cubic_bezier(draw, d0, d1, d2, d3, desc_w, steps=100)

    # --- Stroke 3: 又's 横撇 (long sweep from upper-mid to lower-left) ---
    # Starts near (-5, +5) (slightly right of center-vertical, above
    # midline). Sweeps down-left through control (-35, -40) to tail
    # (-80, -85). Thick head, needle tail.
    q0 = to_px(-5, 5)
    q1 = to_px(-35, -40)
    q2 = to_px(-80, -85)
    tapered_bezier(draw, q0, q1, q2, w0=9, w1=1, steps=90)

    # --- Stroke 4: 又's 捺 ---
    # Head crosses stroke-3 around u=0.35, which is math ~ (-25, -20).
    # Sweeps down-right to (+80, -90).
    def na_width(u):
        if u < 0.15:
            return 2 + (5 - 2) * (u / 0.15)
        elif u < 0.7:
            t = (u - 0.15) / (0.7 - 0.15)
            return 5 + (15 - 5) * t
        else:
            t = (u - 0.7) / 0.3
            return 15 + (4 - 15) * t

    n0 = to_px(-25, -20)
    n1 = to_px(20, -45)
    n2 = to_px(80, -90)
    tapered_bezier_wprofile(draw, n0, n1, n2, na_width, steps=110)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw_shu(img)
    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_118_殳/01_殳.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

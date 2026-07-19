"""p2_radical_046_大 (dà) — retry #1

Fix idea (from errata/sandbox): heng + pie + na all called from bank
in prior attempt; primitives' fixed head/chord logic couldn't yield
大's geometry. Inline all three strokes fresh as tapered beziers with
hand-chosen crossing pixel — G1-style.

Target (from GT PNG):
  - heng: horizontal, spans middle of canvas roughly y=155
  - pie: starts above heng (with small top hook/entry tick),
    crosses heng near center, sweeps down-left ending near (75, 265)
  - na: starts on pie shaft above heng (crossing near center-right
    of heng at ~(160, 155)), sweeps down-right ending near (240, 250)
  - pie and na form an inverted-V above/through the heng
"""
from PIL import Image, ImageDraw


W, H = 300, 300


def bezier(p0, p1, p2, p3, steps=200):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def stroke_tapered(draw, pts, w_start, w_end):
    n = len(pts)
    for i in range(n - 1):
        t = i / max(1, n - 1)
        w = w_start * (1 - t) + w_end * t
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill="black", width=max(1, int(round(w))))
        # cap
        r = w / 2
        draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill="black")


def draw_da(draw):
    # --- Heng (横): horizontal, slight upward tilt on right (calligraphic)
    heng_pts = bezier(
        (55, 158),   # left start
        (110, 154),  # slight dip
        (200, 150),  # rise
        (245, 152),  # right end (little downward tick)
        steps=180,
    )
    stroke_tapered(draw, heng_pts, w_start=5, w_end=6)
    # small right-end 顿: tiny bulge
    draw.ellipse([238, 148, 250, 158], fill="black")

    # --- Pie (撇): starts above heng with small entry tick, crosses heng
    # near center (~150, 155), sweeps down-left, ending curled near (80, 260)
    # Small top hook: draw a tiny angled entry stub
    # entry tick
    draw.line([(148, 78), (156, 90)], fill="black", width=5)

    pie_pts = bezier(
        (155, 88),    # start (just below the entry tick)
        (152, 130),   # near-vertical descent to just above heng
        (130, 200),   # sweep left below heng
        (75, 268),    # end lower-left, thin
        steps=220,
    )
    stroke_tapered(draw, pie_pts, w_start=7, w_end=2)

    # --- Na (捺): starts on pie shaft just above heng (~155, 128),
    # sweeps down-right ending with flat foot near (235, 258)
    na_pts = bezier(
        (156, 128),   # start on pie shaft above heng
        (175, 170),   # descent right of heng crossing
        (205, 220),   # curve
        (235, 262),   # end lower-right (pulled in from 245)
        steps=220,
    )
    stroke_tapered(draw, na_pts, w_start=3, w_end=9)
    # 捺 foot: shorter horizontal outward flick
    foot_pts = bezier(
        (235, 262),
        (243, 261),
        (250, 258),
        (256, 254),
        steps=60,
    )
    stroke_tapered(draw, foot_pts, w_start=9, w_end=2)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_da(draw)
    out = "01_大.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

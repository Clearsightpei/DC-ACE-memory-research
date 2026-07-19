"""
p1_stroke_10_横钩 — heng-gou (horizontal-then-hook-down-left).

Structure per drawer_memory.md:
- Primary 横: left → right, roughly uniform width, tiny 顿笔 at start,
  small press swelling near the right end where the hook launches.
- Hook: from the right endpoint, flicks down-and-left, tapering sharply
  to a fine tip.

Rendering strategy: PIL brush-dabs along each segment (memory formula).
Image coords: y grows DOWN, origin top-left. Canvas 300x300.
"""
from PIL import Image, ImageDraw


def dab_line(draw, x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def main():
    W = H = 300
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # --- 横 (horizontal primary) ---
    # A 横钩 sits in the upper half of a character (it's typically the
    # top cover of glyphs like 冖 / 宀 / 买). Draw it a bit above middle.
    hx0, hy0 = 55, 130   # left start
    hx1, hy1 = 245, 128  # right end (very slight upward tilt, calligraphic)

    # Uniform-ish body: start ~7px, end ~9px (small swell at hook launch).
    dab_line(draw, hx0, hy0, hx1, hy1, r_start=7.0, r_end=9.0, steps=500)

    # 顿笔 at the left start (slightly larger dab).
    r_start_press = 9.0
    draw.ellipse((hx0 - r_start_press, hy0 - r_start_press,
                  hx0 + r_start_press, hy0 + r_start_press), fill="black")

    # Small press swell at right endpoint (hook launch shoulder).
    r_launch = 11.0
    draw.ellipse((hx1 - r_launch, hy1 - r_launch,
                  hx1 + r_launch, hy1 + r_launch), fill="black")

    # --- 钩 (hook: flick down-and-left) ---
    # Hook direction ~ 220° (down-left) from the right endpoint.
    # Length ~ 40 px, tapers from launch width down to a fine tip.
    gx0, gy0 = hx1, hy1
    # Down-left target: dx negative, dy positive.
    gx1, gy1 = hx1 - 26, hy1 + 36  # ~53 px length, steep down-left
    dab_line(draw, gx0, gy0, gx1, gy1, r_start=9.5, r_end=1.2, steps=300)

    out = ("/Users/peilinwu/Documents/AI memory research/experiments/"
           "exp_context_effect/groups/G2_free_form/attempts/"
           "p1_stroke_10_横钩/01_横钩.png")
    img.save(out)
    print(f"saved: {out}")


if __name__ == "__main__":
    main()

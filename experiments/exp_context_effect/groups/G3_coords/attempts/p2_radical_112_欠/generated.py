"""p2_radical_112_欠 — G3 coord-bank attempt (revision 2).

Revision from attempt 1: the heng_gou primitive doesn't scale its
horizontal x-span (scale only affects widths/hook), so calling it with
scale=0.42 still drew a 190-px-wide bar. INLINE-FRESH (TR8) the 横钩
too. Also: top 撇 was too shallow (nearly horizontal) — GT shows a
steeper drop. Thinning the pie/na widths a touch.

Composition (from GT visual inspection):
  欠 = 4 strokes.
  Stroke 1: short 撇 at top — small steep diagonal, upper-center.
  Stroke 2: 横钩 — compact horizontal that hooks DOWN-LEFT at its
            right end.
  Stroke 3: 撇 — long diagonal from mid, sweeping to lower-left.
  Stroke 4: 捺 — long diagonal from mid, sweeping to lower-right.

TR compliance:
- All 4 strokes inlined fresh (TR8). The 横钩 primitive's x-span is
  fixed at 190 px and doesn't shrink with scale, so it would draw a
  bar too wide for 欠. Inline as tapered horizontal + tapered hook.
- Pie/na primitives are tuned for standalone full-canvas sweeps —
  in 欠 both start from a shared upper-middle apex, which is a
  re-anchor (not a pure translation). TR8 rule 3 → inline fresh.
"""

from PIL import Image, ImageDraw
import os


def _tapered_bezier(draw, p0, p1, p2, w_profile, steps=40):
    """Quadratic bezier with tapered width."""
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) * (1 - u) * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) * (1 - u) * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        if prev is not None:
            w = max(1, int(w_profile(u)))
            draw.line([prev, (x, y)], fill="black", width=w)
        prev = (x, y)


def _tapered_line(draw, x0, y0, x1, y1, w_start, w_end, steps=20):
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = max(1, int(w_start + (w_end - w_start) * t0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def render():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: short 撇 at top ---
    # Steep small diagonal, head near (155, 55), tail near (128, 105).
    # Slight scoop (curves gently leftward).
    _tapered_bezier(
        draw,
        p0=(158, 55),
        p1=(146, 82),
        p2=(128, 108),
        w_profile=lambda u: 7 - 5 * u,  # thick head → tapered
        steps=28,
    )

    # --- Stroke 2: 横钩 (top-cap) inlined fresh ---
    # Horizontal from left of 撇's tail to about x=215, at y ~= 110.
    # Slight downward slope. Ends in a small 顿笔 blob + a hook going
    # DOWN-LEFT (short, tapered).
    hx0, hy0 = 120, 108  # picks up from pie 1's tail area
    hx1, hy1 = 218, 116  # end of horizontal (顿笔 point)
    _tapered_line(draw, hx0, hy0, hx1, hy1, w_start=6, w_end=9, steps=20)
    # 顿笔 blob at end
    r = 5
    draw.ellipse([hx1 - r, hy1 - r, hx1 + r, hy1 + r], fill="black")
    # hook: down-left from (hx1, hy1)
    _tapered_line(
        draw,
        hx1 + 2, hy1 + 2,
        hx1 - 12, hy1 + 22,
        w_start=8, w_end=1, steps=14,
    )

    # --- Stroke 3: 撇 (left long leg) ---
    # Long diagonal starting under the 横钩's left region (~x=145, y=118)
    # sweeping down-left to ~x=90, y=250. Curves outward-left (belly to
    # the left of the chord).
    _tapered_bezier(
        draw,
        p0=(148, 118),
        p1=(120, 178),
        p2=(88, 252),
        w_profile=lambda u: 9 - 8 * u,  # thick head → needle tip
        steps=42,
    )

    # --- Stroke 4: 捺 (right long leg) ---
    # Starts from near the pie's head area (~x=155, y=128) sweeping
    # down-right, belly bulges right, ends around (238, 262).
    # Classic 捺: thin head → thick belly (u~0.7) → tapered foot.
    def na_width(u):
        if u < 0.7:
            return 2 + (13 - 2) * (u / 0.7)
        else:
            return 13 - (13 - 3) * ((u - 0.7) / 0.3)

    _tapered_bezier(
        draw,
        p0=(156, 128),
        p1=(196, 198),
        p2=(240, 262),
        w_profile=na_width,
        steps=48,
    )

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_欠.png"
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    render()

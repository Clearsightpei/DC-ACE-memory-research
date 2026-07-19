"""
巛 (chuan radical, 3 strokes) — G3 coord-bank attempt.

Composition analysis:
- Three parallel wavy vertical strokes.
- Each stroke has a small hooked/scooped head at the top (like a 竖's
  scooping head that curls left-to-right briefly), then descends as a
  gently S-curving vertical line, ending in a needle taper.
- GT positions on 300x300: three shafts roughly at x = 115, 150, 185
  (left, mid, right — evenly spaced ~35 px apart), y range ~ 100..220.
- Every stroke has an internal S-shape: top hook curls right, mid
  shaft leans slightly left of vertical, tail curves back to nearly
  centered.
- No bank primitive fits: 竖 is straight and 竖弯 has a horizontal foot.
  The GT stroke is best described as a small "hook top" + a gentle
  S-vertical. Inlining fresh per TR5.

Approach: draw each stroke as one continuous tapered polyline sampled
from a bezier-like path. Width profile: thin head (2 px), thicken to
6-7 px in the belly, taper back to needle (~1 px) at the tail.
Head has a small curl (top going right then down).

TR7 sanity check:
- Left stroke x range ~ [95, 130], y range [95, 225]. Within 300x300 with ~10px margin.
- Mid stroke x range ~ [130, 165], y range [95, 225].
- Right stroke x range ~ [165, 200], y range [95, 225].
- All three strokes are independent — no joints, no welds needed.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300


def draw_wavy_stroke(draw, x_center_top, x_bottom_offset=0):
    """
    Draw one 巛-component stroke.

    - Head: starts at (x_center_top + 8, top_y - 5), curls left+down
      to the shaft head at (x_center_top, top_y + 8) — a small
      right-to-left scoop like the head of a 竖.
    - Shaft: gentle S from the head down to the tail. Sampled from a
      cubic bezier so it curves smoothly.
    - Width: 2 at head -> 6.5 belly (u=0.55) -> 0.8 needle tip.
    """
    top_y = 95
    bot_y = 225
    # Head curl: a small right-facing hook (like the top of the GT strokes).
    head_start = (x_center_top + 10, top_y + 2)
    head_mid = (x_center_top + 5, top_y - 2)
    head_end = (x_center_top - 2, top_y + 12)  # shaft head

    # Shaft: gentle S. Bow RIGHT in upper third, then LEFT in lower third.
    # This is what the GT shows — the shaft wiggles as it descends.
    p0 = head_end
    p1 = (x_center_top + 6, top_y + 45)   # bow right at upper belly
    p2 = (x_center_top - 8, top_y + 95)   # bow left at lower belly
    p3 = (x_center_top + x_bottom_offset - 4, bot_y)

    # Sample bezier
    N = 60
    pts = []
    for i in range(N + 1):
        u = i / N
        mu = 1 - u
        x = mu**3 * p0[0] + 3 * mu**2 * u * p1[0] + 3 * mu * u**2 * p2[0] + u**3 * p3[0]
        y = mu**3 * p0[1] + 3 * mu**2 * u * p1[1] + 3 * mu * u**2 * p2[1] + u**3 * p3[1]
        pts.append((x, y))

    # Draw head curl as a small tapered polyline (2 segments).
    head_pts = [head_start, head_mid, head_end]
    for i in range(len(head_pts) - 1):
        # Width tapers from 2 -> 3.5 into the shaft head.
        w0 = 2.0 + i * 0.6
        w1 = 2.6 + i * 0.6
        _draw_tapered_seg(draw, head_pts[i], head_pts[i + 1], w0, w1)

    # Draw shaft with width profile:
    # width(u) = thin(2.6) -> belly(6.5 at u=0.55) -> needle(0.7 at u=1)
    for i in range(len(pts) - 1):
        u0 = i / N
        u1 = (i + 1) / N
        w0 = _width(u0)
        w1 = _width(u1)
        _draw_tapered_seg(draw, pts[i], pts[i + 1], w0, w1)


def _width(u):
    """Piecewise linear width profile for shaft. u in [0,1].

    GT strokes read as gently thick in the middle 60% and taper only at
    the very ends. Keep width more uniform than the previous belly-heavy
    profile.
    """
    if u < 0.15:
        # 2.8 -> 4.5 (thickening after head curl)
        return 2.8 + (4.5 - 2.8) * (u / 0.15)
    elif u < 0.75:
        # 4.5 -> 4.8 (nearly uniform mid-belly)
        return 4.5 + (4.8 - 4.5) * ((u - 0.15) / 0.60)
    else:
        # 4.8 -> 1.0 (taper to soft needle)
        return 4.8 + (1.0 - 4.8) * ((u - 0.75) / 0.25)


def _draw_tapered_seg(draw, p0, p1, w0, w1):
    """Draw a tapered segment by stamping circles along the segment."""
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    length = math.hypot(dx, dy)
    if length < 0.1:
        return
    steps = max(2, int(length * 2))
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + dx * u
        y = p0[1] + dy * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def main():
    img = Image.new("L", (W, H), 255)
    draw = ImageDraw.Draw(img)

    # Three strokes at evenly-spaced x centers.
    # Left stroke: shaft head near x=118. Tail curves slightly right (offset +2).
    draw_wavy_stroke(draw, x_center_top=118, x_bottom_offset=2)
    # Middle stroke: shaft head near x=153.
    draw_wavy_stroke(draw, x_center_top=153, x_bottom_offset=2)
    # Right stroke: shaft head near x=188.
    draw_wavy_stroke(draw, x_center_top=188, x_bottom_offset=2)

    img.save("01_巛.png")


if __name__ == "__main__":
    main()

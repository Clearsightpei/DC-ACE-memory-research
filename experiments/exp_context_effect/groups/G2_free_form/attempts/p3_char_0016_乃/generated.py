"""
Render 乃 (2 strokes) at 300x300, white bg, black ink.

Analysis of GT:
- Stroke 1: 横折折撇 — top short 横 at upper-right (~y=95), then folds down
  a short 竖-ish, then folds further, then a long 撇 sweeping down-left to
  bottom-left corner. This forms the outer left/top skeleton.
- Stroke 2: 横折钩 — starts at right end of top 横 (or slightly below at
  its right end), goes down-right slightly then bows down and left, ending
  with a small hook flicking left near bottom-center. This is the "belly"
  of the character.

Key silhouette: tall, occupies most of canvas; upper-right dense (folds);
lower-left has the sweeping tail; a small hook at bottom-center-ish.
Aspect: nearly square, slightly tall.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stamp(x, y, r):
    """Draw a filled disk = one 'brush dab'."""
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(pts, r_start, r_end):
    """Interpolate brush dabs along the given point list with tapering radius."""
    # First compute cumulative length
    seg_lengths = []
    total = 0.0
    for i in range(1, len(pts)):
        dx = pts[i][0] - pts[i - 1][0]
        dy = pts[i][1] - pts[i - 1][1]
        L = (dx * dx + dy * dy) ** 0.5
        seg_lengths.append(L)
        total += L
    if total <= 0:
        return
    # Walk with fine step
    step = 0.6
    n = int(total / step) + 1
    for k in range(n + 1):
        t = k / n  # 0..1
        # Radius by t
        r = r_start + (r_end - r_start) * t
        # Which segment?
        target = t * total
        acc = 0.0
        for i, L in enumerate(seg_lengths):
            if acc + L >= target or i == len(seg_lengths) - 1:
                # local u in this segment
                u = 0.0 if L == 0 else (target - acc) / L
                x = pts[i][0] + u * (pts[i + 1][0] - pts[i][0])
                y = pts[i][1] + u * (pts[i + 1][1] - pts[i][1])
                stamp(x, y, r)
                break
            acc += L


def bezier(p0, p1, p2, p3, n=60):
    """Cubic Bezier sampled into n+1 points."""
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def qbezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# ---------- Stroke 1: 横折折撇 ----------
# Segment A: top 横 (short, slight up-tilt). Positioned upper-center.
top_start = (75, 110)
top_end = (205, 100)
seg_A = [top_start, top_end]

# Segment B: short 折 down (small vertical fall from shoulder).
fold1_end = (208, 130)
seg_B = [top_end, fold1_end]

# Segment C: sweeping 撇 from the shoulder, curving down and to the LEFT
# all the way to the lower-left corner. This is the long defining sweep.
pie_ctrl1 = (160, 190)
pie_ctrl2 = (100, 235)
pie_end = (45, 275)
seg_C = bezier(fold1_end, pie_ctrl1, pie_ctrl2, pie_end, n=90)

taper_line(seg_A, 5.0, 5.0)
taper_line(seg_B, 5.5, 5.5)
taper_line(seg_C, 5.5, 1.5)

# 顿 dabs at endpoints of segment A (top-横).
stamp(top_start[0], top_start[1], 5)
stamp(top_end[0], top_end[1], 6.5)

# ---------- Stroke 2: 横折钩 (the interior belly + tail + hook) ----------
# In GT the second stroke starts INSIDE at a middle horizontal position,
# goes right a bit forming a tiny 横, folds down at the shoulder, sweeps
# down through a right-side belly, then LEANS LEFT as a long descender,
# ending in a small hook flicking LEFT near bottom-center.
s2_start = (150, 130)
s2_top_end = (200, 125)  # short internal 横
seg_D = [s2_start, s2_top_end]

# Segment E: down-right curve into belly, then curve back down-left.
# End near bottom-center. Long descender that leans slightly LEFT.
belly_ctrl1 = (225, 175)
belly_ctrl2 = (200, 235)
belly_end = (155, 262)
seg_E = bezier(s2_top_end, belly_ctrl1, belly_ctrl2, belly_end, n=90)

# Hook: sharp flick from belly_end short up-and-left.
hook_end = (130, 250)
seg_F = qbezier(belly_end, (145, 262), hook_end, n=25)

taper_line(seg_D, 4.5, 5.0)
taper_line(seg_E, 5.5, 4.0)
taper_line(seg_F, 4.0, 1.0)

stamp(s2_start[0], s2_start[1], 4.5)
stamp(s2_top_end[0], s2_top_end[1], 5.5)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0016_乃/01_乃.png"
img.save(out)
print("wrote", out)

"""
Retry 1 for 乃. Prior attempt (see errata p3_char_0016_乃) was too
compressed — echoed the 横折折折钩 failure mode. Fix (per errata):
- Fill the vertical ~250 px extent.
- Stroke 1 = 横折折撇: top 横 medium, short vertical fold, short 横 back
  rightward, then LONG bowed 撇 sweeping to lower-left corner.
- Stroke 2 = a second 撇 body-crossing (the hook-flick visible in GT
  near bottom-center). Cross-ref form_catalog "撇 as body-crossing
  diagonal" — must start above/inside the top 横 and cross through.

The dominant visual is the long sweep to the lower-left; the compact
zigzag lives in the upper-right quadrant.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(pts, r_start, r_end):
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
    step = 0.5
    n = int(total / step) + 1
    for k in range(n + 1):
        t = k / n
        r = r_start + (r_end - r_start) * t
        target = t * total
        acc = 0.0
        for i, L in enumerate(seg_lengths):
            if acc + L >= target or i == len(seg_lengths) - 1:
                u = 0.0 if L == 0 else (target - acc) / L
                x = pts[i][0] + u * (pts[i + 1][0] - pts[i][0])
                y = pts[i][1] + u * (pts[i + 1][1] - pts[i][1])
                stamp(x, y, r)
                break
            acc += L


def bezier(p0, p1, p2, p3, n=90):
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
# A: top 横 (medium length, slight up-tilt to the right)
top_start = (65, 88)
top_end = (215, 78)
seg_A = [top_start, top_end]

# B: short 竖 drop from top-right (fold #1)
drop_end = (218, 118)
seg_B = [top_end, drop_end]

# C: short 横 rightward tiny then back
mid_left = (175, 128)
seg_C = [drop_end, mid_left]

# D: LONG sweeping 撇 from mid_left down to the lower-left corner.
# This must be the dominant visual element.
pie_ctrl1 = (140, 180)
pie_ctrl2 = (85, 230)
pie_end = (35, 278)
seg_D = bezier(mid_left, pie_ctrl1, pie_ctrl2, pie_end, n=110)

taper_line(seg_A, 6.0, 6.0)
taper_line(seg_B, 6.0, 6.0)
taper_line(seg_C, 6.0, 5.5)
taper_line(seg_D, 6.5, 1.5)

# 顿 dabs at endpoints
stamp(top_start[0], top_start[1], 6.0)
stamp(top_end[0], top_end[1], 7.0)
stamp(drop_end[0], drop_end[1], 6.5)
stamp(mid_left[0], mid_left[1], 6.0)

# ---------- Stroke 2: body-crossing 撇 ending in small hook flick ----------
# In GT this appears as a short crossing 撇 that starts above the top 横 at
# right area and sweeps down to a small hook-flick near lower-middle.
# Actually looking at GT: it's a 竖 that drops from top area then flicks
# left at the bottom — like a hook. Start just below the top 横 fold,
# curve down and left, terminate near bottom-center with left flick.
s2_start = (200, 130)
s2_ctrl1 = (215, 200)
s2_ctrl2 = (195, 250)
s2_end = (155, 265)
seg_E = bezier(s2_start, s2_ctrl1, s2_ctrl2, s2_end, n=90)

# Terminal hook flicking sharply left
hook_end = (125, 258)
seg_F = qbezier(s2_end, (140, 268), hook_end, n=30)

taper_line(seg_E, 5.5, 4.0)
taper_line(seg_F, 4.0, 1.0)

stamp(s2_start[0], s2_start[1], 5.5)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0016_乃__retry_1/01_乃.png"
img.save(out)
print("wrote", out)

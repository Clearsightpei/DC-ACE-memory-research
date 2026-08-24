"""
p3_char_0510_畟 — 畟
Structure: 田 (top) + 夋 (bottom, with 厶 + 夊 shape)
From GT: top clearly 田 (square with cross), bottom has downward
strokes and a long sweeping 捺.

Applying TIER-0 F (4-move calligraphic weight):
- teardrop taper via stroke() helper
- shoulder dab at 折 corners
- bezier for curved sweeps
- hook flick UP-LEFT (not applicable here; no explicit hook)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths=(6, 6)):
    """Draw a tapered stroke by sampling ellipses along path."""
    n = len(pts)
    if n < 2:
        return
    w0, w1 = widths
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = (w0 * (1 - t) + w1 * t) / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_str(p0, p1, widths=(6, 6), n=30):
    pts = [
        (p0[0] + (p1[0] - p0[0]) * i / n, p0[1] + (p1[1] - p0[1]) * i / n)
        for i in range(n + 1)
    ]
    stroke(pts, widths)


def shoulder(x, y, r=4.5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============ 田 (top) — centered, upper portion ============
# 田 occupies roughly x=95..205, y=40..135
L, R, T, B = 100, 200, 45, 135
# 1. Left vertical (竖)
line_str((L, T), (L, B), widths=(6, 6))
# 2. Top + right shoulder + right vertical (横折)
line_str((L, T), (R, T), widths=(6, 6))
shoulder(R, T, 4.5)
line_str((R, T), (R, B), widths=(6, 6))
# 3. Middle horizontal (横)
midY = (T + B) // 2
line_str((L, midY), (R, midY), widths=(5, 5))
# 4. Middle vertical (竖)
midX = (L + R) // 2
line_str((midX, T), (midX, B), widths=(5, 5))
# 5. Bottom horizontal (closing)
line_str((L, B), (R, B), widths=(6, 6))

# ============ Bottom: 夋-like (厶 + 夊) ============
# 厶 portion — small top-triangle
# 撇 flick down-left from center
p_start = (150, 140)
# Small 撇 down-left
撇1 = bez((150, 145), (140, 160), (128, 172), (118, 182), n=40)
stroke(撇1, widths=(6, 3))
# Small 点/横折 to right
line_str((150, 145), (170, 152), widths=(5, 3))

# 夊 portion — the big sweeping bottom
# Left 撇: from upper-middle sweeping down-left to bottom
撇big = bez((155, 175), (140, 200), (115, 225), (85, 258), n=60)
stroke(撇big, widths=(9, 3))

# Right 捺 with wave: starts near top-middle of 夊, sweeps down-right,
# with a slight lift at the end
捺 = bez((155, 175), (185, 210), (215, 240), (255, 260), n=60)
stroke(捺, widths=(4, 11))
# Terminal flat tail (捺 press-and-release)
line_str((255, 260), (270, 258), widths=(11, 4))

# Middle-inner short stroke of 夊 (the little 撇 crossing near top)
inner = bez((145, 180), (150, 195), (155, 210), (160, 225), n=30)
stroke(inner, widths=(5, 3))

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0510_畟/01_畟.png"
)
print("saved")

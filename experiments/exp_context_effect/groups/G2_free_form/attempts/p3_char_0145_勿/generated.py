"""
勿 (wù) — 4 strokes:
  1) short 撇 at top-left  (the 勹 shoulder)
  2) 横折钩 — 横 shoulder + long right-side 撇-curve descending, terminal hook UP-and-LEFT
  3) short 撇 inside (middle)
  4) longer 撇 inside (below-right of #3)

Structure = 勹 wrap-around bracket + interior 撇 pair.
Hook rule: 横折钩 flick UP-and-LEFT (~-105°..-120°). Never DOWN.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=7):
    d.line(points, fill=BLACK, width=width, joint="curve")
    # end-cap smoothing
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# --- Stroke 1: short top-left 撇 (shoulder of 勹) ---
# closer to the 横's left endpoint; curl down-left
s1 = bezier((115, 70), (100, 92), (78, 118))
stroke(s1, width=6)

# --- Stroke 2: 横折钩 — the wrap-around bracket ---
# 横 (top horizontal, slight upward slope) — starts near where 撇#1 ends laterally
stroke([(100, 112), (218, 100)], width=7)
# shoulder + long descending right-curve
descend = bezier((218, 100), (215, 190), (155, 258))
stroke(descend, width=7)
# hook flick UP-and-LEFT (into character body)
stroke([(155, 258), (132, 238)], width=7)

# --- Stroke 3: short interior 撇 (upper) ---
s3 = bezier((150, 138), (135, 162), (108, 192))
stroke(s3, width=6)

# --- Stroke 4: longer interior 撇 (lower, extends past hook) ---
# begin near the belly's upper interior, sweep down-left past the hook line
s4 = bezier((188, 168), (150, 215), (85, 270))
stroke(s4, width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0145_勿/01_勿.png")

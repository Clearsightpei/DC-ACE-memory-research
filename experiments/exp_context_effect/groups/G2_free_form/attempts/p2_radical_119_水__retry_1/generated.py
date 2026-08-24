"""
水 (water) — 4 strokes, radical 119, retry #1.

Errata fix: prior attempt had wings too short. Increase left/right
wing sweep to ~150 px each, splay outward from mid-height of 竖钩.
Cross-ref form_catalog "捺 as terminal splay under a body".

Stroke order (standard):
  1) 竖钩 — central vertical hook (down, flick up-left at bottom)
  2) 横撇 — short upper-left arm (short 横 then 撇 down-left)
  3) 撇  — long left leg sweeping down-left from mid of 竖钩
  4) 捺  — long right leg sweeping down-right from mid of 竖钩
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush(pts, width_start=6, width_end=6):
    """Draw a smooth stroke with per-segment tapering."""
    n = len(pts)
    for i in range(n - 1):
        t = i / max(1, n - 2)
        w = int(round(width_start * (1 - t) + width_end * t))
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=max(2, w))
    # end caps
    for p, w in ((pts[0], width_start), (pts[-1], width_end)):
        r = max(1, w // 2)
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=BLACK)


def bezier(p0, p1, p2, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


# --- Stroke 1: 竖钩 (central vertical with hook flicking up-left at bottom)
# Vertical spine, top y~60, bottom y~250 at x=150
spine_top = (150, 55)
spine_bot = (150, 245)
brush([spine_top, (150, 100), (150, 160), (150, 220), spine_bot],
      width_start=7, width_end=8)
# Hook: from spine bottom flick up-and-left (per TIER-0 rule B)
hook = bezier((150, 245), (140, 245), (120, 225), n=25)
brush(hook, width_start=8, width_end=3)

# --- Stroke 2: 横撇 (upper-left arm: short 横 then 撇 down-left) — HIGHER
seg1 = [(100, 95), (120, 95), (140, 100)]
brush(seg1, width_start=5, width_end=6)
# 撇 down-left from the shoulder — shorter, ends around y=155
pie = bezier((140, 100), (120, 130), (85, 165), n=30)
brush(pie, width_start=7, width_end=2)

# --- Stroke 3: long 撇 left leg — LONGER, from spine sweeping wide-left
# Starts near (147, 140), sweeps far down-left to about (45, 255)
left_leg = bezier((147, 140), (95, 200), (45, 258), n=45)
brush(left_leg, width_start=6, width_end=2)

# --- Stroke 4: long 捺 right leg — from mid of spine sweeping down-right
# Starts near (150, 145), sweeps down-right to about (255, 245)
right_leg = bezier((152, 145), (200, 190), (255, 245), n=40)
brush(right_leg, width_start=4, width_end=9)
# Terminal splay tail-tip for 捺
brush([(255, 245), (265, 246)], width_start=9, width_end=3)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_119_水__retry_1/01_水.png")
print("saved 01_水.png")

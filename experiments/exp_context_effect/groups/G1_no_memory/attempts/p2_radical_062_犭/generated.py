"""G1 render of radical 犭 (quǎn, dog radical, 3 strokes)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 6

def curve(points, width=STROKE):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    for p in points:
        draw.ellipse([p[0] - width / 2, p[1] - width / 2,
                      p[0] + width / 2, p[1] + width / 2], fill=INK)

# 犭 structure per GT PNG:
# Stroke 1: short 撇 (pie) top — starts upper-right, slants down-left.
#           From ~(175, 55) to ~(130, 105).
# Stroke 2: 弯钩 (wan-gou) — starts higher up-right of stroke 1's top,
#           curves down-left CROSSING stroke 1 near (150, 80), continues down
#           to form the belly of the radical, ends with a small hook at
#           lower-middle area ~(160, 190) hooking right.
#           Actually re-examining GT: stroke 2 starts at top around (165, 60),
#           swings down-right first to (180, 90), then curves back down-left
#           through (150, 130), then curves down forming a J-shape ending
#           in a hook.
# Stroke 3: long 撇 — starts around the middle where stroke 2 ends its belly,
#           sweeps down-left to bottom, ending near (95, 265).

# --- Stroke 1: short 撇 (pie) — the diagonal that goes upper-right to lower-left
s1 = [
    (172, 58),
    (162, 72),
    (150, 88),
    (135, 105),
    (122, 118),
]
curve(s1, width=6)

# --- Stroke 2: 弯钩 - starts top-right, curves down forming belly, ends hook
# Starts high-right (crosses stroke 1 from the right side going down-left initially,
# then bows outward right, then comes back)
s2 = [
    (150, 55),      # top - starts left of stroke1 top
    (162, 78),      # crossing stroke1
    (172, 105),     # bowing right
    (172, 135),
    (162, 165),
    (150, 190),
    (155, 208),     # hook base
    (170, 210),     # small hook tail to the right
]
curve(s2, width=6)

# --- Stroke 3: long 撇 — starts inside the belly, sweeps down-left to bottom
s3 = [
    (150, 145),
    (135, 175),
    (118, 205),
    (100, 235),
    (85, 265),
]
curve(s3, width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_062_犭/01_犭.png")

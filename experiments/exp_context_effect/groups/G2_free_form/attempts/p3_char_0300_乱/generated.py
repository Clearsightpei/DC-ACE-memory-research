"""
乱 (luàn) — 7 strokes = left (舌-like: 千 over 口) + right (乚 竖弯钩)

Layout from GT:
- Left component occupies ~left 55% of canvas, top-heavy with 口 at bottom
- Right component 乚 is a large vertical-bend-hook filling right 45%,
  hooking UP-and-LEFT at terminal (per TIER-0 hook rules)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=8):
    """Draw a smooth polyline stroke."""
    d.line(pts, fill=INK, width=width, joint="curve")
    # round caps
    r = width // 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# ---- LEFT component (舌-like, compact) ----
# 1) short top-left flick (小撇 above)
stroke([(70, 55), (55, 78)], width=7)

# 2) small horizontal cap (short 一 at top center of left)
stroke([(38, 90), (128, 88)], width=8)

# 3) vertical stroke down through center of left (short 竖)
stroke([(83, 92), (83, 168)], width=8)

# 4) middle horizontal (mid-bar of 千/舌)
stroke([(28, 138), (138, 135)], width=8)

# 5-7) 口 at bottom-left: left vertical, top-right corner (横折), bottom horizontal
# left vertical of 口
stroke([(45, 178), (45, 258)], width=8)
# 横折 (top + right side of 口)
stroke([(45, 178), (135, 180), (135, 258)], width=8)
# bottom horizontal closing 口
stroke([(45, 258), (135, 258)], width=8)

# ---- RIGHT component: 乚 (竖弯钩) ----
# starts high-right, comes straight down, bends right along bottom,
# terminal flicks UP-and-LEFT (hook rule)
right_pts = [
    (215, 60),
    (215, 100),
    (215, 160),
    (215, 210),
    (220, 240),
    (240, 258),
    (265, 262),
    (280, 258),
]
stroke(right_pts, width=9)
# hook flick UP-and-LEFT from terminal
stroke([(280, 258), (272, 235)], width=8)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0300_乱/01_乱.png"
)
print("wrote 01_乱.png")

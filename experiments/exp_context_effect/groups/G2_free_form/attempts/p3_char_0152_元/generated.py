"""
元 (yuán) — 4 strokes: 一 (short top) + 一 (longer middle) + 撇 + 竖弯钩

Structure (per form_catalog):
- 亠 lid: short 一 top, longer 一 below (roof plate).
- 儿 legs: 撇 hangs from lid's left-middle, throws down-left.
         竖弯钩 hangs from lid's right-middle, descends, arcs right
         along baseline, then hooks UP-and-LEFT (~-110°).

Sibling caution (亓 vs 元): right leg MUST be 竖弯钩, not straight 竖.
Hook flick UP-LEFT into the character body (never down/right).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 10  # stroke width


def stroke(points, width=INK):
    """Draw a polyline with round joins/caps."""
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=width)
    for p in points:
        d.ellipse((p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2), fill=BLACK)


# Stroke 1: short 一 top (upper, shorter)
stroke([(115, 78), (185, 72)])

# Stroke 2: longer 一 middle (roof plate, wider)
stroke([(60, 128), (245, 122)])

# Stroke 3: 撇 (left leg) — starts just under roof-left, throws down-left
pi_pts = [(112, 130), (100, 170), (82, 215), (58, 268)]
stroke(pi_pts)

# Stroke 4: 竖弯钩 (right leg) — descends, arcs right, hooks up-left
shu_wan_gou = [
    (185, 130),  # top start (hangs from roof-right)
    (188, 170),
    (193, 210),
    (203, 245),  # begin arc
    (222, 265),
    (245, 268),
    (262, 262),  # arc's rightmost tip
    # Hook: flick UP-and-LEFT, more prominent
    (252, 245),
    (240, 225),
]
stroke(shu_wan_gou)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0152_元/01_元.png")
print("wrote 01_元.png")

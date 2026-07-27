"""Render p3_char_0007_乛 to 01_乛.png (300x300, white bg, black ink).

The GT for this item shows a complex 己/巳-like shape (left vertical +
middle 横折 hook + bottom sweeping 竖弯 with a right ascending piece +
small top-left flick), NOT the simple hooked-horizontal usually meant
by the label 乛. We replicate the observed GT silhouette.

Approach: use PIL polylines with variable stroke width (line() + circle
end-caps) to get a calligraphic feel. No memory primitives were a clean
match for this compound shape, so we draw fresh from the GT observation
per shared_rules "memory is supplementary" clause.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=6):
    """Draw a polyline with rounded joints/caps."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=BLACK, width=width)
    for x, y in points:
        r = width / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Top-left small hook / flick (the little curved tick at top-left)
# From ASCII: small piece around (85-95, 100-115)
stroke([(85, 100), (95, 110), (100, 118)], width=6)

# --- Left vertical (the main left wall)
# From ASCII: x ~ 92 from y=110 down to ~y=245, then curls right
left_vert = [
    (92, 108),
    (92, 140),
    (92, 180),
    (92, 210),
    (94, 230),
    (100, 245),
    (115, 254),
    (140, 258),
    (170, 258),
    (200, 256),
    (225, 250),
]
stroke(left_vert, width=7)

# --- Middle horizontal-fold stroke (the shelf with hook)
# horizontal going up-right from x~100 y=145 to x~170 y=130, then hooks down-left
mid_shelf = [
    (100, 148),
    (130, 140),
    (155, 133),
    (175, 128),
    (180, 132),
    (175, 145),
    (168, 155),
    (158, 162),
]
stroke(mid_shelf, width=6)

# --- Right ascending vertical (short piece on the right)
# From ASCII: at x~220, from y=205 up... actually reading again, it's a piece
# going from bottom-right sweep UP to about y=205
right_asc = [
    (225, 250),
    (223, 235),
    (222, 220),
    (222, 205),
]
stroke(right_asc, width=7)

# Save
img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0007_乛/01_乛.png")

"""Draw 毋 (4-画 radical) at 300x300, white bg, black ink.

Structure decomposition from GT:
- Overall square-ish body ~55–235 x, ~55–240 y.
- Four named strokes (4画):
  1. 竖折 — left wall descends, then a horizontal turning right at
     the bottom of the small inner box (upper portion of glyph).
  2. 横折钩 — top 横 across the upper box + right vertical descending
     with a small leftward hook at the bottom of the right wall.
  3. 横 — long horizontal spanning through the whole body, extends
     slightly past both side walls.
  4. 撇 — long diagonal from upper-right slashing down to lower-left,
     crossing through the body.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=6):
    """Draw a thick polyline with rounded joints."""
    d.line(pts, fill="black", width=width, joint="curve")
    # end-caps
    r = width / 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


# Layout constants — taller box matching GT proportions
LEFT_X = 80
RIGHT_X = 220
TOP_Y = 55
MID_Y = 155         # y of the middle long 横
BOX_BOTTOM_Y = 235  # bottom of the outer box (near canvas base)

# --- Stroke 1: 竖折 (left wall descends + short turn right at bottom) ---
# left vertical from top down past middle to bottom, then a short
# horizontal turning right (this becomes the inner bottom, ends inside
# the box roughly at middle x).
stroke([(LEFT_X + 4, TOP_Y + 4),
        (LEFT_X - 2, MID_Y),
        (LEFT_X, BOX_BOTTOM_Y),
        (LEFT_X + 60, BOX_BOTTOM_Y - 4)], width=5)

# --- Stroke 2: 横折钩 (top 横 across + right wall descends + small hook) ---
stroke([(LEFT_X + 4, TOP_Y - 3),
        (RIGHT_X - 4, TOP_Y + 4),         # top horizontal, slight down-tilt
        (RIGHT_X + 3, TOP_Y + 18),        # shoulder dab
        (RIGHT_X - 4, BOX_BOTTOM_Y - 8),  # descend right wall almost to bottom
        (RIGHT_X - 22, BOX_BOTTOM_Y - 2)],# small leftward hook flick
       width=5)

# --- Stroke 3: 横 long middle horizontal, extends past BOTH walls ---
stroke([(LEFT_X - 25, MID_Y + 4),
        (RIGHT_X + 20, MID_Y - 3)], width=5)

# --- Stroke 4: 撇 long diagonal top-right slashing to bottom-left,
#     crosses body (starts above/near top-right, ends outside bottom-left) ---
stroke([(RIGHT_X - 20, TOP_Y + 40),
        (LEFT_X - 20, BOX_BOTTOM_Y + 15)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_125_毋/01_毋.png")

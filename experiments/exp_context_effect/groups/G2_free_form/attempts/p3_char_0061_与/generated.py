"""Render 与 (3 strokes).

Stroke order:
1. 短撇 / 短横 — small top-left mark, slanting down-left slightly
   (in GT it looks like a tiny drop).
2. 竖折折钩 / 横折折钩 — the main frame: middle horizontal (rising
   right), turns down for right column, hooks up-left at bottom.
3. 长横 — long bottom horizontal extending past the frame on the left.

Larger scale to fill the canvas per GT proportions.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=8):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=width)
    r = width // 2
    for (x, y) in points:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- Stroke 1: top-left short mark (a small vertical-drop / short 撇) ---
stroke([(115, 55), (110, 90)], width=7)

# --- Stroke 2: main frame — 横折折钩 ---
# Middle horizontal starts on the left, rises slightly to the right,
# then turns down (right column, slight outward bow),
# then hooks up-left at bottom.
frame_pts = [
    (95, 135),    # start of middle horizontal (left)
    (215, 118),   # end of middle horizontal (rises slightly to the right)
    (230, 250),   # right column comes down (slight outward)
    (195, 275),   # hook curls down-left at bottom
]
stroke(frame_pts, width=9)

# --- Stroke 3: long bottom 横 crossing through ---
# Extends beyond the frame on the left, ends just inside the right column.
stroke([(45, 225), (225, 215)], width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0061_与/01_与.png")

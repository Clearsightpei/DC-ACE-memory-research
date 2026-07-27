"""Render 丨 (vertical stroke) to a 300x300 PNG.

The GT shows a vertical stroke slightly curving into the entry at the
top-left (like a brush 'entry' hook), then descending straight down.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Main vertical stroke: near horizontal center, spans most of the vertical.
# GT shows the stroke top around y=60 curving up-left slightly, and bottom
# around y=260. Slight taper via layered strokes.
cx = 148  # slight left of center (matches GT)

# Small entry curve at top: a short diagonal coming in from upper-left,
# then a smooth transition into vertical.
entry_points = [
    (cx - 8, 62),
    (cx - 5, 72),
    (cx - 2, 82),
    (cx, 92),
]
for i in range(len(entry_points) - 1):
    draw.line([entry_points[i], entry_points[i + 1]], fill="black", width=5)

# Main vertical body
draw.line([(cx, 90), (cx, 260)], fill="black", width=5)

# Slight rounded bottom (taper) — nothing dramatic, GT ends fairly cleanly.
draw.line([(cx, 258), (cx + 1, 264)], fill="black", width=4)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0002_丨/01_丨.png"
img.save(out_path)
print(f"Saved {out_path}")

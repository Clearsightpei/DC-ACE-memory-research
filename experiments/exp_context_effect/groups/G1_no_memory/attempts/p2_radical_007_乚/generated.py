"""Render 乚 radical (1 stroke: vertical drop, curve right, hook up)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

ink = "black"
thick = 8

# Top small entry tick (slight downward-right, like brush landing)
draw.line([(95, 65), (88, 82)], fill=ink, width=thick)

# Vertical body: from ~(90,80) down to ~(95,205) with a very subtle rightward drift
vert = [
    (90, 82),
    (91, 110),
    (92, 140),
    (93, 170),
    (95, 200),
    (98, 218),
]
for i in range(len(vert) - 1):
    draw.line([vert[i], vert[i + 1]], fill=ink, width=thick)

# Rounded corner + horizontal run curving right, then upturn (hook)
curve = [
    (98, 218),
    (108, 232),
    (125, 240),
    (150, 244),
    (180, 246),
    (210, 245),
    (232, 242),
]
for i in range(len(curve) - 1):
    draw.line([curve[i], curve[i + 1]], fill=ink, width=thick)

# Small hook upward at right end
draw.line([(232, 242), (238, 222)], fill=ink, width=thick)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_007_乚/01_乚.png")

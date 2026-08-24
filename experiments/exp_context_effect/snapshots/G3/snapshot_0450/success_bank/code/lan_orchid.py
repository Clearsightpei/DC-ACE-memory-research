# 兰 (lán) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0199_兰/generated.py
# Note: 5 (top 丷 + 3 hengs stacked; thin uniform ink)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

"""兰 (lán, "orchid") — 5 strokes: 丷 on top + 三 (three horizontals) below.

G3 attempt: inline PIL rendering. GT (MMH) shows thin uniform lines,
so we use thin widths (~4-5 px) per P12. Bottom heng is widest.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=5):
    d.line([p0, p1], fill="black", width=w)

# --- 丷 top (mirror-dot pair) ---
# Left stroke: 丶 slanting down-right (short pie-like)
line((122, 78), (140, 110), w=5)
# Right stroke: slanting down-left (short pie ending with slight hook feel)
line((180, 78), (160, 110), w=5)

# --- three horizontals (三 shape) ---
# Upper heng — medium length, just below 丷
line((105, 138), (200, 138), w=5)

# Middle heng — shortest
line((115, 182), (192, 180), w=5)

# Bottom heng — widest, sits low, slight upward tilt then back
line((55,  240), (248, 238), w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0199_兰/01_兰.png")

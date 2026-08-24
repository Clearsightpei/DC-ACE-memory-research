"""
勻 = 勹 (wrap-around bracket) + 二 (two horizontals inside).
Strokes:
  1. 撇 (top-left flick) — short, from ~(115,60) down-left to ~(80,140).
  2. 横折钩 — top 横 from ~(115,75) to ~(210,75); shoulder; 竖 curving
     right then arcing down-left to belly bottom ~(140,225); terminal
     hook flicks UP-and-LEFT (per TIER-0 rule).
  3. Inner 横 (upper) — short horizontal inside, ~(110,140) to (185,140).
  4. Inner 横 (lower) — short horizontal inside, ~(110,180) to (190,180).
Silhouette: tall bracket. Interior populated by two horizontals (this is
the 勻 vs 勺 vs 勹 signature — 勻 has 二 inside).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill="black")

# --- Stroke 1: 撇 (top-left flick) ---
# starts near top-center, throws down-left
pie = [(118, 55), (110, 80), (95, 110), (78, 145)]
brush_line(pie, width=7)

# --- Stroke 2: 横折钩 (wrap bracket) ---
# top 横 from just right of 撇 start
top_h = [(118, 75), (150, 72), (185, 72), (215, 74)]
brush_line(top_h, width=8)
# shoulder + 竖 curving down-right slightly then arcing left
right_curve = [(215, 74), (220, 110), (218, 150), (210, 185), (195, 215), (170, 232), (145, 235)]
brush_line(right_curve, width=8)
# terminal hook flicks UP-and-LEFT (~-110°) — short segment from belly bottom
hook = [(145, 235), (135, 225), (128, 215)]
brush_line(hook, width=8)

# --- Stroke 3: inner 横 (upper) ---
inner1 = [(112, 145), (150, 143), (188, 143)]
brush_line(inner1, width=7)

# --- Stroke 4: inner 横 (lower) ---
inner2 = [(112, 185), (150, 183), (192, 183)]
brush_line(inner2, width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0143_勻/01_勻.png")
print("saved")

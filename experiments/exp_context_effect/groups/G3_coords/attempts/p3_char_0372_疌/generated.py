# BANK_DEVIATION
# skipped: (all bank primitives — 疌 has no direct component match; 聿 not in bank)
# reason: 疌 = 聿-like top over 走-leg bottom; no bank entry fits without extreme
#         transformation. Inlining fresh strokes with thin uniform widths per P12.
# fresh_component: jie_char_9stroke (聿-top + 走-leg composition)

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=3):
    d.line([p1, p2], fill="black", width=w)

def poly(points, w=3):
    for i in range(len(points) - 1):
        line(points[i], points[i + 1], w)

# --- TOP: 聿-like structure ---
# Small tick at very top
line((150, 48), (150, 70), 3)

# Three horizontals stacking the "comb" body of 聿
line((108, 78), (198, 78), 3)      # top bar
line((113, 108), (195, 108), 3)    # middle bar (slightly inset)
line((100, 140), (208, 140), 3)    # widest bar

# Left vertical of the top box
line((113, 78), (110, 140), 3)

# --- MIDDLE horizontal ---
line((78, 170), (222, 170), 3)

# --- CENTRAL vertical piercing top to lower body ---
line((150, 70), (150, 205), 3)

# --- BOTTOM: 走-leg ---
# Short middle-right horizontal (like the horizontal in 走's bottom)
line((150, 200), (200, 202), 3)

# Pie leg from central vertical curving down-left
poly([(150, 205), (138, 220), (120, 240), (95, 262), (72, 275)], 3)

# Long na sweeping down and right from near the pie base
poly([(115, 268), (155, 275), (200, 278), (240, 272), (258, 265)], 3)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0372_疌/01_疌.png")
print("wrote 01_疌.png")

"""G1 render of radical 厂 (2 strokes): horizontal (heng) + left-falling curve (pie).

Revision 1: smoother pie curvature via short segments approximating a cubic-ish
sweep; heng slightly angled up; small dun-bi tuck at the joint where pie leaves.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
TH = 6

def polyline(pts, thickness=TH):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=thickness)
    # round caps
    for p in pts:
        draw.ellipse([p[0]-thickness/2, p[1]-thickness/2,
                      p[0]+thickness/2, p[1]+thickness/2], fill=INK)

# --- Stroke 1: heng (横) --------------------------------------------------
# Angled slightly upward left→right, like the GT.
heng_pts = [
    (90, 102),
    (130, 96),
    (175, 90),
    (220, 84),
    (245, 82),
]
polyline(heng_pts)

# Small dun tuck at the joint (left end of heng, where pie will depart).
# In the GT there's a visible "V" tuck: the heng dips slightly before the pie.
polyline([(90, 102), (96, 112), (92, 108)], thickness=TH)

# --- Stroke 2: pie (撇) ---------------------------------------------------
# Start at joint (~92, 108), gently curve down then sweep left near the bottom.
# Progressive dx increases (in the leftward direction) toward the end.
pie_pts = [
    (92, 108),
    (91, 130),
    (89, 155),
    (85, 180),
    (79, 205),
    (70, 230),
    (58, 253),
    (46, 273),
    (36, 288),
]
polyline(pie_pts)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_014_厂/01_厂.png")

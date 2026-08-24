"""
Render 书 (shū, simplified) at 300x300.

Decomposition (5 written strokes in simplified 书):
1. 横折 — top: short slanted horizontal turning down (top-left hook shape).
2. 竖 (long spine) — long vertical, slight hook flick at bottom-left.
3. 横 — the long middle horizontal bar.
4. 横折 (small, right-side) — a small horizontal at middle-right that
   folds down into a hook (this is the distinctive curl on right of 书).
5. 点 — dot on the upper right.

Consulted TIER-0: 书 not in sibling list. Contains hooks: bottom of
spine flicks UP-and-LEFT (~-110°). Right-side small fold hook also
flicks up-and-left.

Revision-1 fixes vs pass-1:
- Enlarged and slanted the top 横折 more.
- Added the missing small 横折 on the right side of the middle bar
  (this is 书's signature detail — the hooked curl mid-right).
- Elongated bottom-hook flick.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, width=6):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill="black", width=width)
    for (x, y) in points:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# --- Stroke 1: 横折 top (slanted, then bends down) ---
s1 = [(115, 72), (185, 60), (192, 88), (188, 125)]
stroke(s1, width=6)

# --- Stroke 2: long 竖 spine, with hook flick at bottom (UP-LEFT) ---
s2 = [(148, 48), (152, 265), (135, 255), (122, 245)]
stroke(s2, width=7)

# --- Stroke 3: 横 middle horizontal bar, slight rise to the right ---
s3 = [(48, 172), (250, 160)]
stroke(s3, width=6)

# --- Stroke 4: small 横折 on right (signature curl of 书) ---
# short horizontal then folds down and hooks up-left at the end
s4 = [(178, 180), (232, 175), (230, 215), (215, 232), (200, 225)]
stroke(s4, width=6)

# --- Stroke 5: 点 dot upper-right ---
s5 = [(215, 100), (238, 128)]
stroke(s5, width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0148_书/01_书.png")

"""
p3_char_0162_生 — 5 strokes.
Order (standard):
  1. 撇 (short left-falling from upper-center down to left)
  2. 横 (short upper horizontal, crossing the 撇)
  3. 横 (middle horizontal, longer)
  4. 竖 (central vertical from top through to bottom)
  5. 横 (bottom long horizontal, widest of the three)

Layout: character occupies center. Three horizontals stack;
the bottom one is longest, middle in the middle, top short.
Central vertical descends through them all; 撇 kicks out at top-left.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=6):
    """Draw a polyline with rounded joins by dabbing circles + lines."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=width)
    r = width // 2
    for x, y in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# --- Stroke 1: 撇 (long left-falling from top-center down to lower-left) ---
stroke([(155, 55), (140, 85), (115, 130), (80, 180)], width=6)

# --- Stroke 2: 横 (short upper horizontal, slightly rising, crosses 撇) ---
stroke([(140, 90), (200, 82)], width=6)

# --- Stroke 3: 横 (middle horizontal, medium length) ---
stroke([(95, 180), (215, 175)], width=6)

# --- Stroke 4: 竖 (central vertical, from top through to bottom) ---
stroke([(155, 55), (155, 245)], width=6)

# --- Stroke 5: 横 (bottom horizontal, longest of the three) ---
stroke([(55, 250), (255, 245)], width=7)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0162_生/01_生.png"
)
print("saved")

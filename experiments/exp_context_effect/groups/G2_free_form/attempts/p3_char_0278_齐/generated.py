"""
齐 (simplified) - 6 strokes rendering.

Structure (from GT):
- Top: 亠-like cap = 撇 (short down-left) + 捺/点 (short down-right)
  meeting near a peak at the top center.
- Middle: two diagonals forming an X-like crossing —
  a long 撇 (upper-right to lower-left) and a 捺 (upper-left to
  lower-right), converging above a long horizontal.
- A long 横 (horizontal) crossing near mid-height.
- Bottom: a short 丨 (vertical) and a 丿 (short flick) descending
  from the horizontal.

Simple PIL rendering, 300x300 canvas, black brush ~9px.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=9):
    # Draw polyline with rounded joints via ellipse caps
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        r = width // 2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

# --- 1. Top short 撇 (down-left) ---
stroke([(160, 45), (128, 78)], width=8)

# --- 2. Top short 点 (down-right, slightly separated) ---
stroke([(170, 62), (198, 90)], width=8)

# --- 3. Long 撇 (from upper-right down to lower-left, curved) ---
stroke([(215, 95), (180, 130), (140, 170), (85, 220)], width=9)

# --- 4. 捺 / right diagonal (from upper-left down to right, crossing #3) ---
stroke([(110, 100), (150, 130), (200, 155), (250, 168)], width=9)

# --- 5. Long 横 (horizontal across middle-lower) ---
stroke([(45, 180), (270, 183)], width=9)

# --- 6. Short 丿 flick from just above horizontal, down-left ---
stroke([(155, 165), (130, 240)], width=7)

# --- 7. Long 丨 vertical descending well below horizontal, center-right ---
stroke([(180, 185), (180, 275)], width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0278_齐/01_齐.png")
print("saved")

"""
Render 刍 to 01_刍.png at 300x300, white bg, black ink.

Structure (from GT):
- Top portion: two strokes forming a 勹-like cap
    1) short 撇 (small downward-left flick), upper region
    2) a long stroke that starts upper-left, sweeps down and curves
       right along the top/right side of the bottom compartment
       (like a 横折 wrapping around)
- Bottom portion (彐-like, 3 strokes):
    3) top horizontal (inside the wrap)
    4) middle horizontal (shorter)
    5) bottom horizontal (longest, extends beyond right)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(points, width=8):
    """Draw a smooth polyline with rounded joins."""
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill="black", width=width)
    for p in points:
        d.ellipse([p[0] - width // 2, p[1] - width // 2,
                   p[0] + width // 2, p[1] + width // 2], fill="black")


# --- Stroke 1: short 撇 (upper-right, small flick down-left) ---
stroke([(180, 55), (162, 85), (148, 105)], width=7)

# --- Stroke 2: long sweeping stroke (upper-left down, then curving right) ---
# Starts upper-left, descends, then turns right forming the top of the
# lower compartment (横折-like wrap).
stroke([(95, 90), (115, 120), (140, 145), (180, 160),
        (215, 168), (232, 180), (235, 200)], width=8)

# --- Bottom compartment: 3 horizontals (彐-like) ---
# Stroke 3: top horizontal (inside the wrap)
stroke([(120, 190), (218, 192)], width=7)

# Stroke 4: middle horizontal (shorter, inside)
stroke([(115, 225), (218, 227)], width=7)

# Stroke 5: bottom horizontal (longest, extends past right — 一 base)
stroke([(80, 260), (255, 262)], width=8)


import os
out = os.path.join(os.path.dirname(__file__), "01_刍.png")
img.save(out)
print(f"wrote {out}")

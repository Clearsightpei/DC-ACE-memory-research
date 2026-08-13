"""
Render 面 (miàn) at 300x300, black ink on white.

Structural read from GT (9 strokes, standard order):
  1. 一 top horizontal (long, spans most of width, slight rightward taper)
  2. 丿 short pie hanging from left of top horizontal, sweeping down-left
  3. 丨 left vertical of the outer frame (from tail of pie down to bottom)
  4. 𠃍 横折 from right end of top horizontal down to bottom-right (with shoulder dab)
  5. 一 top inner horizontal (spans inside of frame, near the top)
  6. 丨 short inner vertical descending from top inner horizontal
  7. 一 middle inner short horizontal (left portion)
  8. 一 bottom inner short horizontal (left portion)
  9. 一 bottom horizontal closing the frame

Apply TIER-0 F 4-move recipe:
  - teardrop taper on 撇
  - shoulder dab at every 折 joint
  - Bezier for the pie curve
  - no hooks in 面, skip flick rule
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * u * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t * t * t * p3[0]
        y = u * u * u * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t * t * t * p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# --- 1. Top horizontal (long, slight arc) ---
top = bez((45, 55), (110, 52), (180, 52), (255, 58), n=70)
stroke(top, (7, 7))

# --- 2. Short pie 丿 hanging from left-top ---
pie = bez((60, 62), (52, 90), (42, 115), (30, 140), n=60)
stroke(pie, (9, 3))

# --- 3. Left vertical of outer frame ---
left_v = bez((45, 100), (45, 170), (46, 220), (48, 265), n=60)
stroke(left_v, (7, 7))

# --- 4. 横折 top-right corner: shoulder dab then descend ---
dab(248, 60, 6)  # shoulder dab at fold
right_v = bez((248, 62), (250, 130), (250, 200), (250, 265), n=70)
stroke(right_v, (7, 7))

# --- 9. Bottom horizontal closing the frame ---
bottom = bez((48, 265), (120, 265), (190, 265), (250, 265), n=60)
stroke(bottom, (7, 7))

# --- 5. Top inner horizontal ---
inner_top = bez((72, 118), (135, 116), (195, 116), (232, 120), n=50)
stroke(inner_top, (6, 6))

# --- 6. Inner short vertical descending from center of inner top ---
inner_v = bez((150, 122), (150, 165), (150, 205), (150, 245), n=50)
stroke(inner_v, (6, 6))

# --- 7. Middle inner short horizontal (left portion) ---
inner_mid = bez((75, 175), (100, 174), (125, 174), (147, 176), n=40)
stroke(inner_mid, (6, 6))

# --- 8. Bottom inner short horizontal (left portion) ---
inner_bot = bez((75, 225), (100, 224), (125, 224), (147, 226), n=40)
stroke(inner_bot, (6, 6))

# NOTE: GT shows inner short bars only on LEFT side of the middle vertical
# (面's classic 目-with-only-left-bars pattern). Right-side bars removed.

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0443_面/01_面.png")

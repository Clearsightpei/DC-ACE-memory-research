"""
p3_char_0122_五 — G2 attempt 1

Structural read of GT (300x300 canvas):
  Stroke 1: short top 横 — upper region, slight rise
  Stroke 2: 竖/撇 — from top-horizontal down-left to bottom-left area (slight slant)
  Stroke 3: 横折 — internal, forms the 口 middle: horizontal then down (right wall)
  Stroke 4: long bottom 横 — widest, slight rise, ends with subtle terminal thickening

Stroke order for 五: 一, 丨(left-slanting), 𠃍(横折), 一
Uses PIL brush-dab technique (memory principle: brush width ~8-10 at 300 canvas).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=9):
    """Draw a poly-line stroke with rounded joins."""
    d.line(points, fill=BLACK, width=width, joint="curve")
    # dab endpoints for calligraphic feel
    r = width / 2
    for (x, y) in (points[0], points[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Stroke 1: top 横 (short, upper) ---
# Slight rise left→right (calligraphic 横)
stroke([(110, 80), (215, 72)], width=9)

# --- Stroke 2: 竖/撇 — from top 横's left area down-left ---
# In 五 the 2nd stroke slants left as it descends, ending near bottom-left
stroke([(130, 80), (75, 240)], width=10)

# --- Stroke 3: 横折 — inner horizontal then right wall coming down ---
# Middle box: horizontal a bit below vertical midpoint, folds down to meet bottom-横
h_left = (90, 175)
h_right = (220, 168)
v_bottom = (215, 240)
stroke([h_left, h_right, v_bottom], width=10)

# --- Stroke 4: long bottom 横 ---
# Longest stroke, spans nearly full width, slight rise
stroke([(50, 250), (255, 240)], width=11)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0122_五/01_五.png")
print("wrote 01_五.png", W, H)

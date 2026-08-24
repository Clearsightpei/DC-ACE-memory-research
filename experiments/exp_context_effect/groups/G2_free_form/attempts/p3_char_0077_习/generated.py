"""Render 习 (xí) — 3 strokes:
  1. 横折钩 — outer top horizontal, turns down on the right, hook at bottom-left
  2. 撇 (upper inner) — short slanted flick, upper-left inside
  3. 撇 (lower inner) — longer slanted flick, lower-left inside

Layout observed from GT:
  - Top horizontal spans from ~x=70 to ~x=200 at y~90
  - Right vertical drops from (200,90) to ~ (200,235)
  - Bottom hook flicks left from ~(200,235) to ~(175,255)
  - Upper 撇: from ~(110,130) sloping down-left to ~(90,150)
  - Lower 撇: from ~(160,175) sloping down-left to ~(85,225)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 7


def stroke(points, width=WIDTH):
    draw.line(points, fill=INK, width=width, joint="curve")
    # round caps
    for (x, y) in points:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# --- Stroke 1: 横折钩 (outer shape) ---
# top horizontal, slight upward tilt at right end matches GT
top_h = [(70, 92), (120, 88), (170, 86), (200, 88)]
# turn down (折) — corner near (205, 90)
turn_corner = (205, 92)
# vertical descent (slightly leaning), ends near (200, 240)
down = [turn_corner, (203, 130), (201, 180), (199, 225), (198, 240)]
# hook (钩) — flick left-down at the bottom
hook = [(198, 240), (188, 250), (175, 255)]

stroke(top_h + [turn_corner])
stroke(down)
stroke(hook)

# --- Stroke 2: upper inner 撇 (short) ---
upper_pie = [(115, 130), (105, 140), (92, 152)]
stroke(upper_pie, width=6)

# --- Stroke 3: lower inner 撇 (long) ---
lower_pie = [(160, 170), (140, 185), (115, 205), (90, 225)]
stroke(lower_pie, width=7)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0077_习/01_习.png"
)
print("wrote 01_习.png")

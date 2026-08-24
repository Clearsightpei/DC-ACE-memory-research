"""
Render 冎 (guǎ) — a 7-stroke character.

Structure (from GT):
- Small 竖 flick on lower-left (like start of 骨's bottom)
- A top-right box formed by 竖 + 横折 with an inner short 横
- A long sweeping stroke crossing the middle horizontally then hooking
  down on the right (横折 with 撇-like tail)
- Small internal short marks

Approach: PIL polylines with a modest brush thickness.
Memory consulted: drawer_memory PIL brush technique; hook-flick rule
(hooks flick UP-and-LEFT into interior). No sibling checklist match.
"""
from PIL import Image, ImageDraw

W = 300
img = Image.new("RGB", (W, W), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 6  # brush thickness


def stroke(pts, width=TH):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # dab endpoints for calligraphic feel
    r = width // 2
    for (x, y) in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Top box (wider, roughly 口-shape, with an inner short 横) ---
# left vertical (short 竖)
stroke([(115, 55), (110, 145)])
# top horizontal + right vertical (横折), extends to upper-right
stroke([(115, 55), (230, 60), (232, 150)])
# inside short horizontal (the small dash)
stroke([(140, 105), (205, 108)])

# --- Long 撇 sweeping down-left from the box's lower-left area ---
stroke([(110, 140), (70, 245)])

# --- Long sweeping bottom stroke: 横 across then curving down-right with hook ---
stroke([(50, 200), (210, 205), (245, 215), (265, 250)])

# --- Small internal tick / stub inside the lower area (like part of 冎 interior) ---
stroke([(135, 175), (170, 178)])

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0209_冎/01_冎.png"
img.save(out)
print("wrote", out)

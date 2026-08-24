"""
区 (qū) — 4 strokes: 一, 丿, ㇏, ㄈ-shape (竖折 = vertical + horizontal turn).
Structure: 匚 radical (three-sided box open right) enclosing 乂 (X made of 撇+捺).

GT observations:
- top 横 is short-ish, slightly angled, does not extend to the far right
- 乂 sits inside, its 撇 starts high-left, its 捺 crosses it going down-right
- 竖折 forms left side + bottom; the bottom extends further right than the top
- 匚 is open on the right side (right side not closed)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)

def dab_line(pts, width=8):
    """Draw a smooth line with dabs to approximate brushiness."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=BLACK, width=width)
    for x, y in pts:
        d.ellipse([x - width//2, y - width//2, x + width//2, y + width//2], fill=BLACK)

# Stroke 1: 横 top of 匚 — starts around (75, 70), goes right to about (215, 65)
dab_line([(78, 72), (140, 68), (215, 66)], width=7)

# Stroke 2: 撇 of 乂 — starts high-mid, curves down-left. Crossing target near center (~150, 175).
dab_line([(170, 100), (155, 135), (140, 165), (120, 200), (100, 235)], width=7)

# Stroke 3: 捺 of 乂 — starts high-left of 撇 origin, sweeps down-right, crosses 撇 near center.
dab_line([(115, 110), (140, 145), (170, 180), (200, 215), (220, 240)], width=7)

# Stroke 4: 竖折 — left vertical from just below top 横 down, then turns right along bottom
# vertical: (80, 78) down to (75, 258); then bottom horizontal: (75, 258) to (240, 253)
dab_line([(82, 80), (80, 130), (78, 190), (76, 240), (75, 260)], width=7)
dab_line([(75, 260), (130, 258), (190, 256), (240, 253)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0142_区/01_区.png")
print("saved")

"""Render 海 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left radical 氵 (three-dots water) ----
# Upper dot (short slash \)
line([(55, 75), (72, 92)], width=6)
# Middle dot (short slash \)
line([(42, 115), (60, 132)], width=6)
# Lower rising dot (/ pointing up-right)
line([(50, 190), (78, 172)], width=6)

# ---- Right side 每 ----
# 1. 𠂉 top: short horizontal-slash (top of hat)
line([(150, 60), (200, 50)], width=6)
# 2. 丿 long left-falling from top
line([(190, 55), (110, 130)], width=6)

# 3. 母 top horizontal (long)
line([(130, 130), (255, 128)], width=6)

# 4. 母 left vertical curving down and hook
line([(140, 128), (145, 245), (170, 258)], width=6)

# 5. 母 right vertical with hook at bottom
line([(245, 130), (250, 235), (232, 250)], width=6)

# 6. Middle horizontal inside 母 (the crossing 一)
line([(115, 205), (265, 200)], width=6)

# 7. Two dots inside 母
line([(175, 160), (183, 175)], width=5)
line([(215, 160), (223, 175)], width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0511_海/01_海.png")
print("done")

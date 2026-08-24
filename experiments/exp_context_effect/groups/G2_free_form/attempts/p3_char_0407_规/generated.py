"""
规 (guī) — Phase 3 character, item p3_char_0407_规

Composition: 夫 (left, compressed) + 见 (right).

# SIGNATURE CHECK (per sibling_signature_checklist.md, applied to
# component 见 via TIER-0.D compound-sibling rule):
#   right-component = 见
#   bit = 冂 + ONE 横 IN LOWER THIRD of box + 撇+竖弯钩 legs
#        (vs 贝 which has TWO internal 横 + straight ㅅ legs)
#   flick = 竖弯钩 terminal: UP-and-LEFT after the arc (~-110°)

Left dagger stroke sequence for 夫 (compressed to left-half column):
  1) top 横 (short)
  2) bottom 横 (longer)
  3) 撇 crossing both, down-left to bottom
  4) short 提/点 on right side of 撇 (捺 -> tick when compressed left)

Right sequence for 见:
  5) 竖 left wall of 冂
  6) 横折 top + right wall
  7) interior 横 in lower third
  8) 撇 left leg from bottom-left of box
  9) 竖弯钩 right leg with UP-LEFT hook
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# ---------------- LEFT: 夫 (columns ~ x 30-140) ----------------

# Stroke 1: top 横 (shorter)
d.line([(45, 100), (120, 95)], fill=BLACK, width=LW)

# Stroke 2: bottom 横 (longer)
d.line([(25, 155), (140, 150)], fill=BLACK, width=LW)

# Stroke 3: 撇 — from upper-right of 夫 region slanting down-left
# In GT the 撇 ends around the baseline of the character (~y=265), not below
d.line([(95, 55), (85, 110), (70, 165), (50, 220), (28, 265)], fill=BLACK, width=LW)

# Stroke 4: 短捺/点 — from mid of 撇 rising to lower-right (compressed 捺 -> tick)
d.line([(80, 175), (140, 235)], fill=BLACK, width=LW)

# ---------------- RIGHT: 见 (columns ~ x 155-275) ----------------

# Stroke 5: 竖 — left wall of 冂
d.line([(165, 60), (160, 200)], fill=BLACK, width=LW)

# Stroke 6: 横折 — top then right wall
d.line([(160, 58), (270, 55)], fill=BLACK, width=LW)
d.line([(270, 55), (265, 205)], fill=BLACK, width=LW)

# Stroke 7: interior 横 (ONE, in lower third of box)
d.line([(168, 145), (262, 145)], fill=BLACK, width=LW)

# Stroke 8: 撇 — left leg from bottom-left of box slanting down-left
d.line([(162, 200), (145, 275)], fill=BLACK, width=LW)

# Stroke 9: 竖弯钩 — right leg from mid-box descending, curving right, hook UP-LEFT
curve = [
    (220, 145),
    (220, 190),
    (222, 225),
    (228, 255),
    (245, 275),
    (270, 280),
    (280, 273),
]
d.line(curve, fill=BLACK, width=LW)
# Hook: UP-and-LEFT flick
d.line([(280, 273), (268, 258)], fill=BLACK, width=LW)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0407_规/01_规.png"
img.save(out)
print("saved", out)

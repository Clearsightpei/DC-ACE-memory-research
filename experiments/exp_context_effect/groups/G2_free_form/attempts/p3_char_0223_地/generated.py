"""
地 = 提土旁 (left) + 也 (right).

# SIGNATURE CHECK (sibling_signature_checklist, compound rule D):
# 土 as COMPONENT (提土旁): 竖 extends slightly above the top 横; the
# bottom stroke becomes 提 (upward tick, tilts up-right), still LONGER
# than the top 横 (~1.5x). Do NOT flatten the 提 into a 横.
#
# 也 (right): three strokes: (1) 横折钩 - horizontal, then fold down,
# hook UP-LEFT at terminal. (2) 竖 sits inside body, starts at top 横,
# drops down and hooks slightly. Actually 也's strokes are:
#   (a) 横折钩 (top-right frame + hook)
#   (b) 竖 (leftmost vertical, starts above top 横, drops down)
#   (c) 竖弯钩 (starts on top 横, drops, curves right along bottom,
#       hook flicks UP-LEFT).
# All hooks flick UP-and-LEFT per TIER-0 B rule.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def line(pts, w=LW):
    d.line(pts, fill=BLACK, width=w)

# ============= 提土旁 (left component: 土 as radical) =============
# 竖 (vertical stem — extends slightly above top 横 and below to meet 提)
line([(80, 105), (80, 205)], w=LW)
# Top 短横 (short horizontal, sits partway down the 竖)
line([(55, 130), (110, 128)], w=LW)
# 提 (upward tick — bottom stroke; longer than top 横, tilts up-right)
line([(45, 215), (140, 185)], w=LW)

# ============= 也 (right component) =============
# Stroke (b): 竖 — leftmost vertical inside 也, starts above top 横
line([(160, 105), (158, 220)], w=LW)

# Stroke (a): 横折钩
# horizontal top
line([(160, 118), (260, 115)], w=LW)
# fold: down the right side
line([(260, 115), (255, 235)], w=LW)
# hook: flick UP-and-LEFT at bottom-right terminal
line([(255, 235), (240, 220)], w=LW)

# Stroke (c): 竖弯钩
# vertical descent (starts on top 横, inside the frame)
line([(210, 118), (210, 220)], w=LW)
# curve rightward along bottom
line([(210, 220), (225, 245), (255, 255), (280, 250)], w=LW)
# hook flick UP-and-LEFT at terminal
line([(280, 250), (270, 232)], w=LW)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0223_地/01_地.png"
img.save(out)
print("saved", out)

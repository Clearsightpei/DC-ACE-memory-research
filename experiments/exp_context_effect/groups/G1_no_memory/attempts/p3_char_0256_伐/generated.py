from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# 伐 = 亻(left radical) + 戈(right)

# --- 亻 (left, person radical) ---
# Slanting downward stroke (撇) - from upper right to lower left
stroke([(90, 75), (55, 210)], w=6)
# Vertical stroke (竖) - joins the pie about a third down
stroke([(78, 130), (78, 265)], w=6)

# --- 戈 (right side) ---
# Top horizontal (横) - slightly slanted
stroke([(130, 105), (245, 95)], w=6)
# Left downward slanting stroke (撇) - from horizontal down-left
stroke([(160, 90), (120, 260)], w=6)
# Long diagonal hook (斜钩) - long curve from upper mid down to lower-right with hook up
stroke([(175, 115), (210, 180), (250, 245), (275, 235), (280, 220)], w=6)
# Small top-right dot (点)
stroke([(255, 75), (270, 95)], w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0256_伐/01_伐.png")

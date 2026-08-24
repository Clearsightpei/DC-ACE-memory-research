from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(pts, width=LW):
    d.line(pts, fill="black", width=width)

# 身 (7 strokes) — tall body with long sweeping 撇 through it

# 1. Top-left short 撇 (little tick at top)
line([(150, 45), (135, 70)], width=LW)

# 2. Top horizontal + right vertical fold of the body (横折)
line([(120, 78), (175, 72)], width=LW)     # top horizontal
line([(175, 72), (170, 210)], width=LW)    # right vertical descending

# 3. Left vertical of body (撇 slightly)
line([(120, 78), (108, 220)], width=LW)

# 4. First inner horizontal
line([(120, 120), (170, 118)], width=LW)

# 5. Second inner horizontal
line([(115, 165), (170, 163)], width=LW)

# 6. Bottom horizontal closing body (small)
line([(108, 220), (170, 210)], width=LW)

# 7. Long 撇 — from upper right sweeping down-left across entire char
line([(200, 65), (55, 275)], width=LW)

# The last stroke of 身 is actually a long horizontal extending right at bottom
# Actually 身 = 7 strokes: 撇, 横折钩, 横, 横, 横, 撇
# The final 撇 replaces a hypothetical bottom - so 7 strokes total. Skip extra.

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0311_身/01_身.png")

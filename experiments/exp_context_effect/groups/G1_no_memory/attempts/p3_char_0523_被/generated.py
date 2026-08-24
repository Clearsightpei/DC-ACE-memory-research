"""G1 render of 被 (character) to 300x300 PNG."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ===== Left radical 衤 (5 strokes) =====
# 1. top dot 点 (small slanted stroke)
line([(78, 45), (88, 62)], 5)
# 2. horizontal 横 (short, slight tilt up-right)
line([(45, 90), (115, 82)], 5)
# 3. left-falling 撇 - long, from near top going down-left
line([(85, 70), (30, 240)], 5)
# 4. vertical 竖 - from horizontal down
line([(95, 82), (95, 250)], 5)
# 5. left dot 点 (mid-left of radical)
line([(60, 145), (48, 175)], 5)
# 6. right dot 点 (mid-right of radical, slanting down-right)
line([(105, 155), (125, 185)], 5)

# ===== Right part 皮 (5 strokes) =====
# 1. short slanted top stroke (horizontal-ish)
line([(170, 55), (200, 45)], 5)
# 2. horizontal-hook 横钩: horizontal top of 皮, hooks down
line([(160, 78), (255, 70)], 5)
line([(255, 70), (245, 90)], 5)  # hook
# 3. long 撇 - sweep from top-left of 皮 down to lower-left
line([(175, 78), (140, 265)], 5)
# 4. small enclosed 又-like: short horizontal + vertical forming a box
line([(190, 130), (240, 128)], 4)
line([(240, 128), (238, 175)], 4)
line([(190, 175), (238, 175)], 4)
# 5. 捺 (right-falling) - from inside sweeping down-right
line([(210, 155), (280, 260)], 6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0523_被/01_被.png")
print("saved")

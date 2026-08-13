"""G1 render of 把 (bǎ) — 7 strokes: 扌 (3) + 巴 (4)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts, w=LW):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- Left radical 扌 (提手旁) ----
# 1) short horizontal (heng) — slanting slightly up
line([(40, 100), (110, 92)], LW)
# 2) vertical hook (shu-gou) — long vertical with small hook at bottom-left
line([(78, 65), (78, 215)], LW)
line([(78, 215), (62, 200)], LW)  # gou hook
# 3) rising stroke (ti) — from lower-left up to right, crossing the vertical
line([(38, 175), (118, 148)], LW)

# ---- Right component 巴 ----
# Frame roughly x: 145..250, y: 70..235
LX, RX = 150, 245
TY, BY = 78, 225
MY = 155  # middle horizontal

# Stroke 1: 横折 — top horizontal + down the right side
line([(LX, TY), (RX, TY)], LW)
line([(RX, TY), (RX, BY - 20)], LW)  # right vertical, stops a bit above bottom for hook

# Stroke 2: 竖 — left vertical
line([(LX, TY), (LX, BY)], LW)

# Stroke 3: 横 (middle inner horizontal, not touching right side)
line([(LX, MY), (RX - 10, MY)], LW)

# Stroke 4: 竖弯钩 — bottom horizontal + rise + hook out to right
# Actually 巴's 4th stroke: from bottom of left vertical, goes right across bottom, curves up on right, hooks
line([(LX, BY), (RX - 20, BY)], LW)
line([(RX - 20, BY), (RX, BY - 15)], LW)  # curve up
line([(RX, BY - 15), (RX, BY - 30)], LW)  # continue up
line([(RX, BY - 30), (RX + 15, BY - 45)], LW)  # hook up-right

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0321_把/01_把.png"
img.save(out)
print("saved", out)

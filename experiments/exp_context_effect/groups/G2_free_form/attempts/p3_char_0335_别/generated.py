"""
p3_char_0335_别
别 = 另 (kou on top-left + li on bottom-left) + 刂 (立刀旁, right)
Left component 另 occupies ~left 60%, right 刂 ~right 40%.
Top of 另 is 口 (small mouth), bottom is 力 (with a diagonal 撇 crossing).
Right 刂: short vertical (left) + long vertical-hook (right).
Hook flick UP-and-LEFT per Tier-0.B.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def line(p1, p2, w=6):
    d.line([p1, p2], fill=INK, width=w)

def poly(pts, w=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=w)

# ---------- LEFT: 另 (口 on top, 力 on bottom) ----------
# 口 (top-left): a small rectangle-like mouth.
# Place around x=45..130, y=55..115
kx1, ky1 = 50, 60
kx2, ky2 = 130, 115
# left vertical
line((kx1, ky1), (kx1, ky2), 6)
# top horizontal + right small fold (as one 横折)
poly([(kx1 - 2, ky1), (kx2, ky1 - 2), (kx2, ky2)], 6)
# bottom horizontal
line((kx1 - 2, ky2), (kx2 + 2, ky2), 6)

# 力 (bottom-left): 横折钩 + 撇
# 横折钩: horizontal shoulder starting mid-left, folding down into a curved hook.
poly([(45, 145), (150, 143), (152, 155), (148, 200), (135, 230)], 7)
# hook flick up-and-left at end of vertical
poly([(135, 230), (115, 218)], 7)

# 撇 across 力: from the shoulder near right, sweeping down-left through the frame
poly([(115, 155), (95, 195), (65, 245), (40, 280)], 6)

# ---------- RIGHT: 刂 (立刀旁) ----------
# Short left vertical (短竖): around x=200, y=80..160
line((200, 85), (200, 165), 7)

# Long right vertical-hook (竖钩): around x=245, y=55..255, with hook up-left
poly([(245, 55), (245, 255)], 8)
# hook flick up-and-left at bottom
poly([(245, 255), (225, 240)], 7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0335_别/01_别.png")
print("saved")

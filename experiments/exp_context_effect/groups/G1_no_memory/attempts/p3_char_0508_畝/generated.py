from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

# ============================================================
# 畝 = 亠 above 田 (left) + 攵 (right)
# GT layout: 亠 spans across the top;
#            田 sits below 亠 on the LEFT;
#            攵 occupies the RIGHT side, extending from below 亠
#            top down to the bottom-right (its 捺 sweeps far right).
# ============================================================

# ---- Top: 亠 ----
# small dot (点) at top-left
line((70, 35), (85, 55), 4)
# long horizontal (heng) spanning most of the width
line((40, 70), (215, 65), 5)

# ---- Left component: 田 ----
L, T, R, B = 45, 95, 145, 200
# outer rectangle
line((L, T), (R, T))          # top
line((L, B), (R, B))          # bottom
line((L, T), (L, B))          # left
line((R, T), (R, B))          # right
# inner cross
mx = (L + R) // 2
my = (T + B) // 2
line((mx, T), (mx, B))        # inner vertical
line((L, my), (R, my))        # inner horizontal

# ---- Right component: 攵 ----
# short piě at top (小撇)
line((175, 85), (160, 110), 4)
# horizontal (heng) short
line((165, 105), (215, 100), 4)
# long piě sweeping from upper-right down to lower-left middle
line((200, 90), (150, 210), 5)
# nà — long right-sweeping diagonal from mid to far bottom-right
line((180, 165), (280, 275), 5)

out = os.path.join(os.path.dirname(__file__), "01_畝.png")
img.save(out)
print("Saved", out)

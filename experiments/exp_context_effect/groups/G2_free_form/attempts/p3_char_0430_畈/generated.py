"""p3_char_0430_畈 — G2 attempt.

畈 = 田 (left) + 反 (right).
Left 田: small rectangle with cross inside.
Right 反: top-left 撇 anchor, top 横, inner 撇, 捺 sweep down-right.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=6):
    """Draw a smooth stroke through pts (list of (x,y))."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill=BLACK)


# ------------------ 田 (left side, ~x 35..135, y 90..215) ------------------
L, R, T, B = 40, 130, 95, 215
# outer rectangle: 竖 (left), 横折 (top+right), 横 (bottom)
# stroke 1: left 竖
stroke([(L, T), (L, B)], width=6)
# stroke 2: 横折 (top then right down)
stroke([(L, T), (R, T + 2), (R + 2, B)], width=6)
# stroke 3: inner 竖 middle
mx = (L + R) // 2
stroke([(mx, T + 3), (mx, B - 2)], width=5)
# stroke 4: inner 横 middle
my = (T + B) // 2
stroke([(L + 3, my), (R - 2, my)], width=5)
# stroke 5: bottom 横 (close the box)
stroke([(L, B), (R, B)], width=6)

# ------------------ 反 (right side, ~x 150..285, y 60..280) ----------------
# stroke A: top-left 撇 (starts upper, sweeps down-left long)
stroke([(180, 70), (175, 110), (162, 160), (145, 215), (128, 275)], width=6)
# stroke B: 横 across the top (from top of 撇 going right)
stroke([(180, 75), (220, 78), (255, 88)], width=6)
# top-right slight hook down
stroke([(255, 88), (252, 105)], width=5)
# stroke C: inner 撇 of 又 (from right-top going down-left)
stroke([(215, 130), (200, 165), (180, 205), (165, 240)], width=6)
# stroke D: 捺 (from mid, sweeps down-right)
stroke([(200, 170), (225, 205), (250, 240), (278, 278)], width=7)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0430_畈/01_畈.png"
img.save(out)
print("saved", out)

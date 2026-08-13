"""G1 render of 疤 (scar) — 疒 radical + 巴 (revised)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 5


def line(pts, w=W):
    d.line(pts, fill="black", width=w)


def curve_pts(p0, p1, p2, n=24):
    return [
        (
            (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1],
        )
        for t in (i / n for i in range(n + 1))
    ]


# ================= 疒 (upper radical, wraps down-left) =================
# 1. Small top 点 (short slant)
line([(140, 40), (155, 60)])

# 2. Long horizontal (top of 疒) — flat, slightly rightward
line([(75, 80), (245, 78)])

# 3. Left 撇 diagonal (long slant sweeping down-left)
line(curve_pts((150, 80), (95, 165), (55, 265)))

# 4. Two small left dots (inside/under the top horizontal, on left)
line([(95, 130), (108, 148)])   # upper dot
line([(75, 175), (90, 195)])    # lower dot

# ================= 巴 (interior, under horizontal, right side) =================
# 巴 sits mostly to the right of/under the sweep.
# 5. Left vertical of 巴 (short 竖)
line([(150, 115), (150, 230)])

# 6. 横折 top: goes right then down (top of the small box)
line([(150, 115), (225, 115)])
line([(225, 115), (225, 165)])

# 7. Middle horizontal crossing (inside)
line([(150, 165), (225, 165)])

# 8. 竖弯钩 — the bottom sweeping curve with hook
#     Start below middle-cross on left, go down, curve right, hook up
sweep = curve_pts((150, 230), (170, 275), (245, 260))
line(sweep)
# small hook up at end
line([(245, 260), (245, 235)])

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_疤.png")
img.save(out)
print("wrote", out)

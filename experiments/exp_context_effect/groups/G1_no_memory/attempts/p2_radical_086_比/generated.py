"""
G1 render of radical 比 (4 strokes).
Structure: left component (短横 + 竖提) + right component (撇 + 竖弯钩).
Revision: tighter left join, right 撇 clearly rises above right vertical,
smoother 竖弯钩 with cleaner tiny hook.
Renders 300x300 white background, black ink via PIL.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 6  # stroke thickness


def line(pts, width=TH):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# ---- LEFT COMPONENT (x ~ 60..140) ----
# Stroke 2 first (visually): 竖提 vertical descending then flick up-right.
# We'll draw them in a natural order; visual overlap is fine.
# Vertical portion of 竖提
line([(78, 95), (85, 225)], width=TH)
# 提 flick at bottom (up-right)
line([(85, 225), (140, 205)], width=TH)

# Stroke 1: 短横 crossing the vertical near the middle-upper region
line([(72, 138), (140, 128)], width=TH)

# ---- RIGHT COMPONENT (x ~ 150..255) ----
# Stroke 3: 撇 — starts high, sweeps down-left. Head above right vertical top.
line([(215, 78), (160, 232)], width=TH)

# Stroke 4: 竖弯钩
# Vertical portion (starts to the right of and below the 撇 head)
line([(225, 118), (228, 210)], width=TH)
# Curve bending right along the bottom
line([(228, 210), (245, 235)], width=TH)
line([(245, 235), (272, 232)], width=TH)
# Small upward hook
line([(272, 232), (270, 218)], width=TH)

out_path = os.path.join(os.path.dirname(__file__), "01_比.png")
img.save(out_path)
print(f"wrote {out_path}")

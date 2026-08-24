"""
仞 (rèn) — p3_char_0183
Structure: 亻 (LEFT, ~40% width) + 刃 (RIGHT)
  亻 = 撇 + 竖 (per form_catalog: tall-narrow left-position radical)
  刃 = 横折钩 (top+right, hook flicks UP-LEFT) + body-crossing 撇 + interior 丶
5 strokes total.
Notes from memory_index TIER-0:
  - hook of 横折钩 flicks UP-and-LEFT (~-105° to -120°)
  - 亻: 撇 shorter, starts at ~x=100 y=60, ends ~x=60 y=170; 竖 straight down from 撇 mid
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(pts, width_start=6, width_end=6):
    """Draw a polyline with tapered width via segment dabs."""
    n = len(pts)
    if n < 2:
        return
    for i in range(n - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        segs = 40
        for s in range(segs + 1):
            t = s / segs
            # position along whole polyline
            frac = (i + t) / (n - 1)
            w = width_start + (width_end - width_start) * frac
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# ---- 亻 (left radical) ----
# Stroke 1: 撇 — starts ~top ~(105, 55), diagonal down-left to ~(55, 175)
brush_line([(108, 55), (95, 90), (78, 130), (58, 175)], width_start=5, width_end=4)

# Stroke 2: 竖 — starts near 撇 mid-body ~(88, 105), drops straight down to ~(88, 245)
brush_line([(88, 105), (88, 175), (88, 245)], width_start=7, width_end=6)

# ---- 刃 (right component) ----
# Stroke 3: 横折钩 — 横 from (135, 70) rightward to (240, 70), shoulder,
# then 竖 down to (240, 210), then hook flicks UP-and-LEFT to (220, 195)
# Break into: 横 + fold + 竖 + hook
brush_line([(135, 70), (180, 68), (240, 70)], width_start=6, width_end=7)  # 横
brush_line([(240, 70), (242, 130), (238, 210)], width_start=7, width_end=8)  # 竖 (turn)
# hook flick up-left
brush_line([(238, 210), (225, 200), (215, 190)], width_start=8, width_end=3)

# Stroke 4: 撇 — body-crossing diagonal, starts upper inside area ~(200, 95)
# throws down-left through the belly out past bottom to ~(145, 265)
brush_line([(200, 95), (190, 140), (175, 195), (145, 265)], width_start=5, width_end=3)

# Stroke 5: 丶 (dot) — small teardrop inside interior of 刃 (LEFT of 撇, upper area)
# distinctly separated from strokes 3 and 4; short down-right teardrop
brush_line([(158, 115), (168, 128)], width_start=3, width_end=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0183_仞/01_仞.png")
print("wrote 01_仞.png")

"""
p3_char_0374_疙 — G2 attempt (revision 1)

Structure:
  疙 = 疒 (sickness radical, top-left, tall) + 乞 (mid/bottom-right)
  疒 = top 点 + long 横 + long left-falling 撇 + two small inner 点
  乞 = 短横 + 短撇 + 乙 (横折弯钩)

Revision notes:
  - Make inner 疒 dots look like real dots (tapered strokes), not lines
  - Smooth the 乙 arc with more curve points
  - Tighten the 短横 on 乞 so it doesn't overshoot
  - Sharper up-left flick on the 乙 hook
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

def dot_stroke(x1, y1, x2, y2, w1=3, w2=7):
    """Tapered dot rendered as a short thickening line."""
    n = 6
    for i in range(n):
        t = i / (n - 1)
        cx = x1 + (x2 - x1) * t
        cy = y1 + (y2 - y1) * t
        r = w1 + (w2 - w1) * t
        d.ellipse((cx - r/2, cy - r/2, cx + r/2, cy + r/2), fill="black")

# ---------- 疒 radical (top-left, spanning most of the height) ----------

# top 点 — short down-right diagonal dot above the horizontal
dot_stroke(118, 50, 132, 68, w1=3, w2=7)

# top 横 (long horizontal, slight upward tilt to the right)
stroke([(88, 95), (225, 85)], width=5)

# long left-falling 撇 — starts at left end of 横, sweeps down-left, curving
stroke([(93, 90), (78, 140), (58, 200), (32, 275)], width=6)

# two small inner 点 (the "sickness" marks) — diagonal dots on left interior
dot_stroke(72, 138, 92, 155, w1=3, w2=6)
dot_stroke(60, 180, 82, 197, w1=3, w2=6)

# ---------- 乞 (right of the 撇, mid-height and below) ----------

# 短撇 above 乞 — small slash from upper-right down-left
stroke([(215, 108), (192, 138)], width=5)

# 短横 (the top of 乞) — short, ends at right side
stroke([(148, 145), (230, 140)], width=5)

# 乙 (横折弯钩): starts high, folds down and left, sweeps right, hooks up-left
yi = [
    (152, 178),  # start of top horizontal segment
    (222, 175),  # top horizontal end (folder shoulder)
    (218, 195),  # begin the down-left curve
    (198, 220),
    (172, 240),
    (152, 255),  # bottom-left of the bowl
    (170, 272),  # curve back right along the bottom
    (210, 278),
    (248, 272),  # bottom-right, base of the hook
]
stroke(yi, width=6)

# hook flick — UP-and-LEFT from the bottom-right (per memory: 横折弯钩 ~ -115°)
stroke([(248, 272), (243, 248)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0374_疙/01_疙.png")

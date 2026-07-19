"""
G1 (no memory) — p1_stroke_22_横折钩
Stroke: 横折钩 (horizontal, then a sharp turn downward, ending in a hook
flicking to the upper-left). This is the enclosing stroke of characters
like 月, 用, 同 — a 横折 with a hook attached at the bottom.

Renders a 300x300 PNG with white background and black ink using PIL only.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
STROKE_W = 14

# Anchor points on a 300x300 canvas.
# Horizontal (横) runs from upper-left toward upper-right, slightly rising
# as calligraphic 横 do; the turn (折) drops nearly vertically to the
# lower-right; the hook (钩) flicks up and to the left.
x1, y1 = 55, 80          # start of the horizontal
x2, y2 = 240, 72         # end of the horizontal / top of the vertical
                          # (very slight upward tilt to mimic 横 shape)
x3, y3 = 240, 235        # bottom of the vertical, where the hook begins
hook_mid = (225, 232)    # mid-point of the hook curve
hook_end = (200, 210)    # tip of the hook, up and to the left

# --- horizontal segment ---
draw.line([(x1, y1), (x2, y2)], fill=INK, width=STROKE_W)

# --- vertical segment ---
draw.line([(x2, y2), (x3, y3)], fill=INK, width=STROKE_W)

# --- 顿笔 (pause) at the corner: a small filled square to make the
#     90-ish-degree turn crisp rather than rounded.
r = STROKE_W // 2 + 2
draw.rectangle([(x2 - r, y2 - r), (x2 + r, y2 + r)], fill=INK)

# --- hook: two short segments approximating a curved flick ---
draw.line([(x3, y3), hook_mid], fill=INK, width=STROKE_W)
draw.line([hook_mid, hook_end], fill=INK, width=STROKE_W - 2)

# --- rounded caps ---
def cap(cx, cy, rr):
    draw.ellipse([(cx - rr, cy - rr), (cx + rr, cy + rr)], fill=INK)

cap(x1, y1, STROKE_W // 2)          # start of horizontal (slight 起笔)
cap(hook_end[0], hook_end[1], 4)     # tapered hook tip

# Slight thickening at the horizontal's start to mimic 起笔 (entry press).
draw.ellipse([x1 - 5, y1 - 4, x1 + 9, y1 + 8], fill=INK)

out_path = os.path.join(
    os.path.dirname(__file__), "01_横折钩.png"
)
img.save(out_path)
print(f"Wrote {out_path}")

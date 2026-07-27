"""
p3_char_0106_日  — tall-narrow box with one internal 横 at middle.

Consult trail:
- memory_index → form_catalog "内-square box + internal 横 (曰/日)":
  日 aspect is tall-narrow (x ~55%), one internal 横 at ~y=middle.
- form_catalog "竖 as left-wall of a box": TOP-LEFT corner shared
  with top 横's LEFT end; uniform width; length = box height.
- form_catalog "横折 as top-right corner of a box": 横 spans top,
  shoulder at TOP-RIGHT, 竖 down right wall; shoulder must not
  be inset from the actual right edge.
- form_catalog "横 as internal cross-bar": spans wall-to-wall,
  touches both verticals.

4 strokes:
 1) 竖    left wall (top-left → bottom-left)
 2) 横折  top-and-right (top-left → top-right, shoulder, → bottom-right)
 3) 横    internal middle bar (left-wall → right-wall at ~y=middle)
 4) 横    bottom bar (bottom-left → bottom-right)
"""

from PIL import Image, ImageDraw
import random

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Tall-narrow box: width ~55% (~110 px), height ~72% (~215 px).
# Center around canvas center; leave a little top/bottom margin.
LEFT   = 95
RIGHT  = 205
TOP    = 45
BOTTOM = 258
MID_Y  = (TOP + BOTTOM) // 2 + 4   # slightly below geometric middle,
                                   # matches GT where mid bar sits a touch low

INK = (20, 20, 20)
LW  = 8      # base line width (brush-ish look)

def wobble(p, amp=1.2):
    x, y = p
    return (x + random.uniform(-amp, amp), y + random.uniform(-amp, amp))

def brush_stroke(pts, width=LW, dabs=True):
    """Draw a polyline with rounded joints; optional end-dabs to
    fake ink accumulation at start/stop (顿笔)."""
    # slightly wobbled to feel hand-drawn
    pts_w = [wobble(p) for p in pts]
    draw.line(pts_w, fill=INK, width=width, joint="curve")
    if dabs:
        for p in (pts_w[0], pts_w[-1]):
            r = width * 0.55
            draw.ellipse((p[0]-r, p[1]-r, p[0]+r, p[1]+r), fill=INK)

random.seed(7)

# ---- Stroke 1: 竖 left wall (top-left → bottom-left) ----
brush_stroke([(LEFT, TOP + 2), (LEFT, BOTTOM)], width=LW)

# ---- Stroke 2: 横折 (top 横 + shoulder + right 竖) ----
# top 横: left → right along TOP
# shoulder: tiny down-right at top-right corner
# right 竖: down to bottom-right
top_left   = (LEFT - 2, TOP)
top_right  = (RIGHT, TOP)
shoulder   = (RIGHT + 2, TOP + 6)      # small shoulder dab
bot_right  = (RIGHT + 2, BOTTOM)
brush_stroke([top_left, top_right, shoulder, bot_right], width=LW)

# ---- Stroke 3: 横 internal middle cross-bar ----
# Spans wall-to-wall, sits at middle. Slightly shorter than full
# width so it visibly "touches" the walls without over-shooting.
brush_stroke([(LEFT + 2, MID_Y), (RIGHT - 2, MID_Y)], width=LW - 1)

# ---- Stroke 4: 横 bottom bar (closes the box) ----
brush_stroke([(LEFT - 2, BOTTOM), (RIGHT + 2, BOTTOM)], width=LW)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0106_日/01_日.png"
img.save(out)
print("wrote", out)

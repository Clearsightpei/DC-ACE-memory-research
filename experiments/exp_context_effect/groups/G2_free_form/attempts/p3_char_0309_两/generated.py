"""
两 (liang3) — G2 render.

Structure (7 strokes, MMH standard order):
  1. 一 top horizontal (spans nearly full width, slight rise)
  2. 丨 left vertical (drops from below the top-横, forming left wall)
  3. 横折钩 outer right: top short 横 then long 竖 ending in UP-LEFT hook
     (the outer frame's top-right corner + right wall + inward hook)
  4. 丨 inner-left short vertical (left 人-radical simplified: short 竖)
  5. inner-left small 撇 → 人-like bit (actually a 人 inside on left)
     Actual MMH: strokes 4,5 = left inner 人 (short 撇 + short 点)
  6. right inner 撇
  7. right inner 点

Hook flick rule (memory_index TIER-0 B): 横折钩 terminal flicks
UP-and-LEFT (~-105°), never down.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=6):
    """Draw a polyline with round caps/joins."""
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # round end caps
    r = width // 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse([x-r, y-r, x+r, y+r], fill=BLACK)

def bez(p0, p1, p2, n=40):
    """Quadratic bezier sampled."""
    out = []
    for i in range(n+1):
        t = i / n
        x = (1-t)**2 * p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
        out.append((x, y))
    return out

# --- Stroke 1: top 一 (horizontal) ---
# Slight upward tilt left-to-right, then a tiny down-tick at the right end
top_horiz = bez((55, 78), (150, 70), (245, 76), 30)
stroke(top_horiz, width=6)

# --- Stroke 2: left 丨 vertical (the left wall) ---
# Starts just under the top 一's left, drops straight to bottom
stroke([(70, 92), (66, 260)], width=7)

# --- Stroke 3: 横折钩 — top short 横 across, then long 竖 down + hook UP-LEFT ---
# Segment A: short horizontal at top going right from around x=95 to x=240
# Segment B: vertical down from (240, 100) to (238, 250)
# Segment C: hook flick UP-LEFT from (238,250) to (220, 235)
horiz_top = [(95, 98), (240, 100)]
stroke(horiz_top, width=6)
vert_right = [(240, 100), (238, 250)]
stroke(vert_right, width=7)
# hook flick: from bottom of vert_right, up-and-left
hook = [(238, 250), (225, 240), (215, 232)]
stroke(hook, width=6)

# --- Inner content: two 人 side by side inside the frame ---
# The GT shows: left 人 (撇 + 点) and right 人 (撇 + 点), roughly symmetric
# Frame interior spans x≈75..235, y≈110..245

# Left 人 (inside left half, ~x 70..150):
#  撇: curves from apex (~110,140) down-and-left to ~(80, 245)
left_pie = bez((115, 140), (95, 200), (78, 248), 30)
stroke(left_pie, width=6)
#  点: short dot from apex area going down-right to ~(135, 235)
left_dian = bez((118, 155), (128, 195), (140, 240), 20)
stroke(left_dian, width=5)

# Right 人 (inside right half, ~x 155..235):
#  撇: from apex (~185,140) down-and-left to ~(160, 245)
right_pie = bez((185, 140), (170, 200), (155, 248), 30)
stroke(right_pie, width=6)
#  点: from apex area going down-right to ~(215, 240)
right_dian = bez((188, 155), (200, 195), (215, 240), 20)
stroke(right_dian, width=5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0309_两/01_两.png")
print("wrote 01_两.png")

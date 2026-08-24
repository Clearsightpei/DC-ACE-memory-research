"""
p3_char_0006_乚 — G2 free-form drawer (REVISION 1).

乚 is a single compound stroke: 竖弯钩.
GT observations:
- Fills roughly x=[75, 260], y=[55, 260] on 300x300 canvas.
- Top starts with a small hook/kink to the LEFT (like an entry 顿),
  then descent begins slightly right of that top point.
- Long descending 竖 (slightly slanted, near vertical, maybe leaning
  slightly right at first then straight).
- Wide sweeping bend into a long bottom 横 that goes nearly to the
  right edge of the glyph.
- Terminal small up-flick at bottom-right (~15-20 px, angled up).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("L", (W, H), 255)
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def segment(p0, p1, r_start, r_end=None, steps=None):
    if r_end is None:
        r_end = r_start
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if steps is None:
        steps = max(4, int(length))
    for i in range(steps + 1):
        t = i / steps
        rr = r_start + t * (r_end - r_start)
        dab(x0 + t * dx, y0 + t * dy, rr)


def arc_vertdown_to_horiz_right(x0, y0, R, r, steps=90):
    """Quarter arc; starts moving DOWN at (x0,y0), ends moving RIGHT
    at (x0+R, y0+R). Belly opens down-right (center at (x0+R, y0))."""
    for i in range(steps + 1):
        t = i / steps
        x = x0 + R * math.sin(t * math.pi / 2)
        y = y0 + R * (1 - math.cos(t * math.pi / 2))
        dab(x, y, r)
    return (x0 + R, y0 + R)


# --- Parameters -----------------------------------------------------
r = 7  # thick brush like GT

# --- 1. Top entry hook (small left-flick + tiny down-turn) ----------
# GT top-left: a small "j"-like curl. The stroke enters going down-
# then curls slightly leftward at the very top before straightening.
# Model as: a very short down-left segment then merge into the main
# 竖. Draw a short flick from (top_x, top_y_upper) going down-and-a-
# bit-left, then main body starts.
top_x = 92
top_y = 62

# small entry: a stub going down-left then a hairpin back
# GT shows: at very top, ink comes down then loops-back tiny to the
# right — i.e. the pen entered, made a small 顿 dab, then began
# descent. Simplify: a short down-left tick (~14 px) at the top.
entry_top = (top_x + 8, top_y)         # top-right of the hook
entry_dip = (top_x, top_y + 18)        # bottom of the small hook
segment(entry_top, entry_dip, r_start=4, r_end=r)

# --- 2. Main 竖 descent ---------------------------------------------
vert_top = entry_dip  # continue from bottom of entry hook
vert_end = (top_x + 2, 195)  # slight rightward drift as GT shows
segment(vert_top, vert_end, r_start=r, r_end=r)

# --- 3. Wide tangent-continuous bend --------------------------------
R = 62
end_of_arc = arc_vertdown_to_horiz_right(vert_end[0], vert_end[1], R, r)
# end_of_arc ~ (vert_end[0]+R, vert_end[1]+R) = (156, 257)

# --- 4. Long bottom 横 sweep ----------------------------------------
horiz_end_x = 250
segment(end_of_arc, (horiz_end_x, end_of_arc[1]), r_start=r, r_end=r)

# --- 5. Terminal up-hook --------------------------------------------
# Small up-flick, ~20 px, angled roughly straight up with slight
# left-lean. Tapers to a point.
hook_len = 22
hook_angle_deg = 260  # y-down convention; 270=up, 260 = up + tiny left
ang = math.radians(hook_angle_deg)
hx = horiz_end_x + hook_len * math.cos(ang)
hy = end_of_arc[1] + hook_len * math.sin(ang)
steps = 24
for i in range(steps + 1):
    t = i / steps
    x = horiz_end_x + t * (hx - horiz_end_x)
    y = end_of_arc[1] + t * (hy - end_of_arc[1])
    rr = max(2, r - t * (r - 2))
    dab(x, y, rr)

# --- Save -----------------------------------------------------------
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0006_乚/01_乚.png"
img.save(out)
print(f"wrote {out}")

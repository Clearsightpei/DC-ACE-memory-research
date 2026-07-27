"""
Render 仃 (dīng) to a 300x300 PNG.

Structure: 亻 (left radical: 撇 + 竖) + 丁 (right: 一 + 亅 straight hook).

# SIGNATURE CHECK (from sibling_signature_checklist.md):
# 丁 : 一 + straight 亅 (no top flick). Distinguish from 刁 which has top-flick 撇.
# So: horizontal top bar, then a straight vertical going down with a small
# left-turning hook (亅) at the bottom. NO 撇 at the top of 丁.

# Layout notes:
# - 亻 sits on the left, compressed; 撇 starts upper-center of the radical
#   and sweeps down-left; 竖 hangs from about the mid-point of the 撇.
# - 丁 sits on the right; the 一 spans the right portion, the 亅 hangs
#   from roughly the center of the 一 and hooks left at the bottom.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 8  # base ink width


def brush_line(pts, width=INK):
    """Draw a soft polyline with rounded joints."""
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # cap the endpoints with small circles for round feel
    for x, y in (pts[0], pts[-1]):
        r = width // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def taper_stroke(pts, w_start, w_end, steps=24):
    """Draw a stroke that tapers linearly from w_start -> w_end using
    small overlapping ellipses along the polyline (dab-brush)."""
    # densify pts
    dense = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        for s in range(steps):
            t = s / steps
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(n - 1, 1)
        w = w_start + (w_end - w_start) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# ---------- 亻 (left radical) ----------
# 撇 : starts near (110, 65), curves down-left, ends near (40, 210).
# Longer, more slanted, with a soft bow.
pie_pts = [
    (112, 68),
    (105, 95),
    (94, 122),
    (80, 150),
    (63, 180),
    (45, 210),
]
taper_stroke(pie_pts, 10, 2, steps=16)

# 竖 : hangs from the lower-body of the 撇 (~ (85, 145)) straight down.
shu_pts = [(85, 145), (85, 185), (85, 225), (85, 265)]
taper_stroke(shu_pts, 9, 7, steps=14)

# ---------- 丁 (right component) ----------
# 一 (horizontal): spans roughly x=130..260 at y ~= 130 with clear upward tilt.
heng_pts = [(132, 140), (170, 133), (215, 126), (258, 122)]
taper_stroke(heng_pts, 7, 10, steps=16)

# 亅 (vertical hook): straight vertical from roughly (195, 130) down
# to (195, 245), then a small hook curling to the LEFT.
gou_vert = [(200, 128), (201, 170), (201, 215), (200, 255)]
taper_stroke(gou_vert, 10, 8, steps=16)
# hook flick (left-turning terminal)
gou_hook = [(200, 255), (192, 256), (183, 252), (175, 245)]
taper_stroke(gou_hook, 9, 3, steps=12)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0107_仃/01_仃.png"
)
print("wrote 01_仃.png")

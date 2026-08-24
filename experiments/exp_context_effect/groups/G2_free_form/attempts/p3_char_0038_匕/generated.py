"""
匕 — 2 strokes.
  Stroke 1: 撇 (top-crosser) — starts upper-right, throws down-left,
            crossing the body 竖弯钩. Per form_catalog sibling table:
            匕's top stroke is a 撇 (upper-right → lower-left),
            distinguishing it from 七 (which has a 横).
  Stroke 2: 竖弯钩 — starts upper-left, goes down, curves right at
            bottom, then finishes with an upward flick on the right.

Canvas 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_stroke(pts, base_w=11, taper_end=False, taper_start=False):
    """Draw a poly-line as a thick tapered stroke by drawing many
    circles along a sampled path (dab primitive)."""
    if len(pts) < 2:
        return
    # sample along the polyline
    dab_pts = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        dx, dy = x1 - x0, y1 - y0
        steps = max(2, int((dx * dx + dy * dy) ** 0.5))
        for s in range(steps):
            t = s / steps
            dab_pts.append((x0 + t * dx, y0 + t * dy))
    dab_pts.append(pts[-1])

    n = len(dab_pts)
    for i, (x, y) in enumerate(dab_pts):
        t = i / max(1, n - 1)
        w = base_w
        if taper_end:
            # thick at start, thin at end
            w = base_w * (1.0 - 0.55 * t)
        if taper_start:
            w = base_w * (0.5 + 0.5 * t)
        r = max(1.5, w / 2)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# ---------- Stroke 2 (竖弯钩) — draw first as the body backbone ----
# Starts upper-left ~ (100, 90), goes DOWN to ~(100, 230),
# then curves right along the bottom to ~(210, 245),
# then hooks UP on the right to ~(215, 215).
s2_down = [(103, 92), (102, 130), (101, 170), (101, 205), (103, 228)]
s2_curve = [(103, 228), (120, 245), (150, 252), (185, 250), (212, 244)]
s2_hook = [(212, 244), (215, 232), (216, 220), (215, 210)]

brush_stroke(s2_down, base_w=11)
brush_stroke(s2_curve, base_w=11)
# Hook: draw with slight taper to the tip
brush_stroke(s2_hook, base_w=11, taper_end=True)

# ---------- Stroke 1 (撇) — top crosser, upper-right → lower-left --
# Starts ~(190, 100) upper-right, throws down-left to ~(85, 175),
# crossing the 竖 of stroke 2. Thick→thin taper, gentle right-bow.
s1 = [(188, 102), (170, 115), (150, 130), (128, 148), (105, 168), (85, 178)]
brush_stroke(s1, base_w=12, taper_end=True)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0038_匕/01_匕.png"
)

"""
Render 分 (fēn) to 300x300 PNG.

Structure: 八 top (disjoint 撇 + 捺 with top gap) + 刀 bottom
(横折钩 + body-crossing 撇). Four strokes total.

Memory pointers used:
- form_catalog 八: "disjoint 撇+捺 with TOP GAP (distinguishes from 儿)"
- form_catalog 撇 body-crossing (刀): LONG, MODERATE slope, must cross
  through the 横折钩 with top pixel visibly above the crossing line.
- form_catalog 力: "横折钩 + body-crossing 撇 (retry-learned)" — 刀
  follows same recipe minus the 力 shoulder.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    """Draw a variable-width stroke via dabs along a polyline."""
    if len(points) < 2:
        return
    # Sample densely between consecutive control points
    total_segments = len(points) - 1
    for seg in range(total_segments):
        x0, y0 = points[seg]
        x1, y1 = points[seg + 1]
        w0 = widths[seg]
        w1 = widths[seg + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 8)
        for i in range(steps + 1):
            t = i / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")


def bezier_points(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


# =============================================================
# STROKE 1: 八 left 撇 — starts near apex (~135, 50), sweeps down-left
# to (~70, 145). GT: prominent leftward flick with visible gap
# between the 撇 tail and the 捺 head at top (八 signature).
# =============================================================
pts1 = bezier_points((140, 50), (110, 90), (65, 145), n=40)
w1 = [max(3.0, 8.5 - i * 0.14) for i in range(len(pts1))]
brush_stroke(pts1, w1)

# =============================================================
# STROKE 2: 八 right 捺 — starts slightly right of and below the 撇
# apex (leaving a top gap per form_catalog "disjoint 撇+捺"),
# swings down-right with pronounced arc to a fat foot.
# =============================================================
pts2 = bezier_points((155, 62), (205, 100), (255, 150), n=50)
w2 = [3.0 + i * 0.13 for i in range(len(pts2))]
brush_stroke(pts2, w2)

# =============================================================
# STROKE 3: 刀 横折钩 — horizontal roughly centered under 八, then
# turns down at shoulder, drops with leftward lean, tiny hook flick.
# Move horizontal a bit higher/tighter to give room for the crossing 撇.
# =============================================================
# Horizontal segment: (~70, 165) -> (~215, 158). Slight upward slant
h_pts = bezier_points((70, 168), (145, 162), (218, 158), n=40)
h_w = [6.5] * len(h_pts)
brush_stroke(h_pts, h_w)

# Vertical segment down from shoulder — noticeable leftward lean
v_pts = bezier_points((215, 158), (200, 215), (180, 265), n=40)
v_w = [6.5 - i * 0.04 for i in range(len(v_pts))]
brush_stroke(v_pts, v_w)

# Terminal hook flick (small, up-left)
hook_pts = bezier_points((180, 265), (170, 258), (158, 250), n=20)
hook_w = [5.8 - i * 0.15 for i in range(len(hook_pts))]
brush_stroke(hook_pts, hook_w)

# =============================================================
# STROKE 4: body-crossing 撇 — starts ABOVE the 横 line (head visible)
# around (~150, 145), crosses through the horizontal, continues to
# lower-left ending ~ (85, 275). Long, moderate slope, gentle bow.
# =============================================================
pts4 = bezier_points((150, 145), (125, 205), (85, 278), n=45)
w4 = [max(2.5, 7.5 - i * 0.11) for i in range(len(pts4))]
brush_stroke(pts4, w4)

# Save
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0110_分/01_分.png"
img.save(out)
print(f"wrote {out}")

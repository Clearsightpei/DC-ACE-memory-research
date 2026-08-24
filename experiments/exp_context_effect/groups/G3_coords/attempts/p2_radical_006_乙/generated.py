# p2_radical_006_乙 — 1画 radical (visually a 横折弯钩-like single stroke).
# No bank primitive matches this specific compound shape (no heng_zhe_wan_gou
# in bank), so we DRAW FRESH per TR5 (inline the recipe).
#
# Shape decomposition (from GT):
#   Segment A: short 横 at top (thin left-head, gentle rise then fall)
#              approx from (95, 100) to (175, 95) in PIL coords.
#   Segment B: 折 turning down-left, sweeping curve to bottom-left
#              via (155, 115) → (95, 180) → (85, 240).
#   Segment C: 横 along the bottom to the right, from (~85, 240) sweeping
#              right up to (~215, 240).
#   Segment D: 钩 tiny vertical hook up at the right end, (215, 240) → (215, 218).
#
# One continuous ink stroke drawn as tapered stamped-circle spine with a
# width profile that swells at the belly (per P3, P4).

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stamp(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def draw_curve(points, widths, steps_per_seg=60):
    """Draw a piecewise curve through points with the given widths per point,
    interpolating position and width linearly along each segment."""
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for s in range(steps_per_seg + 1):
            u = s / steps_per_seg
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            w = w0 + (w1 - w0) * u
            stamp(x, y, w / 2.0)

# One continuous 乙 stroke path — control points sampled from the GT.
# Coord system: PIL (origin top-left, +y down).
# Revision: thinned the top segment (GT top is delicate), rounded the
# bottom-left corner into a proper sweep (GT curves through, not a
# right-angle), tightened the 顿笔 blobs so they don't lump the corners.
path = [
    (92, 108),   # A start — thin head
    (122, 98),   # A rise
    (154, 94),   # A crest
    (178, 102),  # A end / B start — turn point
    (170, 122),  # B down-left
    (140, 158),  # B mid
    (108, 200),  # B lower
    (92,  228),  # B curving toward bottom
    (88,  245),  # B/C blend — smooth curved corner (no sharp angle)
    (105, 254),  # C sweep begin
    (145, 256),  # C mid
    (188, 252),  # C right
    (216, 246),  # C end / D start — bottom-right corner
    (219, 224),  # D hook tip
]

# Width profile — thinner at head, uniform-ish body, tapered hook tip.
widths = [
    3.0,   # A head very thin
    6.5,
    8.0,
    9.5,   # 折 corner
    9.0,
    8.5,
    9.0,
    9.5,
    10.0,  # bottom curve apex
    10.5,
    10.5,
    9.5,
    7.5,   # bottom-right corner
    2.5,   # hook tip
]

draw_curve(path, widths, steps_per_seg=80)

# Small 顿笔 blobs — tighter now (P6).
stamp(178, 102, 5.5)   # top-right 折
stamp(216, 246, 5.5)   # bottom-right corner before hook

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_006_乙/01_乙.png"
img.save(out_path)
print(f"Saved: {out_path}")

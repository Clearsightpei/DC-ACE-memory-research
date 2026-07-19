"""p1_stroke_08_卧钩 — G4 (grid-bank)

卧钩 (wò gōu, "lying hook"): a shallow horizontally-lying curve that
starts thin at the upper-left, arcs downward (belly hanging low), then
turns and hooks sharply upward-left at its right end. Used in
characters like 心, 必.

Shape breakdown:
- Entry:  starts thin near ML/C border, upper region.
- Belly:  arcs down through BC (lowest point roughly center-bottom).
- Exit:   rises to MR area on the right (thickest portion).
- Hook:   sharp upward-left kick from the exit point, ending toward
          the upper-left of the exit (this is the 钩).

Anchors (米字格) — turtle math-coords convention (y grows UP):
    P0 (start):    ('C',  0.10, 0.60)   ~ (-45,  -10)
    P1 (belly):    ('BC', 0.50, 0.40)   ~ (0,    -70)   lowest point
    P2 (exit):     ('MR', 0.55, 0.85)   ~ (105,  -35)   before the hook
    P3 (hook tip): ('MR', 0.30, 0.30)   ~ (80,    20)   hook ends up-left

Joint spec: single stroke, no inter-stroke joints.

Rendering: pure PIL (Image + ImageDraw) — no turtle screen so this is
deterministic and headless-safe. 米字格 anchors are still the sole
spatial vocabulary.
"""
import os
from PIL import Image, ImageDraw

# ─── 米字格 anchor → math-coords (matches _anchor.py) ──────────────
CELLS = {
    'TL': (-150, -50, +150, +50), 'TC': (-50, +50, +150, +50), 'TR': (+50, +150, +150, +50),
    'ML': (-150, -50, +50, -50),  'C':  (-50, +50, +50, -50),  'MR': (+50, +150, +50, -50),
    'BL': (-150, -50, -50, -150), 'BC': (-50, +50, -50, -150), 'BR': (+50, +150, -50, -150),
}

def anchor_to_xy(anchor):
    cell, xf, yf = anchor
    x_left, x_right, y_top, y_bot = CELLS[cell]
    return float(x_left + xf * (x_right - x_left)), float(y_top + yf * (y_bot - y_top))

# ─── math-coords ([-150, +150]) → PNG pixel coords (300×300) ──────
def to_px(pt):
    x, y = pt
    px = int(round(x + 150))          # -150 -> 0, +150 -> 300
    py = int(round(150 - y))          # +150 -> 0, -150 -> 300 (flip y)
    return px, py


def draw_variable_width_polyline(draw, pts, widths):
    """Draw a polyline whose stroke width varies per-segment.

    pts:    list of (x, y) in pixel coords, length N.
    widths: list of float widths, length N.
    """
    for i in range(len(pts) - 1):
        w = max(1, int(round((widths[i] + widths[i + 1]) * 0.5)))
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
    # Round the joins with small filled circles so the taper looks smooth.
    for (x, y), w in zip(pts, widths):
        r = max(0.5, w * 0.5)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def bezier2(p0, c, p2, s):
    x = (1 - s) ** 2 * p0[0] + 2 * (1 - s) * s * c[0] + s ** 2 * p2[0]
    y = (1 - s) ** 2 * p0[1] + 2 * (1 - s) * s * c[1] + s ** 2 * p2[1]
    return x, y


def draw_wo_gou(draw):
    P0 = anchor_to_xy(('C',  0.10, 0.60))    # start
    P1 = anchor_to_xy(('BC', 0.50, 0.40))    # belly (control-target)
    P2 = anchor_to_xy(('MR', 0.55, 0.85))    # exit
    P3 = anchor_to_xy(('MR', 0.30, 0.30))    # hook tip

    # Quadratic Bezier control chosen so curve grazes P1:
    Cx = 2 * P1[0] - 0.5 * (P0[0] + P2[0])
    Cy = 2 * P1[1] - 0.5 * (P0[1] + P2[1])

    # ── Body arc: 60 samples, thin head -> thick belly/exit ──
    body_steps = 60
    body_pts = []
    body_widths = []
    for i in range(body_steps + 1):
        s = i / body_steps
        p = bezier2(P0, (Cx, Cy), P2, s)
        body_pts.append(to_px(p))
        # Width profile: 3 -> 10 across the arc.
        w = 3 + 7 * (s ** 0.6)
        body_widths.append(w)
    draw_variable_width_polyline(draw, body_pts, body_widths)

    # ── Hook: sharp up-left kick, tapers to a point ──
    hook_steps = 20
    hook_pts = []
    hook_widths = []
    for i in range(hook_steps + 1):
        s = i / hook_steps
        x = P2[0] + (P3[0] - P2[0]) * s
        y = P2[1] + (P3[1] - P2[1]) * s
        hook_pts.append(to_px((x, y)))
        # Taper from body's exit width (~10) down to a sharp tip (~1).
        w = 10 - 9 * s
        hook_widths.append(max(1.0, w))
    draw_variable_width_polyline(draw, hook_pts, hook_widths)


def render():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_png = os.path.join(out_dir, "01_卧钩.png")

    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_wo_gou(draw)
    img.save(out_png, "PNG")
    print(f"Saved: {out_png} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    render()

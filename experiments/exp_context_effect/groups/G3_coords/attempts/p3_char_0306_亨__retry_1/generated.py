"""亨 (hēng) — 7 strokes. retry_1.

# RETRY MEMORY CHECKLIST
# Q1 (errata): no explicit entry — main attempt was too thick/calligraphic
#   vs GT's thin cursive strokes. Fix: thin widths (~2-3px), match GT weight.
# Q2 (form_catalog): GT lines are uniform thin ~3px (MMH-style), not tapered
#   calligraphic. Use thin uniform widths per P12 principle.
# Q3 (helpers): none directly apply — this is a simple stacked composition
#   (dot / long-heng / small 口 / heng / 了-descender). Inline fresh.

# TRAJECTORY DIFF (main → retry_1)
# GT visual:
#   - Very thin uniform strokes (~2-3 px), slightly cursive/wobbly
#   - Top dot: small, tilted upper-center, y~30
#   - Long heng: thin, slightly bowed, spans nearly full width
#   - Small 口: narrower and shorter than main; y ~95-125
#   - Second heng below 口: shorter than long heng, ~x 55-235
#   - 了-style descender: starts inside/right of center, drops with
#     leftward curve, tiny hook at bottom-left. Not a full 弯钩.
# Main FAIL gaps:
#   1. Strokes ~5-8 px thick — GT is ~2-3 px. Too calligraphic.
#   2. 口 too large (85x50). GT 口 is smaller (~70x28).
#   3. Second heng width (5-7) too heavy; GT is thin.
#   4. Hook descender ends too high (y~262) — should reach y~275+
#      and curve further left.
# Fixes this retry:
#   - Drop all widths to 2-3 px uniform
#   - Shrink 口 to ~70x30
#   - Extend hook lower with more leftward curl
"""
from PIL import Image, ImageDraw
from pathlib import Path


def draw_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t = i / (steps - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=0)


def draw_poly(draw, points, widths, steps_per_seg=30):
    for i in range(len(points) - 1):
        draw_line(draw, points[i], points[i + 1], widths[i], widths[i + 1], steps=steps_per_seg)


def render():
    img = Image.new("L", (300, 300), 255)
    d = ImageDraw.Draw(img)

    W = 3  # baseline thin width

    # --- Stroke 1: 点 (top dot) — small, tilted upper-center
    draw_poly(d, [(150, 30), (158, 45)], [2, 4])

    # --- Stroke 2: 长横 (long lid heng), thin, slightly bowed
    draw_poly(d, [(38, 82), (150, 78), (262, 82)], [W, W, W])

    # --- Small 口 (strokes 3,4,5) — narrower, shorter
    # Box roughly x=118..192, y=100..132
    # Stroke 3: 竖 (left vertical)
    draw_poly(d, [(120, 102), (121, 130)], [W, W])
    # Stroke 4: 横折 (top + right vertical)
    draw_poly(d, [(118, 100), (192, 98), (191, 132)], [W, W, W])
    # Stroke 5: 横 (bottom of 口)
    draw_poly(d, [(120, 130), (192, 131)], [W, W])

    # --- Stroke 6: 横 (horizontal below 口), thin
    draw_poly(d, [(55, 158), (150, 155), (238, 158)], [W, W, W])

    # --- Stroke 7: 了-style descender (curved hook)
    # Starts a bit right of center just under stroke 6, drops down and
    # curves leftward, ends with tiny hook flick.
    pts = [
        (168, 160),
        (168, 195),
        (162, 225),
        (150, 250),
        (132, 268),
        (112, 275),
        (98, 268),  # hook flick
    ]
    widths = [W, W, W, W, W, W - 1, W - 1]
    draw_poly(d, pts, widths, steps_per_seg=25)

    out = Path(__file__).parent / "01_亨.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()

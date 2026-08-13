"""亨 (hēng) — 7 strokes. retry_2.

# RETRY MEMORY CHECKLIST
# Q1 (errata): main = too calligraphic thick; retry_1 = too thin and pieces
#   too compact (口 tiny, descender feels weak). Fix: medium uniform width
#   ~4-5 px, keep 口 modest, extend descender lower with proper hook.
# Q2 (form_catalog): GT lines are cursive medium-thin. Use w=4 uniform,
#   slightly thicker on the long heng (~5) for visual weight anchor.
# Q3 (helpers): none — stacked composition, inline fresh.

# TRAJECTORY DIFF (main + retry_1 → retry_2)
# GT visual (再-look at gt/phase3/亨.png):
#   - Cursive medium-weight strokes ~3-4 px
#   - Top dot: small angled dot at (~145,28)->(155,45)
#   - Long lid heng: y~72-78, spans x~30..270, mild bow
#   - Small 口: x~115..185, y~95..130 (box aspect ~70x35, wider than tall)
#   - Lower heng: y~155-160, spans x~40..255
#   - 了-descender: starts near right-of-center below lower heng
#     (~x=175, y=160), curves down and left, ending around
#     (~110, 275) with small leftward hook flick
# Main FAIL (too thick 5-8 px; 口 too large; hook ended too high).
# Retry_1 FAIL (too thin ~2-3 px, 口 barely visible, descender weak).
# Retry_2 fixes:
#   - width baseline 4 (long heng 5)
#   - 口 box 75x33
#   - descender extends to y~275 with clean leftward hook
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

    W = 4  # baseline medium

    # --- Stroke 1: 点 (top dot) — small angled, upper center
    draw_poly(d, [(146, 26), (156, 46)], [3, 6])

    # --- Stroke 2: 长横 (long lid heng), mild bow, spans wide
    draw_poly(d, [(30, 78), (150, 72), (270, 78)], [W + 1, W + 1, W + 1])

    # --- Small 口 (strokes 3,4,5) — box x=115..190, y=98..132
    # Stroke 3: 竖 (left vertical)
    draw_poly(d, [(117, 100), (118, 132)], [W, W])
    # Stroke 4: 横折 (top + right vertical)
    draw_poly(d, [(115, 98), (155, 96), (190, 100), (188, 132)], [W, W, W, W])
    # Stroke 5: 横 (bottom of 口)
    draw_poly(d, [(117, 131), (155, 130), (188, 132)], [W, W, W])

    # --- Stroke 6: 横 (horizontal below 口)
    draw_poly(d, [(42, 160), (150, 156), (258, 160)], [W, W + 1, W + 1])

    # --- Stroke 7: 了-descender (curved hook)
    # Starts right-of-center just under stroke 6, drops down curving
    # leftward, ends with hook flick to the left near bottom.
    pts = [
        (172, 158),
        (172, 190),
        (168, 220),
        (156, 248),
        (138, 268),
        (115, 278),
        (98, 272),  # hook flick
    ]
    widths = [W + 1, W, W, W, W, W - 1, W - 1]
    draw_poly(d, pts, widths, steps_per_seg=25)

    out = Path(__file__).parent / "01_亨.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()

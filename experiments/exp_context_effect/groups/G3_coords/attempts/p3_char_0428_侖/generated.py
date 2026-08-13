# BANK_DEVIATION
# skipped: ji_meet_char.py (turtle math-coord version, would need re-anchoring)
# reason: 侖 needs a compact top 亼 slotted above a tall bottom frame; the
#   bank ji_meet_char occupies the full canvas at its native scale, and
#   converting from turtle math-coords to PIL pixel-coords plus rescaling
#   is more error-prone than re-inlining the roof directly at the target
#   position. Bottom frame (册-like with 2 internal verticals) has no
#   near-fit bank entry (ce_volume is twin-frame, jiong_char is 冂+口).
# fresh_component: lun_char (inline 亼-roof + frame-with-two-inner-verticals)
"""侖 (lún) — inline PIL render.

Structure (8 strokes):
  Top 亼:
    1. 撇 (pie) — apex ~ (150, 55) down-left to (78, 118)
    2. 捺 (na) — apex ~ (150, 55) down-right to (222, 118)
    3. 一 (heng) — below the roof, ~ (72, 138) to (228, 133)
  Bottom rectangular frame with two inner verticals (like 冊 flavor):
    4. Left outer vertical — (74, 152) to (74, 275)
    5. 横折钩 — top horizontal (74,152) -> (226,152) then down to (226, 268)
       with a small hook to the left at the bottom
    6. Inner-left vertical — (122, 165) to (122, 260)
    7. Inner-right vertical — (178, 165) to (178, 260)
    8. Bottom closing horizontal — (78, 275) to (224, 272)
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
        draw_line(draw, points[i], points[i + 1],
                  widths[i], widths[i + 1], steps=steps_per_seg)


def render():
    img = Image.new("L", (300, 300), 255)
    d = ImageDraw.Draw(img)

    # --- Top 亼 (roof + heng) ---
    APEX = (150, 55)
    # Stroke 1: 撇 (pie), tapered
    draw_poly(d, [APEX, (110, 90), (72, 122)], [5, 6, 3])
    # Stroke 2: 捺 (na), belly on right, tapered thin at tail
    draw_poly(d, [APEX, (185, 90), (222, 118), (232, 122)], [4, 6, 6, 3])
    # Stroke 3: 一 under the roof
    draw_poly(d, [(70, 140), (150, 135), (230, 138)], [5, 5, 5])

    # --- Bottom rectangular frame with two internal verticals ---
    # Stroke 4: outer-left vertical
    draw_poly(d, [(82, 160), (80, 210), (80, 272)], [6, 6, 5])

    # Stroke 5: 横折钩 — top horizontal + right vertical + hook
    draw_poly(
        d,
        [(78, 158), (150, 154), (222, 158), (222, 215), (222, 270), (208, 275)],
        [5, 6, 6, 6, 6, 3],
    )

    # Stroke 6: inner-left vertical
    draw_poly(d, [(128, 168), (128, 262)], [4, 4])

    # Stroke 7: inner-right vertical
    draw_poly(d, [(178, 168), (178, 262)], [4, 4])

    # Stroke 8: bottom closing horizontal
    draw_poly(d, [(82, 273), (150, 271), (222, 273)], [5, 5, 5])

    out = Path(__file__).parent / "01_侖.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()

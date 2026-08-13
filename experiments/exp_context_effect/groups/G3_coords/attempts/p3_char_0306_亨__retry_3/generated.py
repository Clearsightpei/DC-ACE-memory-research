"""亨 (hēng) — 7 strokes. retry_3.

# BANK_DEVIATION
# skipped: tou_char.py, kou.py, liao.py (turtle-based; also proportions
#   need to fit explicit y-bands from curator hint)
# reason: 3-stack requires precise y-band placement (see errata B11 hint
#   below); bank primitives use turtle/hardcoded coords that don't align
#   to the tight vertical schedule this composition needs.
# fresh_component: heng_stack_for_ya_top_liao_bottom

# RETRY MEMORY CHECKLIST
# Q1 (errata): B11 curator gave explicit y-band hint —
#   亠 y=40-90, 口 y=100-170, 了 y=180-280. Prior retries had 口 too
#   short (only 30-35 tall) and 了 starting too early. Follow bands.
# Q2 (form_catalog): thin uniform ~3-4px lines match GT cursive look;
#   long lids get slight width bump ~5px.
# Q3 (helpers): none needed — pure stacked composition, no X-crossing
#   or mirror-dots. Inline fresh per v13 BANK_DEVIATION channel.

# TRAJECTORY DIFF (main + retry_1 + retry_2 → retry_3)
# GT visual (re-inspected):
#   - Top dot: small angled slash near x=145, y=45
#   - Long lid heng: y~72-78 spans x=30..270 (already right in retry_2)
#   - 口: NEEDS to be TALLER — GT shows ~y=95..145 not y=98..132
#     Retry_2's 口 was 30px tall (98→132). GT is ~50px tall (95→145).
#     Width also modest ~x=115..185.
#   - Lower heng: y~155-165, spans x~35..265
#   - 了-descender starts at ~x=175, y=160, curves down-left ending
#     with hook near (110, 275).
# Main FAIL: strokes too thick (calligraphic).
# Retry_1 FAIL: too thin AND 口 barely visible.
# Retry_2 FAIL: proportions still off — 口 too short/small; whole
#   composition felt cramped in middle. B11 curator diagnosis:
#   "3-stack proportions still drift".
# Retry_3 fixes (last try before terminal freeze):
#   - Enforce curator y-bands: 亠 (40-90), 口 (100-170), 了 (180-280)
#   - 口 now ~55px tall (y=105..160), width ~x=120..185
#   - Descender starts at y~170 (lower heng), extends to y~278
#   - Uniform medium width 4, long heng gets 5.
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

    # ============================================================
    # BAND 1: 亠 (y = 40-90)
    # ============================================================
    # --- Stroke 1: 点 (top dot) — small angled slash
    draw_poly(d, [(148, 42), (160, 62)], [3, 6])

    # --- Stroke 2: 长横 (long lid heng), mild bow across full width
    draw_poly(d, [(32, 88), (150, 82), (270, 88)], [W + 1, W + 1, W + 1])

    # ============================================================
    # BAND 2: 口 (y = 100-170), ~55px tall, moderate width
    # ============================================================
    # 口 box roughly x=118..188, y=108..162 (~70 wide, ~54 tall)
    # Stroke 3: 竖 (left vertical)
    draw_poly(d, [(120, 110), (121, 162)], [W, W])
    # Stroke 4: 横折 (top + right vertical, single continuous)
    draw_poly(d, [(118, 108), (155, 106), (190, 110), (188, 162)], [W, W, W, W])
    # Stroke 5: 横 (bottom of 口)
    draw_poly(d, [(120, 161), (155, 160), (188, 162)], [W, W, W])

    # ============================================================
    # BAND 3: 了 (y = 180-280)
    # ============================================================
    # --- Stroke 6: 横 (horizontal below 口 — top of 了)
    draw_poly(d, [(38, 190), (150, 186), (262, 190)], [W, W + 1, W + 1])

    # --- Stroke 7: 了-descender (curved hook)
    # Starts right-of-center from just below stroke 6, drops down
    # curving leftward, ends with hook flick at bottom.
    pts = [
        (178, 188),
        (178, 218),
        (172, 248),
        (156, 270),
        (132, 282),
        (108, 280),
        (92, 272),  # hook flick
    ]
    widths = [W + 1, W, W, W, W, W - 1, W - 1]
    draw_poly(d, pts, widths, steps_per_seg=25)

    out = Path(__file__).parent / "01_亨.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()

# BANK_DEVIATION
# skipped: bing.py, bing_char.py (冫 primitive is calibrated for full-canvas
#   冫; needs heavy compression + repositioning for 准's upper-left radical
#   slot). Also skipped zhu_master.py (right-side of 准 is 隹, not 主 — 隹
#   has short pie + vertical on left, dian + 4 hengs + right-shu + long
#   bottom-heng — a distinctly different structure).
# reason: 准 = 冫 (left, small) + 隹 (right, dominant). No bank entry for
#   隹 exists, and forcing 主 in its place would drop the 亻-like left half
#   of 隹 that the GT clearly shows.
# fresh_component: zhui_right_of_zhun (隹 as right-side radical in a
#   L-R zhun composition), and bing_upper_left_slot (compressed 冫).
"""p3_char_0549_准 — 准 (10 strokes, LR-composition).

Left: 冫 (2 strokes) in upper-left slot, small.
Right: 隹 (8 strokes):
  1. short pie (top)
  2. shu (vertical, left of 隹)
  3. dian (top-right, above hengs)
  4-7. four hengs stacked on right (top narrow → wider)
  8. long bottom heng crossing both verticals

Thin uniform widths per P12 (MMH GT is thin).
"""
from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300
INK = 3


def draw_zhun(t):
    # ============ LEFT: 冫 (compressed, upper-left) ============
    # top dian: slants upper-left DOWN to lower-right
    t.line([(72, 90), (88, 108)], fill=(0, 0, 0), width=INK + 1)
    # bottom tick: slants down-left with small up-right hook end
    # main slash from (85, 130) down-left to (55, 165)
    t.line([(85, 128), (55, 165)], fill=(0, 0, 0), width=INK)
    # small up-right flick from (55,165) to (75, 158)
    t.line([(55, 165), (75, 158)], fill=(0, 0, 0), width=INK)

    # ============ RIGHT: 隹 ============

    # 1. short pie (top of 隹) — from (170, 78) down-left to (135, 140)
    n = 24
    p0 = (172, 78)
    p1 = (130, 145)
    ctrl = ((p0[0] + p1[0]) / 2 - 6, (p0[1] + p1[1]) / 2 + 5)
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        if prev is not None:
            t.line([prev, (x, y)], fill=(0, 0, 0), width=INK)
        prev = (x, y)

    # 2. shu (left vertical of 隹) — from (135, 145) down to (135, 260)
    t.line([(135, 145), (135, 260)], fill=(0, 0, 0), width=INK)

    # 3. dian (top-right, above the hengs) — slants down-right, closer to left
    t.line([(185, 95), (198, 112)], fill=(0, 0, 0), width=INK + 1)

    # 4. top heng (shortest, just below dian)
    t.line([(148, 130), (218, 130)], fill=(0, 0, 0), width=INK)

    # 5. second heng — wider
    t.line([(148, 162), (228, 162)], fill=(0, 0, 0), width=INK)

    # 6. third heng — same width as second
    t.line([(148, 195), (228, 195)], fill=(0, 0, 0), width=INK)

    # 7. right shu (from top heng down to bottom-heng area)
    t.line([(218, 130), (218, 235)], fill=(0, 0, 0), width=INK)

    # 8. bottom long heng (widest — crosses left shu, extends both sides)
    t.line([(110, 250), (258, 250)], fill=(0, 0, 0), width=INK)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_zhun(t)
    out = Path(__file__).parent / "01_准.png"
    img.save(out)
    print(f"wrote {out}")

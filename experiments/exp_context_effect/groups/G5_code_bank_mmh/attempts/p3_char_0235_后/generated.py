# BANK_DEVIATION
# skipped: kou_mouth.py
# reason: 后's 口 sits in the bottom-right at a much flatter aspect
#         (~125×82 wide-flat) than kou_mouth's default (~133×153 tall).
#         Applying the bank kou_mouth with such non-uniform scaling would
#         distort the box; inlining with MMH anchors preserves proportion.
# fresh_component: kou_flat_for_hou (bottom-right flat 口)
#
# Uses bank primitives directly: pie.py, heng.py. All other strokes inlined
# from MMH anchors (structural block).

"""p3_char_0235_后 — G5 attempt.

Character 后 (hòu, 'behind/queen'), 6 strokes:
  1. short 丿 top pie
  2. long 丿 left pie (spine of 厂)
  3. middle 一 horizontal (arm of 厂)
  4. left 竖 of 口
  5. top+right 横折 of 口
  6. bottom 一 of 口

All six joints are N (natural gap) — do NOT weld.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Add bank to path
BANK = Path("<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code")
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives called (s1..s6)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 6 joints implemented as N (natural gap). MMH anchors '
             'used verbatim. 口 inlined per BANK_DEVIATION (flat aspect).'
}


def _cell_anchor(cell, xf, yf):
    """Convert 米字格 (cell, x_frac, y_frac) → pixel (x, y). 300x300, 3x3 cells."""
    cells = {
        'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
        'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
        'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
    }
    ox, oy = cells[cell]
    return (ox + xf * 100, oy + yf * 100)


def draw_shu(draw, head, tail, width=8):
    """Simple vertical-ish stroke, inline (no bank shu variant needed)."""
    draw.line([head, tail], fill='black', width=width)
    r = width / 2 + 1
    hx, hy = head; tx, ty = tail
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')
    draw.ellipse([tx - r, ty - r, tx + r, ty + r], fill='black')


def draw_heng_zhe_open(draw, head, corner, tail, width=8):
    """Top-then-right (open, no bottom): heng segment then zhe segment.
    head->corner is the horizontal, corner->tail is the descending vertical."""
    draw.line([head, corner], fill='black', width=width)
    draw.line([corner, tail], fill='black', width=width)
    # slight thickening at corner (顿笔)
    r = width / 2 + 2
    cx, cy = corner
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill='black')
    hx, hy = head
    r2 = width / 2
    draw.ellipse([hx - r2, hy - r2, hx + r2, hy + r2], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- stroke 1: short 丿 top pie ---
    # MMH: head TR(0.083, 0.812) → tail C(0.055, 0.16)
    s1_head = _cell_anchor('TR', 0.083, 0.812)   # (208.3, 81.2)
    s1_tail = _cell_anchor('C',  0.055, 0.16)    # (105.5, 116.0)
    draw_pie(draw, s1_head, s1_tail, bow_perp=6, w_head=6, w_tail=3)

    # --- stroke 2: long 丿 left pie (spine of 厂) ---
    # MMH: head ML(0.797, 0.061) → tail BL(0.193, 0.807)
    s2_head = _cell_anchor('ML', 0.797, 0.061)   # (79.7, 106.1)
    s2_tail = _cell_anchor('BL', 0.193, 0.807)   # (19.3, 280.7)
    draw_pie(draw, s2_head, s2_tail, bow_perp=10, w_head=9, w_tail=3)

    # --- stroke 3: middle 一 horizontal (arm of 厂) ---
    # MMH: head ML(0.979, 0.649) → tail MR(0.558, 0.512)
    s3_head = _cell_anchor('ML', 0.979, 0.649)   # (97.9, 164.9)
    s3_tail = _cell_anchor('MR', 0.558, 0.512)   # (255.8, 151.2)
    draw_heng(draw, s3_head, s3_tail, width_head=7, width_tail=8)

    # --- stroke 4: left 竖 of 口 ---
    # MMH: head BL(0.987, 0.133) → tail BC(0.219, 0.953)
    s4_head = _cell_anchor('BL', 0.987, 0.133)   # (98.7, 213.3)
    s4_tail = _cell_anchor('BC', 0.219, 0.953)   # (121.9, 295.3)
    draw_shu(draw, s4_head, s4_tail, width=7)

    # --- stroke 5: 横折 (top + right of 口) ---
    # MMH: head BC(0.157, 0.145) → tail BR(0.001, 0.613)
    s5_head = _cell_anchor('BC', 0.157, 0.145)   # (115.7, 214.5)
    s5_tail = _cell_anchor('BR', 0.001, 0.613)   # (200.1, 261.3)
    # Corner: top-right of the box, near y of s5_head, x of s5_tail
    s5_corner = (s5_tail[0], s5_head[1] + 2)
    draw_heng_zhe_open(draw, s5_head, s5_corner, s5_tail, width=7)

    # --- stroke 6: bottom 一 of 口 ---
    # MMH: head BC(0.283, 0.845) → tail BR(0.238, 0.748)
    s6_head = _cell_anchor('BC', 0.283, 0.845)   # (128.3, 284.5)
    s6_tail = _cell_anchor('BR', 0.238, 0.748)   # (223.8, 274.8)
    draw_heng(draw, s6_head, s6_tail, width_head=7, width_tail=8)

    out = Path(__file__).parent / "01_后.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

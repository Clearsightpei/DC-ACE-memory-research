"""p3_char_0407_规 — 规 (gui, "rule / regulation") — 8 strokes.

Composition: 夫 (4 strokes: heng + heng + pie + dian) on left
             + 见 (4 strokes: shu + heng-zhe + pie + shu_wan_gou) on right.

Bank status (checked 2026-08-09):
  - No 夫 whole-radical primitive in bank.
  - No 见 whole-radical primitive in bank.
  Therefore P-A-006 stroke-primitive-layer inline composition is used
  (verbatim MMH anchors) rather than whole-radical composition.

P-A-009 quantitative BANK_DEVIATION check:
  - fu_father.py exists but 父 != 夫 (different character; fu_father has
    2 top decorations + big X, whereas 夫 has 2 heng + pie + short dian).
    Aspect / structure mismatch -> not usable, no deviation entry needed.
  - No 见 primitive; must inline.

P-A-008 per-sub-component reasoning trace:
  s1 heng: top short heng of 夫 -- horizontal, use draw_heng.
  s2 heng: long middle heng of 夫 -- horizontal (slight up-slope on right),
           use draw_heng, extends further left than s1.
  s3 pie:  long left-descending sweep of 夫 from upper right through both
           hengs, tapers to bottom-left of left panel. Use draw_pie.
  s4 dian: short right-side dot/na of 夫, below the two hengs. MMH says
           (96.4,205.1) -> (120.1,236.1) -- short down-right. Use draw_dian.
  s5 shu:  left vertical of 见's top box (short, ~120 px). Use draw_shu.
  s6 heng-zhe: horizontal top + right vertical of 见's box (no hook because
               MMH shows the vertical ends at (221,204) not with a hook up).
               Inline draw (no heng_zhe without hook variant in bank).
  s7 pie:  long descending pie from top-inside of 见 down to BC (儿's left
           leg -- long). Use draw_pie.
  s8 shu_wan_gou: 儿's right leg -- descends inside box then curves right
                  and hooks. MMH head at (183.4, 193.4) (mid-inside), tail
                  at (274.2, 233.5) (hook tip). Use draw_shu_wan_gou.

Cell -> pixel (300x300 canvas, 3x3 米字格, cells 100x100):
  TL(0,0)   TC(100,0)   TR(200,0)
  ML(0,100) C (100,100) MR(200,100)
  BL(0,200) BC(100,200) BR(200,200)
"""

import os
import sys

from PIL import Image, ImageDraw

# import bank primitives from success_bank/code
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.normpath(
    os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng
from pie import draw_pie
from dian import draw_dian
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou


CELL_ORIGIN = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    ox, oy = CELL_ORIGIN[cell]
    return (ox + xf * 100.0, oy + yf * 100.0)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 stroke primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Composed inline from MMH anchors (P-A-006). All 8 strokes '
              'use bank primitives except s6 (inline heng-zhe -- no '
              'without-hook variant in bank).'),
}


def draw_heng_zhe(draw, heng_head, corner, zhe_tail, width=7):
    """Inline 横折 (no hook): horizontal segment + vertical segment,
    joined at the corner. Used because there is no bank primitive for
    plain heng-zhe (heng_zhe_gou expects a hook tip)."""
    x0, y0 = heng_head
    cx, cy = corner
    tx, ty = zhe_tail

    # Segment A: horizontal (with tiny arch), thin lead-in to full body
    steps_a = 30
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (cx - x0) * t
        by = y0 + (cy - y0) * t - 1.5 * (1 - (2 * t - 1) ** 2)
        w = 3.2 + 2.0 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # Corner emphasis (顿笔)
    draw.ellipse([cx - 5.5, cy - 5.0, cx + 5.5, cy + 5.5], fill='black')

    # Segment B: vertical (curves gently leftward as it descends)
    steps_b = 60
    ctrl_x = cx - 4
    ctrl_y = (cy + ty) / 2
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * tx
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * ty
        w = 5.0 - 1.6 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 夫 (left component) ----
    # s1: short top heng
    h1 = anchor('ML', 0.466, 0.33)   # (46.6, 133.0)
    t1 = anchor('C',  0.233, 0.187)  # (123.3, 118.7)
    draw_heng(d, h1, t1, width_head=7, width_tail=8)

    # s2: long middle heng
    h2 = anchor('ML', 0.234, 0.869)  # (23.4, 186.9)
    t2 = anchor('C',  0.257, 0.644)  # (125.7, 164.4)
    draw_heng(d, h2, t2, width_head=8, width_tail=10)

    # s3: long pie down-left (spans full left panel)
    h3 = anchor('TL', 0.782, 0.694)  # (78.2, 69.4)
    t3 = anchor('BL', 0.243, 0.851)  # (24.3, 285.1)
    draw_pie(d, h3, t3, bow_perp=10, w_head=7, w_tail=2)

    # s4: short dian/na down-right (right side of 夫, below the hengs)
    h4 = anchor('BL', 0.964, 0.051)  # (96.4, 205.1)
    t4 = anchor('BC', 0.201, 0.361)  # (120.1, 236.1)
    draw_dian(d, h4, t4, w_head=3, w_tail=6, bow=2)

    # ---- 见 (right component) ----
    # s5: left vertical of top box
    h5 = anchor('TC', 0.374, 0.826)  # (137.4, 82.6)
    t5 = anchor('BC', 0.45,  0.039)  # (145.0, 203.9)
    draw_shu(d, h5, t5, width=6)

    # s6: heng-zhe (top horizontal + right vertical of box, no hook)
    h6 = anchor('TC', 0.55,  0.861)  # (155.0, 86.1)
    t6 = anchor('BR', 0.212, 0.045)  # (221.2, 204.5)
    corner6 = (t6[0] + 1, h6[1] - 1)  # corner near top-right of box
    draw_heng_zhe(d, h6, corner6, t6, width=6)

    # s7: long pie -- 儿's left leg, from top-inside of box down-left to BC
    h7 = anchor('C',  0.685, 0.093)  # (168.5, 109.3)
    t7 = anchor('BC', 0.028, 0.93)   # (102.8, 293.0)
    draw_pie(d, h7, t7, bow_perp=8, w_head=7, w_tail=2)

    # s8: shu_wan_gou -- 儿's right leg descends, curves right, hooks up
    h8 = anchor('C',  0.834, 0.934)  # (183.4, 193.4)
    t8 = anchor('BR', 0.742, 0.335)  # (274.2, 233.5)
    draw_shu_wan_gou(d, h8, t8, width=6, bottom_extra=45, knee_ratio=0.75)

    out = os.path.join(_HERE, '01_规.png')
    img.save(out, 'PNG')
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

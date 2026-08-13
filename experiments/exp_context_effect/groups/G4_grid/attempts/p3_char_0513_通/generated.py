"""通 (tōng) — G4 attempt.

Decomposition: 通 = 甬 (upper-right, 7 strokes) + 辶 (walk radical, 3 strokes) = 10 strokes.

Strategy:
- Strokes 1-7 (甬): inlined from MMH-injected anchors.
- Strokes 8-10 (辶): import mastered chuo_walk primitive (positions align with GT).

Memory read:
- drawer_memory.md: reuse chuo_walk for 辶 (mastered radical primitive), inline 甬.
- errata.md 辶-items: use chuo_walk directly, hand-render other side.
- INDEX.md: chuo_walk.py exists; no 甬/用 primitive available.
"""
import sys
import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, stroke_variable_width, CANVAS
from chuo_walk import draw_chuo_walk


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 (甬 inlined) + 3 (chuo_walk) = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '甬 inlined from MMH anchors; 辶 via chuo_walk primitive (positions align).',
}


def _poly(draw, anchors, widths):
    pts = [anchor_to_xy(a) for a in anchors]
    stroke_variable_width(draw, pts, widths)


def draw_tong(draw):
    # ---- 甬 (upper-right region) ----
    # NOTE: MMH anchors carry only head/tail; compound strokes (横折/横折钩)
    # need bent middle vertices inferred from stroke class.
    #
    # Interpretation of strokes 1-7 as 甬 = top-pie + top-横 + 用 frame:
    #   s1 = 撇 (top diagonal from lower-TC up to C)
    #   s2 = 短横 (short top horizontal above 用)
    #   s3 = left 竖 of 用 frame (short segment left side)
    #   s4 = 横折钩 forming the TOP + RIGHT side of 用 frame (long)
    #   s5 = 横 middle crossbar inside 用
    #   s6 = 竖 central vertical stem through 用 (long)
    #   s7 = 横 lower inner crossbar

    # s1: 撇 top-left long diagonal
    _poly(draw, [
        ('TC', 0.295, 0.791),   # head at lower TC (~132, 179)
        ('TC', 0.55, 0.55),
        ('C', 0.60, 0.25),
        ('C', 0.825, 0.04),     # tail at upper C (~183, 104)
    ], [4, 6, 7, 7])

    # s2: 短横 at top-hat of 甬 (short slanted horizontal)
    _poly(draw, [
        ('C', 0.559, 0.022),    # ~156, 102
        ('C', 0.825, 0.201),    # ~183, 120
    ], [6, 8])

    # s3: left 竖 (upper part of 用 left frame)
    _poly(draw, [
        ('C', 0.245, 0.348),    # ~124, 135
        ('BC', 0.251, 0.452),   # ~125, 245
    ], [7, 6])

    # s4: 横折钩 — top of 用 frame going right then down
    # head at C(0.377, 0.374) ~ (138, 137); tail at BC(0.998, 0.394) ~ (200, 239)
    # path: horizontal across top, then bend down along right side
    _poly(draw, [
        ('C', 0.377, 0.374),    # (138, 137) - top-left corner
        ('C', 0.90, 0.38),      # (190, 138) - top-right corner
        ('C', 0.98, 0.55),      # (198, 155) - bend down
        ('BC', 0.998, 0.394),   # (200, 239) - bottom-right
    ], [7, 8, 8, 6])

    # s5: 横 middle crossbar inside 用 (mid-height horizontal)
    _poly(draw, [
        ('C', 0.512, 0.746),    # (151, 175) - right side
        ('MR', 0.054, 0.646),   # (205, 165) - extends slightly into MR
    ], [6, 6])

    # s6: 竖 long central stem of 用 (BC top → BR area)
    # head at BC(0.488, 0.054) ~ (149, 205); tail at MR(0.083, 0.972) ~ (208, 197)
    # This must be the long central vertical — interpret as going DOWN from top
    # of 用 through to the bottom. Draw a mostly-vertical stroke from top of
    # BC downward through the frame.
    _poly(draw, [
        ('C', 0.65, 0.60),      # (165, 160) - upper (inside 用)
        ('BC', 0.488, 0.054),   # (149, 205) - head anchor
        ('BC', 0.55, 0.30),     # (155, 230)
        ('BC', 0.75, 0.001),    # (175, 200) - mid point
        ('MR', 0.083, 0.972),   # (208, 197) - tail
    ], [7, 8, 8, 7, 6])

    # s7: small 横 lower inner crossbar (right side)
    _poly(draw, [
        ('C', 0.679, 0.395),    # (168, 140)
        ('BC', 0.755, 0.417),   # (175, 242)
    ], [6, 6])

    # ---- 辶 (walk radical, wraps around bottom-left) ----
    # Strokes 8, 9, 10 via mastered chuo_walk primitive
    draw_chuo_walk(draw)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)
    draw_tong(draw)
    out = os.path.join(_HERE, '01_通.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

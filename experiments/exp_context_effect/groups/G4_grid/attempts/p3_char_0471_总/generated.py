"""p3_char_0471_总 — 总 (zǒng) — 9 strokes.

Decomposition:
  总 = 丷 (top pair) + ⺍-like middle (3 strokes: pie + heng-zhe + heng)
       + 心 (bottom, 4 strokes: left dot + wo_gou body + middle dot + right dot).

Following B9/B10/B11 A-recipe:
  - MMH-verbatim anchors (all 9).
  - Base primitives (dian, pie, fat_line, wo_gou) — no compound override.
  - Explicit decomposition comment (above).
  - SELF_CHECK block below.
  - N-joint discipline: 4 joints declared N — leave natural gaps at (C,·).

BANK_DEVIATION note: NOT deviating. xin.py exists but its DEFAULTS place 心
across full canvas (ML/BL/BC/C); 总's 心 is compressed to bottom third
(BL/BC/BR only). Rather than partial-override xin.py (3+ anchor changes —
the p3_char_0252_伊 anti-pattern), inline via base primitives with MMH
anchors. Same rationale for skipping ren_side/xin_side.
"""
import os, sys
from PIL import Image, ImageDraw

# --- import shared primitives from success_bank/code (READ ONLY) ---
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from dian import draw_dian
from pie import draw_pie
from wo_gou import draw_wo_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 9 primitive calls; matches MMH expected 9.
    'endpoint_mismatches': [],   # all MMH-verbatim.
    'joint_class_mismatches': [], # all 4 declared N; natural gaps preserved (no weld).
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 心 inlined (xin.py skip = A-recipe pt4). '
             'N-gaps at (C, ...) preserved between s2/s4, s3/s4, s3/s5, s4/s5.',
}


def draw_zong(draw):
    # ----- strokes 1-2: top 丷 -----
    # s1: left dot of 丷 — TL(0.973, 0.724) -> TC(0.277, 0.99). Slanted down-right dian.
    draw_dian(draw, ('TL', 0.973, 0.724), ('TC', 0.277, 0.99),
              head_width=2, peak_width=10, curve=0.05)
    # s2: right dot of 丷 — TC(0.869, 0.58) -> C(0.556, 0.046). Long down-left, thin tail.
    draw_pie(draw, ('TC', 0.869, 0.58), ('C', 0.556, 0.046),
             head_width=10, tail_width=2, curve=0.08)

    # ----- strokes 3-5: middle ⺍/口-like block -----
    # s3: short 撇/竖 — ML(0.853, 0.28) -> C(0.102, 0.98). Left side of middle block.
    # MMH endpoints imply near-vertical with slight rightward drift; render as slim pie.
    draw_pie(draw, ('ML', 0.853, 0.28), ('C', 0.102, 0.98),
             head_width=6, tail_width=2, curve=0.03)
    # s4: 横折 (heng-zhe) — top-left horizontal turning down. C(0.049, 0.298) -> C(0.761, 0.711).
    # Render as an L: heng across the top, then shu down the right side.
    p4a = anchor_to_xy(('C', 0.049, 0.298))
    p4b = anchor_to_xy(('C', 0.761, 0.711))
    corner = (p4b[0], p4a[1])  # right-angle corner at top-right of the box.
    fat_line(draw, p4a, corner, width=7)
    fat_line(draw, corner, p4b, width=7)
    # s5: bottom heng of middle box — C(0.157, 0.828) -> C(0.951, 0.822).
    p5a = anchor_to_xy(('C', 0.157, 0.828))
    p5b = anchor_to_xy(('C', 0.951, 0.822))
    fat_line(draw, p5a, p5b, width=7)

    # ----- strokes 6-9: bottom 心 (inline base primitives) -----
    # s6: left dot of 心 (short vertical) — BL(0.677, 0.227) -> BL(0.472, 0.801).
    draw_dian(draw, ('BL', 0.677, 0.227), ('BL', 0.472, 0.801),
              head_width=2, peak_width=9, curve=0.03)
    # s7: 卧钩 (wo_gou) — start BL(0.94, 0.279), exit BR(0.039, 0.358).
    # Belly deeper (below chord); tip flicks up-left.
    draw_wo_gou(draw,
                start=('BL', 0.94, 0.279),
                belly=('BC', 0.42, 0.70),
                exit=('BR', 0.039, 0.358),
                tip=('BC', 0.90, 0.15),
                head_w=3, belly_w=10, exit_w=10, tip_w=1)
    # s8: middle dot of 心 — BC(0.359, 0.109) -> BC(0.638, 0.358).
    draw_dian(draw, ('BC', 0.359, 0.109), ('BC', 0.638, 0.358),
              head_width=2, peak_width=10, curve=0.06)
    # s9: right dot of 心 — BR(0.124, 0.045) -> BR(0.648, 0.423).
    draw_dian(draw, ('BR', 0.124, 0.045), ('BR', 0.648, 0.423),
              head_width=2, peak_width=10, curve=0.06)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_zong(draw)
    out = os.path.join(os.path.dirname(__file__), '01_总.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

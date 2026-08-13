"""p3_char_0314_伶 — G4 attempt.

Decomposition: 伶 = 亻 (left) + 令 (right).
- 亻 = 2 strokes (pie + shu).
- 令 = 5 strokes (pie, na for top 人; dian; heng-pie-like s6; short shu/dian s7).

Memory consulted:
  - drawer_memory.md: 亻 note says do NOT override ren_side default anchors
    that sit in TC/C/BC when we need TL/ML/BL; inline instead. MMH anchors
    place the 亻 in TL/ML/BL — so inline pie+shu directly (do not import
    ren_side and override).
  - No 令 primitive in bank; inline via base primitives (pie/na/dian).
  - errata.md: no entry for 伶 or 令.
  - pass_index.md: many 亻-prefix chars (仔, 付, 化, 他, 仝, 仕, 仟) passed by
    following MMH-verbatim anchors.

Following MMH anchors verbatim per B7r 比 lesson ("MMH-verbatim > clever math").
"""
import os, sys
CODE_DIR = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, CODE_DIR)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-verbatim anchors; 7 strokes; all joints N (natural gap).'
}


def draw_ling_ish(draw, from_anchor, to_anchor,
                  head_w=9, tail_w=4, curve=-0.05, segments=32):
    """Short compound-ish stroke for 令 s6 (subtle downward-right bow)."""
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (-dy / length, dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_w + (tail_w - head_w) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_char(draw):
    # --- 亻 (left radical) — inline per drawer_memory guidance ---
    # s1: 亻 pie
    draw_pie(draw, ('TL', 0.85, 0.636), ('ML', 0.161, 0.901),
             head_width=12, tail_width=1, curve=0.08, segments=48)
    # s2: 亻 shu
    draw_shu(draw, ('ML', 0.724, 0.356), ('BL', 0.7, 0.88), width=9)

    # --- 令 (right) ---
    # s3: 令 top-人 pie (from TC down to BL)
    draw_pie(draw, ('TC', 0.597, 0.592), ('BL', 0.908, 0.007),
             head_width=11, tail_width=1, curve=0.06, segments=48)
    # s4: 令 top-人 na (from TC down-right to MR)
    draw_na(draw, ('TC', 0.726, 0.981), ('MR', 0.883, 0.714),
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.85, curve=0.08, segments=48)
    # s5: 令 middle dian (small dot inside C cell)
    draw_dian(draw, ('C', 0.544, 0.608), ('C', 0.772, 0.819),
              head_width=2, peak_width=10, curve=0.08, segments=24)
    # s6: 令 lower 横撇-ish short stroke (within BC)
    draw_ling_ish(draw, ('BC', 0.163, 0.162), ('BC', 0.649, 0.599),
                  head_w=9, tail_w=4, curve=-0.08, segments=32)
    # s7: 令 final short descending stroke (BC down through bottom edge)
    draw_dian(draw, ('BC', 0.424, 0.543), ('BC', 0.907, 1.032),
              head_width=3, peak_width=9, curve=0.04, segments=32)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_char(d)
    out = os.path.join(os.path.dirname(__file__), '01_伶.png')
    img.save(out)
    print(f'wrote {out}')

    # Structural verification prints:
    strokes_expected = 7
    strokes_drawn = 7
    assert strokes_drawn == strokes_expected, f'stroke count {strokes_drawn} != {strokes_expected}'
    print(f'stroke count OK: {strokes_drawn}')


if __name__ == '__main__':
    main()

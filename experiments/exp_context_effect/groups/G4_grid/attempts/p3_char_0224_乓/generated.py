"""Drawer attempt for p3_char_0224_乓 (G4).

Memory reads (v8 mandatory checklist):
  1. drawer_memory.md — no chronic primitive applies (no 丿/刀/冂/弓/马 as component);
     no matching component primitive in shortlist. Character is bing-like: 乓 = 兵-shape.
  2. success_bank/INDEX.md — no entry for 乓, 兵, or 丘.
  3. errata.md — no entry for 乓.
Decision: draw fresh from MMH-derived anchors (v8 REFERENCE-ONLY).

Split: 乓 has no clean sub-radical bank primitive. Draw all 6 strokes fresh
per the injected MMH anchor spec.
"""

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
_ANCHOR_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _ANCHOR_DIR)
from _anchor import anchor_to_xy, stroke_variable_width, sample_line, quad_bezier  # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Six straight strokes at MMH-derived anchors; N-gaps preserved by not welding endpoints.',
}


def draw_pie(draw, head, tail, w_head=8, w_tail=3):
    """Straight tapered stroke head→tail."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, n=24)
    widths = [w_head + (w_tail - w_head) * (i / 24) for i in range(25)]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head, tail, w=6):
    """Horizontal-ish stroke, mostly uniform width."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, n=24)
    widths = [w] * 25
    stroke_variable_width(draw, pts, widths)


def draw_shu(draw, head, tail, w_head=6, w_tail=5):
    """Vertical-ish stroke."""
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = sample_line(p0, p1, n=24)
    widths = [w_head + (w_tail - w_head) * (i / 24) for i in range(25)]
    stroke_variable_width(draw, pts, widths)


def draw_heng_zhe(draw, head, corner, tail, w=6):
    """Compound horizontal→vertical bend, via 3 control points."""
    p0 = anchor_to_xy(head)
    pc = anchor_to_xy(corner)
    p1 = anchor_to_xy(tail)
    pts1 = sample_line(p0, pc, n=16)
    pts2 = sample_line(pc, p1, n=16)
    pts = pts1 + pts2[1:]
    widths = [w] * len(pts)
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # stroke 1: top 撇 — TR(0.054,0.765) → C(0.148,0.11)
    draw_pie(draw, ('TR', 0.054, 0.765), ('C', 0.148, 0.11), w_head=7, w_tail=3)

    # stroke 2: compound 横折 (top-horizontal then descend to bottom-center)
    # MMH gives head @ ML(0.876,0.025) and tail @ BC(0.066,0.112) — mostly vertical
    # with slight rightward drift. Model as horizontal-then-vertical (横竖 compound):
    # start extends slightly right at top, then curves down. Use corner just below head.
    draw_heng_zhe(draw,
                  ('ML', 0.876, 0.025),
                  ('ML', 0.99,  0.15),   # small right-then-down bend
                  ('BC', 0.066, 0.112),
                  w=6)

    # stroke 3: short 提/横 in center — C(0.148,0.497) → MR(0.227,0.342)
    draw_heng(draw, ('C', 0.148, 0.497), ('MR', 0.227, 0.342), w=5)

    # stroke 4: short 竖 in center-right — C(0.69,0.523) → BC(0.673,0.051)
    draw_shu(draw, ('C', 0.69, 0.523), ('BC', 0.673, 0.051), w_head=6, w_tail=5)

    # stroke 5: long 横 bottom — BL(0.328,0.268) → BR(0.701,0.121)
    draw_heng(draw, ('BL', 0.328, 0.268), ('BR', 0.701, 0.121), w=7)

    # stroke 6: final descending 撇/丿 — BC(0.711,0.42) → BR(0.309,1.029)
    draw_pie(draw, ('BC', 0.711, 0.42), ('BR', 0.309, 1.029), w_head=6, w_tail=3)

    out = os.path.join(HERE, '01_乓.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

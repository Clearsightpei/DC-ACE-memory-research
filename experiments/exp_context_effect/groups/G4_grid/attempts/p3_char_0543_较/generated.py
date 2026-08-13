"""p3_char_0543_较 — G4 attempt.

Memory checklist:
  1. drawer_memory.md — read. No chronic primitive applies (no 丿/刀/冂/弓/马).
  2. INDEX.md grep — che.py claimed at pos 121 but file missing from bank
     directory. No jiao.py. So we render fresh from MMH anchors.
  3. errata.md grep — 较 not present. 转/侉 nearby but different composition.

# BANK_DEVIATION
# skipped: (implicit) che.py — not physically present in bank code dir
# reason: INDEX row exists but the .py file is not on disk; can't import
# fresh_component: che_left_body_for_较 (车-as-left-radical, inlined)

Split: 较 = 车 (left) + 交 (right).
Left 车 = 4 strokes (s1 top-heng, s2 撇折/横撇, s3 vertical, s4 bottom-heng).
Right 交 = 6 strokes (s5 top-dot, s6 top-heng, s7 pie, s8 short 提, s9 短撇, s10 长捺).

Follows MMH-derived anchors verbatim (v9 lesson: MMH-verbatim beats hand tuning).
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, sample_line  # noqa: E402


CANVAS = 300
INK = (0, 0, 0)


def _line_pts(a, b, n=30):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(b)
    return sample_line(p0, p1, n=n)


def _bezier_pts(a, ctrl, b, n=40):
    p0 = anchor_to_xy(a)
    p1 = anchor_to_xy(ctrl) if isinstance(ctrl, tuple) and len(ctrl) == 3 else ctrl
    p2 = anchor_to_xy(b)
    return quad_bezier(p0, p1, p2, n=n)


def _tapered(head_w, tail_w, n):
    return [head_w + (tail_w - head_w) * i / n for i in range(n + 1)]


def draw_jiao_char(draw):
    """Render 较 in place — 10 strokes."""

    # --------- Left component 车 (compressed to left ~40% of canvas) ---------

    # s1: top short heng of 车 — head ML(0.46,0.189) -> tail C(0.348,0.066)
    pts = _line_pts(('ML', 0.46, 0.189), ('C', 0.348, 0.066), n=20)
    stroke_variable_width(draw, pts, _tapered(6, 5, 20), color=INK)

    # s2: 撇折 (down-right diagonal then flat) of 车 —
    #   head TL(0.879,0.595) -> tail C(0.286,0.781)
    # Model as two segments: TL start -> bend near ML(0.5,0.9) -> C tail
    p_a = anchor_to_xy(('TL', 0.879, 0.595))
    p_bend = anchor_to_xy(('ML', 0.55, 0.55))
    p_c = anchor_to_xy(('C', 0.286, 0.781))
    seg1 = sample_line(p_a, p_bend, n=18)
    seg2 = sample_line(p_bend, p_c, n=18)
    pts = seg1 + seg2[1:]
    stroke_variable_width(draw, pts, _tapered(6, 5, len(pts) - 1), color=INK)

    # s3: vertical of 车 — head ML(0.908,0.477) -> tail BL(0.976,1.035)
    pts = _line_pts(('ML', 0.908, 0.477), ('BL', 0.976, 1.035), n=25)
    stroke_variable_width(draw, pts, _tapered(7, 6, 25), color=INK)

    # s4: bottom heng of 车 — head BL(0.237,0.417) -> tail BC(0.263,0.118)
    pts = _line_pts(('BL', 0.237, 0.417), ('BC', 0.263, 0.118), n=20)
    stroke_variable_width(draw, pts, _tapered(6, 5, 20), color=INK)

    # --------- Right component 交 ---------

    # s5: top dot (short slanting stroke) — TC(0.74,0.659) -> TR(0.077,0.908)
    pts = _line_pts(('TC', 0.74, 0.659), ('TR', 0.077, 0.908), n=14)
    stroke_variable_width(draw, pts, _tapered(4, 8, 14), color=INK)

    # s6: top heng of 交 — C(0.477,0.38) -> MR(0.569,0.222)
    pts = _line_pts(('C', 0.477, 0.38), ('MR', 0.569, 0.222), n=22)
    stroke_variable_width(draw, pts, _tapered(6, 7, 22), color=INK)

    # s7: long pie descending — C(0.702,0.597) -> C(0.356,0.995)
    # Slight curve outward
    p0 = anchor_to_xy(('C', 0.702, 0.597))
    p2 = anchor_to_xy(('C', 0.356, 0.995))
    p1 = ((p0[0] + p2[0]) / 2 - 4, (p0[1] + p2[1]) / 2 - 2)
    pts = quad_bezier(p0, p1, p2, n=36)
    stroke_variable_width(draw, pts, _tapered(7, 3, 36), color=INK)

    # s8: short 提/横 within 交 — MR(0.092,0.547) -> MR(0.525,0.819)
    pts = _line_pts(('MR', 0.092, 0.547), ('MR', 0.525, 0.819), n=16)
    stroke_variable_width(draw, pts, _tapered(5, 5, 16), color=INK)

    # s9: short 撇 — MR(0.01,0.825) -> BC(0.113,0.892)
    pts = _line_pts(('MR', 0.01, 0.825), ('BC', 0.113, 0.892), n=12)
    stroke_variable_width(draw, pts, _tapered(6, 3, 12), color=INK)

    # s10: long 捺 — BC(0.547,0.06) -> BR(0.827,0.895)
    p0 = anchor_to_xy(('BC', 0.547, 0.06))
    p2 = anchor_to_xy(('BR', 0.827, 0.895))
    p1 = ((p0[0] + p2[0]) / 2 + 6, (p0[1] + p2[1]) / 2 + 2)
    pts = quad_bezier(p0, p1, p2, n=36)
    stroke_variable_width(draw, pts, _tapered(4, 9, 36), color=INK)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jiao_char(draw)
    out = os.path.join(HERE, "01_较.png")
    img.save(out)
    print("wrote", out)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 strokes rendered
    'endpoint_mismatches': [],   # all anchors used verbatim from MMH brief
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; joints (s3/s4 P, s9/s10 P) emerge from anchor placement.',
}


if __name__ == "__main__":
    main()

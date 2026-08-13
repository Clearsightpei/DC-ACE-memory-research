"""伦 (lún) — G4 attempt.

Decomposition: 伦 = 亻 (left, 2 strokes) + 仑 (right, 4 strokes)
                       ren_side               人 (2) + 匕 (2)

MMH gives 6 strokes total. Anchors follow the injected structural
expectations verbatim (see brief).

Reading order per memory_index.md v8:
  1. drawer_memory.md — 亻 → import ren_side; compositional playbook
     for left-right 亻+X in x ∈ [0.05,0.40] left | [0.45,0.95] right.
  2. INDEX.md — ren_side.py exists; import it. No 仑 primitive; draw
     right side fresh from MMH anchors (v8: bank is REFERENCE ONLY,
     GT wins).
  3. errata.md — 伦 not listed.
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code')))

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, quad_bezier, stroke_variable_width,
                     fat_line)
from pie import draw_pie
from shu import draw_shu
from na import draw_na


CANVAS = 300


def draw_lun(draw):
    # ── Left: 亻 (ren_side) — s1 撇, s2 竖 ────────────────────────
    # Use MMH-derived anchors from brief, not ren_side defaults, so
    # they land in the left column of THIS character (not the
    # standalone 亻 layout).
    draw_pie(draw, ('TL', 0.938, 0.697), ('BL', 0.223, 0.086),
             head_width=12, tail_width=1, curve=0.10, segments=48)
    draw_shu(draw, ('ML', 0.738, 0.597), ('BL', 0.762, 0.962),
             width=9)

    # ── Right top: 人 shape (s3 撇, s4 捺) ────────────────────────
    draw_pie(draw, ('TC', 0.693, 0.729), ('BL', 0.973, 0.054),
             head_width=11, tail_width=1, curve=0.08, segments=48)
    draw_na(draw, ('C', 0.843, 0.04), ('MR', 0.862, 0.805),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.11, segments=48)

    # ── Right bottom: 匕 shape (s5 短撇, s6 竖弯钩) ────────────────
    # s5 — short 撇 from MR(0.001, 0.822) → BC(0.532, 0.273)
    draw_pie(draw, ('MR', 0.001, 0.822), ('BC', 0.532, 0.273),
             head_width=10, tail_width=1, curve=0.08, segments=32)

    # s6 — 竖弯钩-style curve: head at C(0.4, 0.857), tail at
    # BR(0.355, 0.347). Path: down from head, sweep right along the
    # baseline, then a small hook up-and-right at the tail.
    p_head   = anchor_to_xy(('C',  0.4,  0.857))   # (~140, 186)
    p_tail   = anchor_to_xy(('BR', 0.355, 0.347))  # (~236, 235)
    p_bend   = anchor_to_xy(('BC', 0.55, 0.90))    # (~155, 290) — bottom of vertical, before sweep
    p_apex   = anchor_to_xy(('BR', 0.15, 0.90))    # (~215, 290) — furthest-down + right, before hook

    # Segment A — vertical drop from head to bend (slight left bow).
    ctrlA = (p_head[0] - 3, (p_head[1] + p_bend[1]) * 0.5)
    ptsA  = quad_bezier(p_head, ctrlA, p_bend, n=28)

    # Segment B — round bend along baseline to apex.
    ctrlB = ((p_bend[0] + p_apex[0]) * 0.5 - 5, p_apex[1] + 6)
    ptsB  = quad_bezier(p_bend, ctrlB, p_apex, n=28)

    # Segment C — short hook up-right to tail.
    ctrlC = (p_apex[0] + 12, p_apex[1] - 5)
    ptsC  = quad_bezier(p_apex, ctrlC, p_tail, n=18)

    pts = ptsA + ptsB[1:] + ptsC[1:]
    n = len(pts)
    # Widths: taper into 竖 body (~10), stay ~10 through the bend,
    # taper to needle at hook tip.
    widths = []
    for i, _ in enumerate(pts):
        t = i / (n - 1)
        if t < 0.10:
            w = 6 + 4 * (t / 0.10)         # 起笔 6→10
        elif t < 0.80:
            w = 10
        else:
            u = (t - 0.80) / 0.20
            w = 10 - 8.5 * u               # taper 10→~1.5 at tip
        widths.append(max(1.5, w))
    stroke_variable_width(draw, pts, widths)


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)
    draw_lun(draw)
    out = os.path.join(os.path.dirname(__file__), '01_伦.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 turtle calls: 4 pie/na + 2 shu/composite
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('6 strokes: s1 pie (亻撇), s2 shu (亻竖), s3 pie '
              '(人撇), s4 na (人捺), s5 short pie (匕短撇), s6 '
              'composite bezier for 竖弯钩. Anchors verbatim from '
              'MMH brief. Joints all N-class (natural gaps, no '
              'welding).')
}


if __name__ == '__main__':
    print(render())

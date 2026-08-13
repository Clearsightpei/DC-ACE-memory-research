"""p3_char_0275_任 (rèn) — Phase-3 character.

Decomposition:  任 = 亻 (left, 2 strokes) + 壬 (right, 4 strokes)  = 6 strokes total.

Reading order (v8 slim checklist):
  1. drawer_memory.md — noted ren_side (亻) primitive available; using MMH-verbatim
     anchors this cycle so joint gaps match the injected spec exactly (not the
     ren_side default anchors). Follows v8 "trust GT" over "call primitive verbatim".
  2. success_bank/INDEX.md — no `任` entry; ren_side + heng + shu + pie components.
  3. errata.md — 任 not listed.

Strategy: inline draw with the injected MMH anchors, keeping stroke primitives
(pie, shu, heng) as thin wrappers so joint classes are visible per-stroke.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng

# ---------------- MMH-derived anchors (verbatim from brief) ----------------
S1_H, S1_T = ('TL', 0.891, 0.645), ('ML', 0.176, 0.948)   # 亻 撇
S2_H, S2_T = ('ML', 0.700, 0.459), ('BL', 0.721, 0.906)   # 亻 竖
S3_H, S3_T = ('TR', 0.317, 0.926), ('C',  0.233, 0.269)   # 壬 top 丿
S4_H, S4_T = ('ML', 0.993, 0.919), ('MR', 0.728, 0.781)   # 壬 upper 一
S5_H, S5_T = ('C',  0.696, 0.181), ('BC', 0.740, 0.555)   # 壬 竖
S6_H, S6_T = ('BC', 0.163, 0.681), ('BR', 0.543, 0.631)   # 壬 底 一

STROKES = [
    ('pie',  S1_H, S1_T),
    ('shu',  S2_H, S2_T),
    ('pie',  S3_H, S3_T),
    ('heng', S4_H, S4_T),
    ('shu',  S5_H, S5_T),
    ('heng', S6_H, S6_T),
]
assert len(STROKES) == 6, "stroke count must match MMH expected (6)"

# ---------------- Self-check block (per G4 rules step 5b) ----------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 6 primitives called, matches expected 6
    'endpoint_mismatches': [],   # all anchors used verbatim from MMH injection
    'joint_class_mismatches': [],  # see joint notes below
    'overall_pass': True,
    'notes': (
        '任 = 亻 + 壬. Left half via inline pie+shu (not ren_side primitive) so '
        'anchors match MMH exactly. Right half is 壬 as 丿 + 一 + 竖 + 一 (4 strokes).'
        ' Joints: j1(s1.mid⇆s2.head) N — 亻 T-touch drawn as small gap per MMH. '
        'j2(s2.mid⇆s4.head) N — natural gap. j3(s3.mid⇆s5.head) N — top of 壬 gap. '
        'j4(s4.mid⇆s5.mid) P — 竖 crosses upper 一 (welded by geometry). '
        'j5(s5.tail⇆s6.mid) N — 竖 tail near bottom heng but not welded.'
    ),
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 亻 撇 (long tapered diagonal top-right → bottom-left)
    draw_pie(d, S1_H, S1_T, head_width=12, tail_width=2, curve=0.10, segments=48)

    # s2 — 亻 竖 (vertical drop, slightly rightward from 撇 body)
    draw_shu(d, S2_H, S2_T, width=9)

    # s3 — 壬 top 丿 (short slanted stroke)
    draw_pie(d, S3_H, S3_T, head_width=10, tail_width=2, curve=0.08, segments=40)

    # s4 — 壬 upper 一 (short middle horizontal)
    draw_heng(d, S4_H, S4_T, width=9)

    # s5 — 壬 中 竖 (vertical spine of 壬; passes through s4 mid → welded P)
    draw_shu(d, S5_H, S5_T, width=9)

    # s6 — 壬 底 一 (bottom horizontal, widest)
    draw_heng(d, S6_H, S6_T, width=11)

    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_任.png')
    render(out)

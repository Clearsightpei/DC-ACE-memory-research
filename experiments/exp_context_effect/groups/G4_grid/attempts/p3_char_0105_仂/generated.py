"""p3_char_0105_仂 (lè, "surplus/rest") — 4 strokes: 亻 (2) + 力 (2).

Memory lookup (mandatory checklist):
  1. success_bank/INDEX.md — 亻 → `ren_side.py` (pass); 力 → `li.py`
     (pass, B3 retry). But brief's per-stroke MMH anchors for THIS
     composition differ (亻 compressed to far-left, 力 shifted right).
     Per TR1: OVERRIDE the primitive anchors — do NOT call defaults.
  2. errata.md — 仂 not present; 力 char had one FAIL (p3_char_0025) then
     PASS via li_char.py. Not directly applicable — this is 仂 not 力.
  3. form_catalog — 亻 as left-radical: 撇 upper-right→lower-left, 竖
     starts at 撇 body (T-touch); standard左右 composition.
  4. principles_meta — TR1 override anchors; TR10 keep N joints under
     ~25 px unless family-exception (仂 not a 几-family).
  5. joint_atlas — s2.tail ⇆ s4.tail: N (gap ~33 px acceptable per
     brief); s1.mid ⇆ s2.head: N (~17 px gap); s3.mid ⇆ s4.mid: P
     (welded weld).

Strokes (brief anchors):
  s1 撇 : head=('TL',0.92,0.668) tail=('BL',0.164,0.03)   [亻 upper]
  s2 竖 : head=('ML',0.738,0.512) tail=('BL',0.738,0.997) [亻 lower]
  s3 横折钩: head=('C',0.134,0.629) tail=('BC',0.723,0.704) [力 top+right side]
             — corner and tip derived (not in MMH endpoints alone)
  s4 撇 : head=('TC',0.673,0.668) tail=('BL',0.976,0.938) [力 pierces s3]

Joints:
  s1.mid ⇆ s2.head @ ML : N (~17 px gap) — 竖 head sits just below
                          the 撇 body chord.
  s2.tail ⇆ s4.tail @ BL: N (~33 px gap) — natural 亻/力 spacing.
  s3.mid(0.20) ⇆ s4.mid(0.38) @ C : P (welded) — 撇 pierces the
                                    descending part of 横折钩.
"""

SELF_CHECK = {
    'visual_ok': True,           # revision-1 flattened 力 top bar
    'stroke_count_ok': True,     # 4 primitive calls below
    'endpoint_mismatches': [],   # all anchors match brief within tolerance
    'joint_class_mismatches': [], # P at C weld, N at BL gap, N at ML gap
    'overall_pass': True,
    'notes': 'rev1: flattened 力 top bar (corner y_frac 0.60 in MR) and lifted hook tip',
}

import sys, os
from PIL import Image, ImageDraw

# Load shared primitives from G4 success_bank
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie          # noqa: E402
from shu import draw_shu          # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 撇 (亻 top): head upper-right (TL area), tail lower-left toward BL.
    s1_head = ('TL', 0.92, 0.668)
    s1_tail = ('BL', 0.164, 0.03)
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=1, curve=0.10, segments=48)

    # s2 — 竖 (亻 vertical): starts on 撇 body, drops straight to BL.
    # Brief says head at ML(0.738, 0.512), tail at BL(0.738, 0.997) — same
    # x_frac 0.738 across rows → true vertical (TR8 rule 6).
    s2_head = ('ML', 0.738, 0.512)
    s2_tail = ('BL', 0.738, 0.997)
    draw_shu(draw, s2_head, s2_tail, width=9)

    # s3 — 横折钩 (力 top-and-right): 横 from left going right, then bend
    # down and hook up-left at the bottom.
    # Brief endpoints:  head=('C',0.134,0.629)  tail=('BC',0.723,0.704)
    # 横折钩 needs 4 anchors: head, corner (top-right of L), tail (hook
    # start = bottom), tip (hook end, up-left).
    # Derive: corner ≈ top-right just above the descent — near MR(0.15,0.05)
    #         relative to 横 span. Descent goes down to BC tail. Then hook
    #         tip curls up-left to somewhere around BC(0.55, 0.55).
    # Revision 1: keep 横 nearly horizontal — corner y_frac matches
    # head's y in canvas-terms. head pixel y ≈ 100 + 62.9 ≈ 163.
    # corner cell MR row starts at pixel 100 → need y_frac ≈ 0.63.
    s3_head   = ('C',  0.134, 0.629)
    s3_corner = ('MR', 0.28,  0.60)    # top-right bend, ~horizontal 横
    s3_tail   = ('BC', 0.723, 0.704)   # descent bottom (hook start)
    s3_tip    = ('BC', 0.55,  0.45)    # hook end curls up-left
    draw_heng_zhe_gou(draw, s3_head, s3_corner, s3_tail, s3_tip,
                      h_width=9, v_width=9, shoulder=12, tip_w=2)

    # s4 — 撇 (力 diagonal pierce): head upper mid-right, tail lower-right
    # near BL/BR boundary. Passes through the 力's descending stroke (P).
    s4_head = ('TC', 0.673, 0.668)
    s4_tail = ('BL', 0.976, 0.938)
    draw_pie(draw, s4_head, s4_tail,
             head_width=10, tail_width=1, curve=0.08, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_仂.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

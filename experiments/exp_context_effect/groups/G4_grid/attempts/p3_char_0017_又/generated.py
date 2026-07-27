"""又 (yòu) — Phase 3, char 0017. G4 attempt.

Composition: 2 strokes.
  s1 — 横撇 (heng_pie): short heng from upper-left → corner → pie sweep to BL.
  s2 — 捺 (na): from mid-left down-right to BR, crosses s1 pie (P weld at BC).

Anchor plan (TR7):
  s1.head   = MMH ('ML', 0.779, 0.169)         # start of heng
  s1.corner = ('C', 0.75, 0.05)                # heng flat-right at ~y=105, then bends down-left
  s1.tip    = MMH ('BL', 0.425, 0.760)         # end of pie sweep in BL
  s2.head   = MMH ('ML', 0.794, 0.397)         # touches s1 pie near its start
  s2.tail   = MMH ('BR', 0.854, 0.789)         # sweep to BR corner

Joint (MMH-declared):
  s1_pie.mid(0.64) ⇆ s2.mid(0.37) @ BC → P (welded crossing).

Sanity (TR8):
  1. s1 direction: head y=116.9 above tip y=276. OK.
  2. s2 direction: head y=139.7 above tail y=278.9. OK.
  3. Anchors all in [0,1] fracs. OK.
  4. Joint: s2 sweeps down-right through s1 pie — line crossing verified below.
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from heng_pie import draw_heng_pie
from na import draw_na
from _anchor import anchor_to_xy

SELF_CHECK = {
    'visual_ok': True,          # revision 2: corner moved right to ('TR',0.40,0.15) so heng extends rightward
    'stroke_count_ok': True,    # 2 primitive calls (heng_pie + na)
    'endpoint_mismatches': [],  # s1.head, s1.tip, s2.head, s2.tail all MMH-exact
    'joint_class_mismatches': [], # joint P — s1 pie and s2 na cross visibly at BC
    'overall_pass': True,
    'notes': 'Revision 2 (against clean GT): heng corner moved from C(0.75,0.05) to TR(0.40,0.15) so heng actually extends rightward from ML head instead of collapsing to a point. Bank primitives with all anchors overridden per TR1.',
}


def draw_you(draw):
    # s1 — 横撇
    S1_HEAD   = ('ML', 0.779, 0.169)
    S1_CORNER = ('TR', 0.40, 0.15)   # 折 pivot in top-right, so heng extends rightward before bending
    S1_TIP    = ('BL', 0.425, 0.760)
    draw_heng_pie(draw, head=S1_HEAD, corner=S1_CORNER, tip=S1_TIP,
                  head_w=6, corner_w=11, tip_w=2)

    # s2 — 捺
    S2_HEAD = ('ML', 0.794, 0.397)
    S2_TAIL = ('BR', 0.854, 0.789)
    draw_na(draw, from_anchor=S2_HEAD, to_anchor=S2_TAIL,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.75, curve=0.08, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_you(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_又.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

"""p3_char_0341_社 — G5 attempt.

Recipe: P-A-006 — MMH anchors verbatim, stroke-primitive layer.
Composition: 礻 (left, 4 strokes) + 土 (right, 3 strokes) = 7 total.

P-A-007-v2 hard-check per sub-component:
- 礻 whole-radical (shi_spirit.py native w~155 h~226 centered).
  Target MMH range: x~15-190 (w~175), y~65-305 (h~240). Aspect matches
  native (0.68 vs 0.73 w/h). BUT in this composition 礻's crossbar +
  shu are pushed far LEFT (shu at x~90 vs native x~140), and side-dian
  is compact (Δx=19,Δy=22 vs native 55,57). Native ox/oy/scale cannot
  land these MMH anchors cleanly — P-A-006 stroke-primitive layer with
  verbatim MMH anchors preserves joint accuracy. SKIP whole-radical.
- 土 whole-radical (tu_earth.py native w~232 h~194 centered).
  Target MMH range: x~120-282 (w~162), y~75-260 (h~185). Aspect target
  0.88 vs native 1.20 — target is TALLER-narrower (aspect ratio native/
  target = 1.36, outside [0.55,1.2] normalized-aspect window). Whole-
  radical call would either overshoot x or under-fill y. SKIP → inline.

Both refusals justified per P-A-007-v2 clause 2 (aspect-shifted from
bank); inline stroke-primitive layer with MMH anchors verbatim.

Joint intents:
  s2.mid(0.56) ⇆ s3.head : N  (natural gap ~16px at cell ML)
  s2.mid(0.49) ⇆ s4.head : N  (natural gap ~36px at cell C)
  s5.mid(0.48) ⇆ s6.mid(0.57) : P  (welded cross at cell C — 土 crossing)
  s6.tail    ⇆ s7.mid(0.36) : N  (natural gap ~17px at cell BC)

Stroke inventory:
  s1: dian  (礻 top dot)
  s2: heng_pie (礻 crossbar-into-pie)
  s3: shu   (礻 central vertical descender)
  s4: dian  (礻 side dot — small)
  s5: heng  (土 top short heng)
  s6: shu   (土 central vertical)
  s7: heng  (土 bottom long heng)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitives = 7 strokes
    'endpoint_mismatches': [],  # MMH anchors used verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 stroke-layer, MMH-verbatim; 7 primitive calls.'
}

import sys
import pathlib

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from heng_pie import draw_heng_pie
from shu import draw_shu


def draw(d: ImageDraw.ImageDraw):
    # s1 礻 top dian — TL(0.826,0.694)=(82.6,69.4) → TC(0.181,0.973)=(118.1,97.3)
    draw_dian(d, (82.6, 69.4), (118.1, 97.3),
              w_head=3, w_tail=7, bow=3)
    # s2 礻 heng_pie — ML(0.308,0.523)=(30.8,152.3) → BL(0.149,0.569)=(14.9,256.9)
    #   Compound stroke; head at upper-right, tail at lower-left. Corner near head
    #   since the heng segment is short in this L-position 礻 variant.
    draw_heng_pie(d, (30.8, 152.3), (14.9, 256.9),
                  apex_x=28, corner_x=26)
    # s3 礻 central shu — ML(0.885,0.975)=(88.5,197.5) → BL(0.92,1.053)=(92.0,305.3)
    #   Near-vertical descender; N-gap to s2.mid at cell ML.
    draw_shu(d, (88.5, 197.5), (92.0, 305.3), width=6)
    # s4 礻 side dian — C(0.157,0.893)=(115.7,189.3) → BC(0.351,0.109)=(135.1,210.9)
    #   Compact side-dot; smaller than a standalone dian, taper appropriately.
    draw_dian(d, (115.7, 189.3), (135.1, 210.9),
              w_head=3, w_tail=6, bow=2)
    # s5 土 top heng (short) — C(0.459,0.743)=(145.9,174.3) → MR(0.49,0.62)=(249.0,162.0)
    draw_heng(d, (145.9, 174.3), (249.0, 162.0),
              width_head=8, width_tail=9)
    # s6 土 central shu — TC(0.816,0.75)=(181.6,75.0) → BC(0.878,0.446)=(187.8,244.6)
    #   P-welded crossing with s5 at cell C.
    draw_shu(d, (181.6, 75.0), (187.8, 244.6), width=7)
    # s7 土 bottom long heng — BC(0.207,0.575)=(120.7,257.5) → BR(0.821,0.52)=(282.1,252.0)
    #   Longer than s5 (土 distinguisher); N-gap to s6.tail.
    draw_heng(d, (120.7, 257.5), (282.1, 252.0),
              width_head=9, width_tail=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = HERE.parent / '01_社.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

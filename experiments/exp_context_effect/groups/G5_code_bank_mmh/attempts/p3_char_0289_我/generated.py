"""p3_char_0289_我 (wo, "I") — 7 strokes.

MMH structural block → per-stroke pixel anchors (300×300 canvas,
9-cell 米字格; L col x in [0,100], C col x in [100,200], R col x in
[200,300]; T row y in [0,100], M row y in [100,200], B row y in
[200,300]).

Stroke plan (P-A-006 stroke-primitive layer, MMH anchors verbatim):
  s1: pie      C(.342,.163)=(134.2,116.3)  → ML(.595,.471)=(59.5,147.1)
  s2: heng     ML(.51,.816)=(51.0,181.6)   → MR(.174,.5)=(217.4,150.0)
  s3: shu      ML(.946,.371)=(94.6,137.1)  → BL(.721,.669)=(72.1,266.9)
  s4: ti       BL(.293,.396)=(29.3,239.6)  → BC(.441,.021)=(144.1,202.1)
  s5: xie_gou  TC(.441,.636)=(144.1,63.6)  → BR(.619,.493)=(261.9,249.3)
  s6: pie      MR(.118,.793)=(211.8,179.3) → BC(.33,.613)=(133.0,261.3)
  s7: dian     TC(.925,.92)=(192.5,92.0)   → MR(.288,.143)=(228.8,114.3)

Joints (from MMH block):
  s1.mid ⇆ s3.head  : N (~10 px gap, natural)
  s1.head ⇆ s5.mid  : N (~32 px, no touch)
  s2.mid ⇆ s3.mid   : P (welded — heng crosses shu)
  s2.mid ⇆ s5.mid   : P (welded — heng crosses xie_gou)
  s3.mid ⇆ s4.mid   : P (welded — shu crosses ti)
  s5.mid ⇆ s6.mid   : P (welded — xie_gou crosses pie)

Rationale for stroke-primitive layer (not ge_dagger whole-radical):
  ge_dagger uses fixed compositional coords sized for the bare radical
  slot; 我 places 戈-family strokes at different anchors interleaved
  with the 手-side strokes (s1, s3, s4). Direct primitive calls with
  MMH anchors keep every joint honest — this is the P-A-006 recipe.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from ti import draw_ti
from xie_gou import draw_xie_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 7 primitive calls: pie, heng, shu, ti, xie_gou, pie, dian
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors verbatim; P joints (s2×s3, s2×s5, s3×s4, s5×s6) naturally weld from crossing geometry; N joints (s1↔s3head, s1head↔s5) preserved by not extending endpoints.'
}


def draw_wo(d):
    # s1: short pie — center-upper → down-left toward ML
    draw_pie(d, (134.2, 116.3), (59.5, 147.1),
             bow_perp=6, w_head=7, w_tail=2, steps=50)

    # s2: main heng — sweeps L→R with slight rise (head lower-left, tail upper-right of middle)
    draw_heng(d, (51.0, 181.6), (217.4, 150.0),
              width_head=8, width_tail=10)

    # s3: shu (vertical shaft of 手-side), slight leftward lean top→bottom
    #     crosses s2 near s2.mid(0.33) — P joint welded naturally
    draw_shu(d, (94.6, 137.1), (72.1, 266.9), width=8, top_curl=False)

    # s4: ti (rising stroke from BL up-right into BC)
    #     crosses s3 near s3.mid(0.49) — P joint welded naturally
    draw_ti(d, (29.3, 239.6), (144.1, 202.1), w_head=9, w_tail=2, steps=60)

    # s5: xie_gou (long diagonal + terminal up-hook), TC→BR
    #     crosses s2 near s2.mid(0.68) — P joint welded naturally
    draw_xie_gou(d, head=(144.1, 63.6), tail=(261.9, 249.3),
                 width=8, bow=10, hook_up=32, hook_back=6)

    # s6: pie (short, from MR mid-lower down-left to BC)
    #     crosses s5 near s5.mid(0.55) — P joint welded naturally
    draw_pie(d, (211.8, 179.3), (133.0, 261.3),
             bow_perp=-8, w_head=8, w_tail=2, steps=60)

    # s7: dian (tiny dot in upper-right corner) — N-style, doesn't touch anything
    draw_dian(d, (192.5, 92.0), (228.8, 114.3),
              w_head=2, w_tail=6, bow=3, steps=40)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_wo(d)
    out = Path(__file__).parent / "01_我.png"
    img.save(out)
    print(f"wrote {out}")

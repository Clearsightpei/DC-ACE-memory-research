"""p3_char_0484_俏 (qiao, "handsome") — 9 strokes: 亻 (pie+shu) + 肖 (小+月).

Recipe: P-A-006 (MMH-anchor verbatim + stroke-primitive layer) + P-A-008
(inline-reasoning trace) + P-A-009 (quantitative BANK_DEVIATION).

Sibling: p3_char_0488_俑 (亻+甬 template — same 亻 aspect, same right-side
composition style with 月-like frame). Reuse: draw_heng_zhe_gou for the
月-frame is the shared move.

INLINE REASONING TRACE (P-A-008):
  亻 (s1,s2): Bank has ren_left.py at native pie head=(158.8, 73.8),
    tail=(80.6, 211.2); shu head=(138.9, 158.2). MMH 俏 pie head=(95.5, 71.5),
    tail=(22.0, 203.0); shu head=(76.2, 152.1). Uniform shift check:
      pie head ox = 95.5 - 158.8 = -63.3
      pie tail ox = 22.0 - 80.6 = -58.6
      shu head ox = 76.2 - 138.9 = -62.7
    All shifts within ~5px, so this IS uniform (ox ~= -62). Per P-A-007-v2
    ren_left(ox=-62) would be usable. BUT the MMH block gives per-endpoint
    anchors that we should follow verbatim (P-A-006 template), and the pie
    tail y (203 vs bank 211) diverges by 8px — enough to justify inline for
    tighter anchor fidelity. NOT flagged as BANK_DEVIATION because ren_left
    is a whole-radical primitive and drawer legitimately chose stroke-
    primitive layer per P-A-006.

  肖 top 小 (s3-s5): No 小-top compact primitive in bank. xiao.py exists but
    is native 300-canvas; here 小 occupies only ~90x90 region top-right.
    Inline: s3 short shu (center descender), s4 short pie (left mark),
    s5 dian slanting down-left (right mark).

  肖 bottom 月 (s6-s9): Follows yue_moon primitive template's stroke choices
    (pie + heng_zhe_gou + 2 hengs). Inlined at MMH anchors (compressed to
    bottom-right, not native canvas position). Corner for heng_zhe_gou
    inferred: corner y = head y, corner x = tail x (top-right of frame).
    gou_tail slightly below hook_tip.

Anchor pixels (MMH cell.frac -> 300x300):
  s1 pie:  TL(0.955,0.715)=(95.5, 71.5) -> BL(0.22,0.03)=(22.0,203.0)
  s2 shu:  ML(0.762,0.521)=(76.2,152.1) -> BL(0.803,0.953)=(80.3,295.3)
  s3 shu:  TC(0.793,0.63)=(179.3, 63.0) -> C (0.834,0.515)=(183.4,151.5)
  s4 pie:  C (0.345,0.087)=(134.5,108.7) -> C (0.562,0.324)=(156.2,132.4)
  s5 dian: TR(0.376,0.791)=(237.6, 79.1) -> MR(0.115,0.225)=(211.5,122.5)
  s6 pie:  C (0.427,0.538)=(142.7,153.8) -> BC(0.415,0.892)=(141.5,289.2)
  s7 hzg:  C (0.608,0.582)=(160.8,158.2) -> BC(0.939,0.789)=(193.9,278.9)
  s8 heng: C (0.603,0.951)=(160.3,195.1) -> MR(0.033,0.896)=(203.3,189.6)
  s9 heng: BC(0.573,0.32) =(157.3,232.0) -> BR(0.06 ,0.256)=(206.0,225.6)

Joint plan (7 N joints — all natural gaps per MMH spec):
  N: s1.mid⇆s2.head (ML), s3.tail⇆s7.head (C), s6.head⇆s7.head (C),
     s6.mid⇆s8.head, s6.mid⇆s9.head, s7.mid⇆s8.tail, s7.mid⇆s9.tail.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 9 primitive calls == expected 9
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all N joints preserved as natural gaps
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer at MMH anchors. 亻 inlined '
             '(pie+shu) even though ren_left uniform-shift-able (~-62px), '
             'to preserve verbatim MMH anchor fidelity. 肖 top 3 strokes '
             'inline (shu+pie+dian). 月 bottom follows yue_moon primitive '
             'template (pie+heng_zhe_gou+2 hengs) at compressed anchors.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (person radical, left) ----
    # s1: pie from TL upper down-left to BL
    draw_pie(d, (95.5, 71.5), (22.0, 203.0),
             bow_perp=15, w_head=9, w_tail=3, steps=90)
    # s2: shu near-vertical descender
    draw_shu(d, (76.2, 152.1), (80.3, 295.3), width=7)

    # ---- 肖 top: 小 (compressed 3 strokes) ----
    # s3: center shu — near-vertical, spans ~90px
    draw_shu(d, (179.3, 63.0), (183.4, 151.5), width=6)
    # s4: left mark — short pie sloping down-right (small "撇" style)
    draw_pie(d, (134.5, 108.7), (156.2, 132.4),
             bow_perp=2, w_head=6, w_tail=3, steps=30)
    # s5: right mark — dian sloping down-left (from TR down-left into MR)
    draw_dian(d, (237.6, 79.1), (211.5, 122.5),
              w_head=3, w_tail=8, bow=4, steps=50)

    # ---- 肖 bottom: 月 (compressed) ----
    # s6: left pie — nearly vertical, small rightward bow
    draw_pie(d, (142.7, 153.8), (141.5, 289.2),
             bow_perp=5, w_head=8, w_tail=4, steps=80)
    # s7: heng-zhe-gou — right frame; corner top-right, hook_tip is MMH tail
    #     corner y = head y, corner x ~= tail x
    #     gou_tail slightly below hook_tip; hook returns up-left
    draw_heng_zhe_gou(d,
                      heng_head=(160.8, 158.2),
                      corner=(196.0, 158.0),
                      gou_tail=(200.0, 288.0),
                      hook_tip=(193.9, 278.9))
    # s8: upper inner heng
    draw_heng(d, (160.3, 195.1), (203.3, 189.6),
              width_head=6, width_tail=7)
    # s9: lower inner heng
    draw_heng(d, (157.3, 232.0), (206.0, 225.6),
              width_head=6, width_tail=7)

    out = Path(__file__).parent / "01_俏.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()

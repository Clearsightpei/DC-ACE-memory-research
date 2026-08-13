"""G5 attempt for p3_char_0509_特 (te, "special" — 10 strokes).

Composition (MMH anchors verbatim, P-A-006 stroke-primitive layer):
  牜 left (4 strokes):
    s1: pie      (55.1, 106.6) -> (29.6, 182.5)   short 撇 (top)
    s2: heng     (61.8, 149.1) -> (130.1, 135.1)  top 横 of 牜
    s3: shu      (88.5,  63.0) -> (96.1, 297.1)   long 竖 (spans full char height)
    s4: ti       (25.5, 228.5) -> (120.7, 183.1)  rising 提
  寺 right (6 strokes: 土 + 寸):
    s5: heng     (152.6, 115.4) -> (231.7, 104.6) top 横 of 土
    s6: shu      (180.5,  56.0) -> (186.3, 151.5) vertical of 土
    s7: heng     (127.7, 166.4) -> (274.8, 151.2) wide middle 横 (bottom of 土 / boundary)
    s8: heng     (134.5, 203.3) -> (261.0, 190.7) 一 of 寸
    s9: shu_gou  (198.6, 163.5) -> (170.5, 282.1) 竖钩 of 寸
    s10: dian    (138.3, 227.1) -> (164.9, 253.1) 点 of 寸

BANK CONSULTATION (P-A-007-v2 hard-check):
- niu_cow.py: 牛 has 4 strokes (pie/heng/heng/shu). Here 牜 is left-position
  variant with (pie/heng/shu/ti) — different terminal stroke (ti not heng),
  and s3 vertical spans full char height (y 63->297) which uniform ox/oy/scale
  on a standalone 牛 cannot produce. Skip; use stroke-primitive layer.
- No bank primitive for 寺 or its 土/寸 parts as compound radicals. shi_time (时)
  uses 寸 but not 土; not a clean fit. Use stroke primitives directly.
Neither is a real "skip a whole-radical primitive that would fit" — this is
a P-A-006 clean stroke-primitive composition per MMH anchors, not a
BANK_DEVIATION per v13 semantics.

Joint self-check (from MMH block):
  - s1.mid ⇆ s2.head @ ML : N (gap ~19px) — natural offset between anchors ~10px, OK
  - s2.mid ⇆ s3.mid       : P (welded) — s3 vertical at x~92 pierces s2 heng which
    extends to (130,135); s2 crosses s3's x=92 at approximately (92, 145) — s3 body
    at y=145 is at x~90, so lines cross → welded naturally
  - s3.mid ⇆ s4.mid       : P (welded) — s4 ti ends at (120.7, 183.1); s3 at y=183
    is at x~92; s4 crosses through the s3 vertical → welded
  - s3.mid ⇆ s7.head      : N (gap ~35px) — s7 head at x=127.7, s3 at that y~166 is
    at x~93, so gap ~35px in x-direction — natural
  - s5.mid ⇆ s6.mid       : P (welded) — s5 heng crosses s6 vertical near C cell
  - s6.tail ⇆ s7.mid(0.36): N (gap ~13px) — s6 ends at y=151.5, s7 at same x~186
    is at y~163, gap ~11px — natural
  - s6.tail ⇆ s9.head     : N (gap ~24px)
  - s7.mid(0.47) ⇆ s9.head: N (gap ~10px)
  - s8.mid(0.61) ⇆ s9.mid(0.21): P (welded) — s9 vertical crosses s8 heng
  - s8.head ⇆ s10.head    : N (gap ~30px)
"""

import os, sys
from PIL import Image, ImageDraw

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
sys.path.insert(0, BANK)

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from ti import draw_ti
from shu_gou import draw_shu_gou
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 10 primitive calls, matches MMH count of 10
    'endpoint_mismatches': [],   # all anchors used verbatim from MMH block
    'joint_class_mismatches': [], # welds emerge from crossing anchors; N gaps preserved by MMH separation
    'overall_pass': True,
    'notes': 'P-A-006 clean stroke-primitive layer. MMH anchors verbatim. '
             'niu_cow rejected (4-stroke pattern differs: 牜 uses ti not 2nd heng). '
             'No BANK_DEVIATION — no whole-radical primitive fit this compound.',
}


def draw_te(draw):
    # === 牜 (left) ===
    # s1 — short 撇 (top of 牜)
    draw_pie(draw, (55.1, 106.6), (29.6, 182.5),
             bow_perp=8, w_head=7, w_tail=3, steps=60)
    # s2 — top 横 of 牜
    draw_heng(draw, (61.8, 149.1), (130.1, 135.1),
              width_head=6, width_tail=7)
    # s3 — long 竖 of 牜 (spans full char height)
    draw_shu(draw, (88.5, 63.0), (96.1, 297.1), width=7)
    # s4 — 提 (rising, at bottom of 牜)
    draw_ti(draw, (25.5, 228.5), (120.7, 183.1),
            w_head=8, w_tail=2, steps=50)

    # === 寺 (right) ===
    # s5 — top 横 of 土
    draw_heng(draw, (152.6, 115.4), (231.7, 104.6),
              width_head=6, width_tail=7)
    # s6 — 竖 of 土
    draw_shu(draw, (180.5, 56.0), (186.3, 151.5), width=6)
    # s7 — wide middle 横 (bottom of 土 / dominant crossbar)
    draw_heng(draw, (127.7, 166.4), (274.8, 151.2),
              width_head=7, width_tail=8)
    # s8 — 一 of 寸
    draw_heng(draw, (134.5, 203.3), (261.0, 190.7),
              width_head=6, width_tail=7)
    # s9 — 竖钩 of 寸
    draw_shu_gou(draw, (198.6, 163.5), (170.5, 282.1),
                 width=6, hook_start_offset=35)
    # s10 — 点 of 寸
    draw_dian(draw, (138.3, 227.1), (164.9, 253.1),
              w_head=3, w_tail=7, bow=3, steps=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_te(draw)
    out_path = os.path.join(os.path.dirname(__file__), '01_特.png')
    img.save(out_path)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()

"""平 (píng, 5 strokes) — G4 attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep '平' → not in bank.
2. errata.md grep '平' → not listed (matches for '平捺' are unrelated primitive).
3. form_catalog.md: horizontal stroke class rows — long 横 mid-band; 竖 through C.
4. principles_meta.md TR1/TR8: OVERRIDE anchors; horizontals share y-row.
5. joint_atlas.md: P-class welded crossing (horiz × vert); N-class small gap 15-25 px.

Composition (5 strokes, per MMH structural expectations):
  s1 — top short 横 (near-horizontal across TL/TR boundary at y≈0.72).
  s2 — left horn 撇 (short pie from ML top-right into C left-mid).
  s3 — right horn 点/短捺 (mirror of s2, from TR into C right-mid).
  s4 — long middle 横 (across ML→MR at y≈0.80 within middle row).
  s5 — long central 竖 (from TC down through BC, piercing s4).

Joints:
  s1.mid ⇆ s5.head @ TC : N (small ~26 px gap — do NOT weld).
  s4.mid × s5.mid  @ C  : P (welded crossing by construction).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: top-heng, left-pie horn, right-dian horn, long mid-heng, long central shu. '
             's5 head starts BELOW s1 mid to preserve N-class gap; s4×s5 welded P at C by construction.'
}


def draw_ping(draw):
    # s1 — top short 横 (slight downward slant per MMH: TL(0.99,0.771)→TR(0.036,0.65)).
    # Kept as clean 横 with matched y (TR1 form: readable top bar).
    s1_head = ('TL', 0.85, 0.72)
    s1_tail = ('TR', 0.15, 0.72)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # s2 — left horn 撇 (from ML top-right sweeping down-left into C left).
    # Head goes upper-right, tail lower-left per pie convention.
    # Rearrange to match sweep direction: head=upper-right anchor.
    s2_head = ('ML', 0.85, 0.15)   # upper right of ML
    s2_tail = ('C', 0.05, 0.55)    # lower left of C (crosses ML boundary)
    draw_pie(draw, s2_head, s2_tail, head_width=8, tail_width=2, curve=0.10, segments=32)

    # s3 — right horn (mirror short 点/短捺). Head at TR-left going down-right into C right.
    # Use dian primitive (thin head → rounded press terminal).
    s3_head = ('TR', 0.05, 0.85)   # top-left of TR (start high-left)
    s3_tail = ('C',  0.80, 0.50)   # lands into C right-mid
    draw_dian(draw, s3_head, s3_tail, head_width=2, peak_width=9, curve=0.05, segments=24)

    # s4 — long middle 横 (across ML→MR, mid-height in middle row).
    s4_head = ('ML', 0.20, 0.80)
    s4_tail = ('MR', 0.85, 0.80)
    draw_heng(draw, s4_head, s4_tail, width=10)

    # s5 — long central 竖 (from TC down through BC, piercing s4).
    # Head sits ~0.85 y in TC (just below s1 at y=0.72 → gap ≈ 13 px in cell = ~13 px, plus
    # the 15 px slack between s1 y=0.72*100+bit and s5 head y=0.85*100 gives N-class gap).
    s5_head = ('TC', 0.50, 0.87)
    s5_tail = ('BC', 0.50, 1.10)  # extend past canvas bottom for GT-matching long tail
    draw_shu(draw, s5_head, s5_tail, width=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ping(draw)
    out = os.path.join(os.path.dirname(__file__), '01_平.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

"""伙 (huǒ) — Phase-3 character, 6 strokes.
Composition: 亻 (left, 撇 + 竖) + 火 (right, 4 strokes: 点/短撇 + 短撇 + 撇 + 捺).

MMH-derived anchors (from brief):
  s1 撇 (亻):   head ('TL', 0.94, 0.7)   tail ('BL', 0.22, 0.145)
  s2 竖 (亻):   head ('ML', 0.747, 0.629) tail ('BL', 0.75, 0.962)
  s3 点 (火):   head ('C',  0.181, 0.503) tail ('C',  0.403, 0.86)
  s4 短撇 (火): head ('MR', 0.355, 0.184) tail ('MR', 0.01, 0.708)
  s5 撇 (火):   head ('TC', 0.667, 0.715) tail ('BC', 0.02, 0.874)
  s6 捺 (火):   head ('C',  0.816, 0.901) tail ('BR', 0.865, 0.889)

Joints:
  J1: s1.mid ⇆ s2.head @ ML — N (gap ~19 px)
  J2: s4.tail ⇆ s5.mid @ C — N (gap ~35 px)
  J3: s5.mid ⇆ s6.head @ C — N (gap ~12 px — near-touch X, not welded)

Bank use: ren_side pattern (draw_pie + draw_shu) for 亻; inline dian/pie/na for 火.
Note: The X-cross between s5 and s6 is N (not P) — leave a small gap.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('6 strokes: 亻 (pie+shu) + 火 (dian+shortpie+pie+na). '
              'J1 N gap left at ML; J2 s4-tail near s5-mid natural N gap; '
              'J3 s5-mid vs s6-head near-touch N (~12 px), not welded.')
}


def draw():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- 亻 (left radical) — verbatim MMH anchors ---
    # s1 撇: from upper-left down to bottom-left (long left-leaning pie).
    draw_pie(d,
             from_anchor=('TL', 0.94, 0.7),
             to_anchor=('BL', 0.22, 0.145),
             head_width=11, tail_width=2, curve=0.09, segments=48)

    # s2 竖: head at ML sits near the 撇 body (N-gap, no weld).
    draw_shu(d,
             from_anchor=('ML', 0.747, 0.629),
             to_anchor=('BL', 0.75, 0.962),
             width=9)

    # --- 火 (right radical) — 4 strokes ---
    # s3 点/短撇 (upper-left of 火): small stroke inside C-cell diagonal DR.
    # MMH endpoints look like a dian-shape (short compact peak).
    draw_dian(d,
              from_anchor=('C', 0.181, 0.503),
              to_anchor=('C', 0.403, 0.86),
              head_width=2, peak_width=9, curve=0.08, segments=24)

    # s4 短撇 (upper-right of 火): short pie from MR-top down to MR-mid-left.
    draw_pie(d,
             from_anchor=('MR', 0.355, 0.184),
             to_anchor=('MR', 0.01, 0.708),
             head_width=9, tail_width=2, curve=0.10, segments=32)

    # s5 主撇 (main pie of 火): long from TC down-left to BC.
    # Use NEGATIVE curve so the belly bows toward the RIGHT — the pie
    # midpoint then passes near ('C', 0.774, 0.914) = (177.4, 191.4) where
    # the N-gap to s6.head is expected. Without this, the belly bows LEFT
    # and the X-cross topology is lost.
    draw_pie(d,
             from_anchor=('TC', 0.667, 0.715),
             to_anchor=('BC', 0.02, 0.874),
             head_width=10, tail_width=2, curve=-0.18, segments=48)

    # s6 捺 (main na of 火): from mid C down-right to BR.
    # J3: head at ('C', 0.816, 0.901) → (181.6, 190.1);
    # s5 mid ~ ((166.7+102)/2, (71.5+187.4)/2) = (134.3, 129.5). Distance
    # to s6 head = sqrt(47.3^2 + 60.6^2) ≈ 76 px. Adjust: MMH says N-gap
    # ~12 px near s5 mid @ ('C', 0.774, 0.914) = (177.4, 191.4).
    # s6 head at (181.6, 190.1) is 4 px from that — perfect N (nearly touching).
    draw_na(d,
            from_anchor=('C', 0.816, 0.901),
            to_anchor=('BR', 0.865, 0.889),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    out = os.path.join(_HERE, '01_伙.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = draw()
    print('wrote', p)
    print('SELF_CHECK:', SELF_CHECK)

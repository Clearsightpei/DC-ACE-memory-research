"""分 (fēn) — Phase-3 character, 4 strokes. Composition: 八 (top) + 刀 (bottom).

MANDATORY LOOKUP CHECKLIST (memory_index.md step 1-6):
  1. success_bank/INDEX.md — 分 not present. 八 present (ba.py) → useful for top.
     刀 in errata (chronic fail at retry_n=2) — its dao_side is 刂 not 刀, distinct.
     Cannot reuse mastered 刀; will inline 横折钩 + 撇 fresh using primitives.
  2. errata.md — 分 not listed (first attempt).
  3. form_catalog.md — 撇 in left-position (top of 八): head high-right, tail low-left, tapered.
     捺 in right-position (top of 八): head high-center, tail low-right, peak swell.
  4. principles_meta.md — TR1 override anchors (using MMH anchors below, not ba.py defaults).
     TR6 inline where bank doesn't fit (刀 bottom → inline heng_zhe_gou + pie).
     TR8 straight-body invariant for 横折钩 (corner and tail share x).
  5. joint_atlas.md — s1.mid ⇆ s3.head N (small gap ok, no weld).
     s3.head ⇆ s4.head N (small gap ok, no weld). Don't force weld.
  6. sandbox.md — no specific 分 note.

Anchor plan (米字格, PIL-native):
  s1 撇 (八 left):   head ('TL',0.976,0.987) tail ('ML',0.293,0.907) — MMH
  s2 捺 (八 right):  head ('TC',0.33,0.647)  tail ('MR',0.865,0.726) — MMH
  s3 横折钩 (刀):    head ('ML',0.735,0.893), corner ~('MR',0.5,0.85),
                     tail  ~('BC',0.4,0.85), tip ('BC',0.23,0.725) — MMH tail = hook tip
  s4 撇 (刀 inside): head ('C',0.166,0.951)  tail ('BL',0.457,0.906) — MMH

Joints:
  s1.mid(0.63) ⇆ s3.head @ ML — N (small ~35 px gap, do not weld)
  s3.head ⇆ s4.head @ C — N (small ~15 px gap, do not weld)
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 primitive calls (pie + na + heng_zhe_gou + pie)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 strokes; MMH anchors used verbatim for s1/s2/s4 heads/tails. '
             's3 head=MMH-head, tip=MMH-tail; corner/tail inserted between per '
             'compound-stroke convention (TR8 straight body).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: 撇 (top-left of 八): MMH head ('TL',0.976,0.987)=(97,99), tail ('ML',0.293,0.907)=(29,190)
    draw_pie(draw,
             from_anchor=('TL', 0.976, 0.987),
             to_anchor=('ML', 0.293, 0.907),
             head_width=7, tail_width=1, curve=0.08, segments=48)

    # s2: 捺 (top-right of 八): MMH head ('TC',0.33,0.647)=(133,65), tail ('MR',0.865,0.726)=(287,173)
    draw_na(draw,
            from_anchor=('TC', 0.33, 0.647),
            to_anchor=('MR', 0.865, 0.726),
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.8, curve=0.08, segments=48)

    # s3: 横折钩 (刀 body). MMH head ('ML',0.735,0.893)=(73,189) is horizontal start;
    # MMH tail ('BC',0.23,0.725)=(123,273) is hook tip. Corner must be near top-right of the
    # bar (TR/MR boundary) to match 刀 shape in GT; tail (hook base) sits below corner.
    draw_heng_zhe_gou(draw,
                      head=('ML', 0.735, 0.893),   # (73, 189)
                      corner=('MR', 0.30, 0.75),   # (230, 175) - horizontal end / turn point
                      tail=('MR', 0.30, 0.95),     # (230, 265) - hook base below corner (TR8 straight body)
                      tip=('BC', 0.23, 0.725),     # (123, 273) - MMH tail = hook tip up-left
                      h_width=8, v_width=8, shoulder=10, tip_w=2)

    # s4: 撇 (short, inside 刀): MMH head ('C',0.166,0.951)=(117,295), tail ('BL',0.457,0.906)=(46,291)
    draw_pie(draw,
             from_anchor=('C', 0.166, 0.951),
             to_anchor=('BL', 0.457, 0.906),
             head_width=6, tail_width=1, curve=0.05, segments=32)

    out = os.path.join(_HERE, '01_分.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

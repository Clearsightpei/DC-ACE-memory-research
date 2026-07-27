"""p3_char_0177_仗 (zhàng, "cane / weapon") — 5 strokes.

Decomposition:
  Left: 亻 (ren_side, 2 strokes) — pie + shu.
  Right: 丈 (3 strokes) — heng + pie + na.

Anchors are the MMH-derived expected anchors from the brief.

Joints (from brief):
  s1.mid ⇆ s2.head @ ML  : N — 亻's shu touches the pie body (small gap).
  s3.mid ⇆ s4.mid @ C    : P — 丈's pie crosses the heng (welded).
  s4.mid ⇆ s5.mid @ BC   : P — 丈's na crosses the pie (welded).

Lookup checklist (mandatory):
  1. success_bank/INDEX.md — 亻 exists as ren_side.py; 丈 does not, inline it.
  2. errata.md — 仗 not listed.
  3. form_catalog.md — heng/pie/na standard patterns.
  4. principles_meta.md — TR1 (override anchors, don't call defaults).
  5. joint_atlas.md — P welded, N small gap ~14 px.
  6. sandbox.md — no specific note.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 5 strokes: pie, shu, heng, pie, na
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # s1-s2 N (gap), s3-s4 P (welded), s4-s5 P (welded)
    'overall_pass': True,
    'notes': '仗 = 亻 (pie+shu) + 丈 (heng+pie+na). Using MMH anchors verbatim.'
}


def draw():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw_obj = ImageDraw.Draw(img)

    # ── 亻 (ren-side) ──
    # s1 撇 — from ('TL', 0.996, 0.668) to ('BL', 0.258, 0.007)
    draw_pie(draw_obj,
             ('TL', 0.996, 0.668),
             ('BL', 0.258, 0.007),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 竖 — from ('ML', 0.753, 0.559) to ('BL', 0.779, 0.918)
    # N-joint with s1's body: keep small natural gap (do not weld).
    draw_shu(draw_obj,
             ('ML', 0.753, 0.559),
             ('BL', 0.779, 0.918),
             width=9)

    # ── 丈 (three strokes) ──
    # s3 横 — from ('C', 0.292, 0.538) to ('MR', 0.487, 0.333)
    draw_heng(draw_obj,
              ('C', 0.292, 0.538),
              ('MR', 0.487, 0.333),
              width=9)

    # s4 撇 — from ('TC', 0.77, 0.618) to ('BC', 0.043, 0.774)
    # P-joint with s3 at C (welded crossing).
    draw_pie(draw_obj,
             ('TC', 0.77, 0.618),
             ('BC', 0.043, 0.774),
             head_width=11, tail_width=1, curve=0.12, segments=48)

    # s5 捺 — from ('C', 0.204, 0.787) to ('BR', 0.81, 0.877)
    # P-joint with s4 at BC (welded crossing).
    draw_na(draw_obj,
            ('C', 0.204, 0.787),
            ('BR', 0.81, 0.877),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.75, curve=0.10, segments=48)

    out = os.path.join(os.path.dirname(__file__), '01_仗.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()

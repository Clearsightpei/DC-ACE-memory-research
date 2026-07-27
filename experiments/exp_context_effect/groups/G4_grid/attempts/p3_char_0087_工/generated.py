"""p3_char_0087_工 — 3-stroke character (top 横 + 竖 + bottom 横).

MANDATORY LOOKUP CHECKLIST (memory_index.md reading order):
1. success_bank/INDEX.md grep 工 -> gong.py (p2_radical_049) EXISTS.
   BUT gong.py hard-codes joints as P (welded). MMH-injected Phase-3
   spec for THIS item declares BOTH joints as N (~17 / ~20 px gap).
   GT PNG confirms visible gaps. Honor MMH spec — override anchors +
   inline the strokes rather than reuse a welded P-joint primitive
   (TR6: extreme transformation = inline fresh).
2. errata.md grep 工 -> not listed.
3. form_catalog.md — 横 / 竖 basic; no special context row for 工.
4. principles_meta.md TR9 (full-grid span for standalone) applied
   implicitly: MMH anchors already span the horizontal band widely.
5. joint_atlas.md — N-class = neighbor, small natural gap, DO NOT
   weld. Draw straight strokes; the endpoint anchors themselves
   already produce the natural gap.
6. sandbox.md — nothing relevant.

Structural spec (from MMH block in brief):
  s1 top-横  : head ('ML',0.867,0.143) tail ('MR',0.253,0.017)
  s2 竖      : head ('C',0.421,0.222)  tail ('BC',0.441,0.355)
  s3 bot-横  : head ('BL',0.311,0.493) tail ('BR',0.777,0.481)
Joints:
  s1.mid ⇆ s2.head @ C  : N (~17 px gap)
  s2.tail ⇆ s3.mid @ BC : N (~20 px gap)
"""

from PIL import Image, ImageDraw
import sys, os

# Make the shared primitives importable.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 stroke primitives called
    'endpoint_mismatches': [],        # all anchors identical to MMH spec
    'joint_class_mismatches': [],     # both joints implemented as N
    'overall_pass': True,
    'notes': ('Inlined strokes with MMH-exact anchors so s1 mid vs s2 head '
              'and s2 tail vs s3 mid keep their natural N gaps (~17/20 px). '
              'Reused shared fat_line primitive; refused welded gong.py.'),
}


def draw_gong_char(draw):
    # Stroke 1 — top 横
    s1_head = ('ML', 0.867, 0.143)
    s1_tail = ('MR', 0.253, 0.017)
    fat_line(draw, anchor_to_xy(s1_head), anchor_to_xy(s1_tail), width=9)

    # Stroke 2 — 竖 (central vertical, NOT welded to s1 or s3)
    s2_head = ('C', 0.421, 0.222)
    s2_tail = ('BC', 0.441, 0.355)
    fat_line(draw, anchor_to_xy(s2_head), anchor_to_xy(s2_tail), width=9)

    # Stroke 3 — bottom 横 (wider than s1)
    s3_head = ('BL', 0.311, 0.493)
    s3_tail = ('BR', 0.777, 0.481)
    fat_line(draw, anchor_to_xy(s3_head), anchor_to_xy(s3_tail), width=9)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_gong_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_工.png')
    img.save(out)


if __name__ == '__main__':
    main()

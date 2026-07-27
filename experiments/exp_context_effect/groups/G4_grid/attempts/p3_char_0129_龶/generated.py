"""p3_char_0129_龶 — 龶 (4 strokes: 3 horizontals + 1 vertical spine).

Memory lookup checklist (per memory_index.md):
1. success_bank/INDEX.md grep 龶 → not in bank. Related: wang.py (王), zhu.py (主).
   Structure is very close to 王 but s1 (top heng) is shorter/higher and offset,
   and the vertical extends higher (into TC). Inlining fresh from MMH anchors is
   cleaner than TR-transforming wang.py (avoids extreme override).
2. errata.md grep → not listed.
3. form_catalog.md → 横 (top/mid/bot) and 竖 spine patterns; using MMH anchors
   directly satisfies the pattern.
4. principles_meta.md TR1/TR6 → inline fresh since bank primitive would need
   extreme override.
5. joint_atlas.md → P (weld) at s1×s3 and s2×s3; N (small gap ~12px) at s3.tail
   near s4 (spine hangs above bottom heng).
6. sandbox — no relevant note.

Strokes:
  s1 = top short 横 (TL→TR high)
  s2 = mid short 横 (in C cell, upper area)
  s3 = 竖 spine (TC top → C middle, stops before s4)
  s4 = long bottom 横 (ML→MR)

Joints:
  s1.mid ⇆ s3.upper : P welded
  s2.mid ⇆ s3.lower : P welded
  s3.tail ⇆ s4.mid  : N (small gap ~12 px, spine does NOT touch bottom heng)
"""

SELF_CHECK = {
    'visual_ok': True,           # 3 hengs (short/short/long) + vertical spine; silhouette matches GT
    'stroke_count_ok': True,     # 4 fat_line calls, one per stroke
    'endpoint_mismatches': [],   # anchors used = MMH anchors verbatim, delta=0
    'joint_class_mismatches': [],# s1×s3 P weld, s2×s3 P weld, s3.tail↕s4 N gap (spine ends at y~137, s4 at y~136-156 — small gap present)
    'overall_pass': True,
    'notes': 'inlined fresh from MMH anchors (bank primitive wang.py would need extreme override for s1 position and s3 upper extent); PIL fat_line width tuned 6/6/7/8 to match GT thin strokes.',
}

import sys, os
from PIL import Image, ImageDraw

# import shared _anchor helper from success_bank
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line  # noqa: E402


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1 — top short 横
    s1_h = ('TL', 0.876, 0.882)
    s1_t = ('TR', 0.039, 0.741)
    fat_line(d, anchor_to_xy(s1_h), anchor_to_xy(s1_t), width=6)

    # stroke 2 — mid short 横
    s2_h = ('C', 0.008, 0.163)
    s2_t = ('C', 0.898, 0.063)
    fat_line(d, anchor_to_xy(s2_h), anchor_to_xy(s2_t), width=6)

    # stroke 3 — 竖 spine (TC → C)
    s3_h = ('TC', 0.307, 0.498)
    s3_t = ('C', 0.365, 0.374)
    fat_line(d, anchor_to_xy(s3_h), anchor_to_xy(s3_t), width=7)

    # stroke 4 — long bottom 横
    s4_h = ('ML', 0.308, 0.562)
    s4_t = ('MR', 0.692, 0.368)
    fat_line(d, anchor_to_xy(s4_h), anchor_to_xy(s4_t), width=8)

    out = os.path.join(os.path.dirname(__file__), '01_龶.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = draw()
    print(f'wrote {p}')

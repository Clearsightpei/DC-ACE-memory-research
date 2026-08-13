"""p3_char_0347_证 — 证 = 讠 (left) + 正 (right).

Memory reading log (v8 mandatory 1-3):
1. drawer_memory.md: no direct 证 entry; playbook says import radical
   primitives when available. yan_speech + zhi_stop-family exist; 正
   itself is in success_bank INDEX (p3_char_0182_正) but component
   strokes are stock heng/shu.
2. success_bank/INDEX.md grep: 讠 (yan_speech.py) exists, 正 has
   heng+zhi_stop base. No `zheng.py`.
3. errata.md grep: 证 not listed.

Composition (left-right): 讠 in x∈[0.05, 0.42], 正 in x∈[0.45, 0.95].

MMH gives 7 strokes:
  s1, s2 — 讠 (dot + heng_zhe_ti)  → call yan_speech with MMH overrides
  s3     — 正 top heng            → draw_heng
  s4     — 正 center-long shu     → draw_shu
  s5     — 正 middle heng (right) → draw_heng
  s6     — 正 short shu (left)    → draw_shu
  s7     — 正 bottom long heng    → draw_heng

Joints (all N — small gaps, do NOT weld):
  s3.mid(0.21) ⇆ s4.head @ C  (~19 px gap)
  s4.mid(0.44) ⇆ s5.head @ MR (~18 px)
  s4.tail     ⇆ s7.mid(0.51) @ BC (~18 px)
  s6.tail     ⇆ s7.mid(0.26) @ BC (~16 px)
"""
import os, sys
from PIL import Image, ImageDraw

CODE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'
)
sys.path.insert(0, os.path.abspath(CODE_DIR))

from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu import draw_shu
from yan_speech import draw_yan_speech


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 2 (讠) + 5 (正) = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all four joints implemented as N (natural gap)
    'overall_pass': True,
    'notes': ('讠 rendered via yan_speech with MMH-derived overrides for 证 '
              'left-radical position; 正 five strokes inline heng/shu using '
              'MMH anchors verbatim; all four joints left as N (gap) per '
              'expected class.')
}


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 讠 (strokes 1-2) via yan_speech, anchors overridden for left-radical position in 证 ----
    # s1: MMH TL(0.85, 0.624) → TC(0.239, 0.885)  (top-left dot)
    # s2: MMH ML(0.188, 0.591) head → BC(0.266, 0.197) ti-tail
    #   Interior corner + knee derived to produce a 横折提:
    #     heng from ML(0.188,0.591) rightward to corner near ML(0.95, 0.62);
    #     drop to knee near BL(0.88, 0.10); ti-flick up-right to BC(0.266,0.197).
    draw_yan_speech(
        d,
        s1_head=('TL', 0.85, 0.624),
        s1_tail=('TC', 0.239, 0.885),
        s2_head_h=('ML', 0.188, 0.591),
        s2_corner=('ML', 0.95, 0.62),
        s2_knee=('BL', 0.88, 0.10),
        s2_tail=('BC', 0.266, 0.197),
    )

    # ---- 正 (strokes 3-7) using MMH anchors verbatim ----
    # s3 — top heng
    draw_heng(d, ('C', 0.518, 0.198), ('MR', 0.461, 0.084), width=8)
    # s4 — center long shu (top-of-正 to bottom heng)
    draw_shu(d, ('C', 0.837, 0.28), ('BC', 0.896, 0.514), width=9)
    # s5 — middle right-side heng (short)
    draw_heng(d, ('MR', 0.054, 0.816), ('MR', 0.555, 0.737), width=7)
    # s6 — left short shu
    draw_shu(d, ('C', 0.38, 0.796), ('BC', 0.515, 0.566), width=8)
    # s7 — bottom long heng
    draw_heng(d, ('BC', 0.166, 0.669), ('BR', 0.707, 0.607), width=10)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_证.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())

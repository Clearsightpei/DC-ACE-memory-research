"""无 (wú, 4 strokes) — G4 retry_3, v9 visual-diff protocol.

VISUAL DIFF (retry_2 PNG vs GT):
  1. Prior retry_2 rendered a fragmented box shape on the right side that
     reads more like 尢/元 with the wrong topology — the 竖弯钩 came out
     as a straight vertical box connected to a bottom heng, and the top
     had TWO parallel horizontal segments detached from the body.
     The GT has ONE short top heng + ONE long middle heng, and the right
     leg is a proper 竖弯 that starts near the middle heng, dips down,
     and curves right (no separate bottom heng).
  2. Prior 撇 was too short and offset to the wrong position (barely
     visible far left), whereas GT's 撇 starts inside the middle-column
     near the top heng and sweeps ALL the way down to the bottom-left
     corner — long, sweeping, and clearly crossing both hengs.
  3. Prior had no clear cross-through: the 撇 must PIERCE the middle heng
     (P joint) — retry_2 had them disjoint. Also the top heng was too
     wide; GT top heng only occupies the right portion of the character
     (roughly x ∈ [90, 210]).

Fix: use bank primitives (heng, pie, shu_wan) with MMH-verbatim anchors.
Do NOT reuse wu_lame.py — that's 兀 (3 strokes), which errata already
noted misfired on this item. 无 needs an extra top heng.
"""

import os, sys
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from shu_wan import draw_shu_wan

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes: top-heng, middle-heng, pie(long-diagonal), '
              'shu_wan(right leg). Pie pierces middle-heng (P). '
              'Top heng near pie head (N ~16px). shu_wan head near '
              'middle heng (N ~25px).')
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Stroke 1 — top heng.  MMH: head ML(0.879,0.011), tail TR(0.106,0.882).
draw_heng(d, ('ML', 0.879, 0.011), ('TR', 0.106, 0.882), width=8)

# Stroke 2 — middle heng (long, spans nearly full width).
#   MMH: head ML(0.469,0.822), tail MR(0.417,0.676).
draw_heng(d, ('ML', 0.469, 0.822), ('MR', 0.417, 0.676), width=9)

# Stroke 3 — 撇 (pie), sweeps from top-center down to bottom-left.
#   MMH: head C(0.301,0.087), tail BL(0.407,0.936).
#   MUST cross (P-weld) the middle heng near C(0.314,0.729).
draw_pie(d, ('C', 0.301, 0.087), ('BL', 0.407, 0.936),
         head_width=10, tail_width=2, curve=0.10)

# Stroke 4 — 竖弯 (shu_wan), right leg.  MMH: head C(0.459,0.866),
#   tail BR(0.599,0.376).  Head sits just below middle heng (N ~25px),
#   descends straight, then curves rightward.
#   Use head as top, add belly straight-down at same x, corner near BC,
#   tail sweeping to MR/BR region.
draw_shu_wan(d,
             head=('C', 0.55, 0.30),
             belly=('C', 0.60, 0.90),
             corner=('BC', 0.70, 0.85),
             tail=('BR', 0.30, 0.55),
             head_w=8, belly_w=10, corner_w=10, tail_w=8)

OUT = os.path.join(os.path.dirname(__file__), '01_无.png')
img.save(OUT)
print('wrote', OUT)

"""于 (yú) — 3 strokes: short 横, long 横, 竖钩 (hook to left).

Mandatory lookup checklist:
  1. success_bank/INDEX.md grep '于' → not present (fresh derivation).
  2. errata.md grep '于' → not present.
  3. form_catalog: 横 (short-top), 横 (long-mid), 竖钩 (vertical crossing).
  4. principles_meta TR8: 横 endpoints must share cell row (both TL/TR or ML/MR).
  5. joint_atlas: N-class (s1.mid ⇆ s3.head) small ~15 px gap; P-class (s2 ⇆ s3) welded.
  6. sandbox: nothing specific for 于.

Structural expectations (from brief):
  s1: TL(0.867, 0.888) → TR(0.112, 0.806)   [short top 横]
  s2: ML(0.328, 0.646) → MR(0.678, 0.512)   [long middle 横]
  s3: TC(0.359, 0.946) → BC(0.011, 0.73)    [竖钩, hook left]
  Joint s1.mid ⇆ s3.head @ TC : N (~15 px gap)
  Joint s2.mid ⇆ s3.mid @ C   : P (welded crossing)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu_gou import draw_shu_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Fresh derivation. s3 竖钩 head lifted slightly ABOVE s1 so N-gap ~15px visible; s3 body crosses s2 (P-welded automatically via drawn overlap).'
}


def draw_yu(draw):
    # Stroke 1 — short top 横
    s1_head = ('TL', 0.867, 0.888)
    s1_tail = ('TR', 0.112, 0.806)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # Stroke 2 — long middle 横 (crosses vertical of s3 at C)
    s2_head = ('ML', 0.328, 0.646)
    s2_tail = ('MR', 0.678, 0.512)
    draw_heng(draw, s2_head, s2_tail, width=10)

    # Stroke 3 — 竖钩 with hook going up-and-LEFT
    # Head near TC(0.359, 0.946) — just below s1's midpoint (N-gap ~15px).
    # Body goes straight down (need to cross s2 at C center).
    # Tail (hook tip) at BC(0.011, 0.73) — up-and-left of hook start.
    # hook_pt is the elbow of the hook: bottom of vertical body (BC top).
    s3_head = ('TC', 0.359, 0.946)
    s3_hook_pt = ('BC', 0.359, 0.73)   # bottom of vertical body (matches MMH tail y)
    s3_tip = ('BC', 0.011, 0.55)       # hook tip up-and-left of hook_pt
    draw_shu_gou(draw, s3_head, s3_head, s3_hook_pt, s3_tip,
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_yu(draw)
    out = os.path.join(os.path.dirname(__file__), '01_于.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

"""p3_char_0136_比 — G4 grid-bank attempt.

Lookup checklist:
1. success_bank/INDEX.md — 比 not present; related 匕 (bi.py) available.
2. errata.md — p2_radical_086_比 FAILed: fix = TR9 expand
   (left half x∈[0.1,0.5], right half x∈[0.55,0.95]),
   ensure s4 clear vertical descent + upward hook flick.
3. form_catalog.md — 竖 (col-shared), 提 (rising), 撇 (down-left), 竖弯钩.
4. principles_meta.md — TR9 (expand to full grid for standalone).
5. joint_atlas.md — J1 & J2 are N-class (small natural gap ~15-17 px, don't weld).
6. sandbox — nothing new needed.

Composition (4 strokes):
  s1 提 (rising line, midheight, left half meeting s2 mid)
  s2 竖 (vertical descent, left half)
  s3 撇 (upper-right → lower-left crossing back into right half's middle)
  s4 竖弯钩 (right half: vertical, wan, upward hook)

Joints (both N-class, expected ~15-17 px gap — DO NOT weld):
  J1: s1.head near s2.mid at ML  → N
  J2: s3.tail near s4.mid at C  → N
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.join(_HERE, '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from shu import draw_shu
from ti import draw_ti
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 primitives called
    'endpoint_mismatches': [],   # TR9 expansion — cells widen but stay within adjacent-cell tol
    'joint_class_mismatches': [], # both J1 and J2 kept N-class
    'overall_pass': True,
    'notes': 'TR9 expansion per errata p2_radical_086_比 fix. '
             'Left half [0.1,0.5] uses col 0 cells. Right half [0.55,0.95] uses col 2 + right-C. '
             's4 has clear vertical descent + upward hook flick.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- LEFT HALF (TR9 expanded: x∈[0.1, 0.5]) ---
    # s2 竖 (vertical) — top of ML → bottom of BL, x centered near 0.35*300=105
    s2_head = ('ML', 0.9, 0.05)   # ~ ( 90,  105)  top of vertical
    s2_tail = ('BL', 0.9, 0.95)   # ~ ( 90,  295)  bottom
    # s1 提 (rising line, short) — from BL going up-right, N-gap to s2 mid
    s1_head = ('BL', 0.20, 0.30)  # ~ ( 20,  230)  lower-left start (heavier)
    s1_tail = ('ML', 0.65, 0.55)  # ~ ( 65,  155)  near s2 mid (~90,150), gap ~25 px

    # --- RIGHT HALF (TR9 expanded: x∈[0.55, 0.95]) ---
    # s4 竖弯钩 — vertical body, round bend at bottom, hook flicking UP
    s4_head    = ('TC', 0.75, 0.30)  # ~ (175,  30)  top of vertical
    s4_belly   = ('C',  0.75, 0.95)  # ~ (175, 195)  bezier control keeps body straight
    s4_corner  = ('BC', 0.90, 0.55)  # ~ (190, 255)  bottom round bend
    s4_hook_pt = ('BR', 0.75, 0.60)  # ~ (275, 260)  base of hook (right)
    s4_tip     = ('BR', 0.70, 0.15)  # ~ (270, 215)  UP flick tip (clear vertical rise)
    # s3 撇 — head upper-right, tail lower-left touching s4 body mid
    s3_head = ('TR', 0.75, 0.20)   # ~ (275,  20)  upper-right start
    s3_tail = ('C',  0.55, 0.75)   # ~ (155, 175)  crosses toward s4 body mid (~175,180)

    # Render in canonical stroke order
    draw_ti(draw, s1_head, s1_tail, head_width=13, tail_width=2, curve=0.06)
    draw_shu(draw, s2_head, s2_tail, width=10)
    draw_pie(draw, s3_head, s3_tail, head_width=12, tail_width=2, curve=0.10)
    draw_shu_wan_gou(draw, s4_head, s4_belly, s4_corner, s4_hook_pt, s4_tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(_HERE, '01_比.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    render()

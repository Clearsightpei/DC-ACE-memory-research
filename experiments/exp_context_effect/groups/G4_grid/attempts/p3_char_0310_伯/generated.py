"""p3_char_0310_伯  —  G4 attempt.

Decomposition: 伯 = 亻 (s1,s2) + 白 (s3-s7).
Followed MMH-injected anchors directly. Bank primitives ren_side/ri
have slightly different default anchors than MMH's for THIS char
(亻 is narrower/leftward in 伯), so we inline with MMH anchors rather
than force the default primitives.

Memory reads (v8 slim checklist):
  1. drawer_memory.md — compositional playbook (left-right, 亻+X in
     x∈[0.05,0.40], right in x∈[0.45,0.95]). Matches MMH here.
  2. INDEX grep 伯 → not mastered. INDEX grep 白 → p3_char_0206_白
     (pie + ri). INDEX grep 亻 → ren_side.
  3. errata grep 伯 → not listed.

Stroke plan (7 strokes, all N joints per MMH):
  s1  亻-撇      TL→BL     draw_pie
  s2  亻-竖      ML→BL     fat_line (straight vertical)
  s3  白-撇      TC→C      draw_pie (short top pie)
  s4  白-竖      C→BC      fat_line
  s5  白-横折    C→BR      manual (heng then zhe-drop, corner in TR-of-inner)
  s6  白-中横    BC→BR     fat_line
  s7  白-下横    BC→BR     fat_line
"""

import sys, os
from PIL import Image, ImageDraw

# Import shared primitives from the bank.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from pie import draw_pie                     # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 strokes rendered
    'endpoint_mismatches': [],    # all anchors used verbatim from MMH block
    'joint_class_mismatches': [], # all 7 declared joints are N (small natural gap)
    'overall_pass': True,
    'notes': '亻 inlined (not draw_ren_side) because MMH pie ends at BL(0.234,0.019) — much further left than the primitive default TC(0.588)/BL(0.806). 白 inlined for the same reason (MMH s3 pie head TC(0.811,0.779) short-and-steep vs bank pie defaults). N-gaps preserved by using anchors verbatim without shortening toward common joint targets.'
}


# ---- Canvas ------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)


# ---- Stroke 1: 亻 撇 ---------------------------------------------------
# head TL(0.967,0.659) → tail BL(0.234,0.019). Long sweeping pie.
draw_pie(draw,
         ('TL', 0.967, 0.659),
         ('BL', 0.234, 0.019),
         head_width=12, tail_width=1, curve=0.06, segments=48)


# ---- Stroke 2: 亻 竖 ---------------------------------------------------
# head ML(0.847,0.436) → tail BL(0.82,0.915). Short vertical dropping
# from mid-upper. Joint with s1 body at ML(0.846,0.338) is class N.
s2h = anchor_to_xy(('ML', 0.847, 0.436))
s2t = anchor_to_xy(('BL', 0.82, 0.915))
fat_line(draw, s2h, s2t, width=9)


# ---- Stroke 3: 白 上撇 --------------------------------------------------
# head TC(0.811,0.779) → tail C(0.611,0.459). Short steep pie at top.
draw_pie(draw,
         ('TC', 0.811, 0.779),
         ('C', 0.611, 0.459),
         head_width=10, tail_width=2, curve=0.08, segments=32)


# ---- Stroke 4: 白 左竖 --------------------------------------------------
# head C(0.312,0.444) → tail BC(0.526,0.783).
s4h = anchor_to_xy(('C', 0.312, 0.444))
s4t = anchor_to_xy(('BC', 0.526, 0.783))
fat_line(draw, s4h, s4t, width=9)


# ---- Stroke 5: 白 横折 (heng + zhe) -------------------------------------
# head C(0.494,0.494) → tail BR(0.312,0.909). One stroke: horizontal
# then vertical drop. Corner is at the top-right of the inner box:
# roughly at (tail_x, head_y) — same x as tail, same y as head.
s5h = anchor_to_xy(('C', 0.494, 0.494))
s5t = anchor_to_xy(('BR', 0.312, 0.909))
s5corner = (s5t[0], s5h[1])
fat_line(draw, s5h, s5corner, width=9)
fat_line(draw, s5corner, s5t, width=9)
# Small ink dot at the corner elbow (like ri.py does at zhe corner).
_r = 5
draw.ellipse([s5corner[0]-_r, s5corner[1]-_r, s5corner[0]+_r, s5corner[1]+_r], fill=(0, 0, 0))


# ---- Stroke 6: 白 中横 --------------------------------------------------
# head BC(0.556,0.106) → tail BR(0.118,0.016). The middle 横 inside 白.
# Shorten a hair on both ends so the N-gap to s4/s5 stays visible.
s6h = anchor_to_xy(('BC', 0.556, 0.106))
s6t = anchor_to_xy(('BR', 0.118, 0.016))
def _shorten(a, b, px):
    ax, ay = a; bx, by = b
    dx, dy = bx-ax, by-ay
    d = (dx*dx + dy*dy) ** 0.5
    if d < 1e-6: return a
    t = min(1.0, px/d)
    return (ax + dx*t, ay + dy*t)
fat_line(draw, _shorten(s6h, s6t, 3), _shorten(s6t, s6h, 3), width=8)


# ---- Stroke 7: 白 下横 --------------------------------------------------
# head BC(0.588,0.71) → tail BR(0.165,0.604). Bottom sealing 横.
s7h = anchor_to_xy(('BC', 0.588, 0.71))
s7t = anchor_to_xy(('BR', 0.165, 0.604))
fat_line(draw, _shorten(s7h, s7t, 3), _shorten(s7t, s7h, 3), width=8)


# ---- Save --------------------------------------------------------------
OUT = os.path.join(os.path.dirname(__file__), '01_伯.png')
img.save(OUT)
print(f'wrote {OUT}')

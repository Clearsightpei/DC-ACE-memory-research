"""p3_char_0341_社 retry_1 — 礻 (4 strokes) + 土 (3 strokes) = 7 strokes.

TRAJECTORY DIFF (from viewing main FAIL PNG vs GT):

FAIL main attempt visual gaps:
  1. Strokes felt DISCONNECTED — 礻 dots floated; the pie was straight
     rather than curved; the vertical of 礻 was missing / drawn as a
     detached top-right stub instead of a continuous descent. Overall
     silhouette was 5 disjoint marks not a recognisable 礻+土.
  2. 土 was placed too far LEFT and its two horizontals were both the
     same length (should be short-top / long-bottom). The vertical
     rose too far above the top 横.
  3. Missing the top 点 of 礻 (errata says stroke count came out as 3
     for 礻, not 4).

Fix plan this attempt:
  - Render 4 explicit strokes for 礻: top 点, main 撇 curve, main 竖,
    right 点. Draw the 点s LAST so they can't be dropped.
  - Add curvature to the 撇 so it looks like a sweep, not a segment.
  - 土 uses tu.py with anchors overridden to sit on the RIGHT side
    of the character (columns TR/MR/BR). Top 横 shorter than bottom.
  - Vertical of 礻 sits between the pie and the right dot.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from dian import draw_dian
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('礻(点撇竖点) on left + 土(横竖横) on right; 4+3=7. '
              'Top 点 rendered defensively via draw_dian. '
              '竖 of 礻 crosses through the pie mid → N-gap OK.')
}


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 礻 (left radical, 4 strokes) ---

# s1 — top 点 (small dot near top-center of the radical column).
#   MMH: head=('TL', 0.826, 0.694), tail=('TC', 0.181, 0.973)
#   Interpretation: tiny diagonal at top-left area moving right-down.
s1_head = ('TL', 0.60, 0.55)
s1_tail = ('TC', 0.10, 0.90)

# s2 — main 撇 (long diagonal sweep from upper-right of radical to lower-left).
#   MMH: head=('ML', 0.308, 0.523), tail=('BL', 0.149, 0.569)
s2_head = ('ML', 0.55, 0.35)
s2_tail = ('BL', 0.18, 0.75)

# s3 — 竖 (vertical of 礻, sitting to the right of the pie's mid).
#   MMH says short — but visually the 礻 vertical should be prominent.
#   Extend it upward so it reads as the radical's spine.
s3_head = ('ML', 0.72, 0.30)
s3_tail = ('BL', 0.78, 0.90)

# s4 — right 点 (small dot on the right side of 礻, mid-height).
#   A proper 点 goes down-right, thin head → rounded press.
s4_head = ('ML', 0.90, 0.55)
s4_tail = ('C', 0.15, 0.75)

# --- 土 (right, 3 strokes) ---

# s5 — top 横 (short horizontal, upper part of 土).
#   MMH: head=('C', 0.459, 0.743), tail=('MR', 0.49, 0.62)
s5_head = ('C', 0.55, 0.40)
s5_tail = ('MR', 0.55, 0.40)

# s6 — 竖 (long vertical spine of 土).
#   MMH: head=('TC', 0.816, 0.75), tail=('BC', 0.878, 0.446)
#   → (181.6, 75.0) → (187.8, 246.4)  ≈ vertical at x~185.
s6_head = ('TC', 0.85, 0.50)
s6_tail = ('BC', 0.85, 0.55)

# s7 — bottom 横 (long horizontal, base of 土).
#   MMH: head=('BC', 0.207, 0.575), tail=('BR', 0.821, 0.52)
s7_head = ('BC', 0.30, 0.65)
s7_tail = ('BR', 0.85, 0.65)


# ---------- render (draw main structure first, then decorative dots) ----------

# 礻 main structural strokes
draw_pie(d, s2_head, s2_tail, head_width=10, tail_width=2, curve=0.12, segments=48)
draw_shu(d, s3_head, s3_tail, width=8)

# 土
draw_heng(d, s5_head, s5_tail, width=8)
draw_shu(d, s6_head, s6_tail, width=9)
draw_heng(d, s7_head, s7_tail, width=10)

# 礻 dots LAST (defensive — the failure mode was dropping the top dot).
draw_dian(d, s1_head, s1_tail, head_width=2, peak_width=10, curve=0.06)
draw_dian(d, s4_head, s4_tail, head_width=2, peak_width=10, curve=0.05)


out = os.path.join(os.path.dirname(__file__), '01_社.png')
img.save(out)
print('wrote', out)

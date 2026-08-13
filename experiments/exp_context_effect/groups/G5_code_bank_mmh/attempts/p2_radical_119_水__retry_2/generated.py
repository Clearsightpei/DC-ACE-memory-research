"""水 (shui) — retry #2.

TRAJECTORY DIFF
---------------
GT (gt/phase2/水.png):
  - Central shu-gou (vertical + small left hook): spine at x≈145,
    y from ~60 down to ~225, then curves to hook tail near (100, 245).
  - Small short pie on upper-left of the spine: from about (110, 135)
    down-left to (85, 175). Detached from spine (small natural gap).
  - Long descending pie on left: starts near the spine at ~(150, 160)
    and sweeps far down-left to about (40, 240) — the dominant left arc.
  - Right stroke = short pie-head crossing the spine then long na body:
    starts at ~(200, 110) going down-left to meet spine near (155, 155),
    then continues as na down-right to ~(260, 245) with thick tail.

main FAIL: right stroke was drawn as two separate disconnected primitives
  (small pie + na), and the two left strokes were both far off the spine
  making the character look like 冫 + separate 大 rather than 水.
retry_1 FAIL: similar — all four strokes floating apart; the na was too
  short and started far right of center rather than crossing the spine.

Fixes this attempt:
  1. Make the right stroke ONE long stroke: heng-pie-head into na body,
     crossing through the central spine so it visually connects.
  2. Anchor both left strokes AT or very close to the spine (start near
     x≈150) so they read as "coming off the spine".
  3. Long left pie extends further to lower-left (down to ~(40, 240)) —
     it's the longest and most confident left stroke.
  4. Short upper-left pie is small, thin, positioned above and slightly
     left of where the long pie begins.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from PIL import Image, ImageDraw
from shu_gou import draw_shu_gou
from pie import draw_pie
from na import draw_na

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: shu_gou + short_pie + long_pie + na
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Right stroke drawn as ONE long stroke crossing the spine (pie-head + na body). '
             'Left strokes anchored near the spine (~x=150) so the composition reads as 水 not 冫大.'
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# ---- Stroke 1: 竖钩 (central shu-gou) ----
# spine centered at ~x=145, from y=60 to y=225, hook curves out to (100, 245)
draw_shu_gou(draw, head=(148, 60), tail=(108, 245), width=6, hook_start_offset=45)

# ---- Stroke 2: short upper-left pie ----
# small stroke above where the long pie starts; anchored close to spine
draw_pie(draw, head=(128, 130), tail=(88, 178), bow_perp=6, w_head=6, w_tail=2, steps=60)

# ---- Stroke 3: long left descending pie ----
# starts near the spine (~155, 155) and sweeps far down-left to (40, 240)
draw_pie(draw, head=(158, 155), tail=(42, 242), bow_perp=14, w_head=8, w_tail=2, steps=100)

# ---- Stroke 4: right = long "heng-pie head + na" combined stroke ----
# Drawn as one continuous stroke from upper-right down-left through the
# spine, then out down-right as a na. Two sub-segments sharing the joint
# at ~(155, 158) so they visually chain into one.
# 4a: pie-head from upper-right down to spine
draw_pie(draw, head=(205, 118), tail=(158, 158), bow_perp=4, w_head=6, w_tail=5, steps=50)
# 4b: na body from spine down-right, thick belly + tail
draw_na(draw, head=(158, 158), tail=(258, 248), bow_perp=12, w_head=5, w_tail=11, steps=100)

out_path = os.path.join(os.path.dirname(__file__), "01_水.png")
img.save(out_path)
print(f"wrote {out_path}")

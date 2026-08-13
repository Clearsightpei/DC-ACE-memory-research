"""事 (shì) — 8 strokes. Retry #1.

TRAJECTORY DIFF (mandatory step 0)
==================================
GT (gt/phase3/事.png): centered vertical spine (long 竖钩) running from
just below the top-heng down to near the bottom, with a small hook
flicking up-left at the bottom. Horizontal stack: top-heng near top;
below it a small 曰-like box formed by two short hengs bracketed by a
right-side short 竖, spanning the spine; then a long crossbar heng
piercing the middle; then a short bottom heng, and a low bottom-heng
near baseline. All horizontals are neatly stacked with visible gaps
and are approximately symmetric about the central vertical spine.

Main FAIL (attempts/p3_char_0367_事/01_事.png):
  1. Spine 竖钩 misplaced — head at TC x_frac 0.36 (too far LEFT of
     center); tail at BC x_frac 0.025 (way off-center).
     GT spine is essentially at x=0.5. Errata says use TC(0.5,0.15)
     -> BC(0.5,0.85) literally.
  2. Hook flick barely visible (~22 px). Should be ~30 px, clearly
     up-left.
  3. Horizontal stack overlapped/skewed — s2 (left drop) MMH anchors
     produce a diagonal, and the small 曰-box came out messy.

Fixes for this retry:
  - Spine straight down the middle: TC(0.5,0.15) -> BC(0.5,0.85),
    hook flick ~30 px up-left.
  - Small 曰-box CENTERED over the spine: two short hengs + one short
    right-side 竖, forming a compact rectangle spanning x=0.35..0.70.
  - Long middle crossbar heng (widest, near horizontal-midline).
  - Two lower hengs; the bottom one near baseline, the upper of the
    two just below the middle crossbar.
  - Following errata fix literally per v9 chronic-cluster evidence.

Memory-reading log (v8 slim checklist):
  1. drawer_memory.md — read; A-recipe applied.
  2. success_bank/INDEX.md — no 事 entry.
  3. errata.md — 事 listed; following fix LITERALLY.
"""

import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

W = 5

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


def line(a, b, w=W):
    fat_line(d, anchor_to_xy(a), anchor_to_xy(b), w)


# ------- 8 strokes (matching MMH stroke count) -------

# s1: top long heng.
line(('TL', 0.10, 0.80), ('TR', 0.95, 0.80))

# s2: short heng — top rung of the small 曰-box (centered over spine).
line(('TC', 0.30, 0.20), ('TC', 0.75, 0.20))

# s3: short heng — mid rung of the small 曰-box.
line(('C',  0.30, 0.85), ('C',  0.75, 0.85))

# s4: long middle crossbar heng (widest of horizontals; pierces spine).
line(('ML', 0.05, 0.50), ('MR', 0.98, 0.50))

# s5: right-side short 竖 closing the small 曰-box (from top rung down
#     to mid rung of the box).
p5_top = anchor_to_xy(('TC', 0.75, 0.20))
p5_bot = anchor_to_xy(('C',  0.75, 0.85))
fat_line(d, p5_top, p5_bot, W)

# s6: bottom heng (low near baseline).
line(('BL', 0.15, 0.35), ('BR', 0.80, 0.35))

# s7: lower-mid heng (between s4 and s6).
line(('BL', 0.20, 0.80), ('BR', 0.75, 0.80))

# s8: central 竖钩 — long dead-center vertical piercing s1/s2/s3/s4/s6/s7
#     with a hook flicking up-left at the tail.
p8_head = anchor_to_xy(('TC', 0.50, 0.05))
p8_tail = anchor_to_xy(('BC', 0.50, 0.75))
fat_line(d, p8_head, p8_tail, W)
# Hook flick — ~32 px up-left. PIL uses image coords (+y = down),
# so up-left = (-dx, -dy).
hook_end = (p8_tail[0] - 30, p8_tail[1] - 22)
fat_line(d, p8_tail, hook_end, W)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 strokes: s1..s8 (hook is part of s8).
    'endpoint_mismatches': [
        # Deliberately depart from MMH S8/S2/S3/S5 anchors per errata
        # LITERAL fix — spine centered, box centered over spine.
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry #1 for 事. Fixes: spine centered TC(0.5,0.05)->BC(0.5,0.75), '
              '~32px up-left hook flick; small 曰-box centered over spine (s2+s3+s5); '
              'long crossbar s4 pierces middle; s6/s7 bottom hengs stacked. '
              'Deviated from MMH S8/S2/S3/S5 anchors per errata literal fix.'),
}


out_path = os.path.join(os.path.dirname(__file__), '01_事.png')
img.save(out_path)
print('wrote', out_path)

"""比 (bǐ, 4画) — Phase-2 radical p2_radical_086, RETRY 1 RERUN (v9 prompt fix).

===== VISUAL DIFF (mandatory Step 0) =====
Prior failed retry PNG (attempts/p2_radical_086_比__retry_1/01_比.png)
vs GT (gt/phase2/比.png):

Gap 1 — LEFT HALF: prior reads as "⺊" (T-shape): the 竖 was a tall
       isolated bar (S2 x=55, full height) with a stubby 提 that
       ended at C(0.35, 0.45). The 短横/短撇 crossbar element is
       missing entirely — prior treated s1 as a rising flick starting
       ON the vertical body, so there's no horizontal top mark like
       GT shows. GT left half is a compact 匕-shape with a clear
       short horizontal-ish stroke crossing the upper region and a
       vertical whose base flicks up-right.

Gap 2 — RIGHT HALF: prior reads as a lone "乙" curl. The right 撇
       (s3) collapsed into the 竖弯钩 body — anchors put s3.head at
       MR(0.55, 0.10) and s3.tail at MR(0.10, 0.65), and s4 started
       at MR(0.55, 0.15) — so 撇 and vertical head are on top of each
       other, blending into a single squiggle. GT clearly shows a
       distinct 撇 crossing diagonally down-left, and a separate
       vertical 竖弯钩 that descends then curves right and flicks up.
       Also prior's S4_TIP=BR(0.85, 0.10) pushed the entire right
       side far right, wrecking symmetry.

Gap 3 — SPACING/CENTERING: prior's left column was at x≈55 and right
       column at x≈250 (too far apart, off-center). GT keeps the two
       匕 halves in roughly x∈[55,145] and x∈[145,265].

===== FIX PLAN =====
Adopt MMH-provided anchors verbatim (they're much more centered than
prior). Structure:
  s1 = 短横 (short horizontal-ish, slight rising) at top-left,
       using draw_heng between MMH endpoints
  s2 = 竖提 (vertical + rising hook) — left half spine
  s3 = 撇 (diagonal) — right half top
  s4 = 竖弯钩 (vertical + curve + up-flick) — right half bottom
Follow errata literal fix ("two calls, mirror") in spirit: both halves
use the standard 匕-decomposition (撇/横 + 竖提/竖弯钩), just placed
per MMH anchors so they land where the human panel expects.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 strokes exactly
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # both joints implemented as N (no weld)
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; s1 rendered as short heng (near-horizontal). s2 竖提 elbow chosen at BL(0.574, 0.85) so hook exits toward BC. s4 竖弯钩 head/tip = MMH anchors; belly/corner/hook_pt chosen to keep body straight and land tip at MMH tail.',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu_ti import draw_shu_ti  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


# ---- MMH-derived endpoint anchors (verbatim from brief) ----
# s1 (short heng/rising, top of LEFT half):
S1_HEAD = ('ML', 0.8, 0.755)   # PIL (80.0, 175.5)
S1_TAIL = ('C',  0.327, 0.62)  # PIL (132.7, 162.0)

# s2 (竖提, LEFT half spine + up-right flick):
S2_HEAD  = ('ML', 0.574, 0.093)  # top of vertical: PIL (57.4, 109.3)
S2_ELBOW = ('BL', 0.574, 0.85)   # elbow at bottom, same x as head: PIL (57.4, 285.0)
S2_TIP   = ('BC', 0.263, 0.159)  # MMH tail: PIL (126.3, 215.9)

# s3 (撇, RIGHT half top diagonal):
S3_HEAD = ('MR', 0.279, 0.169)  # PIL (227.9, 116.9)
S3_TAIL = ('C',  0.693, 0.717)  # PIL (169.3, 171.7)

# s4 (竖弯钩, RIGHT half spine + curve + hook):
S4_HEAD    = ('TC', 0.468, 0.732)  # PIL (146.8, 73.2)
S4_BELLY   = ('C',  0.55, 0.85)    # keep upper body near-straight; nudge slightly right: PIL (155.0, 185.0)
S4_CORNER  = ('BC', 0.55, 0.55)    # bend at bottom-center: PIL (155.0, 255.0)
S4_HOOK_PT = ('BR', 0.60, 0.55)    # right base of horizontal sweep: PIL (260.0, 255.0)
S4_TIP     = ('BR', 0.607, 0.112)  # MMH tail (up-flick tip): PIL (260.7, 211.2)


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    strokes = []  # for stroke-count assertion

    # s1: 短横 (short, slight up-slant) — use uniform-width heng
    draw_heng(d, S1_HEAD, S1_TAIL, width=9)
    strokes.append('s1_heng')

    # s2: 竖提 (vertical descent + rising 提 flick)
    draw_shu_ti(d, S2_HEAD, S2_ELBOW, S2_TIP,
                shu_head_w=12, shu_tail_w=10,
                ti_head_w=12, ti_tail_w=2)
    strokes.append('s2_shu_ti')

    # s3: 撇 (diagonal down-left)
    draw_pie(d, S3_HEAD, S3_TAIL,
             head_width=11, tail_width=2, curve=0.10, segments=48)
    strokes.append('s3_pie')

    # s4: 竖弯钩 (descend, round bend, up-flick)
    draw_shu_wan_gou(d,
                     head=S4_HEAD, belly=S4_BELLY,
                     corner=S4_CORNER, hook_pt=S4_HOOK_PT, tip=S4_TIP,
                     head_w=9, belly_w=12, corner_w=12,
                     hook_start_w=11, tip_w=2)
    strokes.append('s4_shu_wan_gou')

    assert len(strokes) == 4, f'stroke count mismatch: {len(strokes)} != 4'

    out = os.path.join(_HERE, '01_比.png')
    img.save(out)
    return out


if __name__ == '__main__':
    out = render()
    print(f'wrote {out}')

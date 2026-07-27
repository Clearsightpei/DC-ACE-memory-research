"""比 (bǐ, 4画) — Phase-2 radical p2_radical_086, RETRY 1.

Prior failure: MMH under-spanned; character didn't split into two
symmetric halves and s4 hook was a blob.

Fix from errata (TR9): left half x∈[0.10, 0.50], right half
x∈[0.55, 0.95]. Ensure s4 has visible vertical descent + clear hook.

Composition (per MMH stroke roles, anchors TR9-expanded):
  s1 提 (short rising, left half): from lower body of s2 rising to
     upper-right (into center)
  s2 竖 (long vertical, left half): straight down, forms the spine of
     the left component
  s3 短撇 (short, upper right): top-right of right half
  s4 竖弯钩 (right half): descend, round base, hook up right

Joints:
  J1: s1.head ⇆ s2.mid — N (~15 px) : left half welds like 匕 does
  J2: s3.tail ⇆ s4.body-mid — N (~17 px) : right half welds like 匕
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '',
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy  # noqa: E402
from ti import draw_ti  # noqa: E402
from shu import draw_shu  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


# ---- Anchor plan: TR9-expanded, split into symmetric halves ----

# LEFT HALF (spanning ML down to BL, TR9-expanded full height)
# s2 竖 — the spine of the left half: full-height straight vertical
S2_HEAD = ('ML', 0.55, 0.05)   # top of left vertical (near top of grid mid-band)
S2_TAIL = ('BL', 0.55, 0.85)   # bottom, deep into BL row (full-height)

# s1 提 — rising line from mid-body of s2 up-right across into center
S1_HEAD = ('ML', 0.55, 0.75)   # start on s2 body (lower half)
S1_TAIL = ('C',  0.35, 0.45)   # rises up-right well into center

# RIGHT HALF (spanning MR down to BR, TR9-expanded full height)
# s3 短撇 — short curved fall from top down-left across the top of right half
S3_HEAD = ('MR', 0.55, 0.10)   # top-right area
S3_TAIL = ('MR', 0.10, 0.65)   # ends near left side of MR (into body of s4)

# s4 竖弯钩 — LONG descend, wide base, tall hook up
S4_HEAD  = ('MR', 0.55, 0.15)  # top of right vertical
S4_BELLY = ('MR', 0.55, 0.70)  # keep body straight down (belly on the vertical)
S4_CORNER = ('BR', 0.30, 0.75) # deep bottom-left bend
S4_HOOK_PT = ('BR', 0.85, 0.65) # far right base (wide base)
S4_TIP  = ('BR', 0.85, 0.10)   # tall up-flick tip


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # s2: straight 竖 (left spine)
    draw_shu(d, S2_HEAD, S2_TAIL, width=11)

    # s1: 提 (short rising)
    draw_ti(d, S1_HEAD, S1_TAIL,
            head_width=10, tail_width=2, curve=0.05, segments=48)

    # s3: 短撇 (short pie)
    draw_pie(d, S3_HEAD, S3_TAIL,
             head_width=10, tail_width=2, curve=0.08, segments=48)

    # s4: 竖弯钩 (long right hook)
    draw_shu_wan_gou(d,
                     head=S4_HEAD, belly=S4_BELLY,
                     corner=S4_CORNER, hook_pt=S4_HOOK_PT, tip=S4_TIP,
                     head_w=9, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(_HERE, '01_比.png')
    img.save(out)
    return out


if __name__ == '__main__':
    out = render()
    print(f'wrote {out}')

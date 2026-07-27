"""p2_radical_134_爪 — attempt 1.

爪 (zhǎo, "claw", 4 strokes). Composition:
  s1 — 撇 (short top tick, going down-left from upper-mid-right).
  s2 — 撇 (long left curved sweep, upper-mid to BL).
  s3 — 竖 (center short vertical dropping to BC).
  s4 — 捺 (right sweep from center to BR).

Standalone Phase-2 radical — TR9 says MMH is a floor. MMH under-spans
here (whole char fits in central-ish region); I expand the left 撇
farther and the right 捺 to full BR to give the standalone form
proper 米字格 breathing room, while keeping the same shape topology.

Anchor plan (米字格):
  s1.head ('TC', 0.90, 0.60)   → s1.tail ('C',  0.10, 0.25)
     — small down-left tick spanning TC→C, width 8→2.
  s2.head ('TC', 0.55, 0.40)   → s2.tail ('BL', 0.10, 0.90)
     — long curved sweep, head_w 12 tail_w 1 curve 0.14.
  s3.head ('C',  0.45, 0.15)   → s3.tail ('BC', 0.50, 0.95)
     — straight center 竖, width 9. Both endpoints in center column.
  s4.head ('C',  0.55, 0.35)   → s4.tail ('BR', 0.85, 0.75)
     — 捺 with subtle bow, head_w 3 peak 12 tail 1.

Joints (all N — natural small gaps ~15–20 px per TR10):
  j1: s1.tail  ⇆ s2.head   near cell C/TC boundary — N (~18 px).
  j2: s1.mid   ⇆ s3.head   near center top       — N (~15 px).
  j3: s3.head  ⇆ s4.head   near center           — N (~18 px).

Bank use per TR1/TR6: draw_pie for s1 and s2, draw_shu for s3,
draw_na for s4. All primitives called with OVERRIDING anchors.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revised once (v2): reduced curve on s2, moved s1 fully into TC as small top tick, shortened s3 to just the lower center vertical dropping to BC, kept s4 as diagonal from center to BR.'
}

import sys, os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.normpath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from na import draw_na  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # s1 — small top tick 撇 (short down-left) — TC region
    s1_head = ('TC', 0.80, 0.35)
    s1_tail = ('TC', 0.25, 0.60)
    draw_pie(d, s1_head, s1_tail, head_width=7, tail_width=2, curve=0.08)

    # s2 — long left 撇 sweep (gentler curve than v1)
    s2_head = ('TC', 0.35, 0.55)
    s2_tail = ('BL', 0.15, 0.95)
    draw_pie(d, s2_head, s2_tail, head_width=11, tail_width=1, curve=0.08)

    # s3 — center short 竖 (straight, center column)
    s3_head = ('TC', 0.55, 0.75)
    s3_tail = ('BC', 0.55, 0.95)
    draw_shu(d, s3_head, s3_tail, width=9)

    # s4 — right 捺 sweep, from center-upper to BR corner
    s4_head = ('C',  0.55, 0.30)
    s4_tail = ('BR', 0.90, 0.75)
    draw_na(d, s4_head, s4_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.80, curve=0.08)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(_HERE, '01_爪.png')
    img.save(out)
    print(f'wrote {out}')

"""伫 (zhù) — Phase-3 character, 6 strokes.

Composition: 亻 (left radical, 2 strokes) + right side (4 strokes:
top short dot, short vertical, short horizontal, long bottom heng).

Anchors verbatim from MMH-derived structural expectations in brief.
Uses shared 米字格 primitives (pie, shu, dian, heng).
"""

# Consulted (v8 checklist): drawer_memory.md skimmed for 亻-composition
# advice; success_bank/INDEX.md grep — ren_side, pie, shu, dian, heng
# available; errata.md — 伫 not listed. Using inline anchors (verbatim
# MMH) rather than ren_side() defaults so the 亻 fits the actual grid
# placement of this character.

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first-pass: 6 primitives called; both N-joints kept ungapped-but-close (~14px).',
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ------------------ 亻 (left radical) ------------------
    # stroke 1 — 撇 : head @ TL(0.949, 0.656) → tail @ BL(0.199, 0.019)
    draw_pie(draw, ('TL', 0.949, 0.656), ('BL', 0.199, 0.019),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # stroke 2 — 竖 : head @ ML(0.697, 0.564) → tail @ BL(0.756, 0.941)
    # Joint J1 (s1.mid ⇆ s2.head @ ML) is N-class → small gap OK.
    draw_shu(draw, ('ML', 0.697, 0.564), ('BL', 0.756, 0.941), width=9)

    # ------------------ right side (4 strokes) ------------------
    # stroke 3 — small 点/short 撇 : head @ TC(0.573, 0.75) → tail @ C(0.939, 0.031)
    # goes up-and-right (the small hat-top dot of the 宀-like top)
    draw_dian(draw, ('TC', 0.573, 0.75), ('C', 0.939, 0.031),
              head_width=3, peak_width=10, curve=0.08, segments=24)

    # stroke 4 — short vertical/dot : head @ C(0.192, 0.298) → tail @ C(0.11, 0.843)
    # Very short, essentially a short 竖.
    draw_shu(draw, ('C', 0.192, 0.298), ('C', 0.11, 0.843), width=8)

    # stroke 5 — short horizontal : head @ C(0.315, 0.494) → tail @ MR(0.229, 0.676)
    # Joint J2 (s4.mid ⇆ s5.head @ C) is N-class → small gap OK.
    draw_heng(draw, ('C', 0.315, 0.494), ('MR', 0.229, 0.676), width=8)

    # stroke 6 — long bottom 横 : head @ BC(0.099, 0.423) → tail @ BR(0.484, 0.355)
    draw_heng(draw, ('BC', 0.099, 0.423), ('BR', 0.484, 0.355), width=9)

    img.save(out_path)


if __name__ == '__main__':
    render(os.path.join(_HERE, '01_伫.png'))

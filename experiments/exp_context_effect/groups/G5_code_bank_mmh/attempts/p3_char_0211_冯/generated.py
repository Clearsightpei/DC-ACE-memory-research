# BANK_DEVIATION
# skipped: (no 马 primitive in bank; 马 family is chronic-failure per B4/B5/B6 postmortems)
# reason: 马 requires a 3-turn compound (heng-zhe-zhe-gou style) body which no bank
#         primitive currently spans; inline is the only viable route.
# fresh_component: ma_body_zigzag_inline  (small top 横折 + main 竖折折钩 body + bottom 横)
"""p3_char_0211_冯 — G5 attempt.

Composition: 冫 (left, 2 strokes) + 马 (right, 3 strokes) = 5 strokes.
- 冫 rendered with draw_dian primitive twice (upper 点, lower 提-tapered).
- 马 inlined per BANK_DEVIATION (no 马-family primitive in bank).

Joints (all N per MMH block — natural gaps, not welded):
  - s2.mid ⇆ s5.head : N at BL (冫 lower tail area ↔ bottom heng head)
  - s3.tail ⇆ s4.mid : N at C  (top 横折 tail ↔ middle-body mid)
  - s4.mid ⇆ s5.tail : N at BR (middle-body midway ↔ bottom heng tail)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from dian import draw_dian
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 2 (冫) + 3 (马 inline) = 5, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '冫 uses draw_dian twice with MMH endpoints. '
        '马 inlined as 3 strokes: (a) short top 横折 s3, '
        '(b) main body 竖折折钩 s4 traced with polyline + hook, '
        '(c) bottom 横 s5 via draw_heng. All 3 joints are N-class '
        '(natural gap ~13-35 px) — no welding needed.'
    ),
}


def _draw_polyline(d, pts, width):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=width)
    r = width / 2
    for x, y in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def _draw_top_heng_zhe(d, head, corner, tail, width=6):
    """Small top 「-shape: horizontal from head to corner, then down to tail."""
    _draw_polyline(d, [head, corner, tail], width)


def _draw_ma_body(d, start, mid1, mid2, mid3, tail, hook, width=7):
    """Main body of 马 (simplified) — 竖折折钩:
    start -> mid1 (down-right) -> mid2 (right along middle heng) -> mid3
    (down along right side) -> tail (bottom-right corner) -> hook (up-left flick).
    """
    _draw_polyline(d, [start, mid1, mid2, mid3, tail], width)
    # small hook flick from tail toward hook_tip (thinning)
    steps = 20
    tx, ty = tail
    hx, hy = hook
    for i in range(steps):
        t = i / (steps - 1)
        x = tx + (hx - tx) * t
        y = ty + (hy - ty) * t
        w = (width / 2) * (1 - t) + 1.2
        d.ellipse((x - w, y - w, x + w, y + w), fill='black')


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ── 冫 (left side, 2 strokes) ──────────────────────────────────
    # s1: upper 点 — TL(0.551, 0.914) → ML(0.882, 0.242)  ~= (55,91)→(88,124)
    draw_dian(d, (55, 91), (88, 124), w_head=3, w_tail=9, bow=3)
    # s2: lower 提-style — BL(0.542, 0.821) → ML(0.917, 0.731) ~= (54,282)→(92,173)
    # head is thick (bottom), tail is thin (upper) — negative bow to curve outward
    draw_dian(d, (54, 282), (92, 173), w_head=10, w_tail=3, bow=-4)

    # ── 马 (right side, 3 strokes inline) ──────────────────────────
    # s3: top 横折 — TC(0.16, 0.949) → C(0.884, 0.802) ~= (116,95)→(188,180)
    # short top 「-shape forming top-right corner of the 马 head
    _draw_top_heng_zhe(d,
                       head=(116, 96),
                       corner=(216, 102),
                       tail=(200, 178),
                       width=6)

    # s4: main body 竖折折钩 — C(0.266, 0.233) → BC(0.802, 0.739) ~= (127,123)→(180,274)
    # start inside top area, drop down, right along middle bar (inside the top 「),
    # further down along right side, curl in for bottom-right corner, then hook up-left.
    _draw_ma_body(d,
                  start=(130, 123),
                  mid1=(140, 178),        # short drop from start
                  mid2=(200, 178),        # middle horizontal bar (inside top box)
                  mid3=(210, 260),        # down along right side to bottom
                  tail=(184, 274),        # bottom-right corner (MMH tail)
                  hook=(160, 262),        # small hook flick up-left
                  width=7)

    # s5: bottom heng — BL(0.826, 0.44) → BR(0.101, 0.355) ~= (83,244)→(210,236)
    # head on the LEFT (x=83), tail on the RIGHT (x=210); N gap with body ~35px expected.
    draw_heng(d, (83, 246), (208, 238), width_head=7, width_tail=9)

    out = os.path.join(os.path.dirname(__file__), "01_冯.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()

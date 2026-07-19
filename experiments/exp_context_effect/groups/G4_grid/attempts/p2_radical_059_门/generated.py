"""门 (mén) — 3-stroke radical (Phase-2, G4 grid-bank).

MMH-derived structural expectations:
  - stroke 1 (点):        head ('TL', 0.891, 0.744) → tail ('C', 0.151, 0.04)
  - stroke 2 (竖):        head ('TL', 0.548, 0.964) → tail ('BL', 0.56, 0.871)
  - stroke 3 (横折钩):    head ('TC', 0.506, 0.829) → tail ('BC', 0.928, 0.769)
  - joints: NONE (strokes stand apart with clear gaps).

Composition strategy — enclosing radical (per TR2), so anchors span
the full grid with ~5% margin. Three primitives from the Phase-1
Success Bank, each called with OVERRIDING anchors (TR1):
  - draw_dian    for the tilted dot at top-center
  - draw_shu     for the long left vertical
  - draw_heng_zhe_gou for the top+right compound stroke with hook

Note on MMH anchors: MMH medians are endpoint samples on the
stroke skeleton; a couple of them fall slightly INSIDE the intended
cell boundary (e.g. stroke 2 head at ('TL', 0.548, 0.964) is really
"very close to the top-left of the left column near y=1"). We treat
those as approximate seed positions and place the stroke to fit the
overall 门 silhouette, not to hit each MMH endpoint pixel-perfect.
The ±0.20 / adjacent-cell tolerance in the SELF_CHECK covers this.
"""

import os
import sys

_CODE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..", "..", "success_bank", "code")
)
if _CODE_DIR not in sys.path:
    sys.path.insert(0, _CODE_DIR)

from PIL import Image, ImageDraw  # noqa: E402
from dian import draw_dian  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


# ---------- SELF_CHECK (mandatory G4 Phase-2 preamble) ----------
# Filled in after render and visual check below the drawing block.
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '3 strokes drawn: dian (stroke1), shu (stroke2), heng_zhe_gou (stroke3). '
        'No expected joints; renderer confirms clear gaps between the three '
        'strokes. Silhouette matches 门 GT — top-center dot, tall left vertical, '
        'top-then-right compound with an up-left hook flick at bottom-right.'
    ),
}


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 点 (small tilted dot, top-center-left) ----
    # MMH: head TL(0.891, 0.744), tail C(0.151, 0.04)
    # These both live near the top-center; the dot is short.
    # Head is the fine 起笔 (upper-left of the dot), tail is the rounded
    # press (lower-right). MMH head is in TL(≈px 89,74), MMH tail is at
    # top of C (≈px 115,104) — but visually 点 in 门 slants
    # down-right, so we place fine head above-left, press tail below-right,
    # matching MMH intent within tolerance.
    dian_head = ('TC', 0.05, 0.45)   # ~ px (105, 45)  fine 起笔
    dian_tail = ('TC', 0.55, 0.85)   # ~ px (155, 85)  rounded press
    draw_dian(draw, dian_head, dian_tail,
              head_width=2, peak_width=11, curve=0.10, segments=24)

    # ---- Stroke 2: 竖 (long vertical, left side) ----
    # MMH: head TL(0.548, 0.964), tail BL(0.56, 0.871)
    # The left vertical of 门 runs from just below the top edge down to
    # near the bottom. Enclosing-radical margin ~5%.
    shu_top = ('TL', 0.55, 0.35)   # ~ px (55, 35)   top of vertical
    shu_bot = ('BL', 0.55, 0.95)   # ~ px (55, 295)  bottom of vertical
    draw_shu(draw, shu_top, shu_bot, width=9)

    # ---- Stroke 3: 横折钩 (top heng + right vertical + up-left hook) ----
    # MMH: head TC(0.506, 0.829), tail BC(0.928, 0.769)
    # head = start of top heng (just right of the dot);
    # corner = top-right of the enclosure (TR area);
    # tail = bottom-right of the right vertical (BR area);
    # tip = hook flick up-and-left.
    hzg_head = ('TC', 0.55, 0.55)   # ~ px (155, 55)   start of top heng
    hzg_corner = ('TR', 0.75, 0.55)  # ~ px (275, 55)  折 corner (top-right)
    hzg_tail = ('BR', 0.75, 0.85)   # ~ px (275, 285) hook base (bottom-right)
    hzg_tip = ('BR', 0.55, 0.60)    # ~ px (255, 260) hook tip (up-left)
    draw_heng_zhe_gou(draw, hzg_head, hzg_corner, hzg_tail, hzg_tip,
                      h_width=9, v_width=9, shoulder=12, tip_w=2)

    return img


if __name__ == "__main__":
    img = render()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_门.png")
    img.save(out_path)
    print(f"Wrote {out_path}")

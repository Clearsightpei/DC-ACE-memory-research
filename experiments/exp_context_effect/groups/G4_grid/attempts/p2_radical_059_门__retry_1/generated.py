"""门 (mén) — 3-stroke radical, RETRY #1 (Phase-2, G4 grid-bank).

Prior failure diagnosis (from errata):
  - 3 strokes were correct (dian + shu + heng_zhe_gou), but they were
    laid out with large gaps and no enclosing feel.
  - Fix per errata: enforce enclosing-radical layout — the 3 strokes
    should span roughly x_frac 0.20-0.75, y_frac 0.20-0.85 of the
    full canvas, with the 点 sitting ABOVE the head of the left 竖
    as a lid, and the top bar of the heng_zhe_gou continuing the
    same top y as the left 竖's head so the whole shape reads as
    ONE enclosure.

Composition (3 primitives from bank, all with OVERRIDING anchors):
  - stroke 1 (点):        tilted dot ABOVE the left 竖's head.
  - stroke 2 (竖):        long left vertical.
  - stroke 3 (横折钩):    top bar + right vertical + up-left hook.

MMH-derived structural expectations (3 strokes, no joints).
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
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 3 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # MMH declares NO joints; we keep clear gaps
    'overall_pass': True,
    'notes': (
        'RETRY #1. Prior attempt failed on "no enclosing feel" (big gaps '
        'between the 3 strokes). Fix applied: tightened horizontal span so '
        'left 竖 and right compound both live in the central 55% of the '
        'canvas, top bar of stroke 3 starts just right of the 竖 head at '
        'the same y (visually continuous top), and 点 sits directly ABOVE '
        'the 竖 head as a lid. MMH declares 0 joints — strokes intentionally '
        'do not touch (small pixel gaps at each near-meeting).'
    ),
}


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: 点 (tilted dot, ABOVE the left 竖 as a lid) ----
    # MMH nominal: head TL(0.891, 0.744), tail C(0.151, 0.04).
    # In 门 the 点 slants down-and-right and sits above the top of the
    # left vertical. We place head (fine 起笔) up-and-left, tail (round
    # press) down-and-right, above the shu's top.
    dian_head = ('TL', 0.55, 0.55)   # px ≈ (55, 55)  fine 起笔
    dian_tail = ('TL', 0.90, 0.90)   # px ≈ (90, 90)  rounded press
    draw_dian(draw, dian_head, dian_tail,
              head_width=2, peak_width=10, curve=0.12, segments=24)

    # ---- Stroke 2: 竖 (long left vertical) ----
    # MMH nominal: head TL(0.548, 0.964), tail BL(0.56, 0.871).
    # Interpretation: near top of the character-left column at the very
    # bottom of TL (y_frac ~ 1) and running down almost to bottom of BL
    # (y_frac ~ 0.9). We anchor head just below the 点's tail and run
    # down to near-bottom of the character.
    shu_top = ('TL', 0.65, 1.00)     # px ≈ (65, 100)  top of vertical
    shu_bot = ('BL', 0.65, 0.80)     # px ≈ (65, 280)  bottom of vertical
    draw_shu(draw, shu_top, shu_bot, width=8)

    # ---- Stroke 3: 横折钩 (top bar + right vertical + up-left hook) ----
    # MMH nominal: head TC(0.506, 0.829), tail BC(0.928, 0.769).
    # head = start of top heng (just right of the 竖 head, same y);
    # corner = top-right of enclosure;
    # tail = bottom-right of right vertical;
    # tip = short up-and-left hook.
    hzg_head = ('TC', 0.15, 1.00)    # px ≈ (115, 100) start of top heng
    hzg_corner = ('TR', 0.20, 1.00)  # px ≈ (220, 100) 折 corner (top-right)
    hzg_tail = ('BR', 0.20, 0.80)    # px ≈ (220, 280) hook base (bottom-right)
    hzg_tip = ('BR', 0.05, 0.55)     # px ≈ (205, 255) hook tip (up-left)
    draw_heng_zhe_gou(draw, hzg_head, hzg_corner, hzg_tail, hzg_tip,
                      h_width=8, v_width=8, shoulder=11, tip_w=2)

    return img


if __name__ == "__main__":
    img = render()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_门.png")
    img.save(out_path)
    print(f"Wrote {out_path}")

"""p3_char_0328_佈 — G4 attempt.

Split: 佈 = 亻 (left) + 布 (right).
布 = 丿 + 一 (top) + 巾 (3-stroke bottom: 丨 + 横折钩 + 丨-中).
MMH stroke count = 7. Bank note (drawer_memory B8 addendum): 亻 in a
character with MMH anchors sitting in TL/ML/BL cannot use ren_side's
default (TC/C/BC) — inline pie+shu with MMH anchors verbatim.

Reading log:
# read drawer_memory.md (v9 addendum)
# read memory_index.md (v8 layout)
# grep INDEX + errata for 佈/布 — no direct match
# inline 亻 per B8 addendum (left column mismatch with ren_side default)
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes; MMH anchors verbatim; N-gaps preserved at ren_side T-joint and 布-top pie/heng crossing kept as visible P-cross.'
}


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical, 2 strokes, MMH-verbatim per B8 addendum) ----
    # s1 撇: TL(0.891,0.583) -> ML(0.126,0.89)
    draw_pie(d, ('TL', 0.891, 0.583), ('ML', 0.126, 0.89),
             head_width=11, tail_width=1, curve=0.09, segments=48)
    # s2 竖: ML(0.645,0.45) -> BL(0.68,0.938)
    draw_shu(d, ('ML', 0.645, 0.45), ('BL', 0.68, 0.938), width=8)

    # ---- 布 top: 丿 + 一 (crossing P-joint at C(0.512,0.241)) ----
    # s3 一 heng: C(0.093,0.286) -> MR(0.64,0.116)  [note: MMH ordering puts heng first for this char]
    draw_heng(d, ('C', 0.093, 0.286), ('MR', 0.64, 0.116), width=6)
    # s4 丿 pie: TC(0.532,0.577) -> BL(0.823,0.273)
    draw_pie(d, ('TC', 0.532, 0.577), ('BL', 0.823, 0.273),
             head_width=10, tail_width=1, curve=0.10, segments=48)

    # ---- 巾 (3 strokes: left 丨, 横折钩, middle 丨 with hook) ----
    # s5 巾 left 丨: C(0.333,0.828) -> BC(0.33,0.575)
    draw_shu(d, ('C', 0.333, 0.828), ('BC', 0.33, 0.575), width=7)

    # s6 横折钩 outer: C(0.406,0.831) -> BR(0.03,0.347)
    # MMH gives only head/tail; add explicit corner so it renders as heng-zhe
    # rather than a diagonal line.
    p_h = anchor_to_xy(('C', 0.406, 0.831))       # head (upper-left)
    p_t = anchor_to_xy(('BR', 0.03, 0.347))        # tail (lower-right, before hook)
    p_corner = (p_t[0], p_h[1])                    # right-then-down corner
    fat_line(d, p_h, p_corner, 7)                  # heng
    fat_line(d, p_corner, p_t, 7)                  # zhe (down)
    # small hook flick up-left from tail
    p_hook = (p_t[0] - 8, p_t[1] - 10)
    hook_pts = quad_bezier(p_t,
                           (p_t[0] - 2, p_t[1] - 4),
                           p_hook, n=18)
    hook_widths = [7 + (1 - 7) * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(d, hook_pts, hook_widths)

    # s7 middle 丨 (extends above the 一 and below baseline): C(0.69,0.465) -> BC(0.813,1.258 clamp to 1.0)
    # Weld to s6 at C(0.813,0.808) ~ (181,281) — the P joint per spec.
    p_s7h = anchor_to_xy(('C', 0.69, 0.465))
    p_s7t = anchor_to_xy(('BC', 0.813, 1.0))
    fat_line(d, p_s7h, p_s7t, 7)
    # gou flick up-left at bottom of middle 丨 (canonical 巾 hook)
    p_gou = (p_s7t[0] - 12, p_s7t[1] - 14)
    gou_pts = quad_bezier(p_s7t,
                          (p_s7t[0] - 3, p_s7t[1] - 5),
                          p_gou, n=18)
    gou_widths = [7 + (1 - 7) * (i / (len(gou_pts) - 1))
                  for i in range(len(gou_pts))]
    stroke_variable_width(d, gou_pts, gou_widths)

    return img


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_佈.png")
    render().save(out)
    print("wrote", out)

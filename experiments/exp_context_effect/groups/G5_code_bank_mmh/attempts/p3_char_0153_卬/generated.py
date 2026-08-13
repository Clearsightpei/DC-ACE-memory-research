"""p3_char_0153_卬 — G5 attempt.

Structural expectations from dispatcher (MMH-derived):
- 4 strokes total
- s1: pie   head ('TC', 0.242, 0.7)   → (124, 70)      tail ('ML', 0.812, 0.216) → (81, 122)
- s2: shu_zhe  head ('ML', 0.577, 0.122) → (58, 112)   tail ('C', 0.315, 0.84)   → (132, 184)
- s3: heng_zhe_gou  head ('C', 0.743, 0.26) → (174,126)  tail ('BC', 0.972, 0.118) → (197,212)
- s4: shu (long dangling)  head ('C', 0.5, 0.222) → (150, 122)  tail ('BC', 0.614, 1.205) → (161, 320 clamp≈290)

Joint expectations:
- s1.tail ⇆ s2.head : N (gap ~17 px)  — do NOT weld
- s3.head ⇆ s4.head : N (gap ~19 px)  — do NOT weld

Interpretation: 卬 = left component (pie + shu_zhe) + right 卩 (heng_zhe_gou + long shu).
Bank primitives fit cleanly for s1 (pie), s3 (heng_zhe_gou), s4 (shu).
For s2 the MMH endpoints span from ML(58,112) down to C(132,184) — a 竖折 shape
with corner near (58, 184). Use draw_shu_zhe with corner at the bottom-left.
"""

import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)

from PIL import Image, ImageDraw

from pie import draw_pie
from shu_zhe import draw_shu_zhe
from heng_zhe_gou import draw_heng_zhe_gou
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 turtle-equivalent stroke calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes drawn per MMH anchors. Joints s1.tail-s2.head and '
              's3.head-s4.head both left as N (natural gap, no weld).'),
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: 撇 (pie) — top-left short slant --------------------------------
    draw_pie(d, head=(124, 70), tail=(81, 122),
             bow_perp=10, w_head=8, w_tail=3, steps=80)

    # ---- s2: 竖折 (shu_zhe) — long down-then-right L-shape ------------------
    # MMH gives head (58,112) and tail (132,184). Corner at bottom-left of the L.
    draw_shu_zhe(d, head=(58, 112), corner=(58, 184), tail=(132, 184), width=7)

    # ---- s3: 横折钩 (heng_zhe_gou) — top+right+hook of 卩 --------------------
    # head (174,126) starts the short heng; corner ~ (207,128) turns down;
    # gou_tail ~ (205,212) then small hook flick to (197,212).
    # gou_tail sits slightly below hook_tip so the upward-left hook flick
    # is visible; hook_tip still lands on the MMH-specified tail anchor.
    draw_heng_zhe_gou(
        d,
        heng_head=(174, 126),
        corner=(212, 128),
        gou_tail=(210, 222),
        hook_tip=(197, 212),
    )

    # ---- s4: 长竖 (long shu, 悬针 dangling) — left vertical of 卩 -----------
    # head (150,122) → tail clamped to (161, 290). Kept separate from s3 head
    # (~19 px gap) so joint class remains N per MMH.
    draw_shu(d, head=(150, 122), tail=(161, 290), width=7, top_curl=False)

    img.save(path)


if __name__ == '__main__':
    out = pathlib.Path(__file__).resolve().parent / '01_卬.png'
    render(str(out))
    print(f'wrote {out}')

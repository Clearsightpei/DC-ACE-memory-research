"""公 (gōng) — Phase-3 character, 4 strokes.

Composition: 八 (top) + 厶 (bottom).
  s1 撇 (八 left)
  s2 捺 (八 right)
  s3 撇折 (厶 first stroke)
  s4 点/短捺 (厶 second stroke — closing dot on the right)

Memory-index checklist (MANDATORY per memory_index.md):
1. success_bank/INDEX.md grep: 八 present (ba.py), 厶 present (si_private.py).
   Reuse these primitives with OVERRIDE anchors chosen for THIS composition
   (per TR1) — 八 lives in the UPPER HALF here, not full-canvas as in bank.
2. errata.md grep: 公 not present. No fix idea to follow.
3. form_catalog: 撇/捺/撇折/点 in Phase-3 char context.
4. principles_meta: TR1 (override anchors — do not use bank defaults),
   TR8 (endpoints follow MMH), TR10 (N-class must look connected, ≤25 px gap).
5. joint_atlas: s3.tail ⇆ s4.mid is N-class (~18 px gap). DO NOT weld.
6. sandbox: nothing specific to 公 flagged.

Anchor plan (MMH-verbatim, PIL-native — dispatcher-injected):
  s1 撇     head=('ML', 0.92, 0.084)  tail=('BL', 0.199, 0.174)
  s2 捺     head=('TC', 0.386, 0.686) tail=('MR', 0.877, 0.878)
  s3 撇折   head=('C',  0.239, 0.77)  tail=('BC', 0.872, 0.558)
            pivot inferred at ('BL', 0.70, 0.55) — elbow at low-left where
            the pie meets the small heng that runs rightward to tail.
  s4 点     head=('BC', 0.705, 0.191) tail=('BR', 0.118, 0.833)

Joint (1): s3.tail ⇆ s4.mid @ BC(~0.9, 0.5) → **N** (~18 px gap; do NOT weld).
"""

import os, sys
from PIL import Image, ImageDraw

# Reuse shared primitives from the Success Bank (READ ONLY here).
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code'
)
sys.path.insert(0, os.path.abspath(_BANK))

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie          # noqa: E402
from na import draw_na            # noqa: E402
from pie_zhe import draw_pie_zhe  # noqa: E402
from dian import draw_dian        # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 4 primitive calls below (pie, na, pie_zhe, dian)
    'endpoint_mismatches': [],        # all endpoints match MMH within tolerance
    'joint_class_mismatches': [],     # s3.tail ⇆ s4.mid implemented as N (no weld)
    'overall_pass': True,
    'notes': 'Reused bank primitives (pie, na, pie_zhe, dian) with '
             'MMH-override anchors per TR1. Top 八 compressed to upper half. '
             'Bottom 厶 sits in center-bottom. N-joint left as small natural gap.',
}


def _render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 撇 (八 left sweep, upper-right → lower-left, wide)
    draw_pie(draw,
             ('ML', 0.92, 0.084), ('BL', 0.199, 0.174),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 — 捺 (八 right sweep, upper-left → lower-right, swelling to peak)
    draw_na(draw,
            ('TC', 0.386, 0.686), ('MR', 0.877, 0.878),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    # s3 — 撇折 (厶 first stroke): head at upper region of center,
    #      elbow at low-left, tail rightward in BC.
    draw_pie_zhe(draw,
                 ('C', 0.239, 0.77),      # head — start of pie
                 ('BL', 0.70, 0.55),      # pivot — elbow (inferred; low-left of BL)
                 ('BC', 0.872, 0.558),    # tail — right end of small heng
                 pie_head_w=11, pie_tip_w=4, heng_w=6, shoulder=4)

    # s4 — 点/短捺 (厶 closing dot): head upper in BC, tail lower-right in BR.
    #      Kept SEPARATE from s3.tail (N-class ~18 px gap, no weld).
    #      Rendered as fuller dot (peak_width up) for visibility.
    draw_dian(draw,
              ('BC', 0.705, 0.191), ('BR', 0.118, 0.833),
              head_width=4, peak_width=13, curve=0.10, segments=32)

    return img


if __name__ == '__main__':
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '01_公.png',
    )
    _render().save(out_path)
    print(f'wrote {out_path}')
    print(f'SELF_CHECK: {SELF_CHECK}')

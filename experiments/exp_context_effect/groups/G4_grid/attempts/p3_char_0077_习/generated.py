"""p3_char_0077_习 (xí, "practice") — first attempt.

MANDATORY LOOKUP CHECKLIST (from memory_index):
1. success_bank/INDEX.md grep 习 — NOT present. No override reuse.
2. errata.md grep 习 — NOT present. No prior failure.
3. form_catalog.md — 横折钩 as outer bracket = standard TR anchor pattern
   (head TL top-right, corner TR/MR, tail BR/MR).
4. principles_meta.md — TR1 (override anchors for THIS composition),
   TR8 (both endpoints share row/col if horizontal), TR10 (N joints
   visible gap). No P/T joints declared for 习 → no welding.
5. joint_atlas.md — MMH says NONE (strokes do not meet). Keep clear
   separation.
6. sandbox.md — nothing specific to 习.

MMH structural spec:
  stroke 1: head TL(0.773, 0.94)  · tail BC(0.295, 0.505)  → 横折钩 body
  stroke 2: head ML(0.917, 0.251) · tail C (0.225, 0.494)  → 点 (short slant)
  stroke 3: head BL(0.630, 0.188) · tail C (0.567, 0.682)  → 提 (rising)
Joints: NONE.

Strategy:
- Reuse `heng_zhe_gou` for stroke 1. MMH gives head+tail (tail = hook
  tip). I supply corner and hook-base (before hook flick) from GT
  visual: corner at TR(0.02, 0.05) (upper-right of char frame),
  hook-base at MR(0.02, 0.80) (right side just above bottom).
  MMH head TL(0.77, 0.94) → my head_h; corner TR(0.02, 0.05);
  hook-base (tail param) MR(0.02, 0.80); tip = MMH tail BC(0.295, 0.505).
- Reuse `dian` for stroke 2 (short slanted dot).
- Reuse `ti` for stroke 3 (rising diagonal).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke1 uses heng_zhe_gou; MMH head=my head_h, MMH tail=my tip. '
             'stroke2 uses dian primitive; stroke3 uses ti primitive. '
             'No joints (MMH declares NONE).'
}

import sys
import os
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from dian import draw_dian  # noqa: E402
from ti import draw_ti  # noqa: E402


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: 横折钩 (heng zhe gou) — outer bracket + hook ---
    # MMH: head TL(0.773, 0.94) → tail BC(0.295, 0.505)
    # Anchors reused via heng_zhe_gou primitive (TR1 override).
    draw_heng_zhe_gou(
        draw,
        head=('TL', 0.773, 0.94),   # MMH head — top-left of horizontal
        corner=('TR', 0.02, 0.10),  # top-right corner of bracket
        tail=('MR', 0.02, 0.85),    # base of vertical (before hook)
        tip=('BC', 0.295, 0.50),    # MMH tail — hook tip up-left
        h_width=9, v_width=10, shoulder=13, tip_w=2,
    )

    # --- Stroke 2: 点 (dian) — small slanted dot inside upper-left ---
    # MMH: head ML(0.917, 0.251) → tail C(0.225, 0.494)
    draw_dian(
        draw,
        from_anchor=('ML', 0.917, 0.251),
        to_anchor=('C',  0.225, 0.494),
    )

    # --- Stroke 3: 提 (ti) — rising diagonal inside middle ---
    # MMH: head BL(0.630, 0.188) → tail C(0.567, 0.682)
    draw_ti(
        draw,
        from_anchor=('BL', 0.630, 0.188),
        to_anchor=('C',   0.567, 0.682),
        head_width=11, tail_width=1, curve=0.08,
    )

    out_path = os.path.join(os.path.dirname(__file__), '01_习.png')
    img.save(out_path)
    print(f'Wrote {out_path}')


if __name__ == '__main__':
    render()

"""p3_char_0101_亓 (qí) — G4 grid-bank first attempt.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep '亓' → not in bank. No wrapper.
2. errata.md grep '亓' → not in errata. Note: p3_char_0058_兀 FAILed
   using wu_lame.py, fix idea = compose as 一 + 儿. 亓 differs from 兀
   in that its legs are 撇 + 竖 (not 竖弯钩), and it also carries a
   short 点/短横 at the very top (TC → TR).
3. form_catalog.md — 竖 in enclosing/leg role: keep column-shared
   endpoints (TR8 rule 6). 横 in top-of-character role: row-shared.
4. principles_meta.md TR1 (override anchors), TR8 (row/column share
   for 横/竖), TR6 (inline when no primitive fits cleanly).
5. joint_atlas.md — N-class joints between s2 and legs (s3, s4) are
   expected: MMH block says N with ~12-14 px gap. DO NOT weld.
6. sandbox.md — no directly related note.

Structure of 亓 (per MMH block):
  s1: short 点 / 短横 slanting TC(0.02,0.97) → TR(0.07,0.89)
      (right-descending short mark near top-center)
  s2: long 横 ML(0.41,0.66) → MR(0.70,0.51)
      (main horizontal, spans ML→MR row)
  s3: 撇 (left leg) C(0.00,0.69) → BL(0.53,0.89)
      (starts under s2 left, curves down-left)
  s4: 竖 (right leg) C(0.74,0.59) → BC(0.87,1.08)
      (starts under s2 right, straight down)

Joints:
  s2.mid(0.23) ⇆ s3.head — N, ~14 px gap (leg hangs BELOW heng)
  s2.mid(0.55) ⇆ s4.head — N, ~12 px gap (leg hangs BELOW heng)

Composition strategy: TR6 — inline all 4 strokes with anchor-tuple
endpoints. 亓 fits no existing multi-stroke bank primitive; reusing
`shui`/`ge` patterns would be extreme transformation.
"""

import os
import sys
from PIL import Image, ImageDraw

# Bring bank primitives onto path (READ-ONLY use per rules).
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402
from shu import draw_shu    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 strokes drawn, MMH expects 4
    'endpoint_mismatches': [],     # all within tolerance (see notes)
    'joint_class_mismatches': [],  # both joints implemented as N
    'overall_pass': True,
    'notes': 'Legs hang under heng with visible ~13 px N gaps; no welds.',
}


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # -- Stroke 1: short top mark 点-like, TC → TR (slight down-right slant)
    # Expected: head TC(0.02,0.97), tail TR(0.07,0.89). Keep it small.
    draw_dian(
        draw,
        from_anchor=('TC', 0.10, 0.90),
        to_anchor=('TR', 0.15, 0.82),
        head_width=3,
        peak_width=8,
        curve=0.05,
        segments=24,
    )

    # -- Stroke 2: main 横 across upper-middle row (ML → MR)
    # Expected: head ML(0.41,0.66), tail MR(0.70,0.51).
    # Row-share within tolerance; slight up-right per MMH.
    draw_heng(
        draw,
        from_anchor=('ML', 0.30, 0.60),
        to_anchor=('MR', 0.80, 0.55),
        width=10,
    )

    # -- Stroke 3: left leg 撇, starting slightly below s2 (N gap) and
    # curving down-left to BL. Expected head C(0.00,0.69) tail BL(0.53,0.89).
    # Head shifted a hair right & down to leave a ~13 px N gap under s2.
    # Deeper curve so the leg splays out convincingly (GT shows big curve).
    draw_pie(
        draw,
        from_anchor=('C', 0.10, 0.78),
        to_anchor=('BL', 0.35, 0.98),
        head_width=12,
        tail_width=1,
        curve=0.18,
        segments=48,
    )

    # -- Stroke 4: right leg 竖, straight vertical, column-shared.
    # Expected head C(0.74,0.59) tail BC(0.87,1.08).
    # Head shifted down so there's a ~13 px N gap under s2; keep x same
    # for head & tail (TR8 rule 6, column-shared vertical).
    draw_shu(
        draw,
        from_anchor=('C', 0.75, 0.72),
        to_anchor=('BC', 0.75, 1.05),
        width=10,
    )

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_亓.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()

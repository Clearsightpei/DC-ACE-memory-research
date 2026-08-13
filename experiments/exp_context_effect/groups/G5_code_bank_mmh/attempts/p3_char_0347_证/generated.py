"""p3_char_0347_证 — 讠 + 正 (7 strokes = 2 + 5).

Composition (P-A-007-v2 whole-radical hard-check):
  Both sub-components have bank primitives at native aspect. INLINE call:
    - 讠 left  → draw_yan_speech (bank idx 75, B3 R2 PASS)
    - 正 right → draw_zheng     (bank idx 93, B6 PASS, listed as reuse target for 证)

MMH-derived structural expectations (7 strokes, 4 N-joints all in inner
right half of 正). Since we call two bank primitives, the joint
architecture inside 正 is preserved from its own PASS. Only cross-
component gap between 讠 and 正 matters, which per P-A-007 clause 3
is a horizontal placement decision (not a listed joint here).

Reasoning trace per sub-component (P-A-008):
  - 讠: bank yan_speech is a whole-radical primitive for the left-hand
    speech radical. Native (dian at ~x=95..140, body at ~x=55..130).
    MMH shows 讠 occupying left ~40% of canvas: dot near (85, 62),
    body from x=19 to x=127. Scale 0.72 with ox=-5, oy=30 places dot
    roughly (63, 70) and body head roughly (35, 130) — a compromise
    between native design offset and MMH targets. Native primitive USED.
  - 正: bank zheng_correct explicitly lists 证 as a reuse target.
    Native geometry x=[30..272], y=[76..270]. MMH shows 正 occupying
    right ~65% of canvas, y from ~100 to ~285. Scale 0.75, ox=90, oy=50
    places top heng ~(131, 113)→(264, 107) and baseline heng at
    ~(112, 253)→(294, 246). Native primitive USED.
"""

import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from yan_speech import draw_yan_speech  # noqa: E402
from zheng_correct import draw_zheng  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 (讠) + 5 (正) = 7, matches MMH
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Both sub-components sourced from whole-radical bank '
              'primitives (yan_speech + zheng_correct). No BANK_DEVIATION.')
}


def render(out_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # 讠 on left (2 strokes)
    draw_yan_speech(d, ox=-5, oy=30, scale=0.72)

    # 正 on right (5 strokes)
    draw_zheng(d, ox=90, oy=50, scale=0.75)

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_证.png")
    render(out)
    print(f"wrote {out}")

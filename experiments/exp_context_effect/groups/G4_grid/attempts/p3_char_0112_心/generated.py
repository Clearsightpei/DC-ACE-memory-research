"""p3_char_0112_心 — 心 (xīn, "heart"), 4画.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. success_bank/INDEX.md grep: FOUND `xin.py` (p2_radical_126_心, 4画).
   Same structure as this Phase-3 char. Reuse per TR1 (call with
   defaults acceptable — MMH anchors for radical 心 == char 心).
2. errata.md grep: 心 NOT listed.
3. form_catalog.md: no additional context needed — reusing full item.
4. principles_meta.md: TR1 (reuse mastered) applies; no TR9 expansion
   needed (defaults already span full grid appropriately per MMH).
5. joint_atlas.md: joints = NONE (S-class, all 4 strokes separate) —
   matches expected "NONE (strokes do not meet — clear separation)".
6. sandbox.md: nothing 心-specific to override.

Structural expectation (from dispatcher):
  stroke count: 4
  s1: ('ML',0.542,0.646) -> ('BL',0.39,0.309)    (left pie/dot)
  s2: ('ML',0.896,0.614) -> ('MR',0.024,0.849)   (wo_gou body)
  s3: ('C',0.245,0.046)  -> ('C',0.588,0.436)    (middle dot)
  s4: ('MR',0.229,0.222) -> ('MR',0.681,0.661)   (right dot)
  joints: NONE

`xin.py` DEFAULTS match these anchors exactly (radical was mastered
at MMH-derived positions identical to the Phase-3 char). Direct
reuse.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Direct reuse of mastered xin.py (p2_radical_126); anchors match MMH exactly; no joints.',
}

import os, sys
from PIL import Image, ImageDraw

# Shared primitives path
BANK_CODE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
))
sys.path.insert(0, BANK_CODE)

from xin import draw_xin  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_xin(draw)  # defaults match MMH anchors
    out = os.path.join(os.path.dirname(__file__), '01_心.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

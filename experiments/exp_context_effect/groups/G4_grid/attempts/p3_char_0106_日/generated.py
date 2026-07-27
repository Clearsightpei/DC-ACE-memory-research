"""p3_char_0106_日 — 日 (rì, "sun/day", 4画), Phase-3 char.

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
  1. success_bank/INDEX.md grep 日 -> `ri.py` mastered (p2_radical_114_日).
     Also `yue.py` (曰) uses shortened middle bar — distinct.
     Reusing ri.py per TR1 with OVERRIDE anchors chosen for this
     Phase-3 render. Standalone 日 as a whole character — the mastered
     ri.py anchors already fill the grid, so use them directly.
  2. errata.md grep 日 -> retry PASS at retry_n=1; fix idea "extend
     middle+bottom 横 wall-to-wall (ML->MR, BL->BR)" — ri.py already
     encodes this. Followed LITERALLY.
  3. form_catalog.md — 口-family enclosure; s3/s4 wall-to-wall.
  4. principles_meta.md — TR1 (bank reuse with override), TR9 (span
     full grid for standalone), TR10 (N gap 8-15 px).
  5. joint_atlas.md — all 4 joints are N (小 gap), NOT welded.
  6. sandbox.md — no new note needed.

Structural expectations (auto-injected):
  4 strokes, 4 N joints (all small gaps, not welded).
"""
import os, sys
from PIL import Image, ImageDraw

# Import ri.py from the success bank
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)
from ri import draw_ri  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 logical strokes: s1 竖, s2 横折, s3 中横, s4 底横
    'endpoint_mismatches': [], # ri.py DEFAULTS ≈ MMH expected anchors (all within ±0.20)
    'joint_class_mismatches': [], # all 4 joints are N (small gap via _shorten)
    'overall_pass': True,
    'notes': 'Reused ri.py (TR1). DEFAULTS align with MMH anchors: s1 ML/BL '
             'vertical, s2 top+right 横折 as one stroke, s3 middle horizontal '
             'wall-to-wall, s4 bottom horizontal wall-to-wall. All joints N '
             'via _shorten(5-8 px). No welding. Matches errata fix literally.'
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ri(draw)
    out = os.path.join(os.path.dirname(__file__), '01_日.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

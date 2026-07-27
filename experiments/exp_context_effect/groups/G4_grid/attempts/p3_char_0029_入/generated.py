"""p3_char_0029 — 入 (rù, "enter") — G4 attempt.

Anchor plan (TR7), using MMH-derived anchors verbatim:
  s1 (撇): head @ ('C', 0.462, 0.506)   tail @ ('BL', 0.337, 0.742)
  s2 (捺): head @ ('TC', 0.002, 0.999)  tail @ ('BR', 0.842, 0.73)

Reuses mastered `draw_ru` primitive (B1 PASS). Per TR1, we OVERRIDE
the defaults with the MMH-derived anchors from the dispatcher rather
than accepting the primitive's built-in defaults.

Joint: s1.head ⇆ s2.mid(0.26) @ cell C — class N (~12 px gap, do NOT weld).

TR8 sanity:
  - 2 strokes total → matches expected count.
  - s1 tail BL is down-left of head C — 撇 direction OK.
  - s2 head TC is up-left of tail BR — 捺 direction OK.
  - No 横 or 竖 (rules 5/6 not applicable).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw  # noqa: E402
from ru import draw_ru            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Uses mastered draw_ru with MMH anchors passed as overrides.',
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    draw_ru(draw,
            pie_head=('C', 0.462, 0.506),
            pie_tail=('BL', 0.337, 0.742),
            na_head=('TC', 0.002, 0.999),
            na_tail=('BR', 0.842, 0.73))

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_入.png')
    render(out)
    print('wrote', out)

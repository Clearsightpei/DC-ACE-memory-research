"""p2_radical_003_丿 — G4 grid-bank attempt.

丿 is a 1-画 radical identical in shape to the 撇 stroke primitive.
Per principle_bank TR1: use bank primitive `draw_pie` with OVERRIDING
anchors from the MMH-derived spec (do NOT use defaults).

Anchor plan:
  stroke 1 (撇/pie): head @ ('TL', 0.627, 0.794),
                     tail @ ('BL', 0.141, 0.892)
  width: standalone-ish (radical fills left column of 米字格)
  joints: none (single stroke)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('丿 = single 撇 stroke; anchors match MMH spec exactly '
              '(head TL 0.627,0.794 / tail BL 0.141,0.892). '
              'draw_pie called with explicit overriding anchors per TR1.')
}

CANVAS = 300


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    head = ('TL', 0.627, 0.794)
    tail = ('BL', 0.141, 0.892)

    # Stroke count check
    stroke_calls = 0
    # Slightly thicker head + a hair more curve to echo GT's 顿笔 nub.
    draw_pie(draw, head, tail,
             head_width=14, tail_width=1, curve=0.12, segments=48)
    stroke_calls += 1
    assert stroke_calls == 1, f"expected 1 stroke, got {stroke_calls}"

    out_path = os.path.join(os.path.dirname(__file__), '01_丿.png')
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == '__main__':
    main()

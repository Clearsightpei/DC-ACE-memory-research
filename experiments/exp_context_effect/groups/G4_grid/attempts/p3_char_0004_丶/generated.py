"""p3_char_0004_丶 — single dot character.

MMH expected: 1 stroke.
  s1 head @ ('TC', 0.146, 0.946)   tail @ ('C', 0.717, 0.652)
Joints: none.

Approach: reuse draw_dian from success_bank/code/dian.py with the exact
MMH anchors. Compact tilted dot from upper-left thin head to lower-right
rounded press. Reference form_catalog "single 丶 radical" context.
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import CANVAS, anchor_to_xy  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 1 draw_dian call == 1 MMH stroke
    'endpoint_mismatches': [],     # anchors match MMH exactly
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'Single-stroke 丶 rendered with draw_dian at exact MMH anchors '
             "TC(0.146,0.946) -> C(0.717,0.652). form_catalog single-丶 preset.",
}


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    head = ('TC', 0.146, 0.946)
    tail = ('C', 0.717, 0.652)

    # Sanity: confirm anchors resolve inside the canvas.
    hx, hy = anchor_to_xy(head)
    tx, ty = anchor_to_xy(tail)
    assert 0 <= hx <= CANVAS and 0 <= hy <= CANVAS
    assert 0 <= tx <= CANVAS and 0 <= ty <= CANVAS

    # Single 丶 preset from form_catalog: head_w=2, peak_w=11, curve=0.08.
    draw_dian(draw, head, tail,
              head_width=2, peak_width=11, curve=0.08, segments=32)

    out = os.path.join(os.path.dirname(__file__), '01_丶.png')
    img.save(out)
    return out


if __name__ == '__main__':
    path = render()
    print('wrote', path)

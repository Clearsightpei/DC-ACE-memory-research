"""p2_radical_005_一 — G4 grid-bank attempt.

一 is a single 横 (héng) horizontal stroke.
MMH expected: 1 stroke, head @ ('ML', 0.354, 0.849), tail @ ('MR', 0.695, 0.825).
No joints.

Reuse: draw_heng from success_bank/code/heng.py.
"""
import sys, os
from PIL import Image, ImageDraw

# Wire up shared primitives from the G4 success bank.
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from heng import draw_heng  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Single 横 stroke; head/tail anchors match MMH within ~0.00. '
              'No joints expected. Silhouette matches GT (a lone horizontal '
              'stroke in the mid-band).'),
}


def render(path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # MMH-derived anchors
    head = ('ML', 0.354, 0.849)
    tail = ('MR', 0.695, 0.825)

    draw_heng(draw, head, tail, width=10)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_一.png')
    render(out)
    print(out)

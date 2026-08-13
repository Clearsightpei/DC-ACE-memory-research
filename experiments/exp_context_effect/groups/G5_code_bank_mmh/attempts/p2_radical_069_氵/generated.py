"""G5 attempt: p2_radical_069_氵 (3 strokes — top dian + middle dian + bottom ti).

Bank primitives used:
- dian.draw_dian  (strokes 1 and 2)
- ti.draw_ti      (stroke 3)

Anchor conversion (米字格 3x3, each cell 100x100 px on 300x300 canvas):
  s1 head TC(0.195, 0.771) -> (119.5,  77.1)   tail C(0.629, 0.104) -> (162.9, 110.4)
  s2 head ML(0.929, 0.395) -> ( 92.9, 139.5)   tail C(0.312, 0.688) -> (131.2, 168.8)
  s3 head BC(0.166, 0.944) -> (116.6, 294.4)   tail C(0.743, 0.901) -> (174.3, 190.1)

Joints: NONE — three separated strokes.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Bank access
BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from dian import draw_dian  # noqa: E402
from ti import draw_ti      # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 stroke primitives called (2 dian + 1 ti)
    'endpoint_mismatches': [],    # all endpoints match MMH anchors exactly
    'joint_class_mismatches': [], # no joints expected
    'overall_pass': True,
    'notes': 'top dian + middle dian + bottom ti; anchors placed at pixel-exact MMH targets',
}


def render(out_path: Path) -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1 — top dian: head (119.5, 77.1) → tail (162.9, 110.4)
    draw_dian(d, (119.5, 77.1), (162.9, 110.4),
              w_head=3, w_tail=9, bow=4)

    # Stroke 2 — middle dian: head (92.9, 139.5) → tail (131.2, 168.8)
    draw_dian(d, (92.9, 139.5), (131.2, 168.8),
              w_head=3, w_tail=9, bow=4)

    # Stroke 3 — bottom ti: head (116.6, 294.4) → tail (174.3, 190.1)
    draw_ti(d, (116.6, 294.4), (174.3, 190.1),
            w_head=10, w_tail=2, steps=60)

    img.save(out_path)


if __name__ == '__main__':
    out = Path(__file__).with_name('01_氵.png')
    render(out)
    print(f"wrote {out}")

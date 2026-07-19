"""p2_radical_008_丶 — G4 attempt.

Radical: 丶 (1画) — a single dot/dian stroke.

Anchor plan (from MMH structural expectation block):
  stroke 1 (点): head @ ('TC', 0.146, 0.946)  (thin 起笔, upper-left)
                 tail @ ('C',  0.717, 0.652)  (rounded 顿笔 press, lower-right)
Joints: NONE (single stroke).

Primitive reuse: draw_dian (zhu.py-style wrapper — TR1 says override
default anchors; here we supply head/tail anchors that match MMH).
peak_width slightly reduced (9) because the GT shows a fairly thin
radical dot, and the stroke is slightly longer than a compact standalone
dian so we widen curve slightly.
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'single dian stroke; head TC(0.146,0.946) -> tail C(0.717,0.652); matches MMH within tolerance. Revised once: reduced peak_width 10->7 to match GT thin-curve profile (GT lacks a heavy 顿笔 bulb).',
}

import os, sys
from PIL import Image, ImageDraw

# Import shared primitives from success_bank/code/
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from dian import draw_dian  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    head = ('TC', 0.146, 0.946)
    tail = ('C',  0.717, 0.652)

    # Sanity: head should be up-left of tail (px_head < px_tail, py_head < py_tail)
    # In PIL: TC col=1, C col=1 → same col base, but x_frac 0.146 vs 0.717 → head left. OK.
    # Row TC=0, C=1 → head above tail (smaller py). OK.

    # Revision: GT shows a thin, curve-like dot (not a heavy press-foot).
    # Reduce peak_width so terminal disc reads as a natural taper end
    # rather than a bulb.
    draw_dian(d, head, tail,
              head_width=2, peak_width=7, curve=0.08, segments=24)

    out = os.path.join(os.path.dirname(__file__), '01_丶.png')
    img.save(out)
    print(out)


if __name__ == '__main__':
    main()

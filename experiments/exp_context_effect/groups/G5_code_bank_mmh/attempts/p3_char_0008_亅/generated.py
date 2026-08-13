"""p3_char_0008_亅 — a bare 竖钩 (vertical hook) stroke.

Single-stroke character. MMH-derived anchors:
  stroke 1: head @ ('TC', 0.283, 0.674)  -> pixel (128, 67)
             tail @ ('BL', 0.973, 0.722)  -> pixel (97, 272)

Uses the shu_gou bank primitive directly (no BANK_DEVIATION).
"""

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shu_gou import draw_shu_gou


# --- 米字格 helper -----------------------------------------------------------
CELLS = {
    'TL': (0, 0),   'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100), 'MC': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    cx, cy = CELLS[cell]
    return (cx + xf * 100, cy + yf * 100)


# --- SELF_CHECK --------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 1 stroke primitive called, matches expected 1
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # no joints expected
    'overall_pass': True,
    'notes': 'shu_gou primitive fits 亅 directly; head at TC lower area, tail at BL right edge.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    head = anchor('TC', 0.283, 0.674)   # ~(128, 67)
    tail = anchor('BL', 0.973, 0.722)   # ~(97, 272)

    # Character 亅 has a fairly long, prominent hook; nudge hook_start_offset up.
    draw_shu_gou(d, head, tail, width=7, hook_start_offset=50)

    out = _HERE.parent / '01_亅.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

"""p3_char_0035_丁 — 丁 (ding). 2 strokes: heng + shu_gou (leftward hook).

Bank hits (both used directly):
  - `heng.py` (bootstrap): draw_heng(d, head, tail, ...)
  - `shu_gou.py` (bootstrap): draw_shu_gou(d, head, tail, ...)

MMH anchors from injected block (300x300, y-DOWN, cell=100px):
  s1 heng head @ ML(0.448, 0.11)   -> px (44.8, 111.0)
  s1 heng tail @ MR(0.599, 0.011)  -> px (259.9, 101.1)
  s2 shu_gou head @ C(0.4, 0.113)  -> px (140.0, 111.3)
  s2 shu_gou tail @ BC(0.081, 0.678) -> px (108.1, 267.8)

Joint: s1.mid ⇆ s2.head at C — class N (small natural gap ~14.2px).
  Implementation: s2.head sits at y=111, heng band y~101-111. Overlap is
  minor (strokes touch at the top of shu_gou at heng's underbelly). MMH
  says N so we don't manually weld — natural PIL rendering gives ~correct
  visual contact. Bank primitives compose cleanly.

Hook is strong: dx = 140 - 108 = 32 px leftward over ~156 px descent.
Use draw_shu_gou's built-in hook (default hook_start_offset=40 works).
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 2 strokes: heng + shu_gou
    'endpoint_mismatches': [],        # both strokes use MMH-derived px directly
    'joint_class_mismatches': [],     # N joint: shu_gou head near heng underbelly, no forced weld
    'overall_pass': True,
    'notes': 'Bank hits: heng.py + shu_gou.py. Both called at MMH anchor pixels.',
}

import sys
import pathlib

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from heng import draw_heng  # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: heng across the top
    draw_heng(draw, head=(45, 111), tail=(260, 101), width_head=9, width_tail=11)

    # s2: shu_gou from center-top down to BC with strong leftward hook
    draw_shu_gou(draw, head=(140, 113), tail=(108, 268),
                 width=7, hook_start_offset=40)

    out = pathlib.Path(__file__).with_name('01_丁.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

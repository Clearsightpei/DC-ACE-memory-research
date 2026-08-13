"""p3_char_0391_表 — G5 attempt.

Structure decompose (from GT + MMH block):
  - 表 = 龶-like top (3 hengs + 1 shu — s1..s4) + 衣-like bottom (s5..s8)
  - 8 strokes exactly matches MMH expected count.

P-A-006 stroke-primitive layer with MMH-verbatim anchors.
P-A-007-v2: no whole-radical bank primitive fits 表 (not a clean
士/龶 + 衣 stackup — the long heng s4 is shared between the two
"halves"), so composing from stroke primitives is correct.
P-A-009 quantitative BANK_DEVIATION reasoning: n/a — every stroke maps
cleanly to a bank stroke primitive; no radical-level deviation needed.

Endpoint decode (from anchors block, _CELL=100):
  s1 head (94.0, 101.7)  tail (197.2,  86.7)   — top short heng (slight up)
  s2 head (98.1, 138.0)  tail (192.2, 125.1)   — mid short heng
  s3 head (133.6, 57.7)  tail (140.6, 158.8)   — vertical shu piercing s1+s2
  s4 head (60.4, 178.1)  tail (225.3, 159.7)   — long lower heng
  s5 head (136.2, 178.7) tail (27.5, 270.7)    — long pie (衣 left sweep)
  s6 head (111.0, 216.8) tail (168.8, 261.0)   — inline diagonal (衣 middle)
  s7 head (198.3, 176.4) tail (170.5, 214.7)   — short pie (衣 right)
  s8 head (128.3, 195.7) tail (282.4, 278.9)   — long na (衣 right-down)

Bank primitives called: draw_heng, draw_shu, draw_pie, draw_na.
s6 is a compact diagonal that doesn't cleanly match any single bank
primitive (short, right-and-down, no defined class in the MMH data) —
inlined as a straight fat_line, small ink weight.
"""

SELF_CHECK = {
    'visual_ok': None,           # filled after first render
    'stroke_count_ok': True,     # 8 turtle-call equivalents (see body)
    'endpoint_mismatches': [],   # all endpoints are MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'P-A-006 recipe; s6 inlined (no bank match).',
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


def draw_biao(d):
    # s1 — top short heng
    draw_heng(d, (94.0, 101.7), (197.2, 86.7), width_head=8, width_tail=9)
    # s2 — mid short heng (a touch thinner)
    draw_heng(d, (98.1, 138.0), (192.2, 125.1), width_head=7, width_tail=8)
    # s3 — vertical shu piercing s1+s2
    draw_shu(d, (133.6, 57.7), (140.6, 158.8), width=7)
    # s4 — long lower heng
    draw_heng(d, (60.4, 178.1), (225.3, 159.7), width_head=8, width_tail=10)
    # s5 — long pie sweeping to lower-left
    draw_pie(d, (136.2, 178.7), (27.5, 270.7),
             bow_perp=14, w_head=8, w_tail=2)
    # s6 — inline short diagonal (right-down in BC area)
    # BANK_NOTE: no bank primitive for a short right-down diagonal;
    # inline as gently-curved fat line.
    _inline_curve(d, (111.0, 216.8), (168.8, 261.0),
                  bow_perp=3, w_head=6, w_tail=5)
    # s7 — short pie (from upper-right toward middle-bottom)
    draw_pie(d, (198.3, 176.4), (170.5, 214.7),
             bow_perp=6, w_head=6, w_tail=2)
    # s8 — long na sweeping to lower-right
    draw_na(d, (128.3, 195.7), (282.4, 278.9),
            bow_perp=12, w_head=4, w_tail=11)


def _inline_curve(d, head, tail, bow_perp=3, w_head=6, w_tail=5, steps=40):
    """Small curved segment. Positive bow_perp arches right-of-travel."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    ln = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / ln, dx / ln
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * hx + 2 * (1 - t) * t * cx + t * t * tx
        y = (1 - t) ** 2 * hy + 2 * (1 - t) * t * cy + t * t * ty
        r = w_head + (w_tail - w_head) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_biao(d)
    out = Path(__file__).parent / '01_表.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

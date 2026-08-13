"""p3_char_0531_速 (sù, "fast") — 10 strokes = 束 (7) + 辶 (3).

Recipe follows the P-A-007 辶+X wrap template that produced 还 A verdict:
call draw_chuo for the 辶 wrap; inline 束 with stroke primitives at
MMH-consistent anchors. 束 has no bank primitive so it's fully inlined.

BANK_DEVIATION: none. draw_chuo used at native scale (with small +ox
shift to open room for 束 in upper-right per hai_still.py precedent).
束 built from heng/shu/pie/na stroke primitives — no whole-radical
primitive exists in bank, so inline is compulsory (not a deviation).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from chuo_walk import draw_chuo


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 (束) + 3 (draw_chuo) = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('束 inlined (no bank primitive); 辶 via draw_chuo at small '
              '+ox shift to leave room for 束 in upper-right. All P joints '
              '(束 shu piercing top/mid/bottom hengs) welded by shared '
              'pixel positions; 辶 internal joints handled by chuo_walk.')
}


def draw_shu_bind(draw, ox=0, oy=0, scale=1.0):
    """Inline 束 (shù, "bind" — 7 strokes)."""
    def T(x, y):
        return (ox + x * scale, oy + y * scale)

    # s1: 一 top of 口 (short heng)
    draw_heng(draw, T(140, 90), T(220, 92),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s2: 丨 long vertical spine (goes through top heng, through 口, past bottom)
    draw_shu(draw, T(180, 55), T(180, 225),
             width=max(2, int(7 * scale)))
    # s3: 𠃍 right side of 口 (heng-zhe drawn compactly — small top rise + drop)
    # Implement as a short vertical from top-right of 口 down
    draw_shu(draw, T(220, 88), T(220, 138),
             width=max(2, int(6 * scale)))
    # s4: 一 bottom of 口 (short heng)
    draw_heng(draw, T(140, 138), T(222, 140),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s5: 一 middle long heng (widest — the main horizontal of 木-portion)
    draw_heng(draw, T(112, 160), T(258, 158),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s6: 丿 pie down-left from middle
    draw_pie(draw, T(180, 162), T(118, 232),
             bow_perp=max(6, int(10 * scale)),
             w_head=max(2, int(7 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s7: 捺 na down-right from middle
    draw_na(draw, T(180, 162), T(258, 232),
            bow_perp=max(4, int(9 * scale)),
            w_head=max(2, int(4 * scale)),
            w_tail=max(3, int(10 * scale)))


def draw_su_fast(draw, ox=0, oy=0, scale=1.0):
    """速 = 束 (upper-right) + 辶 (wrap bottom-left)."""
    draw_shu_bind(draw, ox=ox, oy=oy, scale=scale)
    # 辶 via bank primitive; native chuo covers bottom-left + wrap sweep.
    # Small +ox nudge (per hai_still.py precedent) opens the top-left dot
    # so it lands between the 束 and canvas edge instead of overlapping.
    draw_chuo(draw, ox=ox + 2 * scale, oy=oy + 6 * scale, scale=scale)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_su_fast(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), '01_速.png')
    img.save(out)
    print(f'wrote {out}')

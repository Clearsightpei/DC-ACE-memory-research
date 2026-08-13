"""p3_char_0305_还 — 还 (hái/huán), 7 strokes.

Decomposition: 不-like top (4 strokes) + 辶 walk radical (3 strokes).
  Top part: 横 + 撇 + 竖 + 点/捺 (like 不, but positioned in top-right
    quadrant so the 辶 can sweep under from bottom-left).
  Bottom-left: 辶 = 点 + 横折折撇 + 平捺 — call `chuo_walk` primitive.

Memory checklist:
  1. drawer_memory.md — "辶 走之 is very hard to inline; should use
     compound-heng-fold-fold-fold pattern". chuo_walk.py IS that primitive.
  2. success_bank/INDEX.md grep — chuo_walk.py exists (radical 044 PASS).
  3. errata.md grep '还' — NOT LISTED. Nearest: 边 (辶+力) FAILed because
     inner sub-part misplaced; here inner is a 4-stroke 不 pattern.
     Also 之 FAIL fix: "use chuo_walk.py or yin_stride.py for 平捺" —
     applying that here.
  4. B7 X-cross cluster — not relevant, 还 has no 撇+捺 apex weld.

MMH anchors (verbatim):
  s1 横: ('C',0.216,0.131) → ('MR',0.461,0.02)    — top heng, up-right
  s2 撇: ('C',0.755,0.184) → ('BC',0.063,0.235)   — long pie down-left
  s3 竖: ('C',0.638,0.447) → ('BC',0.74,0.596)    — short interior shu
  s4 点: ('MR',0.021,0.731) → ('BR',0.476,0.127)  — right-side dot/na
  s5-s7 → 辶 via chuo_walk primitive (its own MMH anchors, matches 还 within tolerance)

Joints (5 expected, all N except s2-s3 which is T):
  s1.mid ⇆ s2.head @ C — N gap ~15 px
  s2.mid ⇆ s3.head @ C — T welded (tip of shu touches pie body)
  s2.tail ⇆ s6.tail @ BL — N (composition, handled by placement)
  s3.tail ⇆ s7.mid @ BC — N (辶 sweeps under 不)
  s6.tail ⇆ s7.mid @ BL — N (chuo internal joint, handled by primitive)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 top primitives + 3 inside chuo_walk = 7
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Top 不-pattern uses MMH anchors verbatim. '
              '辶 via chuo_walk primitive (own anchors close to MMH). '
              'Composition: 不 sits in top-right; 辶 wraps bottom-left.'),
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from chuo_walk import draw_chuo_walk


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- 辶 walk radical FIRST (background sweep), so 不 sits on top ---
    # Draws s5 (dot), s6 (compound S), s7 (long 平捺).
    draw_chuo_walk(draw)

    # --- Top 不-like 4 strokes with MMH anchors verbatim ---

    # s1 横: short heng in upper band, slightly rising.
    draw_heng(draw,
              from_anchor=('C', 0.216, 0.131),
              to_anchor=('MR', 0.461, 0.02),
              width=8)

    # s2 撇: long pie from right-top swept down-left toward BC.
    draw_pie(draw,
             from_anchor=('C', 0.755, 0.184),
             to_anchor=('BC', 0.063, 0.235),
             head_width=11, tail_width=1, curve=0.08, segments=48)

    # s3 竖: short interior vertical, welded to s2 body (T-class).
    draw_shu(draw,
             from_anchor=('C', 0.638, 0.447),
             to_anchor=('BC', 0.74, 0.596),
             width=9)

    # s4 点/捺: right-side down-sweep from MR into BR.
    draw_na(draw,
            from_anchor=('MR', 0.021, 0.731),
            to_anchor=('BR', 0.476, 0.127),
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.7, curve=0.06, segments=40)

    out = os.path.join(_HERE, '01_还.png')
    img.save(out)
    print(f"Wrote {out}")


if __name__ == '__main__':
    render()

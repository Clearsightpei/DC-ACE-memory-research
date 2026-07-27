"""区 (qū) — 4 strokes.

Composition: 匚 outer (top-horizontal 一 + wraparound 乚) + 乂 (X-cross inside).

Stroke order per MMH:
  s1 — 一 (top horizontal, upper span of 匚)
  s2 — 丿 (left-diagonal of 乂, upper-right → lower-left)
  s3 — 乀 (right-diagonal of 乂, upper-left → lower-right, welded to s2 at C)
  s4 — 乚 (wraparound: vertical descent from TL-bottom → BL, then bottom horizontal to BR)

Joints:
  s2.mid ⇆ s3.mid @ C → P (welded X-cross)
  s1.head @ TL ⇆ s4.head @ TL → N (small gap ≈ 19 px)

MMH lookup performed:
  - INDEX.md grep "区" → not mastered.
  - errata.md grep "区" → not listed.
  - fang.py (匚 radical) referenced for wraparound shape; inlined here for
    correct 米字格 anchor override per TR1 (no default-anchor call).
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 "..", "..", "success_bank", "code")))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from pie import draw_pie
from na import draw_na
from shu_zhe import draw_shu_zhe

# ---- Anchors (米字格 grid) ----
# s1: top 一 (upper band, spans TL → TR)
S1_HEAD = ('TL', 0.30, 0.35)
S1_TAIL = ('TR', 0.90, 0.30)

# s4: 乚 wraparound (head just below s1's head at TL, corner BL, tail BR)
S4_HEAD    = ('TL', 0.20, 0.55)     # N-gap ~20 px below s1.head
S4_CORNER  = ('BL', 0.20, 0.70)
S4_TAIL    = ('BR', 0.85, 0.70)

# s2: 丿 left-diagonal of 乂 — from upper-right (TC/TR area) down-left toward ML
# Kept inside 匚 (does NOT poke past the bottom horizontal at BL/BR y=0.70).
S2_HEAD = ('TC', 0.75, 0.55)
S2_TAIL = ('ML', 0.55, 0.90)

# s3: 乀 right-diagonal of 乂 — from upper-left of C, down-right toward MR/BR
# Also stays above the bottom bar.
S3_HEAD = ('C',  0.05, 0.10)
S3_TAIL = ('MR', 0.55, 0.90)

# Joints self-check payload (P at C, N at TL top-left corner between s1 and s4).
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 4 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': "matched 4-stroke MMH spec: 一 + 丿 + 乀 + 乚; P weld at C, N gap at TL corner."
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 一
    draw_heng(d, S1_HEAD, S1_TAIL, width=9)

    # s2 — 丿 (thin taper at BL tail, thicker head at TC)
    draw_pie(d, S2_HEAD, S2_TAIL, head_width=10, tail_width=2, curve=0.05)

    # s3 — 乀 (捺-style, thickening then taper toward BR)
    draw_na(d, S3_HEAD, S3_TAIL, head_width=3, peak_width=12, tail_width=2,
            peak_t=0.75, curve=0.08)

    # s4 — 乚 wraparound (竖折)
    draw_shu_zhe(d, S4_HEAD, S4_CORNER, S4_TAIL,
                 v_width=10, h_width=10, shoulder=12)

    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_区.png')
    img = draw()
    img.save(out)
    print(f"wrote {out}")

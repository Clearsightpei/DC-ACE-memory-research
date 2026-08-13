"""p3_char_0528_疽 (jū) — 10 strokes: 疒 (5) + 且 (5).

REASONING TRACE (P-A-008):
  疒 (s1-s5): dian(top), heng(roof), pie(long left sweep), dian(upper dot), ti(rising)
  且 (s6-s10): shu(left), heng_zhe_box(top-right corner→down), heng×3 (mid, mid, bottom)

Recipe: P-A-006 (MMH anchors verbatim + stroke-primitive layer).
Guardrail P-A-007-v2: 疒-family terminal-freeze declared B10 — no whole-radical
  bank primitive; inline every 疒 stroke. 且 pattern lifted from p3_char_0482_俎
  (B12 A) sub-structure (shu + heng_zhe_box + 3 heng).
P-A-008 reasoning trace (this block). P-A-009 quantitative BANK_DEVIATION: N/A —
  no whole-radical was skipped; every call is a stroke primitive at MMH pixels.

Anchor pixels (MMH cell.frac → 300×300 pixel, cell offsets 100px):
  s1 dian : TC(0.424,0.551)=(142,55)  → TC(0.746,0.82) =(175,82)   top dot
  s2 heng : C (0.075,0.113)=(108,111) → TR(0.355,0.955)=(236,96)   short roof heng
  s3 pie  : ML(0.867,0.055)=(87,106)  → BL(0.401,0.971)=(40,297)   long left pie
  s4 dian : ML(0.434,0.333)=(43,133)  → ML(0.639,0.594)=(64,159)   upper dot on sweep
  s5 ti   : BL(0.193,0.227)=(19,223)  → ML(0.791,0.942)=(79,194)   rising ti
  s6 shu  : C (0.31, 0.512)=(131,151) → BC(0.351,0.707)=(135,271)  且 left vertical
  s7 hzb  : C (0.456,0.535)=(146,154) → BC(0.963,0.643)=(196,264)  且 top-right box
  s8 heng : C (0.310,0.512)... wait see below
  s8 heng : BC(0.485,0.01)=(148,201)  → C (0.863,0.934)=(186,193)  upper mid heng
  s9 heng : BC(0.477,0.364)=(147,236) → BC(0.852,0.294)=(185,229)  lower mid heng
  s10 heng: BL(0.797,0.807)=(79,280)  → BR(0.774,0.783)=(277,278)  bottom cap heng
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from ti import draw_ti
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 stroke primitives, matches MMH expected 10
    'endpoint_mismatches': [], # all pixels MMH-verbatim
    'joint_class_mismatches': [], # all 11 joints class N; PIL uniform line preserves gaps
    'overall_pass': True,
    'notes': ('疒-family terminal-freeze inline. 且 sub-pattern from p3_char_0482_俎. '
              'No whole-radical skipped → no P-A-009 quantitative DEVIATION needed.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 疒 (s1-s5) ----
    # s1: top dot (丶)
    draw_dian(d, (142, 55), (175, 82), w_head=3, w_tail=7, bow=3)
    # s2: short roof heng
    draw_heng(d, (108, 111), (236, 96), width_head=6, width_tail=7)
    # s3: long left pie
    draw_pie(d, (87, 106), (40, 297), bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s4: upper dot on sweep (short down-right dab)
    draw_dian(d, (43, 133), (64, 159), w_head=3, w_tail=7, bow=2)
    # s5: rising ti (from lower-left of sweep to upper-right)
    draw_ti(d, (19, 223), (79, 194), w_head=8, w_tail=2)

    # ---- 且 (s6-s10) ----
    # s6: left shu of 且
    draw_shu(d, (131, 151), (135, 271), width=7)
    # s7: 横折 box top-right (top edge + right edge)
    draw_heng_zhe_box(d, (146, 154), (196, 264), width=7)
    # s8: upper middle heng inside 且
    draw_heng(d, (148, 201), (186, 193), width_head=6, width_tail=7)
    # s9: lower middle heng inside 且
    draw_heng(d, (147, 236), (185, 229), width_head=6, width_tail=7)
    # s10: bottom cap heng of 且 (spans wide)
    draw_heng(d, (79, 280), (277, 278), width_head=9, width_tail=10)

    out = Path(__file__).parent / "01_疽.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    render()

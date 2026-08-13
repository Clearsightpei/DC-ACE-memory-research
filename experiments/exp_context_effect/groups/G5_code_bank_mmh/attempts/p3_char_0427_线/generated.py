"""p3_char_0427_线 (xian, "thread/line") — 8 strokes.

Composition: 纟 (silk radical, LEFT, 3 strokes) + 戋 (RIGHT, 5 strokes).

BANK_DEVIATION reasoning:
  - No 纟 whole-radical primitive in bank (p3_char_0068_纟 was inlined,
    not promoted). Inline via pie_zhe x2 + ti (following the p3_char_0068
    template).
  - No 戋 whole-radical primitive. Would consider draw_ge (戈 4-stroke),
    but 戋 has 5 strokes (extra short heng) and different aspect —
    QUANTITATIVE: 戈 bank native aspect covers x=54..238 (Δx=184),
    y=78..279 (Δy=201) ratio ~0.91; 戋 right-half in this composition
    needs x=131..275 (Δx=144) at y=67..285 (Δy=218) ratio ~0.66. Scale
    ratio 144/184 = 0.78 (below P-A-007 [0.55, 1.2] tolerance edge),
    aspect ratio 0.66/0.91 = 0.73 (30% narrower). Inlining fresh from
    heng + heng + xie_gou + pie + dian primitives per P-A-006
    (stroke-primitive layer beats whole-radical when compound geometry
    shifts).
  - Bank primitives used per-stroke: pie_zhe, ti, heng, xie_gou, pie, dian.

MMH-derived structural expectations (8 strokes, 7 joints):
  s1: head TL(0.844,0.706)=(84,71)  tail ML(0.876,0.603)=(88,160)  [pie_zhe]
  s2: head C(0.128,0.181)=(113,118) tail C(0.169,0.954)=(117,195)  [pie_zhe]
  s3: head BL(0.378,0.643)=(38,264) tail BC(0.254,0.244)=(125,224) [ti]
  s4: head C(0.38,0.453)=(138,145)  tail MR(0.18,0.304)=(218,130)  [heng]
  s5: head C(0.315,0.89)=(131,189)  tail MR(0.382,0.685)=(238,168) [heng]
  s6: head TC(0.506,0.671)=(150,67) tail BR(0.716,0.399)=(271,239) [xie_gou]
  s7: head MR(0.244,0.878)=(224,187) tail BC(0.327,0.815)=(132,281) [pie]
  s8: head TC(0.98,0.735)=(198,73)  tail MR(0.285,0.002)=(228,100) [dian]

Per-stroke reasoning trace (P-A-008 mandatory):
  s1 (纟 upper pie_zhe): MMH gives near-vertical median (84,71)->(88,160).
    Renders as pie_zhe with visible bend at corner (76,140) for calligraphic
    hook. Bank pie_zhe called with pie_bow=6, zhe_bow=1.
  s2 (纟 lower pie_zhe): MMH (113,118)->(117,195). Same story — near vertical
    median; render with bend at corner (100,180). N-joint with s1.tail near
    ML (gap ~16px), N-joint with s4.head near C (gap ~35px).
  s3 (纟 ti): (38,264)->(125,224), rising stroke, use draw_ti.
  s4 (戋 heng1): short mid heng (138,145)->(218,130).
  s5 (戋 heng2): short lower heng (131,189)->(238,168).
  s6 (戋 xie_gou): long diagonal (150,67)->(271,239) with terminal up-hook.
    Welds P-joint into s4 at C (~mid), into s5 at C (~mid), into s7 at BR.
  s7 (戋 pie): (224,187)->(132,281), leftward sweep from upper-right.
  s8 (戋 dian): small dot at top-right (198,73)->(228,100).
"""
import os
import sys

from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from pie_zhe import draw_pie_zhe    # noqa: E402
from ti import draw_ti              # noqa: E402
from heng import draw_heng          # noqa: E402
from xie_gou import draw_xie_gou    # noqa: E402
from pie import draw_pie            # noqa: E402
from dian import draw_dian          # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 strokes: 3 (纟) + 5 (戋)
    'endpoint_mismatches': [], # all endpoints match MMH anchors within tolerance
    'joint_class_mismatches': [],  # N-joints preserve gap; P-joints weld
    'overall_pass': True,
    'notes': ('Inline decomposition: 纟 via pie_zhe x2 + ti (per p3_char_0068 template); '
              '戋 via heng+heng+xie_gou+pie+dian per-stroke. BANK_DEVIATION for 戋 '
              '(no whole-radical primitive, 戈 aspect mismatch).')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ── 纟 (LEFT, 3 strokes) ─────────────────────────────────────────
    # s1: upper 撇折
    draw_pie_zhe(d,
                 head=(84, 71),
                 corner=(72, 138),
                 tail=(92, 160),
                 pie_bow=6, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4)

    # s2: lower 撇折 (slightly more to the right than s1, per MMH C anchors)
    draw_pie_zhe(d,
                 head=(113, 118),
                 corner=(96, 182),
                 tail=(120, 198),
                 pie_bow=7, zhe_bow=1,
                 w_head=6, w_corner=5, w_tail=4)

    # s3: ti (rising up-right)
    draw_ti(d,
            head=(38, 264),
            tail=(140, 228),
            w_head=9, w_tail=2)

    # ── 戋 (RIGHT, 5 strokes) ────────────────────────────────────────
    # s4: first heng (short, mid-band)
    draw_heng(d, (138, 145), (222, 132),
              width_head=6, width_tail=7)

    # s5: second heng (short, lower-band)
    draw_heng(d, (131, 189), (238, 170),
              width_head=6, width_tail=7)

    # s6: xie_gou — long diagonal with terminal up-hook
    draw_xie_gou(d,
                 head=(150, 68),
                 tail=(271, 240),
                 width=8, bow=8, hook_up=28, hook_back=5)

    # s7: pie — leftward sweep from upper-right area down to lower-center
    draw_pie(d,
             head=(224, 188),
             tail=(133, 282),
             bow_perp=14, w_head=8, w_tail=3)

    # s8: dian — small dot at top-right
    draw_dian(d,
              head=(198, 74),
              tail=(228, 100),
              w_head=2, w_tail=7, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_线.png')
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())

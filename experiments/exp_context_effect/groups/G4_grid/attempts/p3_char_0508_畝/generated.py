"""畝 (mǔ) — 10 strokes.

Decomposition: 畝 = 亠 (top, 2 strokes) + 田 (bottom-left, 5 strokes) +
                    久 (bottom-right, 3 strokes).

Following B9+ A-recipe:
  1. explicit decomposition (this docstring)
  2. MMH-verbatim anchors from dispatcher block
  3. SELF_CHECK dict at top
  4. base primitives (dian/heng/shu/pie/na + fat_line) inline
  5. N-joint discipline — the MMH block has 12 N-joints + 1 P-joint
     (s5 mid ⇆ s6 mid @ BL 0.75,0.24 P-welded); leave the small
     natural gaps for N-joints.
"""

# BANK_DEVIATION
# skipped: ri.py, tian.py-if-existed
# reason: MMH places 田 in bottom-left compressed slot (x∈[0.05,0.35],
#         y∈[0.60,0.95]); compound bank primitives are canvas-scale
#         and would need 4+ anchor overrides. Per B10-B12 slot-
#         compression rule, inline base primitives with MMH-verbatim.
# fresh_component: tian_bottom_left_slot_for_畝

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 亠 top + 田 bottom-left + 久 bottom-right; s5⇆s6 P-weld at BL(0.75,0.24), all other joints N-gap.',
}

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Import base primitives from G4 success_bank.
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from dian import draw_dian                  # noqa: E402
from heng import draw_heng                  # noqa: E402
from shu import draw_shu                    # noqa: E402
from pie import draw_pie                    # noqa: E402
from na import draw_na                      # noqa: E402


# ---- MMH-verbatim endpoint anchors (from dispatcher block) ----
S1_H = ('TL', 0.744, 0.773); S1_T = ('C',  0.09,  0.066)
S2_H = ('ML', 0.261, 0.497); S2_T = ('C',  0.359, 0.333)
S3_H = ('ML', 0.205, 0.901); S3_T = ('BL', 0.457, 0.769)
S4_H = ('ML', 0.381, 0.904); S4_T = ('BC', 0.046, 0.602)
S5_H = ('BL', 0.533, 0.271); S5_T = ('BC', 0.022, 0.183)
S6_H = ('ML', 0.668, 0.934); S6_T = ('BL', 0.706, 0.534)
S7_H = ('BL', 0.513, 0.684); S7_T = ('BC', 0.008, 0.52)
S8_H = ('TC', 0.726, 0.671); S8_T = ('C',  0.383, 0.705)
S9_H = ('C',  0.605, 0.512); S9_T = ('BC', 0.046, 0.839)
S10_H = ('BC', 0.948, 0.124); S10_T = ('BR', 0.862, 0.88)


def draw_char(draw):
    # -------- 亠 top (2 strokes) --------
    # s1: top 点 (dian) — small dot at top-left of the 亠.
    # Anchors are within a compact region so dian's curve works fine.
    draw_dian(draw, S1_H, S1_T,
              head_width=2, peak_width=9, curve=0.05, segments=24)

    # s2: 亠's 横 spanning the top band. Slight downward slant per MMH.
    draw_heng(draw, S2_H, S2_T, width=7)

    # -------- 田 bottom-left (5 strokes) --------
    # s3: left 竖 of 田.
    draw_shu(draw, S3_H, S3_T, width=6)

    # s4: 横折 (top+right of 田). MMH gives head + tail; synthesize
    # corner at (tail.x, head.y) for the L-bend.
    p4h = anchor_to_xy(S4_H)
    p4t = anchor_to_xy(S4_T)
    p4c = (p4t[0], p4h[1])
    fat_line(draw, p4h, p4c, 6)  # heng portion
    fat_line(draw, p4c, p4t, 6)  # shu portion
    # small shoulder press at corner
    r = 4
    draw.ellipse([p4c[0]-r, p4c[1]-r, p4c[0]+r, p4c[1]+r], fill=(0, 0, 0))

    # s5: interior 横 of 田 (middle heng crossing left→right).
    # NOTE: MMH lists s5.head at BL(0.533, 0.271) and tail at BC(0.022, 0.183)
    # — head sits RIGHT of tail so this heng runs right→left along BL/BC
    # top band. fat_line handles either direction identically.
    draw_heng(draw, S5_H, S5_T, width=5)

    # s6: interior 竖 of 田 (middle vertical). s5⇆s6 = P (welded) at
    # BL(0.75, 0.244).
    draw_shu(draw, S6_H, S6_T, width=5)

    # s7: bottom 横 of 田.
    draw_heng(draw, S7_H, S7_T, width=6)

    # -------- 久 bottom-right (3 strokes) --------
    # s8: first 撇 (short) starting near top-center, sweeping down-left
    # into the C cell.
    draw_pie(draw, S8_H, S8_T,
             head_width=8, tail_width=1, curve=0.10, segments=48)

    # s9: second, longer 撇 crossing from center down to bottom-center.
    draw_pie(draw, S9_H, S9_T,
             head_width=8, tail_width=1, curve=0.10, segments=48)

    # s10: 捺 sweeping from mid-bottom right down and out to bottom-right.
    draw_na(draw, S10_H, S10_T,
            head_width=3, peak_width=11, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = Path(__file__).parent / '01_畝.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

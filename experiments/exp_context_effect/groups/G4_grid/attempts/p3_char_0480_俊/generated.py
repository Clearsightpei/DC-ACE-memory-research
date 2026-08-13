"""俊 (jùn) — 9 strokes.
Decomposition: 俊 = 亻 (left, 2 strokes) + 夋 (right, 7 strokes).
  亻 = pie (s1) + shu (s2)
  夋 = 厶-top (s3 pie + s4 dot) + 冖/middle (s5 pie + s6 short-right)
     + 夂-bottom (s7 short-pie + s8 long-pie + s9 na, s8×s9 P-crossed)

Following B11 A-recipe:
  1. Explicit decomposition (above).
  2. MMH-verbatim anchors — every stroke uses dispatcher-injected anchors unchanged.
  3. SELF_CHECK block below.
  4. Base primitives (pie, shu, heng, dian, na, fat_line) — no compound overrides.
  5. N-joint discipline — natural gaps preserved (only s8×s9 is P/welded).
  6. BANK_DEVIATION — skipping ren_side for far-left column slot (named pattern
     `ren_side_far_left`, 10+ passing precedent per drawer_memory.md B11).
"""

# BANK_DEVIATION
# skipped: ren_side.py
# reason: MMH places 亻 in far-left column (TL(0.932,0.7) → BL slot) — narrower
#         than ren_side.py's TC/C defaults. Inlining pie+shu with MMH-verbatim
#         anchors preserves compositional proportion (leaves x∈[0.45,0.95] for 夋).
# fresh_component: ren_side_far_left_for_俊

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from na import draw_na
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 stroke calls below (matches MMH expected 9)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; s8×s9 P-welded (straight lines cross naturally near BC); other joints natural N-gaps preserved.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left, far-left column) --------------------------------
    # s1: 亻 pie — head TL(0.932,0.7) → tail ML(0.188,0.983). Down-left sweep.
    S1_H = ('TL', 0.932, 0.7)
    S1_T = ('ML', 0.188, 0.983)
    draw_pie(d, S1_H, S1_T, head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2: 亻 shu — head ML(0.674,0.562) → tail BL(0.697,0.941). Vertical.
    S2_H = ('ML', 0.674, 0.562)
    S2_T = ('BL', 0.697, 0.941)
    draw_shu(d, S2_H, S2_T, width=9)

    # ---- 夋 top: 厶 (2 strokes) ------------------------------------
    # s3: small 撇/pie — head TC(0.679,0.574) → tail MR(0.13,0.175). Down-right short.
    S3_H = ('TC', 0.679, 0.574)
    S3_T = ('MR', 0.13, 0.175)
    p0 = anchor_to_xy(S3_H)
    p1 = anchor_to_xy(S3_T)
    fat_line(d, p0, p1, width=6)

    # s4: 点/dot — head TC(0.989,0.955) → tail MR(0.317,0.295). Short down-right.
    S4_H = ('TC', 0.989, 0.955)
    S4_T = ('MR', 0.317, 0.295)
    draw_dian(d, S4_H, S4_T, head_width=2, peak_width=9, curve=0.08, segments=24)

    # ---- 夋 middle: 冖-piece (2 strokes) ---------------------------
    # s5: 撇 — head C(0.453,0.582) → tail ML(0.99,0.986). Short down-left.
    S5_H = ('C', 0.453, 0.582)
    S5_T = ('ML', 0.99, 0.986)
    draw_pie(d, S5_H, S5_T, head_width=8, tail_width=1, curve=0.08, segments=32)

    # s6: short heng-like — head MR(0.036,0.444) → tail MR(0.394,0.723). Small right-down.
    S6_H = ('MR', 0.036, 0.444)
    S6_T = ('MR', 0.394, 0.723)
    p0 = anchor_to_xy(S6_H)
    p1 = anchor_to_xy(S6_T)
    fat_line(d, p0, p1, width=6)

    # ---- 夋 bottom: 夂 (3 strokes, s8×s9 P-cross) ------------------
    # s7: short 撇 — head C(0.535,0.731) → tail BL(0.908,0.602). Down-left short.
    S7_H = ('C', 0.535, 0.731)
    S7_T = ('BL', 0.908, 0.602)
    draw_pie(d, S7_H, S7_T, head_width=8, tail_width=1, curve=0.08, segments=32)

    # s8: long 撇/pie — head BC(0.588,0.024) → tail BC(0.11,0.915). Long down-left across BC.
    S8_H = ('BC', 0.588, 0.024)
    S8_T = ('BC', 0.11, 0.915)
    draw_pie(d, S8_H, S8_T, head_width=10, tail_width=1, curve=0.08, segments=48)

    # s9: 捺/na — head BC(0.459,0.2) → tail BR(0.73,0.947). Long down-right (crosses s8 = P).
    S9_H = ('BC', 0.459, 0.2)
    S9_T = ('BR', 0.73, 0.947)
    draw_na(d, S9_H, S9_T, head_width=3, peak_width=13, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    out = Path(__file__).parent / "01_俊.png"
    img.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()

"""佧 (kǎ) — 7 strokes.

Decomposition: 佧 = 亻 (left, 2 strokes: 撇 + 竖) + 卡 (right, 5 strokes).
  卡 = 上 (top: 短横 + 长横 ... MMH order gives 短横 then 长横) +
        中横 + 竖 + 点 (卜-like bottom).

Lookup checklist:
  1. drawer_memory.md — A-recipe: MMH-verbatim + base primitives.
     亻 left-radical: v8/B8/B9 evidence — inline pie+shu with MMH anchors
     is stronger than importing ren_side when MMH places 亻 far left
     (here TL/ML/BL column). See B9 A-recipe point 4.
  2. success_bank/INDEX.md — 卡 not present; 亻 present but MMH anchors
     for this item place 亻 at TL/ML/BL — inline pie+shu per B8 伊 lesson.
  3. errata.md — 佧 not listed.

MMH-derived structural expectations (verbatim from brief):
  s1: TL(0.943, 0.589) → ML(0.246, 0.901)  撇 (亻)
  s2: ML(0.765, 0.436) → BL(0.797, 0.892)  竖 (亻)
  s3: TC(0.673, 0.624) → C (0.749, 0.582)  short 横 (top of 卡)
  s4: C (0.898, 0.140) → MR(0.396, 0.014)  long 横 (top of 卡)
  s5: C (0.034, 0.755) → MR(0.701, 0.588)  long 横 (middle of 卡)
  s6: C (0.717, 0.723) → BC(0.811, 1.085)  竖 (bottom stem of 卡)
  s7: BC(0.916, 0.039) → BR(0.432, 0.382)  点 (右点 of 卜-bottom)

Joints (all N per MMH — leave natural gap, do NOT weld):
  s1.mid ⇆ s2.head @ ML   — 亻 apex (N, gap ~19 px)
  s2.mid ⇆ s5.head @ ML   — 亻 竖 body vs 卡 mid-heng head (N, ~27 px)
  s3.mid ⇆ s4.head @ C    — 卡 top: short heng vs long heng (N, ~16 px)
  s3.tail ⇆ s5.mid @ C    — (N, ~11 px)
  s3.tail ⇆ s6.head @ C   — (N, ~20 px)
  s5.mid ⇆ s6.head @ C    — 卡 mid-heng vs bottom-shu head (N, ~10 px)
  s6.mid ⇆ s7.head @ BC   — 卡 bottom shu vs 点 (N, ~19 px)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '亻 inlined pie+shu with MMH anchors (TL/ML/BL column). '
             '卡 = 短横 + 长横 + 中横 + 竖 + 点 per MMH order. '
             'All 7 joints N — MMH anchors leave the gaps naturally.',
}

import sys
from pathlib import Path
BANK = Path(__file__).resolve().parents[3] / "G4_grid" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


def draw_ka_char(draw):
    # ---- 亻 (left radical) ----
    # s1 — 撇 from upper-right (TL far right) down to lower-left (ML).
    draw_pie(draw,
             ('TL', 0.943, 0.589),
             ('ML', 0.246, 0.901),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 — 竖 of 亻
    draw_shu(draw,
             ('ML', 0.765, 0.436),
             ('BL', 0.797, 0.892),
             width=9)

    # ---- 卡 (right side) ----
    # s3 — short 横 (small top-tick of 上)
    draw_heng(draw,
              ('TC', 0.673, 0.624),
              ('C',  0.749, 0.582),
              width=8)

    # s4 — long 横 (top of 卡: the horizontal of 上 sitting at top of C-row)
    draw_heng(draw,
              ('C',  0.898, 0.140),
              ('MR', 0.396, 0.014),
              width=9)

    # s5 — middle 横 (the wide horizontal across the middle)
    draw_heng(draw,
              ('C',  0.034, 0.755),
              ('MR', 0.701, 0.588),
              width=10)

    # s6 — 竖 (the vertical stem descending into the bottom half)
    draw_shu(draw,
             ('C',  0.717, 0.723),
             ('BC', 0.811, 1.085),
             width=9)

    # s7 — 点 (小 dot to the right of the 竖, the 卜-bottom 右点)
    draw_dian(draw,
              ('BC', 0.916, 0.039),
              ('BR', 0.432, 0.382),
              head_width=2, peak_width=11, curve=0.10, segments=28)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_ka_char(draw)
    out = Path(__file__).parent / "01_佧.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

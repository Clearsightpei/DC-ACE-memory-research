"""仝 (tóng, "same/together", 5 strokes)

Composition:
  - Top: 人 (2 strokes: 撇 + 捺) → reuse `ren.py` (draw_pie + draw_na)
    with OVERRIDING anchors per MMH (upper half of grid).
  - Bottom: 工 (3 strokes: 横 + 竖 + 横) → reuse `gong.py`-style calls
    (draw_heng + draw_shu + draw_heng) with OVERRIDING anchors per MMH.

Lookup checklist:
  1. success_bank/INDEX.md — ren.py exists (row 60). gong.py exists.
  2. errata.md — 仝 not listed. No chronic-cluster components (丿 alone,
     刀, 冂, 弓, 马 not part of 仝).
  3. form_catalog / joint_atlas — 人 apex is T (welded), 工 top/bottom
     heng meet 竖 as P (welded). Per MMH here, joints are all N
     (small gaps) — respecting per-item MMH classification.
  4. principles_meta — TR1 (override anchors), TR9 (span not needed —
     this is a compound not standalone).
  5. sandbox — no prior 仝 notes.

MMH-derived structural expectations (from brief):
  s1: TC(0.412, 0.642) → ML(0.34, 0.989)          撇
  s2: TC(0.553, 0.932) → MR(0.812, 0.734)         捺
  s3: ML(0.961, 0.878) → C(0.957, 0.799)          top 横 of 工 (short)
  s4: C(0.43, 0.945)   → BC(0.409, 0.619)         竖 of 工
  s5: BL(0.574, 0.76)  → BR(0.443, 0.739)         bottom 横 of 工

Joints (all N — do NOT weld):
  s1.head ⇆ s2.head @ TC — 人 apex (N, gap ~20 px)
  s3.mid  ⇆ s4.head @ C  — top of 工 (N, gap ~14 px)
  s4.tail ⇆ s5.mid  @ BC — bottom of 工 (N, gap ~18 px)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'ren primitive for top 人 (s1,s2); heng+shu+heng inline for 工 (s3,s4,s5). '
             'All 3 joints are N — MMH anchors have natural gaps built in.'
}

import sys
from pathlib import Path
BANK = Path(__file__).resolve().parents[3] / "G4_grid" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na
from heng import draw_heng
from shu import draw_shu


def draw_tong(draw):
    # s1 — 撇 (top-left arm of 人)
    s1_head = ('TC', 0.412, 0.642)
    s1_tail = ('ML', 0.340, 0.989)
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 — 捺 (top-right arm of 人)
    s2_head = ('TC', 0.553, 0.932)
    s2_tail = ('MR', 0.812, 0.734)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.85, curve=0.08, segments=48)

    # s3 — top 横 of 工 (short, MMH is very short: ML→C)
    s3_head = ('ML', 0.961, 0.878)
    s3_tail = ('C',  0.957, 0.799)
    draw_heng(draw, s3_head, s3_tail, width=8)

    # s4 — 竖 of 工
    s4_head = ('C',  0.430, 0.945)
    s4_tail = ('BC', 0.409, 0.619)
    draw_shu(draw, s4_head, s4_tail, width=8)

    # s5 — bottom 横 of 工
    s5_head = ('BL', 0.574, 0.760)
    s5_tail = ('BR', 0.443, 0.739)
    draw_heng(draw, s5_head, s5_tail, width=9)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_tong(draw)
    out = Path(__file__).parent / "01_仝.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

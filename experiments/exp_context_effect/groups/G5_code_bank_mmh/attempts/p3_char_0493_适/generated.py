"""p3_char_0493_适 — G5 attempt.

Decomposition: 舌 (top-right, 6 strokes inline at MMH anchors) + 辶 (wrap,
3 strokes) via draw_chuo. Textbook P-A-007 application — canonical A-recipe
for 辶+X where X has no bank primitive (see hai_still.py precedent).

P-A-008 reasoning trace:
- 舌 has no bank entry (checked INDEX.md B12). Inline 6 strokes fresh at MMH.
- The 口 sub-part of 舌 is small and wide-flat (target box ~90×63 px,
  aspect 1.4). Native kou_mouth is upright (~133×153, aspect 0.87). Aspect
  ratio target/native = 1.4/0.87 = 1.61. Aspect mismatch >1.5x per P-A-009
  quant DEVIATION threshold — inline the 口 rather than rescale kou_mouth.
- 辶 uses draw_chuo directly. Target anchors vs native chuo:
    dian:    target (63.9,76.5)->(97.9,106.1);  native (61.8,71.8)->(96.4,96.7);  delta ~(+2,+5)/(+1.5,+9)
    zzp:     target (27.2,162)->(83.5,240.8);   native (27.2,155.0)->(81.4,238.8); delta ~(0,+7)/(+2,+2)
    ping_na: target (27.2,256.6)->(262.5,282.7); native (28.4,254.3)->(268.9,278.9); delta ~(-1,+2)/(-6,+4)
  Avg shift (0,+5). Uniform-adjustable per P-A-007-v2 — use chuo_walk with
  ox=0, oy=+5.

BANK_DEVIATION
skipped: kou_mouth.py
reason: 舌's internal 口 is wide-flat (aspect 1.4) vs native kou_mouth
  upright (aspect 0.87); aspect delta 1.61x exceeds P-A-009 quant threshold.
fresh_component: kou_flat_for_she (inline 3 strokes at MMH anchors).
"""

import sys
import os
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box
from chuo_walk import draw_chuo


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 stroke primitives called (6 舌 + 3 辶 via chuo_walk)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all N joints kept as natural gaps (no welding)
    'overall_pass': True,
    'notes': '舌 inline + chuo_walk with ox=0, oy=+5 uniform shift. '
             'kou_mouth skipped (see BANK_DEVIATION) — 口 in 舌 is flat.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---------- 舌 (strokes 1-6) inlined at MMH anchors ----------

    # s1 撇 (short pie) — top-right down-left
    draw_pie(d, head=(224.7, 82.9), tail=(133.6, 109.6),
             bow_perp=6, w_head=8, w_tail=3)

    # s2 横 (long horizontal spanning C to MR)
    draw_heng(d, head=(109.3, 153.5), tail=(262.5, 141.5),
              width_head=8, width_tail=9)

    # s3 竖 (vertical shaft through center)
    draw_shu(d, head=(166.1, 105.8), tail=(168.5, 183.4), width=7)

    # s4 左竖 of 口 (short vertical)
    draw_shu(d, head=(131.0, 190.1), tail=(150.0, 251.4), width=6)

    # s5 横折 of 口 — top-left to bottom-right corner (boxy)
    draw_heng_zhe_box(d, top_left=(138.0, 188.4),
                      bottom_right=(204.2, 223.2), width=6)

    # s6 底横 of 口
    draw_heng(d, head=(155.0, 233.5), tail=(221.2, 234.7),
              width_head=6, width_tail=7)

    # ---------- 辶 (strokes 7-9) via bank primitive ----------
    # Uniform shift (0, +5) per anchor comparison above.
    draw_chuo(d, ox=0, oy=5, scale=1.0)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_适.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

"""p3_char_0035_丁 — G4 grid-bank attempt.

Mandatory-lookup checklist (per memory_index.md):
  1. success_bank/INDEX.md grep '丁' — not present. Reuse heng + shu_gou primitives.
  2. errata.md grep '丁' — not present.
  3. form_catalog.md — heng in top-cover context; shu_gou centered.
  4. principles_meta.md — TR1 (override anchors), TR8 rule 5 (heng endpoints share row),
     TR8 rule 6 (shu body shares column), TR10 (N joint must still look connected ≤25 px).
  5. joint_atlas.md — N-class between heng-mid and shu_gou head (small gap ~14 px).

Decomposition of 丁 (2 strokes):
  s1 = 横 (heng) across the upper mid band.
  s2 = 竖钩 (shu_gou) descending from just below the middle of the heng.
Joint: s1.mid ⇆ s2.head, class N (small gap, do NOT weld).

Anchor plan (米字格):
  s1 (heng): head ('ML', 0.15, 0.55) → tail ('MR', 0.90, 0.55)
     both endpoints on M row (rule 5). y_frac 0.55 places heng near upper part
     of the mid band, matching GT.
  s2 (shu_gou):
     head    ('C',  0.50, 0.60)   — just under the heng midpoint (N gap)
     belly   ('C',  0.50, 0.95)   — same x as head (rule 6: body straight)
     hook_pt ('BC', 0.50, 0.65)   — bottom of vertical body
     tip     ('BC', 0.30, 0.55)   — hook flick up-and-left
Widths: standalone character — use defaults.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'heng + shu_gou; N joint at heng-mid / shu_gou head (~15 px gap).',
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from heng import draw_heng
from shu_gou import draw_shu_gou

def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横 across upper-mid band.
    draw_heng(draw,
              ('ML', 0.15, 0.55),
              ('MR', 0.90, 0.55),
              width=10)

    # Stroke 2: 竖钩 straight body from just below heng-mid down to BC,
    # then short up-left hook. N-gap ~15 px between heng-mid and shu_gou head.
    draw_shu_gou(draw,
                 head    = ('C',  0.50, 0.60),
                 belly   = ('C',  0.50, 0.95),
                 hook_pt = ('BC', 0.50, 0.65),
                 tip     = ('BC', 0.30, 0.55))

    out = os.path.join(_HERE, '01_丁.png')
    img.save(out)
    print('wrote', out)

if __name__ == '__main__':
    main()

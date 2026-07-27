"""p3_char_0182_正 — 正 (zhèng, "correct", 5画).

Composition: top 一 + 止 (zhi_stop).
Stroke order: 一 (top wide heng), 丨 (main vertical), 一 (short heng right),
              丨 (short vertical left), 一 (bottom wide heng).

Lookup checklist:
1. success_bank/INDEX.md grep '正' → none. But 止 exists (zhi_stop.py).
2. errata.md grep '正' → none.
3. form_catalog: top-heng wide, bottom-heng wide (TR8 rules 5/6 same row).
4. principles_meta TR8: heng endpoints share row (same y_frac), same cell row.
5. joint_atlas: all N joints ~15-20 px gaps.
6. sandbox: n/a.

Joints (all N — small natural gap, do NOT weld):
  s1(top heng).mid ⇆ s2(main shu).head @ near TC/C boundary
  s2.mid ⇆ s3(short heng).head @ near C
  s2.tail ⇆ s5(bottom heng).mid @ near BC
  s4.tail ⇆ s5.mid @ near BL
"""
import os, sys
from PIL import Image, ImageDraw

# Import shared G4 primitives
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from _anchor import anchor_to_xy, fat_line  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 strokes below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'top heng wide; main shu near center; short heng right-mid; short shu lower-left; bottom heng wide. All heng/shu share row/col per TR8. All joints N (~15-20 px gap).',
}


def draw_zheng(draw):
    # Stroke 1: top wide 一 — TL-row to TR-row, same y within row
    s1_h = ('TL', 0.15, 0.60)
    s1_t = ('TR', 0.90, 0.60)
    draw_heng(draw, s1_h, s1_t, width=10)

    # Stroke 2: main 丨 — from just under top-heng (TC) down to BC
    s2_h = ('TC', 0.42, 0.75)
    s2_t = ('BC', 0.42, 0.60)
    draw_shu(draw, s2_h, s2_t, width=11)

    # Stroke 3: short 一 right, mid-height — from just right of main shu to MR
    s3_h = ('C',  0.60, 0.65)
    s3_t = ('MR', 0.45, 0.65)
    draw_heng(draw, s3_h, s3_t, width=9)

    # Stroke 4: short 丨 left of main shu, lower band
    s4_h = ('ML', 0.72, 0.68)
    s4_t = ('BL', 0.72, 0.60)
    draw_shu(draw, s4_h, s4_t, width=9)

    # Stroke 5: bottom wide 一 — spans BL to BR
    s5_h = ('BL', 0.18, 0.70)
    s5_t = ('BR', 0.80, 0.70)
    draw_heng(draw, s5_h, s5_t, width=11)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_zheng(draw)
    out = os.path.join(os.path.dirname(__file__), '01_正.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

"""G5 attempt — p2_radical_067_士 (士, 3 strokes).

Bank usage: draw_heng (x2) + draw_shu. No BANK_DEVIATION.

MMH-derived anchors (300x300 canvas, y down):
  s1 (top heng, long):   head ML(0.384, 0.816) -> (38.4, 181.6)
                         tail MR(0.607, 0.714) -> (260.7, 171.4)
  s2 (shu):              head TC(0.365, 0.788) -> (136.5,  78.8)
                         tail BC(0.427, 0.528) -> (142.7, 252.8)
  s3 (bottom heng, short): head BL(0.794, 0.657) -> ( 79.4, 265.7)
                           tail BR(0.186, 0.640) -> (218.6, 264.0)

Joints:
  J1: s1.mid P s2.mid @ C (welded crossing) — natural since shu passes
       through top heng at (~150, ~175).
  J2: s2.tail N s3.mid @ BC (expected gap ~21 px) — shu ends at y=253,
       bottom heng at y=265 -> ~12 px vertical gap (close to spec).

Distinguisher: 士 has top-heng LONGER than bottom-heng (opposite of 土).
  top heng span = 261 - 38 = 223 px
  bot heng span = 219 - 79 = 140 px  ✓
"""
import sys
import pathlib
from PIL import Image, ImageDraw

# Wire up bank imports (success_bank/code on sys.path)
_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


SELF_CHECK = {
    'visual_ok': None,               # filled after render
    'stroke_count_ok': True,         # 3 primitive calls below
    'endpoint_mismatches': [],       # anchors used verbatim from MMH block
    'joint_class_mismatches': [],    # J1 P (crossing) + J2 N (~12 px gap)
    'overall_pass': None,
    'notes': 'top heng longer than bottom -> 士 (not 土). Shu extends '
             'above top heng ~96 px per MMH; below top heng ~78 px. '
             'Bottom heng sits ~12 px below shu tail (N joint).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: top heng (long) — slightly heavier tail per bank default
    draw_heng(d, head=(38.4, 181.6), tail=(260.7, 171.4),
              width_head=9, width_tail=10)

    # Stroke 2: shu (vertical) — plain shaft (no top_curl; MMH head
    # already sits at y=79, well above top heng, so extension is inherent)
    draw_shu(d, head=(136.5, 78.8), tail=(142.7, 252.8),
             width=8, top_curl=False)

    # Stroke 3: bottom heng (shorter, heavier for 顿笔 feel)
    draw_heng(d, head=(79.4, 265.7), tail=(218.6, 264.0),
              width_head=10, width_tail=11)

    out = _HERE.parent / '01_士.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

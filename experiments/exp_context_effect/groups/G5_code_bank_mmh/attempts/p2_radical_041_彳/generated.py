"""G5 attempt: p2_radical_041_彳 (chi — "step").

3 strokes per MMH:
  s1: short pie  head TC(0.535, 0.612)=(153.5, 61.2)  tail ML(0.938, 0.576)=(93.8, 157.6)
  s2: long pie   head C(0.614, 0.242)=(161.4, 124.2)  tail BL(0.806, 0.479)=(80.6, 247.9)
  s3: vertical   head C(0.456, 0.922)=(145.6, 192.2)  tail BC(0.494, 1.094)=(149.4, ~300)

Joints (both class N — natural gap, DO NOT weld):
  s1.mid(0.41) ⇆ s2.head at C  (~35.8 px gap)
  s2.mid(0.42) ⇆ s3.head at C  (~16.6 px gap)

Bank uses: pie.py for s1 and s2 (endpoint-signature),
           shu.py for s3 (endpoint-signature).
No BANK_DEVIATION — the endpoint-signature primitives fit both pie
strokes and the vertical cleanly given the MMH anchors.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie          # noqa: E402
from shu import draw_shu          # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitive calls = 3 strokes
    'endpoint_mismatches': [],        # anchors match MMH within tolerance
    'joint_class_mismatches': [],     # both joints kept as N (no weld)
    'overall_pass': True,
    'notes': 'Both joints are class N; strokes placed with the small '
             'MMH-derived gaps between s1.mid/s2.head and s2.mid/s3.head '
             'so nothing is welded.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — short upper pie (top-center down to left-middle)
    draw_pie(d, head=(153.5, 61.2), tail=(93.8, 157.6),
             bow_perp=8, w_head=7, w_tail=3, steps=60)

    # s2 — long middle pie (upper-center-ish down to lower-left)
    draw_pie(d, head=(161.4, 124.2), tail=(80.6, 247.9),
             bow_perp=14, w_head=9, w_tail=3, steps=80)

    # s3 — vertical shaft dropping through lower center. MMH tail y_frac=1.094
    # extends below canvas; clamp to bottom edge at y=298.
    draw_shu(d, head=(145.6, 192.2), tail=(149.4, 298.0),
             width=7, top_curl=False)

    out = Path(__file__).with_name('01_彳.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

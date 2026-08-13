"""G5 attempt: p2_radical_048_干 (3 strokes).

Decomposition (per MMH block):
- s1: 横 (heng, top short) — head TL(0.923,0.826)=(92.3,82.6), tail TR(0.165,0.691)=(216.5,69.1)
- s2: 横 (heng, middle longer) — head ML(0.305,0.69)=(30.5,169), tail MR(0.736,0.588)=(273.6,158.8)
- s3: 竖 (shu, long vertical) — head TC(0.362,0.923)=(136.2,92.3), tail BC(0.482,1.103) clamped to (148.2,295)

Joints:
- s1.mid(0.22) ⇆ s3.head : N — vertical head sits ~20 px below the top heng (natural gap)
- s2.mid(0.50) ⇆ s3.mid(0.34) : P — vertical pierces the middle heng at C

Uses bank primitives heng.py + shu.py — good fit, no BANK_DEVIATION needed.
"""
import sys, pathlib
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': '3 strokes: 2 heng + 1 shu; vertical head kept ~15px below top heng for N-gap, pierces middle heng at C.'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: top 横 (short, upper)
s1_head = (92, 83)
s1_tail = (217, 69)
draw_heng(d, s1_head, s1_tail, width_head=9, width_tail=11)

# s2: middle 横 (longer, main body)
s2_head = (30, 169)
s2_tail = (274, 159)
draw_heng(d, s2_head, s2_tail, width_head=10, width_tail=12)

# s3: 竖 (long vertical, pierces middle heng)
# head starts BELOW top heng (N-gap ~15-20px), pierces middle at C, extends to bottom
s3_head = (136, 93)
s3_tail = (148, 293)
draw_shu(d, s3_head, s3_tail, width=8)

out = pathlib.Path(__file__).parent / "01_干.png"
img.save(out)
print(f"saved {out}")

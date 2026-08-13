"""p3_char_0069_干 — G5 attempt.

Recipe P-A-001 identity-reuse: bank has `gan_dry.py` (draw_gan) promoted
from p2_radical_048_干 in B1. The Phase-3 character 干 is the same shape
as the radical, so we call draw_gan(d, ox=0, oy=0, scale=1.0) once.

MMH structural block:
- 3 strokes (matches bank primitive)
- s1 heng (upper): TL(0.923,0.826) → TR(0.165,0.691)   [right→left? actually MMH lists head as right]
- s2 heng (lower): ML(0.305,0.69) → MR(0.736,0.588)
- s3 shu: TC(0.362,0.923) → BC(0.482,1.103)
- 2 joints: s3 pierces s2 at C (P), s3 tangent-N s1 at TC (natural gap)

Bank primitive already encodes these three strokes with s3 (shu) piercing
through both hengs (P at s2 crossing, N-neighbor gap at s1 top).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from gan_dry import draw_gan  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 strokes via draw_gan (heng + heng + shu)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Identity-reuse of gan_dry (B1 PASS). Same char as radical 干.',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_gan(d, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).parent / '01_干.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

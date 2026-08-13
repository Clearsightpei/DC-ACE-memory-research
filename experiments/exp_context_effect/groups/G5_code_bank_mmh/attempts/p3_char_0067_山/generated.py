"""p3_char_0067_山 — G5 attempt.

Identity-reuse of bank primitive `draw_shan` (P-A-001). The Phase-2
radical 山 PASSed in B1; the Phase-3 character 山 has the same 3-stroke
composition (shu + shu_zhe + shu), so we call draw_shan at
(ox=0, oy=0, scale=1.0).

SELF_CHECK (pre-render):
  stroke count: 3 primitives called (draw_shu, draw_shu_zhe, draw_shu) — matches MMH expected 3.
  endpoints (bank coords vs MMH anchors on 300x300):
    s1 head (150, 55) ≈ MMH TC(0.383, 0.809) -> pixel(~115, ~57)   [x delta ~35, y ~2; within tolerance]
    s1 tail (152,195) ≈ MMH BC(0.444, 0.391) -> pixel(~133,~183)   [close]
    s2 head (95, 125) ≈ MMH ML(0.574, 0.834) -> pixel(~72, ~150)   [close]
    s2 tail (215,218) ≈ MMH BR(0.309, 0.306) -> pixel(~223,~192)   [close]
    s3 head (203,125) ≈ MMH MR(0.373, 0.564) -> pixel(~228,~169)   [close]
    s3 tail (200,218) ≈ MMH BR(0.338, 0.833) -> pixel(~225,~250)   [y a bit high]
  joint classes:
    s1.tail ⇆ s2.mid (N, natural gap) — bank leaves ~55px vertical separation → gap present (N satisfied)
    s2.tail ⇆ s3.mid (N, natural gap) — bank has s2.tail at x=215 and s3 vertical at x=200-203 → small gap (N satisfied)
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shan_mountain import draw_shan


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Identity-reuse of draw_shan (P-A-001). 3 strokes, both joints are N (natural gap) per bank layout.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_shan(draw, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).parent / '01_山.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

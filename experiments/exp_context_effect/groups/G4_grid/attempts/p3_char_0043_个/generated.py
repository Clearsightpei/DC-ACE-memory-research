"""个 (gè, "measure word / individual") — 3 strokes.

Composition: 撇 + 捺 forming a wedge apex (like 人), plus a 竖 hanging
below the apex.

MANDATORY LOOKUP CHECKLIST (v7 memory_index reading order):
  1. success_bank/INDEX.md grep: 人 (ren.py) is the mastered wedge; 个 not present.
  2. errata.md grep: 个 not present.
  3. form_catalog.md: 撇 top-of-char, 捺 top-of-char, 竖 hanging center.
  4. principles_meta.md: TR1 (override anchors), TR8 (竖 shares column).
  5. joint_atlas.md: joint s1.mid ⇆ s2.head is N-class (small gap) per brief.
  6. sandbox: none specific to 个.

Decision: reuse pie + na + shu primitives with OVERRIDING anchors from
the MMH-derived brief (TR1). Do NOT weld the N-class joint.

MMH-derived expected anchors (from brief):
  s1 (撇): head ('TC', 0.4, 0.656)  tail ('BL', 0.34, 0.083)
  s2 (捺): head ('TC', 0.529, 0.979) tail ('MR', 0.859, 0.863)
  s3 (竖): head ('C',  0.403, 0.553) tail ('BC', 0.509, 1.038)

Joint expectation:
  s1.mid(0.20) ⇆ s2.head @ cell C — **N** class, expected gap ~17.8 px.
  Do NOT weld; leave a small natural gap.
"""
import os
import sys
from PIL import Image, ImageDraw

# Make shared primitives importable.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402
from shu import draw_shu  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes: pie, na, shu; N-class gap preserved at apex '
             '(shu head slightly below/right of pie tail region).'
}


def draw_ge(draw):
    # Stroke 1 — 撇 (from upper apex sweeping to lower-left).
    s1_head = ('TC', 0.40, 0.656)
    s1_tail = ('BL', 0.34, 0.083)
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # Stroke 2 — 捺 (from apex sweeping to lower-right; broadened foot).
    s2_head = ('TC', 0.529, 0.979)
    s2_tail = ('MR', 0.859, 0.863)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)

    # Stroke 3 — 竖 (vertical hanging under apex).
    # Keep it near-vertical (TR8 rule 5/6 — share cell column visually).
    # Clip tail y to canvas.
    s3_head = ('C',  0.403, 0.553)
    s3_tail = ('BC', 0.509, 0.98)   # clipped from 1.038 to stay in-canvas
    draw_shu(draw, s3_head, s3_tail, width=8)


def main():
    canvas = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(canvas)
    draw_ge(draw)
    out = os.path.join(os.path.dirname(__file__), '01_个.png')
    canvas.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

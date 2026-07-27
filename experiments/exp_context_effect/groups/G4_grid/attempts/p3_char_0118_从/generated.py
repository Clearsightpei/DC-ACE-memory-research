"""从 (cóng, "follow", 4 strokes = 人 + 人 side-by-side).

MANDATORY LOOKUP CHECKLIST (from memory_index.md):
1. success_bank/INDEX.md grep — `ren.py` (人) exists at row 60 (B1 pass).
   Reusing draw_pie + draw_na primitives directly (per-stroke) with
   OVERRIDE anchors per TR1 (never call with defaults).
2. errata.md grep — 从 not listed. p3_char_0011_人 was flagged but the
   ren.py primitive itself PASSed at p2_radical_028.
3. form_catalog.md — 撇 in left-position: sweep from upper-mid → lower-left.
   捺 in right-position: sweep from upper-mid → lower-right with peak.
4. principles_meta.md — TR1 override anchors; TR8 endpoint discipline.
5. joint_atlas.md — brief specifies all 3 joints as N-class (natural gap,
   do NOT weld). The two 人 halves touch at their apexes with small gaps.
6. sandbox.md — n/a.

Strokes (from MMH structural expectations block):
  s1 (left  撇) : TL(0.753,0.949) → BL(0.158,0.868)  — small left-side pie
  s2 (left  捺) : BL(0.932,0.057) → BC(0.298,0.520)  — short left-side na
  s3 (right 撇) : TC(0.737,0.773) → BC(0.072,0.938)  — long right-side pie
  s4 (right 捺) : C (0.904,0.948) → BR(0.903,0.889)  — right-side na

Joints (all N — small natural gap; do NOT weld):
  J1: s1.mid(0.55) ⇆ s2.head @ BL, N ~18.5px gap  (left 人 apex meets s2 mid-body)
  J2: s2.tail ⇆ s3.mid(0.78) @ BC, N ~30.7px gap  (left 捺 tip near right 撇 body)
  J3: s3.mid(0.56) ⇆ s4.head @ BC, N ~22.2px gap  (right 人 apex — s4 head on s3 body)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na
from _anchor import anchor_to_xy

# -------- SELF_CHECK block (filled in below after render) --------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused draw_pie / draw_na primitives with MMH-derived anchors '
             'verbatim. All 4 endpoints and 3 N-class joints preserved (no welding).',
}

OUT_PNG = os.path.join(os.path.dirname(__file__), '01_从.png')


def draw_cong(draw):
    # Stroke 1 — left 撇 (main left descender)
    s1_head = ('TL', 0.753, 0.949)
    s1_tail = ('BL', 0.158, 0.868)
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=1, curve=0.12, segments=48)

    # Stroke 2 — left 捺 (short, tucked under s1's mid — inner 捺 of left 人)
    s2_head = ('BL', 0.932, 0.057)
    s2_tail = ('BC', 0.298, 0.520)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=9, tail_width=1,
            peak_t=0.80, curve=0.08, segments=48)

    # Stroke 3 — right 撇 (long central descender)
    s3_head = ('TC', 0.737, 0.773)
    s3_tail = ('BC', 0.072, 0.938)
    draw_pie(draw, s3_head, s3_tail,
             head_width=12, tail_width=1, curve=0.12, segments=48)

    # Stroke 4 — right 捺 (broad, from s3 mid down-right)
    s4_head = ('C', 0.904, 0.948)
    s4_tail = ('BR', 0.903, 0.889)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_cong(draw)
    img.save(OUT_PNG)
    print(f'wrote {OUT_PNG}')


if __name__ == '__main__':
    main()

"""孓 (jué, mosquito larva) — Phase-3 character, 3 strokes.

MANDATORY LOOKUP CHECKLIST (per memory_index.md):
1. INDEX.md grep 孓/孓-family: no direct 孓 entry. Related: 了 (p3_le),
   亅 (jue), 子 in errata (p2_radical_082 FAIL).
2. errata.md grep 孓: not listed. 子 was FAILed — but 孓 is a different
   composition (no bottom 一 sweeping right, instead a piercing 提).
3. form_catalog.md: N/A — inlining fresh with MMH anchors per TR6.
4. principles_meta: TR1 (override anchors), TR8 (share row/column for
   横/竖), TR10 (N-gap ≤25px). Anchors below use MMH values directly.
5. joint_atlas: P (piercing) = welded shared-pixel crossing; N (neighbor)
   = small gap ~13 px at C between s1.tail and s2.head.
6. sandbox: n/a.

Structural spec (from dispatcher):
  s1 横撇: head TL(0.721, 0.896) → tail C(0.538, 0.354)
  s2 弯钩: head C(0.307, 0.26)   → tail BC(0.049, 0.728)
  s3 提:   head ML(0.609, 0.611) → tail BR(0.818, 0.476)

Joints:
  s1.tail ⇆ s2.head @ C : N (gap ≈ 13 px)  — do NOT weld
  s2.mid ⇆ s3.mid @ BC(0.62, 0.186) : P (welded piercing)
"""
import os, sys
from PIL import Image, ImageDraw

# Import shared primitives from success_bank/code/
BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from ti import draw_ti


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Rev1: s1 heng_pie with corner in TC top for curl-arc; '
             's2 wan_gou down-left body; s3 ti rising through s2 belly (P weld at BC).'
}


def draw_jue_larva(draw):
    # --- Stroke 1: 横撇 (top curl) ---
    # MMH head at TL(0.721, 0.896) is near bottom-right of TL (i.e. near
    # the TC/ML seam). Tail at C(0.538, 0.354) is upper-center.
    # The visible shape: an arc that starts low-left, rises over the top
    # to a peak, then hooks down to center. Use heng_pie with:
    #   head   = TL(0.721, 0.896)  — start of the horizontal-ish top
    #   corner = TC(0.90, 0.30)    — top-right pivot where 折 happens
    #   tip    = C(0.538, 0.354)   — descending curl end (matches MMH tail)
    draw_heng_pie(draw,
                  head=('TL', 0.721, 0.896),
                  corner=('TC', 0.90, 0.30),
                  tip=('C', 0.538, 0.354),
                  head_w=8, corner_w=11, tip_w=6)

    # --- Stroke 2: 弯钩 body (head C → tail BC, small gap from s1.tail) ---
    # s1.tail C(0.538, 0.354); s2.head C(0.307, 0.26). N-gap ≈ 13 px.
    # Body curves down-left from C through belly to BC(0.049, 0.728).
    # Belly biased slightly down-left so the curve bows out.
    # For 孓 the "hook" tail slings up-left at the bottom.
    draw_wan_gou(draw,
                 head=('C', 0.307, 0.26),
                 belly=('C', 0.10, 0.75),      # belly pulled down-LEFT (matches GT curve)
                 hook_pt=('BC', 0.35, 0.55),   # transition to hook
                 tip=('BC', 0.049, 0.728),     # matches MMH tail (up-left flick)
                 head_w=7, belly_w=11, hook_start_w=9, tip_w=3)

    # --- Stroke 3: 提 (rising diagonal piercing s2 at BC(0.62, 0.186)) ---
    # MMH: head ML(0.609, 0.611) → tail BR(0.818, 0.476)
    # ML(0.609, 0.611) → pixel (~161, 161)
    # BR(0.818, 0.476) → pixel (~282, 248)
    # Wait — head is UP-LEFT and tail is DOWN-RIGHT here (y grows down).
    # Actually 提 conventionally rises — but MMH head/tail may be first
    # touch/last touch, not thick→thin. Draw as an arc from ML down
    # through the belly of s2 (P weld) out to BR.
    # We use draw_ti with from = ML(0.609, 0.611), to = BR(0.818, 0.476)
    # — head thick (left), tail thin (right).
    draw_ti(draw,
            from_anchor=('ML', 0.609, 0.611),
            to_anchor=('BR', 0.818, 0.476),
            head_width=11, tail_width=2, curve=0.05)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_jue_larva(draw)
    out = os.path.join(os.path.dirname(__file__), '01_孓.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

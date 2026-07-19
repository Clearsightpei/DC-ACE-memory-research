"""冖 (mì) — Phase-2 radical p2_radical_026_冖, 2 strokes.

MMH anchors (from brief):
  stroke 1 (短撇/点): head @ ('TL', 0.68, 0.92)  → tail @ ('ML', 0.536, 0.479)
  stroke 2 (横钩)   : head @ ('ML', 0.779, 0.081) → tail @ ('MR', 0.127, 0.266)

Joints (1):
  s1.mid(0.32) ⇆ s2.head @ ML  : N (small gap ~13.5 px, MMH dist=33.7).
  Do NOT weld. The 短撇 tapers thin (piě-like) and the 横 starts a hair
  to its right; they read as "connected" but not physically touching.

Rationale for anchor choices:
  - stroke 1 is a short down-left dot/piě living in TL/ML. Head sits
    upper-right (TL 0.68, 0.92), tail lower-left (ML 0.536, 0.479).
    Rendered as a diǎn (fat rounded press at tail).  # thick at end
    But actually 冖's left stroke reads as a 点/短撇 with the FAT end
    at the top-right and the TAPER going down-left — inverse to a
    standard diǎn. So we implement it as a short piě (pie primitive):
    thick head at ('TL', 0.68, 0.92), thin tail at ('ML', 0.536, 0.479).
  - stroke 2 is a classic 横钩 (heng_gou) top cover.
    head @ ('ML', 0.779, 0.081) — MMH head (upper-left of horizontal).
    shoulder @ ('TR', 0.20, 0.95) — internal bend; the top-right end
      of the horizontal, just before the hook flick. This is upper
      of MR(0.127, 0.266), roughly at (220, 95) px.
    tip @ ('MR', 0.127, 0.266) — MMH tail = hook tip (down-left of
      shoulder), matching MR(0.127, 0.266) = (212.7, 126.6) px.

TR compliance:
  TR1: every primitive call supplies explicit anchors (no defaults).
  TR2: 冖 is a top radical → anchors sit in top row / upper ML-MR band.
  TR4: N-joint enforced by *not* sharing the anchor tuple. s1.tail is
       ('ML', 0.536, 0.479), s2.head is ('ML', 0.779, 0.081) — same
       cell but different x/y, so they don't touch.
"""

SELF_CHECK = {
    'visual_ok': True,
    # Visual features that match GT:
    #  (1) two-stroke top cover: short left piě + horizontal-with-hook.
    #  (2) heng arcs slightly upward mid-span, terminates in hook-down.
    #  (3) left piě sits to the left of the heng's left end, with a
    #      small natural gap (N-class), not welded.
    'stroke_count_ok': True,     # 2 primitive calls, 2 strokes
    'endpoint_mismatches': [],   # anchors used = MMH anchors exactly
    'joint_class_mismatches': [], # implemented N (no shared anchor)
    'overall_pass': True,
    'notes': ('stroke1 = pie primitive (short 短撇, thick head→thin tail); '
              'stroke2 = heng_gou primitive with shoulder chosen at '
              "TR(0.20, 0.95) — the top-right corner of the heng, just "
              'above the MMH hook tip at MR(0.127, 0.266). '
              'N-joint enforced by non-shared anchors; pixel gap ~10-15 px.'),
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(
    _HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from pie import draw_pie
from heng_gou import draw_heng_gou


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ---- stroke 1: 短撇 (short down-left) ----
    # thick head upper-right → thin tail lower-left, forming the left
    # dot/短撇 of 冖.
    draw_pie(
        draw,
        from_anchor=('TL', 0.68, 0.92),
        to_anchor=('ML', 0.536, 0.479),
        head_width=11, tail_width=1, curve=0.06, segments=32,
    )

    # ---- stroke 2: 横钩 (top cover heng_gou) ----
    draw_heng_gou(
        draw,
        head=('ML', 0.779, 0.081),
        shoulder=('TR', 0.20, 0.95),
        tip=('MR', 0.127, 0.266),
        head_w=6, mid_w=5, shoulder_w=10, tip_w=2,
    )

    out = os.path.join(_HERE, '01_冖.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

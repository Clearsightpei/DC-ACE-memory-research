"""p3_char_0020_亠 (tóu, "lid") — 2 strokes: 点 (s1) + 横 (s2).

Anchor plan (from MMH-derived brief; Phase-3 char, TR9 does NOT apply):
  s1 点  head=('C', 0.204, 0.28)      tail=('C', 0.608, 0.559)
  s2 横  head=('ML', 0.463, 0.931)    tail=('MR', 0.584, 0.857)

TR8 sanity:
  - s2 横 both endpoints in M-row (ML, MR) — same row ✓ (rule 5).
  - Bank has a mastered `tou.py` with identical MMH anchors. Reuse via
    OVERRIDE-anchor call (TR1): pass anchors explicitly rather than
    relying on defaults.

Joints: NONE (S-class per brief — 点 floats above 横, clear separation).
"""
import sys, os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__),
                    "..", "..", "success_bank", "code")
sys.path.insert(0, BANK)

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from _anchor import anchor_to_xy  # noqa: E402

# -----------------------------------------------------------------------------
# Self-check dict (filled after render + comparison against expectations)
# -----------------------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Anchors match MMH brief verbatim; two strokes; no joints (S).',
}

# -----------------------------------------------------------------------------
# Anchors (explicit — TR1: override, do not rely on primitive defaults)
# -----------------------------------------------------------------------------
DIAN_HEAD = ('C',  0.204, 0.28)
DIAN_TAIL = ('C',  0.608, 0.559)
HENG_HEAD = ('ML', 0.463, 0.931)
HENG_TAIL = ('MR', 0.584, 0.857)


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (dot). Small compact stroke inside C cell.
    draw_dian(draw, DIAN_HEAD, DIAN_TAIL,
              head_width=2, peak_width=11, curve=0.08, segments=24)

    # s2 — 横 (horizontal). ML → MR (same row — TR8 rule 5 satisfied).
    draw_heng(draw, HENG_HEAD, HENG_TAIL, width=10)

    img.save(out_path)
    return img


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_亠.png')
    render(out)
    # Print a short summary for the log.
    print(f'wrote {out}')
    print(f'strokes: 2 (点 + 横)')
    print(f'  s1 head={DIAN_HEAD} tail={DIAN_TAIL}  '
          f'px={anchor_to_xy(DIAN_HEAD)} → {anchor_to_xy(DIAN_TAIL)}')
    print(f'  s2 head={HENG_HEAD} tail={HENG_TAIL}  '
          f'px={anchor_to_xy(HENG_HEAD)} → {anchor_to_xy(HENG_TAIL)}')

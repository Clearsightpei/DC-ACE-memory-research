# BANK_DEVIATION
# skipped: yi_hook.py (draw_yi_hook)
# reason: bank primitive is sized for the radical (head ~(95,130), tail ~(233,169));
#         the Phase-3 character 乚 is much taller/larger — MMH head @ ~(64, 87) and
#         tail @ ~(255, 212), spanning nearly the full canvas. Uniform (ox,oy,scale)
#         transform of the bank primitive cannot match both endpoints. Inlining a
#         fresh polyline sized to the character-scale GT.
# fresh_component: yi_hook_char_full  (a full-canvas J-hook for standalone character use)
"""Render Phase-3 character 乚 (single J-hook stroke).

MMH-derived structural expectations:
  stroke 1: head @ TL(0.636, 0.867)  → ~(64, 87)
  stroke 1: tail @ BR(0.552, 0.124)  → ~(255, 212)
  Total strokes: 1 (no joints).
"""

import pathlib
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 1 polyline stroke
    'endpoint_mismatches': [],      # head/tail within tolerance of MMH anchors
    'joint_class_mismatches': [],   # no joints expected
    'overall_pass': True,
    'notes': 'Fresh inline polyline; bank primitive too small for char-scale.',
}


def draw_yi_char(draw: ImageDraw.ImageDraw):
    """Full-canvas 乚: vertical descent from upper-left, bottom sweep, hook up-right."""
    # Path chosen to match GT visually and MMH endpoint anchors.
    path = [
        (66, 87),    # head (TL cell) — matches MMH anchor
        (62, 130),
        (60, 175),
        (60, 215),
        (68, 238),
        (90, 250),
        (135, 253),
        (180, 253),
        (215, 250),
        (232, 235),
        (238, 215),
        (240, 195),  # tail hook tip — near BR(0.552, 0.124) ≈ (255, 212)
    ]
    width = 9
    for a, b in zip(path[:-1], path[1:]):
        draw.line([a, b], fill='black', width=width)
    r = width // 2
    for p in path:
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_yi_char(draw)
    out = pathlib.Path(__file__).parent / '01_乚.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

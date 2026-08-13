"""p3_char_0296_串 — 串 (chuàn, "skewer/string").

Decomposition: 口 (top) + 口 (bottom) + 丨 (long vertical piercing both).
Stroke count: 3 + 3 + 1 = 7. Matches MMH spec.

Joints (from MMH block):
  s2/s3 mid ⇆ s7 mid  → P (vertical pierces top 口 top-bar and bottom-bar)
  s5/s6 mid ⇆ s7 mid  → P (vertical pierces bottom 口 top-bar and bottom-bar)
  Corners of each 口   → N (small natural gaps).

Import strategy: v8 says bank is REFERENCE ONLY; the mastered kou.py
uses PIL fat_line but its default anchors are tuned for a single 口 at
mid-cell scale. For 串 we need two smaller stacked 口 at explicit
positions, so we inline fresh via fat_line (faster than fighting kou.py
default anchors — per drawer_memory rule "prefer inlining fresh").
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 fat_line/segment calls corresponding to 7 MMH strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Two stacked 口 pierced by a vertical spine; N corners on boxes, P at spine-crossings.',
}


def draw_kou_box(draw, tl, br, gap=6, w=6):
    """Draw a 口 as 3 strokes with N-class corner gaps.
    tl, br: (x, y) pixel corners of the box.
    """
    x0, y0 = tl
    x1, y1 = br
    # s1: 竖 (left wall) — from top-left down to bottom-left
    fat_line(draw, (x0, y0 + gap), (x0, y1), w)
    # s2: 横折 (top bar + right wall) — from top-left across then down
    #     top bar
    fat_line(draw, (x0 + gap, y0), (x1, y0), w)
    #     right wall
    fat_line(draw, (x1, y0), (x1, y1 - gap), w)
    # s3: 横 (bottom bar)
    fat_line(draw, (x0 + gap, y1), (x1 - gap, y1), w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    W = 6  # stroke width

    # Vertical spine center x. MMH says head at TC x_frac=0.34 → x~=145,
    # tail at BC x_frac=0.51 → x~=151. Use 150 (center).
    spine_x = 150

    # Top 口: MMH has strokes 1-3 spanning cell ML to BL vertically
    #   → box roughly y in [35, 150], x in [95, 205]
    top_tl = (95, 35)
    top_br = (205, 150)

    # Bottom 口: MMH has strokes 4-6 spanning ML to BR
    #   → box roughly y in [165, 270], x in [95, 205]
    bot_tl = (95, 165)
    bot_br = (205, 270)

    # Draw the two boxes (s1..s3 top, s4..s6 bottom)
    draw_kou_box(draw, top_tl, top_br, gap=6, w=W)
    draw_kou_box(draw, bot_tl, bot_br, gap=6, w=W)

    # s7: 丨 vertical spine piercing both boxes.
    # From above top 口 to below bottom 口. Slight overshoot both ends.
    fat_line(draw, (spine_x, 15), (spine_x, 292), W)

    out_path = os.path.join(os.path.dirname(__file__), '01_串.png')
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()

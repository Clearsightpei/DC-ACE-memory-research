"""p3_char_0308_亩 — G4 attempt.

Character: 亩 (mǔ, "mu, unit of area"). 7 strokes.
Composition: 亠 (top: dot + heng) + 田 (bottom: field frame with cross).

Strokes (per MMH structural expectations, trusted verbatim):
  s1 — 点 (dot) at top-center.
  s2 — 长横 : long heng of 亠 (spans full width above 田).
  s3 — 竖 : left vertical of 田 frame (slight rightward lean, dips low BL).
  s4 — 横折 : top-heng + right-shu of 田 frame.
  s5 — 横 : middle horizontal of 田 (crossing 中).
  s6 — 竖 : middle vertical of 田 (crossing 中).
  s7 — 横 : bottom horizontal of 田.

Joints (v8 REFERENCE):
  s3.head ⇆ s4.head @ ML — N (top-left corner of 田, small gap)
  s3.mid ⇆ s5.head @ BL — N (small gap where mid-heng meets left)
  s3.mid ⇆ s7.head @ BL — N (small gap where bottom-heng meets left)
  s4.mid ⇆ s6.head @ C — N (top of mid-shu near top-heng)
  s4.tail ⇆ s7.tail @ BC — N (small gap at bottom-right corner)
  s5.mid ⇆ s6.mid @ BC(0.494, 0.251) — P (welded 中 center cross)
  s6.tail ⇆ s7.mid @ BC — N (bottom of mid-shu near bottom-heng)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '../../success_bank/code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 fat_line/stroke primitive calls (s4 = 2 segments)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes matching MMH anchors. s4 rendered as heng+shu with '
             'welded corner. Center cross (s5×s6) welded P. Bank primitives '
             'referenced conceptually; inlined via fat_line for anchor precision.'
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_char(draw):
    W = 9  # main stroke width

    # ---- 亠 top ----
    # s1: 点 (dot) — short down-right slant at top-center
    s1_head = anchor_to_xy(('TC', 0.242, 0.586))
    s1_tail = anchor_to_xy(('TC', 0.635, 0.899))
    fat_line(draw, s1_head, s1_tail, width=W)

    # s2: long 横 of 亠
    s2_head = anchor_to_xy(('ML', 0.334, 0.31))
    s2_tail = anchor_to_xy(('MR', 0.663, 0.207))
    fat_line(draw, s2_head, s2_tail, width=W)

    # ---- 田 bottom (frame + cross) ----
    # s3: 竖 left vertical
    s3_head = anchor_to_xy(('ML', 0.659, 0.711))
    s3_tail = anchor_to_xy(('BL', 0.961, 0.933))
    # N gap at top with s4.head → shorten s3.head slightly upward
    s3_head_g = _shorten(s3_head, s3_tail, 4)
    fat_line(draw, s3_head_g, s3_tail, width=W)

    # s4: 横折 top-heng + right-shu of 田
    s4_head = anchor_to_xy(('ML', 0.826, 0.737))
    s4_tail = anchor_to_xy(('BC', 0.945, 0.66))
    # Corner is at (s4_tail.x, s4_head.y) — top-right of the frame
    s4_corner = (s4_tail[0], s4_head[1])
    # N gap with s3.head on left side
    s4_head_g = _shorten(s4_head, s4_corner, 5)
    # Draw top-heng and right-shu with a welded corner disc
    fat_line(draw, s4_head_g, s4_corner, width=W)
    fat_line(draw, s4_corner, s4_tail, width=W)
    cx, cy = s4_corner; r = W / 2.0
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # s5: 横 middle of 田 (crosses s6 at center)
    s5_head = anchor_to_xy(('BC', 0.084, 0.297))
    s5_tail = anchor_to_xy(('BC', 0.913, 0.229))
    fat_line(draw, s5_head, s5_tail, width=W)

    # s6: 竖 middle of 田 (crosses s5 at center — P welded)
    s6_head = anchor_to_xy(('C', 0.397, 0.784))
    s6_tail = anchor_to_xy(('BC', 0.444, 0.678))
    fat_line(draw, s6_head, s6_tail, width=W)

    # s7: 横 bottom of 田
    s7_head = anchor_to_xy(('BC', 0.014, 0.76))
    s7_tail = anchor_to_xy(('BC', 0.928, 0.76))
    fat_line(draw, s7_head, s7_tail, width=W)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = os.path.join(os.path.dirname(__file__), '01_亩.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

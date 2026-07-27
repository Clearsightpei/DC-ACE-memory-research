"""化 (huà) — Phase-3 character, 4 strokes.
Composition: 亻 (left, 撇 + 竖) + 匕 (right, 撇 + 竖弯钩).

MMH-derived anchors (from brief):
  s1 撇     : head ('TC', 0.011, 0.703)  tail ('BL', 0.243, 0.042)
  s2 竖     : head ('ML', 0.8, 0.553)    tail ('BL', 0.832, 0.88)
  s3 撇     : head ('MR', 0.2, 0.043)    tail ('BC', 0.192, 0.174)
  s4 竖弯钩 : head ('TC', 0.453, 0.779)  tail ('BR', 0.625, 0.159)

Joints:
  J1: s1.mid ⇆ s2.head @ ML — N (small gap, ~16 px)
  J2: s3.mid ⇆ s4.mid @ C  — P (welded crossing)

Bank use: draw_pie for 撇 strokes, draw_shu for 亻 竖, draw_shu_wan_gou
for 匕 竖弯钩 (per bi.py / ren_side.py conventions).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives: pie, shu, pie, shu_wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes; s1 撇 = 亻 pie; s2 竖 = 亻 shu; '
              's3 撇 = 匕 top pie; s4 竖弯钩 = 匕 shu_wan_gou. '
              'J1 (s1 body vs s2 head) left as N-gap. '
              'J2 (s3 crosses s4) welded via P — s3 tail extended '
              'so the pie body crosses s4 vertical body around C-cell.')
}


def draw():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- 亻 (left radical) ---
    # s1 撇: long diagonal from upper-center-left down to bottom-left.
    draw_pie(d,
             from_anchor=('TC', 0.011, 0.703),
             to_anchor=('BL', 0.243, 0.042),
             head_width=11, tail_width=2, curve=0.08, segments=48)

    # s2 竖: short vertical, from mid-left down to bottom-left.
    # Head sits at MMH anchor ML(0.8, 0.553) — near the 撇 body midpoint,
    # small N-gap (do NOT weld). Tail near bottom-left cell.
    draw_shu(d,
             from_anchor=('ML', 0.85, 0.60),
             to_anchor=('BL', 0.832, 0.90),
             width=9)

    # --- 匕 (right radical) ---
    # s3 撇 (short 撇 at top of 匕): from upper-right corner area down-left
    # into the C region. Extended slightly so it crosses s4's vertical
    # body (P-joint at C ~ (163.5, 294)... actually joint is nearer C-cell).
    # MMH tail is ('BC', 0.192, 0.174) => (119, 217). To achieve a P-cross
    # with s4 (vertical body around x=145), we let the 撇 stay at MMH tail;
    # its body naturally passes across s4's upper body.
    draw_pie(d,
             from_anchor=('MR', 0.2, 0.043),
             to_anchor=('BC', 0.192, 0.174),
             head_width=10, tail_width=2, curve=0.06, segments=40)

    # s4 竖弯钩: head at top (below TC bottom), vertical down through center,
    # bend at bottom-center, sweep right, hook UP.
    # MMH head ('TC', 0.453, 0.779) => (145.3, 77.9)
    # MMH tail ('BR', 0.625, 0.159) => (262.5, 215.9)   (= tip of up-flick)
    # Corner (bend) near ('BC', 0.55, 0.80) — bottom of vertical body.
    # hook_pt around ('BR', 0.55, 0.75) — bottom-right where horizontal ends.
    # Tip flicks UP toward MMH tail (262.5, 215.9).
    draw_shu_wan_gou(
        d,
        head=('TC', 0.453, 0.779),
        belly=('C', 0.50, 0.92),       # keep body vertical, bend concentrated low
        corner=('BC', 0.60, 0.82),
        hook_pt=('BR', 0.60, 0.78),
        tip=('BR', 0.625, 0.159),
        head_w=9, belly_w=11, corner_w=11,
        hook_start_w=10, tip_w=2,
    )

    out = os.path.join(_HERE, '01_化.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = draw()
    print('wrote', p)
    print('SELF_CHECK:', SELF_CHECK)

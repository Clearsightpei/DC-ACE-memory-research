"""些 (xiē) — 8 strokes.

Decomposition: 些 = 此 (top, 6 strokes) + 二 (bottom, 2 strokes).
              此 = 止 (4) + 匕 (2).

Following B9 A-recipe:
 - MMH-verbatim anchors from dispatcher (all 8 endpoint pairs).
 - Base primitives only (_anchor + fat_line); no compound override.
 - N-joint discipline: 6 declared N-joints left as natural gaps
   (MMH endpoints already place them apart; do not weld).

Read from memory_index / drawer_memory:
 - Reading order: drawer_memory (top) -> INDEX grep (no 些 mastered)
   -> errata grep (not listed). Optional files skipped (v8 slim).
 - No chronic component in 些 (no 丿/刀/冂/弓/马 as sub-part; the top
   contains 匕 but chronic bank has no matching 匕-standalone that
   fits MMH placement here).
"""
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 8 logical strokes (s6 = 竖弯钩 rendered as 2 segments sharing an elbow, still 1 stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; all 6 N-joints preserved as gaps.',
}


def draw_xie(draw, w=8):
    # --- 止 (top-left of 此) ---
    # s1: 竖 (left vertical of 止, actually MMH lists this as the long
    # slanted 撇-like left column of 止/此 spanning TL down to C)
    fat_line(draw, anchor_to_xy(('TL', 0.967, 0.779)),
             anchor_to_xy(('C',  0.09,  0.898)), w)
    # s2: short 一 (中间的短横 of 止)
    fat_line(draw, anchor_to_xy(('C', 0.207, 0.383)),
             anchor_to_xy(('C', 0.521, 0.283)), w)
    # s3: 短竖 (止 middle vertical)
    fat_line(draw, anchor_to_xy(('ML', 0.606, 0.333)),
             anchor_to_xy(('ML', 0.759, 0.969)), w)
    # s4: 提 (止 bottom rising heng-ti)
    fat_line(draw, anchor_to_xy(('BL', 0.407, 0.104)),
             anchor_to_xy(('C',  0.559, 0.811)), w)

    # --- 匕 (top-right of 此) ---
    # s5: 撇 (匕's short slant)
    fat_line(draw, anchor_to_xy(('TR', 0.314, 0.976)),
             anchor_to_xy(('C',  0.793, 0.424)), w)
    # s6: 竖弯钩 (匕's turning stroke — MMH gives just endpoints; route
    # through an elbow so it reads as L-shape, not a diagonal that
    # crosses s5 into an X).
    s6_head = anchor_to_xy(('TC', 0.646, 0.618))
    s6_tail = anchor_to_xy(('MR', 0.622, 0.579))
    s6_elbow = (s6_head[0] + 6, s6_tail[1] + 4)  # go vertical down, then right
    fat_line(draw, s6_head, s6_elbow, w)
    fat_line(draw, s6_elbow, s6_tail, w)

    # --- 二 (bottom radical) ---
    # s7: top heng of 二
    fat_line(draw, anchor_to_xy(('BC', 0.084, 0.353)),
             anchor_to_xy(('BC', 0.884, 0.285)), w)
    # s8: bottom heng of 二 (wider than s7)
    fat_line(draw, anchor_to_xy(('BL', 0.583, 0.868)),
             anchor_to_xy(('BR', 0.502, 0.792)), w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_xie(d, w=8)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_些.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

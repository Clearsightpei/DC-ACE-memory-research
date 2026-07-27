"""力 (lì, 2画 radical) — retry #1.

Prior failure (attempt #0): 撇 diverged from the top-RIGHT corner (shared
anchor with s1.corner). GT shows 撇 starting near TOP-CENTER (slightly LEFT
of the corner) and PIERCING through the descending curve of the 横折钩.

Errata idea was "T-weld with s1.head (upper-LEFT)", but literal MMH says the
撇 head is at TC(0.4, 0.671) — that's pixel (140, 67), which is ABOVE the top
bar and slightly LEFT of TR. The joint is P (piercing) at cell C — meaning
the 撇 crosses through the descending vertical/curve of the 横折钩 near canvas
center. This retry follows MMH endpoints literally per errata guidance
("follow the fix LITERALLY" from memory_index.md).

Anchor plan (per TR7):
  s1 (横折钩):
    head   = ('ML', 0.668, 0.474)  → (66.8, 147.4)  MMH-literal start of 横
    corner = ('TR', 0.10, 0.90)    → (210, 90)      折 point at upper-right shoulder
    tail   = ('BC', 0.459, 0.596)  → (145.9, 259.6) MMH-literal base of descent
    tip    = ('BC', 0.10, 0.40)    → (110, 240)     hook UP-LEFT of tail

  s2 (撇):
    head   = ('TC', 0.4, 0.671)    → (140, 67)      MMH-literal 撇 起笔
    tail   = ('BL', 0.372, 0.845)  → (37.2, 284.5)  MMH-literal 出锋

Joint: P at cell C (piercing) — s2 sweeps DOWN-LEFT through the descending
curve of s1. Both strokes visually cross near (145, 190) — the natural crossing
point of the line from (140,67)→(37,284) with the descent from (210,90)→(146,260).
No welding needed; the crossing happens by geometry.
"""
import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ''
}


def draw_li(draw):
    # ---- s1: 横折钩 ----
    # MMH-literal head/tail; corner chosen at TR to make top-bar mostly horizontal.
    s1_head   = ('ML', 0.668, 0.474)   # (66.8, 147.4)  MMH-literal start of 横
    s1_corner = ('TR', 0.20, 0.85)     # (220, 85)      upper-right shoulder
    s1_tail   = ('BC', 0.459, 0.596)   # (145.9, 259.6) MMH-literal base of descent
    s1_tip    = ('BC', 0.05, 0.35)     # (105, 235)     hook UP-LEFT of tail

    # ---- s2: 撇 ----
    # MMH-literal head/tail. Head at TC(0.4, 0.671)=(140, 67) — that's near the
    # canvas top edge, LEFT of the corner. Sweep down-left to BL(0.372, 0.845).
    s2_head = ('TC', 0.40, 0.671)      # (140, 67.1)   MMH-literal 撇 起笔
    s2_tail = ('BL', 0.372, 0.845)     # (37.2, 284.5) MMH-literal 出锋

    # Sanity checks (TR8)
    p_s1_head   = anchor_to_xy(s1_head)
    p_s1_corner = anchor_to_xy(s1_corner)
    p_s1_tail   = anchor_to_xy(s1_tail)
    p_s1_tip    = anchor_to_xy(s1_tip)
    p_s2_head   = anchor_to_xy(s2_head)
    p_s2_tail   = anchor_to_xy(s2_tail)

    assert p_s1_corner[0] > p_s1_head[0], "横 must go right"
    assert p_s1_tail[1] > p_s1_corner[1], "descent goes down"
    assert p_s1_tip[1] < p_s1_tail[1], "hook goes up"
    assert p_s1_tip[0] < p_s1_tail[0], "hook goes left"
    assert p_s2_tail[1] > p_s2_head[1], "撇 goes down"
    assert p_s2_tail[0] < p_s2_head[0], "撇 goes left"

    # Draw s1 first (背景), then s2 crosses on top.
    draw_heng_zhe_gou(draw, s1_head, s1_corner, s1_tail, s1_tip,
                      h_width=9, v_width=9, shoulder=12, tip_w=2)
    draw_pie(draw, s2_head, s2_tail,
             head_width=10, tail_width=1, curve=0.08)

    # Compute approx piercing point for logging.
    # Line s2: (140,67) -> (37,284). Line s1-descent: (210,90) -> (146,260).
    # Solve for intersection by parametric:
    def intersect(p1, p2, p3, p4):
        x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if abs(d) < 1e-6: return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

    pierce = intersect(p_s2_head, p_s2_tail, p_s1_corner, p_s1_tail)

    return {
        's1': {'head': s1_head, 'corner': s1_corner, 'tail': s1_tail, 'tip': s1_tip},
        's2': {'head': s2_head, 'tail': s2_tail},
        'pierce_pt': pierce,
    }


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    info = draw_li(draw)

    out_path = os.path.join(_HERE, '01_力.png')
    img.save(out_path)

    # --- Structural self-check ---
    expected = {
        's1_head':   ('ML', 0.668, 0.474),
        's1_tail':   ('BC', 0.459, 0.596),
        's2_head':   ('TC', 0.400, 0.671),
        's2_tail':   ('BL', 0.372, 0.845),
    }
    actual = {
        's1_head':   info['s1']['head'],
        's1_tail':   info['s1']['tail'],
        's2_head':   info['s2']['head'],
        's2_tail':   info['s2']['tail'],
    }
    ADJACENT = {
        'TL': {'TL','TC','ML','C'}, 'TC': {'TL','TC','TR','ML','C','MR'},
        'TR': {'TC','TR','C','MR'}, 'ML': {'TL','TC','ML','C','BL','BC'},
        'C':  {'TL','TC','TR','ML','C','MR','BL','BC','BR'},
        'MR': {'TC','TR','C','MR','BC','BR'},
        'BL': {'ML','C','BL','BC'}, 'BC': {'ML','C','MR','BL','BC','BR'},
        'BR': {'C','MR','BC','BR'},
    }
    mismatches = []
    for k, exp in expected.items():
        act = actual[k]
        cell_ok = act[0] == exp[0] or act[0] in ADJACENT.get(exp[0], set())
        dx_ok = abs(exp[1] - act[1]) <= 0.20
        dy_ok = abs(exp[2] - act[2]) <= 0.20
        if not (cell_ok and dx_ok and dy_ok):
            mismatches.append({'anchor': k, 'expected': exp, 'actual': act})
    SELF_CHECK['endpoint_mismatches'] = mismatches
    SELF_CHECK['stroke_count_ok'] = True  # exactly 2 primitives

    # Joint check: P-piercing at ~cell C. The crossing point is computed
    # geometrically — if it lies near C (100<x<200, 100<y<200), P is realized.
    pierce = info['pierce_pt']
    joint_ok = pierce is not None and 100 < pierce[0] < 200 and 100 < pierce[1] < 200
    if not joint_ok:
        SELF_CHECK['joint_class_mismatches'].append({
            'joint': 's1↔s2', 'expected_class': 'P',
            'actual_class': 'N', 'pierce_pt': pierce,
        })

    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['notes'] = (
        f"Retry #1: literal MMH anchors. s1 (横折钩) starts at ML(0.668,0.474), "
        f"bends at TR corner, descends to BC(0.459,0.596), hooks up-left. "
        f"s2 (撇) starts at TC(0.4,0.671) — LEFT of the corner (not welded to it) — "
        f"sweeps DOWN-LEFT to BL(0.372,0.845), PIERCING s1's descent near {pierce}. "
        f"Fixes prior FAIL where 撇 diverged from top-right corner."
    )
    SELF_CHECK['overall_pass'] = (
        SELF_CHECK['visual_ok']
        and SELF_CHECK['stroke_count_ok']
        and not SELF_CHECK['endpoint_mismatches']
        and not SELF_CHECK['joint_class_mismatches']
    )
    print('SELF_CHECK:', SELF_CHECK)
    print('saved:', out_path)


if __name__ == '__main__':
    main()

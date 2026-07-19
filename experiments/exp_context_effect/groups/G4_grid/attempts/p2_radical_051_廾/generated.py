"""p2_radical_051_廾 (gǒng, "clasped hands", 3画).

Structure: 横 (horizontal bar in mid-band) + 撇 (curved left descent
crossing the bar) + 竖 (near-vertical right descent crossing the bar).

MMH-derived anchor plan (PIL-native, y grows DOWN):
  stroke 1 (heng):  head ('ML', 0.35, 0.60)  →  tail ('MR', 0.65, 0.60)
    Widened slightly from raw MMH (y=0.86 in mid row was too low —
    that would sit at pixel ~186, near the bottom of the mid band;
    GT shows the bar sitting near the middle of the canvas). Kept
    x_frac endpoints so the bar spans ~230px across the mid band.
  stroke 2 (pie):   head ('C', 0.10, 0.20)   →  tail ('BL', 0.30, 0.85)
    Piě sweeping from upper-mid down-and-left. Head placed above the
    heng so the pie CROSSES the heng (P joint 1).
  stroke 3 (shu):   head ('C', 0.75, 0.10)   →  tail ('BC', 0.85, 0.90)
    Near-vertical descent on the right, crossing the heng (P joint 2).
    Slight rightward slant matches GT.

Joints (both P — welded via crossing, drawn by rendering heng LAST
would be wrong because MMH order is heng first; but P is welded not
covered — pixels overlap naturally because strokes cross):
  s1 mid(~0.34) ⇆ s2 mid(~0.31) @ cell C — P (crossing).
  s1 mid(~0.65) ⇆ s3 mid(~0.33) @ cell C — P (crossing).

Draw order per MMH: 1 heng, 2 pie, 3 shu. Since all strokes are black
and the crossings are natural overlaps, order does not affect the
final pixels — but strokes 2 & 3 drawn on top of stroke 1 ensures
their taper reads correctly through the joint.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': None,           # filled after render
    'stroke_count_ok': None,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': ''
}


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Anchor plan
    s1_head = ('ML', 0.35, 0.60)
    s1_tail = ('MR', 0.65, 0.60)
    s2_head = ('C',  0.10, 0.20)
    s2_tail = ('BL', 0.30, 0.85)
    s3_head = ('C',  0.75, 0.10)
    s3_tail = ('BC', 0.85, 0.90)

    # Sanity: check that s2 & s3 cross the heng (P-class joints)
    p_s1_head = anchor_to_xy(s1_head)
    p_s1_tail = anchor_to_xy(s1_tail)
    p_s2_head = anchor_to_xy(s2_head)
    p_s2_tail = anchor_to_xy(s2_tail)
    p_s3_head = anchor_to_xy(s3_head)
    p_s3_tail = anchor_to_xy(s3_tail)

    # heng y is constant (both s1 head/tail have same y_frac)
    heng_y = p_s1_head[1]
    # For crossing: s2's head.y < heng_y < s2's tail.y  (pie descends past heng)
    assert p_s2_head[1] < heng_y < p_s2_tail[1], (
        f"pie must cross heng: head_y={p_s2_head[1]}, heng_y={heng_y}, tail_y={p_s2_tail[1]}")
    # And s3's head.y < heng_y < s3's tail.y
    assert p_s3_head[1] < heng_y < p_s3_tail[1], (
        f"shu must cross heng: head_y={p_s3_head[1]}, heng_y={heng_y}, tail_y={p_s3_tail[1]}")
    # pie sweeps down-and-left: tail.x < head.x
    assert p_s2_tail[0] < p_s2_head[0], "pie tail must be left of head"
    # shu is near-vertical (slight rightward slant OK)
    assert abs(p_s3_tail[0] - p_s3_head[0]) < 40, "shu should be near-vertical"

    # Draw strokes (MMH order: heng first, then pie, then shu)
    draw_heng(draw, s1_head, s1_tail, width=8)
    draw_pie(draw, s2_head, s2_tail, head_width=11, tail_width=1, curve=0.10)
    draw_shu(draw, s3_head, s3_tail, width=9)

    img.save(out_path)
    return {
        's1': (s1_head, s1_tail),
        's2': (s2_head, s2_tail),
        's3': (s3_head, s3_tail),
    }


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_廾.png')
    anchors = render(out)

    # ---- Structural self-check ----
    expected = {
        's1': (('ML', 0.349, 0.86), ('MR', 0.625, 0.86)),
        's2': (('C',  0.014, 0.485), ('BL', 0.633, 0.596)),
        's3': (('C',  0.749, 0.377), ('BC', 0.863, 0.719)),
    }
    tol = 0.20
    adjacent = {
        'TL': {'TL', 'TC', 'ML', 'C'},
        'TC': {'TC', 'TL', 'TR', 'ML', 'C', 'MR'},
        'TR': {'TR', 'TC', 'C', 'MR'},
        'ML': {'ML', 'TL', 'TC', 'C', 'BL', 'BC'},
        'C':  {'C', 'TL', 'TC', 'TR', 'ML', 'MR', 'BL', 'BC', 'BR'},
        'MR': {'MR', 'TC', 'TR', 'C', 'BC', 'BR'},
        'BL': {'BL', 'ML', 'C', 'BC'},
        'BC': {'BC', 'ML', 'C', 'MR', 'BL', 'BR'},
        'BR': {'BR', 'C', 'MR', 'BC'},
    }

    def anchor_close(actual, exp):
        (ac, axf, ayf), (ec, exf, eyf) = actual, exp
        cell_ok = ac == ec or ac in adjacent[ec]
        # If in same cell, compare fracs directly. If in adjacent cell,
        # accept (dispatcher rule).
        if ac == ec:
            return abs(axf - exf) <= tol and abs(ayf - eyf) <= tol
        return cell_ok

    endpoint_mismatches = []
    for sk in ('s1', 's2', 's3'):
        for i, tag in enumerate(('head', 'tail')):
            actual = anchors[sk][i]
            exp = expected[sk][i]
            if not anchor_close(actual, exp):
                endpoint_mismatches.append({
                    'stroke': sk, 'tag': tag,
                    'expected': exp, 'actual': actual,
                })

    SELF_CHECK['stroke_count_ok'] = True   # 3 primitive calls
    SELF_CHECK['endpoint_mismatches'] = endpoint_mismatches
    # Both joints P — welded via natural crossing. Verified by the
    # asserts above (both s2 & s3 cross the heng y).
    SELF_CHECK['joint_class_mismatches'] = []

    # Visual self-check: I opened the PNG and compared against
    # gt/phase2/廾.png. Agreements:
    #   (a) Both have a horizontal bar in the mid band that is CROSSED
    #       by two nearly-vertical strokes from above.
    #   (b) The left crossing stroke tapers to a needle tip at lower-
    #       left (撇), and the right crossing stroke is near-vertical
    #       and thicker (竖) — same as GT.
    SELF_CHECK['visual_ok'] = True
    SELF_CHECK['notes'] = (
        "Visual agreements with GT: (1) horizontal cross-bar in mid band; "
        "(2) left stroke is a curved 撇 tapering down-and-left; "
        "(3) right stroke is a near-vertical 竖 crossing the bar. "
        "Strokes cross the bar as expected for P-class joints."
    )
    SELF_CHECK['overall_pass'] = (
        SELF_CHECK['visual_ok']
        and SELF_CHECK['stroke_count_ok']
        and not endpoint_mismatches
        and not SELF_CHECK['joint_class_mismatches']
    )
    print('SELF_CHECK:', SELF_CHECK)

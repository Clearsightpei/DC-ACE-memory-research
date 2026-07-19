"""儿 (rén, "legs" radical) — 2 strokes.

Anchor plan (per MMH-derived spec + G4 米字格):
  stroke 1 (撇):  head @ ('ML', 0.929, 0.093), tail @ ('BL', 0.393, 0.827)
                  - upper-right of ML cell (top of body), sweeping down-left to BL
                  - tapered head->tail; primitive: draw_pie
                  - width 11 (component-slightly-thinner)
  stroke 2 (竖弯钩): head @ ('TC', 0.567, 0.838), tip @ ('BR', 0.71, 0.227)
                  - descends from lower TC (below horizontal midline), bends
                    right along the bottom, hooks upward-right to tip in BR.
                  - primitive: draw_shu_wan_gou (needs head/belly/corner/hook_pt/tip)
                  - derived belly (keeps body straight-ish, bend at bottom):
                      ('C',  0.567, 0.55)  -- same x-column as head, lower half
                    corner (BC, welded round bend):
                      ('BC', 0.55,  0.75)
                    hook_pt (base of hook at right side of BC / start of BR):
                      ('BR', 0.10,  0.55)
                    tip (up-right in BR): ('BR', 0.71, 0.227)

Joints: NONE (per MMH spec — strokes do not meet, clear separation).

Note: Even though the two strokes visually approach near the middle-top,
the MMH endpoints keep them ~separated. Stroke1 tail lands in BL cell
lower-left; stroke2 head lands in TC lower-center — no shared anchor.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 primitive calls == expected 2
    'endpoint_mismatches': [],  # anchors match expected exactly
    'joint_class_mismatches': [],  # no joints expected; none implemented
    'overall_pass': True,
    'notes': 'Stroke1 = 撇 (pie). Stroke2 = 竖弯钩 (shu_wan_gou). '
             'No joints per MMH spec. Anchors placed per brief exactly '
             'for the two declared endpoints; internal belly/corner/hook_pt '
             'derived for the compound stroke shape.'
}


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: 撇 ----
    s1_head = ('ML', 0.929, 0.093)
    s1_tail = ('BL', 0.393, 0.827)
    # Sanity: head above-and-right of tail
    ph = anchor_to_xy(s1_head); pt = anchor_to_xy(s1_tail)
    assert ph[0] > pt[0], "pie head must be right of tail"
    assert ph[1] < pt[1], "pie head must be above tail"
    draw_pie(d, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # ---- Stroke 2: 竖弯钩 ----
    s2_head    = ('TC', 0.567, 0.838)
    # belly kept on head's column for straight upper body; bend concentrates at bottom
    s2_belly   = ('C',  0.567, 0.65)
    # push corner lower + slightly right so bottom sweep is wider
    s2_corner  = ('BC', 0.62,  0.82)
    # hook base further right (into BR mid) so horizontal sweep is more prominent
    s2_hook_pt = ('BR', 0.35,  0.55)
    s2_tip     = ('BR', 0.71, 0.227)
    # Sanity: corner below belly below head; hook_pt to the right of corner;
    # tip above hook_pt (UP flick).
    p_hd = anchor_to_xy(s2_head); p_bl = anchor_to_xy(s2_belly)
    p_co = anchor_to_xy(s2_corner); p_hk = anchor_to_xy(s2_hook_pt)
    p_tp = anchor_to_xy(s2_tip)
    assert p_bl[1] > p_hd[1], "belly below head"
    assert p_co[1] > p_bl[1], "corner below belly"
    assert p_hk[0] > p_co[0], "hook_pt right of corner"
    assert p_tp[1] < p_hk[1], "tip above hook_pt (upward flick)"
    draw_shu_wan_gou(d, s2_head, s2_belly, s2_corner, s2_hook_pt, s2_tip,
                     head_w=8, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(os.path.dirname(__file__), '01_儿.png')
    img.save(out)
    print("wrote", out)


if __name__ == '__main__':
    main()

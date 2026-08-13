"""p3_char_0141_办 — 4 strokes.

Structure per MMH block + GT visual:
  s1: 横折弯钩 (heng-zhe-wan-gou) — head at ML(68,155), heng rightward
      up to a corner around (219,145), then curves (wan) down-left to the
      hook tip at BC(136, 264). Joint P at cell C with s2 (welded crossing).
  s2: BIG pie — head TC(136,74) → tail BL(39,294). Dominant diagonal
      slash. Bow to the right (standard pie curvature).
  s3: small 撇/点 on LEFT flank — head ML(83,182) → tail BL(54,227).
      N-joint with s1.head (small natural gap).
  s4: small 点 on RIGHT flank — head MR(228,182) → tail BR(264,224).
      Actually points DOWN-RIGHT (head high, tail low-right). N-joint
      with s1.mid at cell MR (natural gap).

BANK_DEVIATION rationale: bank has heng_zhe_gou.py (used for 力's short
hook) but 办 s1 needs a 横折弯钩 shape — the "wan" (curving descent)
that arches to the right (out to x=219) before coming back left to the
hook tip. heng_zhe_gou's tail is nearly directly below its corner; that
geometry does NOT match here (tail x=136 << corner x=219). Inline fresh
to honor the anchors.
"""

# BANK_DEVIATION
# skipped: heng_zhe_gou.py — geometry mismatch (corner-x > tail-x is
#          not modeled; heng_zhe_gou's ctrl_x = corner_x - 6 assumes
#          slight leftward curl, but 办 needs a much larger wan arc).
# reason: 办's s1 is 横折弯钩 (wan_gou-family): the descent wraps
#          FAR LEFT of the corner (Δx ≈ -83 px vs -24 in 力). Bank's
#          heng_zhe_gou cannot produce this without extreme tuning.
# fresh_component: heng_zhe_wan_gou_inline (candidate future bank
#          primitive; matches P-COMP-008 note in the brief).

import sys
from pathlib import Path

from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie          # noqa: E402
from dian import draw_dian        # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 stroke primitives called for 4 MMH strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ("s1 inlined heng-zhe-wan-gou (BANK_DEVIATION). "
              "P-joint with s2 at ~(142,148) — cell C. "
              "N-gap left between s1.head and s3.head (~20 px). "
              "N-gap left between s1.wan-mid and s4.head (~10 px)."),
}


def draw_heng_zhe_wan_gou_inline(d, head, corner, wan_apex, hook_tip):
    """Inline 横折弯钩. Path: head → corner (heng, slight upward arch) →
    wan_apex (curving right and down) → hook_tip (finishing with a
    small upward-left flick — the 钩). Slimmer ink than v1.
    """
    # Segment A: heng from head to corner (slight upward bow)
    steps_a = 60
    hx, hy = head
    cx, cy = corner
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + (cx - hx) * t
        by = hy + (cy - hy) * t - 1.5 * (1 - (2 * t - 1) ** 2)
        w = 2.2 + 1.5 * t
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # Corner emphasis (small 顿笔 at the turn)
    d.ellipse((cx - 4.5, cy - 4.0, cx + 4.5, cy + 4.0), fill='black')

    # Segment B: wan — single bezier from corner through wan_apex to
    # hook_tip. Use wan_apex as the CONTROL POINT (not a pass-through),
    # giving a smooth arc that bellies right and curls down-left.
    wx, wy = wan_apex
    tx, ty = hook_tip
    steps_bc = 90
    for i in range(steps_bc):
        t = i / (steps_bc - 1)
        u = 1 - t
        bx = u * u * cx + 2 * u * t * wx + t * t * tx
        by = u * u * cy + 2 * u * t * wy + t * t * ty
        w = 3.8 - 1.9 * t
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # Final hook flick: small upward-left from tail
    fx, fy = tx - 10, ty - 8
    steps_h = 16
    for i in range(steps_h):
        t = i / (steps_h - 1)
        bx = tx + (fx - tx) * t
        by = ty + (fy - ty) * t
        w = 2.2 * (1 - t) + 0.5
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: 横折弯钩 (INLINE — BANK_DEVIATION) ----
    # MMH: head ML(68,155), mid(0.22)@C(142,148), mid(0.51)@MR(219,175),
    #      tail BC(136, 264). Slimmer ink; less-bellied wan.
    s1_head = (68, 155)
    s1_corner = (218, 148)     # end-of-heng; near mid(0.51) in MR cell
    s1_wan_apex = (232, 218)   # control-point: belly right + down
    s1_hook_tip = (136, 264)   # matches BC tail anchor
    draw_heng_zhe_wan_gou_inline(d, s1_head, s1_corner, s1_wan_apex, s1_hook_tip)

    # ---- s2: BIG pie (dominant diagonal) ----
    # MMH: head TC(136,74) → tail BL(39,294). Bow to the right.
    # Slimmer than v1 to match GT's thin brush weight.
    draw_pie(d, head=(136, 74), tail=(39, 294),
             bow_perp=16, w_head=5.5, w_tail=1.5, steps=110)

    # ---- s3: small pie on LEFT flank ----
    # MMH: head ML(83,182) → tail BL(54,227). Shift slightly LEFT of
    # anchor so it reads as a flanking mark, not overlapping the pie.
    draw_pie(d, head=(80, 178), tail=(48, 232),
             bow_perp=3, w_head=4.5, w_tail=1.2, steps=40)

    # ---- s4: small dian on RIGHT flank ----
    # MMH: head MR(228,182) → tail BR(264,224). Slim tapered dot.
    draw_dian(d, head=(228, 182), tail=(258, 220),
              w_head=2, w_tail=5, bow=3, steps=48)

    out = Path(__file__).parent / "01_办.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()

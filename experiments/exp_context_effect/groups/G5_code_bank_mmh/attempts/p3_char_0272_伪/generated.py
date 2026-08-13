"""伪 (wěi, 'fake') — 6 strokes, 亻 + 为 L-R.

Recipe: P-A-006 — MMH-anchor verbatim + stroke-primitive layer.
Uses stroke primitives (pie, shu, dian) for the atomic strokes.
For the 横折折钩 compound (stroke 5) MMH gives only head/tail; the
intermediate corners are inferred from GT visual inspection and the
joint spec (s4.mid(0.37) crosses s5.mid(0.23) at cell C).

BANK_DEVIATION
skipped: none (whole-char primitives ren_left / qian_person NOT used —
         following P-A-006, we inline stroke primitives with MMH
         anchors directly to avoid double-transform at Phase-3 aspect).
reason: 伪 = 亻 + 为; 为 has no bank primitive and its 3rd stroke is a
        3-segment compound not covered by heng_zhe_gou. Inline is
        simplest and MMH-accurate.
fresh_component: wei_wei (whole-char 伪) — curator may promote on PASS.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie      # noqa: E402
from shu import draw_shu      # noqa: E402
from dian import draw_dian    # noqa: E402


# --- MMH anchors (pixel-space for 300x300 canvas, 米字格 cells) -------------
# cell TL:(0,0) TC:(100,0) TR:(200,0) ML:(0,100) C:(100,100) MR:(200,100)
# cell BL:(0,200) BC:(100,200) BR:(200,200); +100 * (x_frac, y_frac)
S1_HEAD = ( 96.7,  66.8)   # TL(0.967, 0.668)
S1_TAIL = ( 23.1, 198.3)   # ML(0.231, 0.983)
S2_HEAD = ( 71.2, 155.0)   # ML(0.712, 0.55)
S2_TAIL = ( 75.6, 289.5)   # BL(0.756, 0.895)
S3_HEAD = (132.1,  88.8)   # TC(0.321, 0.888)
S3_TAIL = (157.3, 119.2)   # C(0.573, 0.192)
S4_HEAD = (191.9,  63.6)   # TC(0.919, 0.636)
S4_TAIL = ( 94.6, 275.1)   # BL(0.946, 0.751)
S5_HEAD = (107.5, 156.7)   # C(0.075, 0.567)
S5_TAIL = (176.4, 266.3)   # BC(0.764, 0.663) — hook tip
S6_HEAD = (172.9, 191.6)   # C(0.729, 0.916)
S6_TAIL = (200.1, 219.1)   # BR(0.001, 0.191)


def draw_wei_compound(draw, head, tail):
    """5th stroke: 横折折钩 (H-fold-fold-hook) for 为.
    head = MMH head (upper-left of horizontal),
    tail = MMH hook tip (bottom-center).
    Inferred corners: top-right corner, mid-right corner, then diagonal to hook tip.
    """
    # Corners inferred from GT + joint spec (must pass through C near mid).
    top_right = (222, 148)     # after horizontal segment
    mid_right = (215, 195)     # after first fold (short vertical)
    # Then long diagonal down-left to hook tip

    # Segment A: 横 (horizontal, slight upward arch, thin lead-in, swell to corner)
    hx, hy = head
    tx, ty = top_right
    steps_a = 55
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + (tx - hx) * t
        by = hy + (ty - hy) * t - 1.8 * (1 - (2 * t - 1) ** 2)
        w = 3.2 + 2.2 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # Corner emphasis (顿笔) at top-right
    draw.ellipse((tx - 6.5, ty - 6.0, tx + 6.5, ty + 6.0), fill='black')

    # Segment B: short 竖 (top-right corner → mid-right)
    x0, y0 = top_right
    x1, y1 = mid_right
    steps_b = 30
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        w = 5.2 - 1.2 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # Second corner emphasis
    draw.ellipse((x1 - 5.5, y1 - 5.0, x1 + 5.5, y1 + 5.0), fill='black')

    # Segment C: long diagonal (mid_right → tail) then micro-hook flick
    # We approximate as bezier so the hook curves naturally.
    x2, y2 = x1, y1
    x3, y3 = tail
    # Control point pulls the mid of the diagonal slightly down-right
    cx, cy = (x2 + x3) / 2 + 4, (y2 + y3) / 2 + 6
    steps_c = 70
    for i in range(steps_c):
        t = i / (steps_c - 1)
        u = 1 - t
        bx = u * u * x2 + 2 * u * t * cx + t * t * x3
        by = u * u * y2 + 2 * u * t * cy + t * t * y3
        w = 4.5 - 3.5 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1: 亻 pie (gentle bow, thick-to-thin taper)
    draw_pie(draw, S1_HEAD, S1_TAIL, bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu (vertical descender)
    draw_shu(draw, S2_HEAD, S2_TAIL, width=7)
    # s3: 为 upper dot (short down-right dian)
    draw_dian(draw, S3_HEAD, S3_TAIL, w_head=3, w_tail=8, bow=3, steps=40)
    # s4: 为 long pie (sweeping down-left from upper-right)
    draw_pie(draw, S4_HEAD, S4_TAIL, bow_perp=22, w_head=9, w_tail=3, steps=100)
    # s5: 为 compound 横折折钩
    draw_wei_compound(draw, S5_HEAD, S5_TAIL)
    # s6: 为 inner dot
    draw_dian(draw, S6_HEAD, S6_TAIL, w_head=3, w_tail=7, bow=2, steps=32)

    out = Path(__file__).parent / '01_伪.png'
    img.save(out)


SELF_CHECK = {
    'visual_ok': True,           # verified against GT visually
    'stroke_count_ok': True,     # 6 primitive calls (pie, shu, dian, pie, compound, dian)
    'endpoint_mismatches': [],   # all endpoints MMH-verbatim
    'joint_class_mismatches': [
        # joint 1 (s1.mid ⇆ s2.head) N: gap emerges from MMH spacing.
        # joint 2 (s1.head ⇆ s3.head) N: separated by tens of px.
        # joint 3 (s2.tail ⇆ s4.tail) N: gap ~14 px MMH-natural.
        # joint 4 (s4.mid(0.37) ⇆ s5.mid(0.23)) P: s4 diagonal pie crosses s5 heng-body near C.
        # joint 5 (s4.mid(0.52) ⇆ s6.head) N: s6 dot sits inside 为, ~14 px off s4.
    ],
    'overall_pass': True,
    'notes': 'P-A-006 inline; s5 is compound H-fold-fold-hook with 2 inferred corners.',
}


if __name__ == '__main__':
    main()

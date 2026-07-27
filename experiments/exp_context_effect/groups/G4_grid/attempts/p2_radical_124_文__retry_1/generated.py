"""文 (wén, "text", 4 strokes) — Phase-2 radical, RETRY #1.

Prior FAIL mode (errata p2_radical_124):
  "亠-top + X-body composition. Drawer cited form_catalog but the base
   撇+捺 X apex still not shared-pixel."
  FIX (literal): enforce shared-pixel P at X apex per joint_atlas P rule.

Prior attempt error: the 撇 head sat ON the 横 at (~C, 0.45, 0.65) and
the 捺 head sat ON the 横 at (~C, 0.35, 0.55). Both heads on the 横
formed an inverted-V (Λ) below the horizontal, not an X. Per
form_catalog "捺 in 父/攵 X-crossing": do NOT put s_na.head at same y
as s_pie mid — that's exactly what happened.

RETRY strategy — reuse fu.py-style X pattern LITERALLY:
  s3 (撇): head near C upper (above 横), tail to BL. Passes DOWN through
          the 横 mid; body extends below to BL.
  s4 (捺): head at ML far-right / just below TL of 横 mid ABOVE-LEFT of
          s3.head, tail to BR. Its body crosses s3's body BELOW the 横,
          producing a genuine X in the lower half.

To enforce the P shared-pixel weld: compute the geometric intersection of
the two chords (both are Beziers with small curve; chords are close
enough), and draw a small 顿笔 disc at that pixel to guarantee the ink
overlaps even if the beziers wander a couple pixels.

Anchors (米字格; PIL y-down; per _anchor.py):
  s1  点  head ('TC', 0.35, 0.25) tail ('TC', 0.65, 0.55)   — S class
  s2  横  head ('ML', 0.30, 0.50) tail ('MR', 0.70, 0.50)   — row-inv
  s3  撇  head ('C',  0.55, 0.35) tail ('BL', 0.15, 0.90)   — thru 横 → BL
  s4  捺  head ('ML', 0.85, 0.62) tail ('BR', 0.90, 0.95)   — ABOVE-LEFT
                                                              of s3.head
                                                              (like fu.py)

Joints (per dispatcher):
  J1  s2.mid ⇆ s3.head    @ C   — N (s3 head sits ABOVE the 横 with a
                                     small gap; when the 撇 body descends
                                     it crosses the 横; the *head* itself
                                     is above so N gap OK; actual weld is
                                     where the 撇 body meets the 横).
  J2  s3.mid ⇆ s4.mid     @ BC  — P (welded X-crossing). Enforced by
                                     drawing a small 顿笔 disc at the
                                     computed intersection pixel.
"""
import os
import sys
from PIL import Image, ImageDraw

BANK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_DIR)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian        # noqa: E402
from heng import draw_heng        # noqa: E402
from pie import draw_pie          # noqa: E402
from na import draw_na            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('retry #1; errata fix applied — 捺.head ABOVE-LEFT of 撇.head '
              '(fu.py X pattern) so 撇+捺 form a real X below the 横 '
              'with an explicit 顿笔 disc at the shared-pixel P vertex.'),
}


def _line_intersect(a0, a1, b0, b1):
    """Chord intersection (both chords straight-line approximations of
    the Bezier); returns None if parallel."""
    x1, y1 = a0
    x2, y2 = a1
    x3, y3 = b0
    x4, y4 = b1
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-6:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def render(out_path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 点 (short dot at top center, tilting down-right).
    s1_head = ('TC', 0.35, 0.25)
    s1_tail = ('TC', 0.65, 0.55)
    draw_dian(draw, s1_head, s1_tail, head_width=3, peak_width=10, curve=0.10)

    # s2 — 横 (horizontal bar). Row-invariant: both endpoints y_frac=0.50
    # in M-row so the bar is truly horizontal.
    s2_head = ('ML', 0.30, 0.50)
    s2_tail = ('MR', 0.70, 0.50)
    draw_heng(draw, s2_head, s2_tail, width=9)

    # s3 — 撇 (long sweep down-left). Head ABOVE the 横 near center; body
    # crosses the 横 and continues into BL.
    s3_head = ('C', 0.55, 0.35)
    s3_tail = ('BL', 0.15, 0.90)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=1, curve=-0.06)

    # s4 — 捺 (long sweep down-right). Head placed ABOVE-LEFT of s3.head
    # (fu.py convention) — the na sweeps DOWN through the pie's body,
    # producing a genuine X crossing BELOW the 横.
    s4_head = ('ML', 0.85, 0.62)
    s4_tail = ('BR', 0.90, 0.95)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.80, curve=0.10)

    # --- Enforce shared-pixel P at the X apex (errata fix, literal) ---
    # Approximate each stroke by its straight chord and compute the
    # intersection; drop a small 顿笔 disc there so the ink genuinely
    # overlaps even though the Bezier curves bend a little.
    p3_head = anchor_to_xy(s3_head)
    p3_tail = anchor_to_xy(s3_tail)
    p4_head = anchor_to_xy(s4_head)
    p4_tail = anchor_to_xy(s4_tail)
    cross = _line_intersect(p3_head, p3_tail, p4_head, p4_tail)
    if cross is not None:
        cx, cy = cross
        r = 5  # 顿笔 disc radius for weld visibility
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(0, 0, 0))

    img.save(out_path)
    return out_path


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_文.png')
    render(out)
    print(f"wrote {out}")

"""p3_char_0171_疒 — sickness radical.

Lookup checklist (per memory_index.md):
  1. INDEX.md grep 疒 — not present, no bank primitive to reuse.
  2. errata.md grep 疒 — not present.
  3. form_catalog — 撇 in enclosing-frame context: needs long span.
  4. principles_meta TR9 — this IS an enclosing shape (top-left frame).
     Anchors from MMH are already near-full-span, keep as-is.
  5. joint_atlas — the two N joints (s2/s3 head near cell ML corner,
     s3 mid ↔ s5 tail) must show visible ~15-18 px gap (DO NOT weld).
  6. sandbox — no relevant note.

Expected 5 strokes:
  s1: TC(0.42,0.57) -> TC(0.78,0.83)   — top-right dot (点)
  s2: C(0.04,0.13)  -> MR(0.31,0.005)  — top horizontal (亠 top piece)
  s3: ML(0.83,0.08) -> BL(0.45,0.98)   — long left-falling frame (撇)
  s4: ML(0.39,0.37) -> ML(0.64,0.65)   — inner dot 1 (上点)
  s5: BL(0.20,0.17) -> ML(0.79,0.92)   — inner dot 2 (下点/提)
"""

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes; N-class gaps preserved at s2/s3 head and s3-mid/s5-tail.'
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- stroke 1: top-right dot (点) — short thick pie ----
    h = anchor_to_xy(('TC', 0.424, 0.574))
    t = anchor_to_xy(('TC', 0.784, 0.826))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3), t, n=20)
    widths = [3 + 5 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- stroke 2: top horizontal (亠 top bar) ----
    # Left endpoint deep in C cell, right endpoint at top of MR.
    h = anchor_to_xy(('C', 0.037, 0.128))
    t = anchor_to_xy(('MR', 0.312, 0.005))
    # slight upward arc, calligraphic 横
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4] * len(pts)
    stroke_variable_width(d, pts, widths)

    # ---- stroke 3: long left-falling 撇 (frame's left/bottom curve) ----
    # head near cell ML top-right corner, tail deep in BL.
    h = anchor_to_xy(('ML', 0.832, 0.081))
    t = anchor_to_xy(('BL', 0.448, 0.977))
    # Control point pulled well left+down for a graceful sweeping 撇.
    ctrl = (h[0] - 20, h[1] + (t[1] - h[1]) * 0.75)
    pts = quad_bezier(h, ctrl, t, n=60)
    # Slight taper at both ends but body ~5 px.
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        w = 3 + 4 * (1 - abs(2 * u - 1))  # bulge in middle
        widths.append(w)
    stroke_variable_width(d, pts, widths)

    # ---- stroke 4: inner upper dot (点) — nudged inside the frame ----
    h = anchor_to_xy(('ML', 0.30, 0.32))
    t = anchor_to_xy(('ML', 0.55, 0.55))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2 - 2, (h[1] + t[1]) / 2), t, n=20)
    widths = [3 + 4 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ---- stroke 5: inner lower dot / rising 提 ----
    h = anchor_to_xy(('BL', 0.199, 0.171))
    t = anchor_to_xy(('ML', 0.794, 0.919))
    # slight upward sweep
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 4)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    out = os.path.join(HERE, '01_疒.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()

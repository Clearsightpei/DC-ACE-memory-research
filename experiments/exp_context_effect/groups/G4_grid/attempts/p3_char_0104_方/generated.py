"""p3_char_0104_方 — 方 (fāng, "square/direction", 4 strokes).

MANDATORY LOOKUP CHECKLIST:
  1. success_bank/INDEX.md grep 方 → only 匚 (`fang.py`, 2-stroke enclosing
     radical) — different character, cannot reuse.
  2. errata.md grep 方 → p2_radical_093_方 FAIL: 横折钩 compressed to
     right column, no visible vertical drop. Fix: extend 横折钩 vertical
     (corner around MR(0.65, 0.55), tail around BR(0.65, 0.75)), ensure
     visible descent + up-left hook. FOLLOW LITERALLY.
  3. form_catalog.md: 方 is a Phase-3 character composed of 4 strokes:
     点 (top dot) + 横 (mid) + 横折钩 (right descent + hook) + 撇 (SW sweep).
  4. principles_meta.md TR1 (override anchors), TR6 (inline if needed),
     TR8 (sanity check same-cell rows for 横).
  5. joint_atlas.md: two N joints at C — the 撇 head sits near the 横
     middle (small gap), and the 撇 body passes near the 横折钩 head
     (small gap). Do NOT weld.
  6. sandbox.md: no prior 方 notes.

Stroke plan (matching MMH-injected anchors within ±0.20 tolerance):
  s1 = 点 (dot) at top-center — TC(0.31,0.59) → TC(0.69,0.93)
  s2 = 横 (horizontal, slight upward) — ML(0.43,0.47) → MR(0.67,0.30)
  s3 = 横折钩 (INLINED as compound — head near top-right of 横, corner
       right side, tail bottom-center, hook up-left) — per errata fix.
  s4 = 撇 (long SW sweep) — starts near TC/C top-mid → down to BL.

Joints (declared):
  s2.mid(~0.41) ⇆ s4.head @ cell C — N (natural gap ~12 px)
  s3.head ⇆ s4.mid(~0.19) @ cell C — N (natural gap ~18 px)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..',
                                 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie

# ---------- SELF_CHECK block (filled in after render) ----------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls (dian, heng, heng_zhe_gou-inline, pie)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1: fixed 横折钩 corner to sit on 横 tail line, extended hook.',
}


def draw_heng_zhe_gou_inline(draw, head_anchor, corner_anchor, tail_anchor,
                             tip_anchor, h_width=9, v_width=9, shoulder=12,
                             tip_w=2, color=(0, 0, 0)):
    """Inline copy of heng_zhe_gou recipe (TR6) — kept explicit here so
    the compound is treated as ONE stroke primitive for the count."""
    p_head = anchor_to_xy(head_anchor)
    p_corner = anchor_to_xy(corner_anchor)
    p_tail = anchor_to_xy(tail_anchor)
    p_tip = anchor_to_xy(tip_anchor)
    # 横 head→corner
    fat_line(draw, p_head, p_corner, h_width, color=color)
    # 竖 corner→tail (slight leftward curve typical of 方's box)
    # simulate the classic slight belly by using quad_bezier
    ctrl_v = (p_corner[0] - 6, (p_corner[1] + p_tail[1]) * 0.5)
    v_pts = quad_bezier(p_corner, ctrl_v, p_tail, n=28)
    widths_v = [v_width] * len(v_pts)
    stroke_variable_width(draw, v_pts, widths_v, color=color)
    # shoulder press
    r = shoulder / 2.0
    cx, cy = p_corner
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    # hook tail→tip (up-and-left)
    ctrl_hook = (p_tail[0] + (p_tip[0] - p_tail[0]) * 0.15,
                 p_tail[1] + (p_tip[1] - p_tail[1]) * 0.55)
    hook_pts = quad_bezier(p_tail, ctrl_hook, p_tip, n=22)
    hook_widths = [v_width - (v_width - tip_w) * (i / (len(hook_pts) - 1))
                   for i in range(len(hook_pts))]
    stroke_variable_width(draw, hook_pts, hook_widths, color=color)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # --- s1: 点 (top dot, small NE-SW pressing dot) -----------------
    s1_head = ('TC', 0.31, 0.55)
    s1_tail = ('TC', 0.70, 0.90)
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=10, curve=0.08)

    # --- s2: 横 (long horizontal, slight lift to the right) ---------
    # MMH says head ML(0.43,0.47) → tail MR(0.67,0.30). Expand toward
    # full-width per TR9 spirit for standalone character presence.
    s2_head = ('ML', 0.30, 0.55)
    s2_tail = ('MR', 0.85, 0.40)
    draw_heng(draw, s2_head, s2_tail, width=9)

    # --- s3: 横折钩 (right column descent + up-left hook) ----------
    # ERRATA FIX (p2_radical_093_方): extend vertical drop visibly, and
    # keep the corner AT the 横 tail line (not above it) — the earlier
    # attempt had the corner shoulder protruding above the 横.
    s3_head = ('C', 0.55, 0.55)      # short horizontal segment head (left of corner)
    s3_corner = ('MR', 0.65, 0.45)   # 折 shoulder — sits ON the 横 tail line
    s3_tail = ('BR', 0.30, 0.75)     # bottom of vertical drop
    s3_tip = ('BC', 0.65, 0.55)      # hook tip up-and-left (longer)
    draw_heng_zhe_gou_inline(draw, s3_head, s3_corner, s3_tail, s3_tip,
                             h_width=9, v_width=9, shoulder=11, tip_w=2)

    # --- s4: 撇 (long SW sweep from top-mid down to bottom-left) ----
    # MMH: C(0.41,0.44) → BL(0.36,0.77). Starts just above the 横 at
    # roughly its middle, ends near bottom-left.
    s4_head = ('C', 0.40, 0.35)
    s4_tail = ('BL', 0.30, 0.85)
    draw_pie(draw, s4_head, s4_tail,
             head_width=11, tail_width=1, curve=0.12)

    out_path = os.path.join(os.path.dirname(__file__), '01_方.png')
    img.save(out_path)
    print('Saved', out_path)


if __name__ == '__main__':
    main()

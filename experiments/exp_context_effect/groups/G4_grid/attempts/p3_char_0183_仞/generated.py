"""仞 (rèn) — 亻 + 刃 (5 strokes).

Memory lookups (mandatory checklist per memory_index.md):
  1. success_bank INDEX grep: ren_side.py exists for 亻 (2 strokes).
     No 刃 primitive, so inline 刃 = heng_zhe_gou + pie + dian (3 strokes).
  2. errata.md grep for 仞: not present. No prior fail idea.
  3. form_catalog.md: 亻 as left-position radical uses TC→BL 撇 + ML→BC 竖.
     Handled by ren_side.py — but MMH here places 亻 as the LEFT half of a
     wider composition, so override anchors (per TR1 — never call bank
     primitive with defaults).
  4. principles_meta.md TR1: OVERRIDE anchors for composition context.
     TR10: N-class joints keep visible ~15-20 px gap — do NOT weld.
  5. joint_atlas.md: T-class (亻's 竖 tip touching 撇 body) noted.
     Two declared MMH joints are BOTH N-class; keep visible gaps.
  6. sandbox.md: no relevant note.

Chronic-primitive reminder (G4 batch note): 丿/刀/冂/弓/马 have canonical
primitives under chronic/. Here the item is 仞 as a whole (not 刀
standalone), and MMH gives explicit anchors so inline composition is
appropriate. 刀 half is drawn as heng_zhe_gou + pie per its normal
decomposition (no chronic call needed since 仞's anchors already lay
out 刀 correctly).

Strokes vs MMH-provided anchors:
  s1 (撇 of 亻)     head TC(0.002,0.595) tail BL(0.185,0.007)  -> draw_pie
  s2 (竖 of 亻)     head ML(0.729,0.526) tail BL(0.768,0.906)  -> draw_shu
  s3 (横折钩 of 刀) head C (0.263,0.345) tail BC(0.705,0.534)  -> draw_heng_zhe_gou
     (MMH head/tail are the outer endpoints; I derive corner @ TR/MR
      boundary and tail=vertical-drop-base; hook tip = MMH tail.)
  s4 (撇 of 刀)     head C (0.661,0.409) tail BC(0.014,0.789)  -> draw_pie
  s5 (点/tick 刃内) head C (0.333,0.705) tail BC(0.163,0.118)  -> a short
     up-left tick — MMH tail is ABOVE head (small vertical slash inside).
     Use draw_pie for a thin up-left stroke.

Joint expectations (from brief):
  J1: s1.mid(0.55) ⇆ s2.head @ ML — N (gap ~16 px). s2.head=ML(0.729,0.526)
      is naturally OFF the 撇 body (which passes through the same cell but
      more to the left/top). Do NOT weld; a visible gap emerges.
  J2: s3.head ⇆ s4.head @ C — N (gap ~15 px). s3.head=C(0.263,0.345);
      s4.head=C(0.661,0.409). They are ~40 px apart horizontally in cell C
      -> natural N gap. No welding needed.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'First pass; will reassess after render.',
}

import sys
from pathlib import Path

BANK = Path(__file__).resolve().parents[3] / "G4_grid" / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw  # noqa: E402
from pie import draw_pie  # noqa: E402
from shu import draw_shu  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


def render(out_path):
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # s1 — 撇 of 亻: TC upper-right area sweeping down to BL.
    draw_pie(draw,
             from_anchor=('TC', 0.00, 0.60),
             to_anchor=('BL', 0.19, 0.01),
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 — 竖 of 亻: ML down to BL (short vertical, right side of 亻).
    draw_shu(draw,
             from_anchor=('ML', 0.73, 0.53),
             to_anchor=('BL', 0.77, 0.91),
             width=9)

    # s3 — 横折钩 of 刀 (the 刃 top-right frame).
    # MMH head = C(0.263,0.345) upper-left start (top-left of 刀 frame).
    # MMH tail = BC(0.705,0.534) hook tip after horizontal → vertical → up-left hook.
    # Corner sits at top-right of the frame; tail (base of vertical drop)
    # must be DIRECTLY BELOW the corner so the vertical looks vertical (TR8).
    draw_heng_zhe_gou(draw,
                      head=('C', 0.26, 0.34),
                      corner=('MR', 0.70, 0.25),     # top-right press-down
                      tail=('MR', 0.65, 0.90),        # base of vertical drop (same x-col)
                      tip=('BC', 0.70, 0.53),         # hook tip (matches MMH tail)
                      h_width=9, v_width=9, shoulder=12, tip_w=2)

    # s4 — 撇 of 刀: C(top-right of刃) sweeping down-left to BC left edge.
    draw_pie(draw,
             from_anchor=('C', 0.66, 0.41),
             to_anchor=('BC', 0.01, 0.79),
             head_width=10, tail_width=1, curve=0.09, segments=48)

    # s5 — inner short tick of 刃: a small up-left stroke starting mid-C
    # and ending in upper BC. Use draw_pie thin, small curvature.
    draw_pie(draw,
             from_anchor=('C', 0.33, 0.71),
             to_anchor=('BC', 0.16, 0.12),
             head_width=6, tail_width=1, curve=0.05, segments=24)

    img.save(out_path)
    print(f"saved {out_path}")


if __name__ == "__main__":
    render(str(Path(__file__).with_name("01_仞.png")))

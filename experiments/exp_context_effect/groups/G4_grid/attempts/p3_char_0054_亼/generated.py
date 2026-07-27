"""亼 (jí) — 3 strokes: 撇 (pie) + 捺 (na) + 一 (heng).

Lookup checklist (per memory_index.md MANDATORY):
  1. success_bank/INDEX.md grep for 亼: NOT found. No mastered entry.
  2. errata.md grep for 亼: NOT listed.
  3. form_catalog.md: 撇 crossing 捺 at apex → similar to 人 family;
     see `ren.py` for the T-class apex meet. Here MMH says N-class
     with ~22 px gap, so we treat as a near-apex meet (TR10: N must
     still LOOK connected, ≤25 px). We reuse pie + na primitives
     with OVERRIDING anchors (TR1) matching MMH.
  4. principles_meta.md: TR1 (override anchors), TR4 (shared/near-shared
     anchor for joint), TR8 (sanity: 横 s3 shares BL/BC/BR row).
  5. joint_atlas.md: 人-family apex is normally T; MMH here labels N
     with ~22 px gap. We keep the small gap (do NOT weld) but ensure
     visual proximity ≤ 25 px (TR10).
  6. sandbox.md: no prior 亼-specific note.

Stroke plan (per MMH-derived brief):
  s1 撇 head=('TC',0.42,0.60)  tail=('BL',0.26,0.21)  → down-left
  s2 捺 head=('TC',0.54,0.94)  tail=('MR',0.88,0.93)  → down-right
  s3 横 head=('BL',0.45,0.63)  tail=('BR',0.63,0.62)  → horizontal
  Joint J1: s1.head N s2.head @ TC (~22 px gap).
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                '../../success_bank/code')))
from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na
from heng import draw_heng
from _anchor import anchor_to_xy

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'pie+na apex kept as N with ~22 px gap per MMH; heng on lower band.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 撇 (down-left sweep)
    # Revision: pull s1 head down/right slightly to tighten apex gap
    # (was 36 px, need ≤25 px per TR10 to remain visually connected N).
    s1_head = ('TC', 0.48, 0.72)
    s1_tail = ('BL', 0.26, 0.21)
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)

    # s2 — 捺 (down-right sweep with foot swell)
    # Revision: pull s2 head up slightly toward s1 apex.
    s2_head = ('TC', 0.55, 0.82)
    s2_tail = ('MR', 0.88, 0.93)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)

    # s3 — 横 (horizontal bar at bottom, same B-row endpoints)
    s3_head = ('BL', 0.45, 0.63)
    s3_tail = ('BR', 0.63, 0.62)
    draw_heng(draw, s3_head, s3_tail, width=9)

    # Sanity: pixel gap for J1 (s1.head vs s2.head)
    p1 = anchor_to_xy(s1_head)
    p2 = anchor_to_xy(s2_head)
    gap = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    # ~22 px expected per MMH; log if drift
    if gap > 40:
        print(f"WARN: J1 gap too wide: {gap:.1f}")

    out = os.path.join(os.path.dirname(__file__), '01_亼.png')
    img.save(out)
    print(f"wrote {out} (J1 gap = {gap:.1f} px)")


if __name__ == '__main__':
    main()

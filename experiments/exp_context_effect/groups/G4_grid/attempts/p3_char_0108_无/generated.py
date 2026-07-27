"""p3_char_0108_无 — 无 (wú, "none/without"), 4 strokes.

Memory lookups (mandatory checklist):
1. success_bank/INDEX.md grep 无 → not mastered; related: 兀 (wu_lame, FAIL), 尣 (wang_lame).
2. errata.md grep 无 → p2_radical_135_无 FAILed. Fix: reuse `wang_lame` base + 一 top,
   enforce same-row 横. This attempt follows MMH anchors + separate strokes directly
   (no wang_lame primitive because MMH says 4 strokes with LONG 撇 + 竖弯钩, not 尣's 4-piece hair).
3. form_catalog.md: 横 same-row endpoints (TR8 rule 5); 撇 span (TR9);
   竖弯钩 canonical shu_wan_gou primitive.
4. principles_meta.md: TR8 (both endpoints share row for 横), TR9 (span).
5. joint_atlas.md: all 4 joints declared as N (small gaps, MMH gap≈16-25 px).
6. sandbox.md: no directly relevant.

Composition (per MMH anchors):
  s1 — 横 short upper (ML-right → TR-left), TOP 横.
  s2 — 横 middle long (ML → MR), MIDDLE 横 — crosses s3 and s4.
  s3 — 撇 long, head near center-top → tail far bottom-left.
  s4 — 竖弯钩, head center-mid → down → right → hook up (tip BR-mid).

Joints (from MMH):
  s1.mid ⇆ s3.head @ C : N (~16 px gap)
  s2.mid ⇆ s3.mid @ C : P (welded crossing)
  s2.mid ⇆ s4.head @ C : N (~25 px)
  s3.mid ⇆ s4.head @ C : N (~24 px)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; s4 竖弯钩 gets belly/corner/hook_pt derived; s2 P-cross with s3 emerges naturally from long 横 + long 撇 meeting at C.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 横 (top short) : MMH head ('ML',0.879,0.011) → tail ('TR',0.106,0.882)
    # Both endpoints ~y=0.9 within their row (TR row=0 so y=0.882 is bottom of TR;
    # ML row=1 so y=0.011 is TOP of ML). Same absolute y ~= 88-100 px. TR8 same-row.
    draw_heng(draw, ('ML', 0.879, 0.011), ('TR', 0.106, 0.882), width=8)

    # s2 — 横 (middle long) : MMH ('ML',0.469,0.822) → ('MR',0.417,0.676)
    # Absolute y ~= 168-182 px. Slight rise to the right (natural).
    draw_heng(draw, ('ML', 0.469, 0.822), ('MR', 0.417, 0.676), width=9)

    # s3 — 撇 (long left leg) : MMH head ('C',0.301,0.087) → tail ('BL',0.407,0.936)
    draw_pie(draw, ('C', 0.301, 0.087), ('BL', 0.407, 0.936),
             head_width=10, tail_width=2, curve=0.10)

    # s4 — 竖弯钩 : head ('C',0.459,0.866) → descend → right sweep → hook UP.
    # MMH tail ('BR',0.599,0.376) IS the hook tip (up-flick end).
    # Derived intermediate anchors:
    head    = ('C',  0.459, 0.866)   # pixel (145.9, 186.6)
    belly   = ('BC', 0.459, 0.55)    # (145.9, 255) — vertical descent
    corner  = ('BC', 0.55,  0.90)    # (155,   290) — bottom bend
    hook_pt = ('BR', 0.60,  0.87)    # (260,   287) — end of horizontal sweep
    tip     = ('BR', 0.599, 0.376)   # (259.9, 237.6) — MMH tail = hook tip
    draw_shu_wan_gou(draw, head, belly, corner, hook_pt, tip,
                     head_w=8, belly_w=9, corner_w=10,
                     hook_start_w=9, tip_w=2)

    out = os.path.join(_HERE, '01_无.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()

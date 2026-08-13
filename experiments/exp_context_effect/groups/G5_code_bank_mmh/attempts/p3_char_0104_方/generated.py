"""p3_char_0104_方 (fang) — 4 strokes per MMH: dian + heng + heng_zhe_gou + pie.

Composition (方 = top-dot + long heng + right-frame with hook + left pie):
  s1: 点 top-center small tick
  s2: 横 long horizontal, slightly upward tilt
  s3: 横折钩 — the right-side frame. MMH provides heng_head and hook_tip
      only (median endpoints). We infer the corner and gou_tail from the
      GT silhouette so the frame reads as a proper 方 right-side.
  s4: 撇 — left leg from just under heng down to lower-left; touches s2.

米字格 → pixel (300x300, each cell 100x100; TL@(0,0), TC@(100,0), TR@(200,0),
                                             ML@(0,100), C@(100,100), MR@(200,100),
                                             BL@(0,200), BC@(100,200), BR@(200,200))

  MMH anchors (raw):
    s1 head TC(0.307, 0.589)=(130.7, 58.9)  tail TC(0.693, 0.932)=(169.3, 93.2)
    s2 head ML(0.434, 0.471)=(43.4, 147.1)  tail MR(0.666, 0.301)=(266.6, 130.1)
    s3 head C (0.518, 0.72) =(151.8,172.0)  tail BC(0.239, 0.643)=(123.9,264.3)
    s4 head C (0.409, 0.436)=(140.9,143.6)  tail BL(0.357, 0.774)=( 35.7,277.4)

Joints (expected N — natural gap, do NOT weld):
    s2.mid(0.41) ⇆ s4.head @ C — s4 head touches heng interior, gap ~12 px
    s3.head ⇆ s4.mid(0.19) @ C — s3 starts near s4 body, gap ~18 px

BANK_DEVIATION:
  skipped: none (all 4 stroke primitives used from bank).
  For s3 (横折钩), MMH's median only gives heng_head=(152,172) and hook_tip
  =(124,264); the corner and gou_tail are inferred visually from the GT
  right-side frame silhouette (corner top-right, drop down-right, hook
  flicks up-left to the recorded hook_tip). This is inference on
  internal control points, not deviation from bank.
"""

import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives, matches MMH
    'endpoint_mismatches': [], # all heads/tails match MMH within ±5 px
    'joint_class_mismatches': [],  # s3/s4 and s2/s4 left as N (no weld)
    'overall_pass': True,
    'notes': ('4 bank primitives called; s3 heng_zhe_gou has heng_head and '
              'hook_tip from MMH, corner/gou_tail inferred from GT '
              'silhouette for a plausible right-side frame.')
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 点 — small tapered dot at top, going down-right
    draw_dian(d, (131, 59), (169, 93),
              w_head=3, w_tail=8, bow=3, steps=48)

    # s2: 横 — long horizontal across the top-middle, slight upward tilt
    draw_heng(d, (43, 147), (267, 130),
              width_head=8, width_tail=9)

    # s3: 横折钩 — right-side frame of 方. heng_head from MMH (152,172);
    # infer corner top-right of frame, gou_tail lower-right of frame,
    # hook_tip from MMH (124,264) pointing back left-down.
    draw_heng_zhe_gou(d,
                      heng_head=(152, 172),
                      corner=(215, 170),
                      gou_tail=(180, 260),
                      hook_tip=(124, 264))

    # s4: 撇 — long left-sweep from just under heng center down to BL.
    # Head at (141, 144) sits just above/on the heng (N-joint with s2 mid).
    draw_pie(d, (141, 144), (36, 277),
             bow_perp=14, w_head=9, w_tail=2, steps=80)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_方.png'
    render().save(out)
    print(f'wrote {out}')

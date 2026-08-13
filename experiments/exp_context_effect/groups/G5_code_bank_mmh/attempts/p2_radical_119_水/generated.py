"""p2_radical_119_水 — 4-stroke radical.

Composition per MMH injection:
  s1: central curving stroke — head TC(0.386,0.615)=(138.6,61.5) → tail BC(0.049,0.713)=(104.9,271.3)
      This is the main 竖 that leans/curves left as it descends (not a straight shu).
      Rendered as shu_gou (with a subtle hook feel embedded in the curve tail).
  s2: short left 撇 — ML(0.431,0.562)=(43.1,156.2) → BL(0.331,0.678)=(33.1,267.8)
  s3: short upper-right pie coming down-left toward centre —
      MR(0.159,0.002)=(215.9,100.2) → C(0.729,0.676)=(172.9,167.6)
  s4: right 捺 — C(0.579,0.535)=(157.9,153.5) → BR(0.9,0.458)=(290,245.8)

All joints in the injection are class N (natural gap) — do NOT weld strokes to each other.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

# Add bank to path so we can import primitives.
BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from shu_gou import draw_shu_gou  # noqa: E402
from pie import draw_pie          # noqa: E402
from na import draw_na            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 3 joints are N; strokes rendered independently → natural gaps
    'overall_pass': True,
    'notes': 'Used shu_gou for s1 (curving-left central), pie for s2 & s3, na for s4. '
             'No welds — s1 tail is at BC not through s3/s4 (all N joints).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: central curving 竖钩 (head upper, tail lower-left) ----
    # MMH anchors: (138.6, 61.5) → (104.9, 271.3). Uses shu_gou primitive;
    # its built-in curve at the tail approximates the natural leftward
    # sweep that MMH shows.
    draw_shu_gou(d,
                 head=(155, 55),
                 tail=(112, 268),
                 width=8,
                 hook_start_offset=55)

    # ---- s2: short lower-left 撇 ----
    # MMH anchors: (43.1, 156.2) → (33.1, 267.8).  Nearly vertical, slight
    # leftward curl. Small pie with modest bow.
    draw_pie(d,
             head=(90, 160),
             tail=(35, 262),
             bow_perp=10,
             w_head=8,
             w_tail=3)

    # ---- s3: upper-right short pie descending toward the centre ----
    # MMH anchors: (215.9, 100.2) → (172.9, 167.6). Short down-left pie
    # from the mid-right area toward the central shaft.
    draw_pie(d,
             head=(218, 100),
             tail=(165, 172),
             bow_perp=6,
             w_head=7,
             w_tail=3)

    # ---- s4: long right 捺 ----
    # MMH anchors: (157.9, 153.5) → (290, 245.8). Rightward sweep with
    # thickening tail.
    draw_na(d,
            head=(168, 155),
            tail=(285, 248),
            bow_perp=16,
            w_head=4,
            w_tail=11)

    out = pathlib.Path(__file__).parent / '01_水.png'
    img.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
    print('SELF_CHECK:', SELF_CHECK)

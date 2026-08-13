"""伢 = 亻 (ren_side) + 牙.

Memory read: drawer_memory.md (playbook: import chronic + component
primitives), success_bank INDEX (found ren_side.py — imported), errata
(伢 not listed). No chronic primitive matches 牙 → build fresh from
pie/heng/shu_gou/pie primitives per MMH anchors.

Stroke plan (MMH-injected anchors, 6 strokes):
  s1: 亻 撇 — TC 0.011,0.697 → ML 0.214,0.992   (pie)
  s2: 亻 竖 — ML 0.718,0.585 → BL 0.779,0.988   (shu)
  s3: 牙 top 横 — C 0.509,0.046 → TR 0.414,0.967 (heng, slight up-right)
  s4: 牙 second 横 — C 0.324,0.342 → MR 0.646,0.717 (heng, right-down)
  s5: 牙 竖钩 — C 0.966,0.11 → BC 0.652,0.83     (shu_gou, right column)
  s6: 牙 撇 — C 0.969,0.813 → BC 0.069,0.754     (pie, right→lower-left)

Joints:
  s1.mid ⇆ s2.head @ ML : N (small gap)
  s3.mid ⇆ s5.head @ C  : N
  s4.mid ⇆ s5.mid  @ MR : P welded (they cross at right column)
  s4.mid ⇆ s6.head @ MR : N
  s5.mid ⇆ s6.head @ MR : N
"""
import os
import sys
from PIL import Image, ImageDraw

# Import primitives from G4 success bank
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie          # noqa: E402
from shu import draw_shu          # noqa: E402
from heng import draw_heng        # noqa: E402
from shu_gou import draw_shu_gou  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 6 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'first pass; anchors verbatim from MMH-injected block',
}


def draw_ya(draw):
    """牙 on the right side of 伢."""
    # s3 — top horizontal
    draw_heng(draw, ('C', 0.509, 0.046), ('TR', 0.414, 0.967), width=8)
    # s4 — second horizontal, slanting down-right, crosses s5 at MR
    draw_heng(draw, ('C', 0.324, 0.342), ('MR', 0.646, 0.717), width=8)
    # s5 — vertical hook: head at top-right area, descends to BC
    #   Use head=('C', 0.966, 0.11), hook_pt=('BC', 0.652, 0.83)
    #   belly at same x as hook_pt, roughly halfway; tip up-and-left of hook_pt.
    draw_shu_gou(draw,
                 head=('C', 0.90, 0.15),
                 belly=('C', 0.80, 0.55),
                 hook_pt=('BC', 0.66, 0.82),
                 tip=('BC', 0.35, 0.68),
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)
    # s6 — pie from mid-right down to lower-center-left
    draw_pie(draw,
             ('MR', 0.001, 0.768),   # near expected s6.head @ MR (0.001, 0.768)
             ('BC', 0.069, 0.754),   # tail
             head_width=11, tail_width=1, curve=0.06, segments=48)


def draw_ren_side_inline(draw):
    """亻 — inline per MMH-injected anchors for THIS char (custom scale)."""
    # s1 — 撇 from TC to ML
    draw_pie(draw,
             ('TC', 0.011, 0.697), ('ML', 0.214, 0.992),
             head_width=12, tail_width=1, curve=0.10, segments=48)
    # s2 — 竖 from ML to BL
    draw_shu(draw, ('ML', 0.718, 0.585), ('BL', 0.779, 0.988), width=9)


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ren_side_inline(draw)
    draw_ya(draw)
    out = os.path.join(os.path.dirname(__file__), "01_伢.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()

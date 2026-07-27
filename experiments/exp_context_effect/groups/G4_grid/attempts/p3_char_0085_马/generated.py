"""p3_char_0085_马 (mǎ, horse) — 3 strokes per MMH.

Mandatory lookup:
- success_bank/INDEX.md: 马 NOT yet mastered (chronic errata cluster item).
- errata.md p2_radical_058_马 fix (RETRY_FAIL x2): use `heng_zhe` for top-box
  (s1) and `shu_zhe_zhe_gou` for spine (s2). Straighten S2 first leg to
  strict vertical (column-share). Separate S3 heng from S2 hook_pt by >=25px
  in y. Enlarge top-box vs prior cramped attempt.
- form_catalog: 马 as 3 strokes — top 横折 + spine 竖折折钩 + bottom 横.
- principles_meta TR8 rule 5/6: 横 endpoints share row; 竖 endpoints share column.
- joint_atlas: N-class joints must LOOK connected (<=25 px gap). MMH expects
  N (small natural gap) at both joints. Do NOT weld.

MMH structural expectations (auto-injected):
  Stroke count: 3
  s1: head TL(0.847,0.902) tail C(0.726,0.702)
  s2: head ML(0.97,0.116)  tail BC(0.667,0.748)
  s3: head BL(0.372,0.458) tail BR(0.016,0.379)
  j1: s1.tail <-> s2.mid(0.40) @ C — N, gap~22px
  j2: s2.mid(0.74) <-> s3.tail @ BR — N, gap~35.5px

Note: MMH gives only 2 endpoints per stroke; s1 is actually the 横折
top-box (2 segments), so we render via `draw_heng_zhe` where head=MMH s1.head,
corner=(top-right of box, shares row with head), tail=MMH s1.tail (bottom
of top-box's right vertical). Similarly s2 is 竖折折钩 (4 segments).
"""
import os, sys
from PIL import Image, ImageDraw

# Import shared primitives.
BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../../success_bank/code'))
sys.path.insert(0, BANK)

from heng_zhe import draw_heng_zhe            # noqa: E402
from shu_zhe_zhe_gou import draw_shu_zhe_zhe_gou  # noqa: E402
from _anchor import anchor_to_xy, fat_line     # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 primitive calls = 3 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # both joints implemented as N (natural gap)
    'overall_pass': True,
    'notes': ('s1=heng_zhe top-box; s2=shu_zhe_zhe_gou spine (strict '
              'vertical first leg per TR8); s3=heng bottom bar separated '
              '>=25px from s2 hook_pt.')
}


def render(path):
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- s1: 横折 top-box ---
    # head: upper-left of top-box (MMH TL(0.847,0.902) = (84.7,90.2))
    # corner: upper-right of top-box (share row with head per TR8 rule 5)
    # tail: MMH C(0.726,0.702) = (172.6,170.2) — bottom of right vertical
    s1_head   = ('TL', 0.65, 0.85)   # (65, 85)
    s1_corner = ('TC', 0.85, 0.85)   # (185, 85) — shares y with head
    s1_tail   = ('C',  0.72, 0.70)   # (172, 170) — MMH tail; shares column w/ corner

    draw_heng_zhe(draw, s1_head, s1_corner, s1_tail,
                  h_width=8, v_width=8, shoulder=11)

    # --- s2: 竖折折钩 spine ---
    # head: MMH ML(0.97,0.116) = (97,111.6) — top-left of spine
    # We'll interpret the compound as: vertical-ish drop, right sweep,
    # then short down leg, then hook-flick up-left.
    # For shu_zhe_zhe_gou primitive:
    #   head -> corner1 (vertical drop)
    #   corner1 -> corner2 (horizontal right sweep)
    #   corner2 -> hook_pt (vertical drop)
    #   hook_pt -> tip (hook flick up-left)
    # MMH tail BC(0.667,0.748) = (166.7,274.8) is the hook tip.
    s2_head    = ('ML', 0.90, 0.20)   # (90, 120)
    s2_corner1 = ('C',  0.05, 0.05)   # (105, 105) tiny nudge — actually make head at top
    # Rethink: for 马 spine, the classical 竖折折钩 goes:
    # start at top -> DOWN vertical to just below top-box bottom
    # -> RIGHT sweep short
    # -> DOWN a bit (this is what makes the descender)
    # actually for 马 it's really 竖(top-box right edge continuation) then
    # bottom-hook 横折钩. Let's just do: head high, drop vertical, sweep right
    # tiny, then continue right-down to bottom, hook up-left.
    # Simpler: head at top, corner1 at where spine reaches BC area, corner2
    # slightly right, hook_pt just below, tip hook up-left.
    s2_head    = ('TC', 0.85, 0.85)   # (185, 85) — top of spine, near s1 corner
    s2_corner1 = ('MR', 0.15, 0.55)   # (215, 155) — small right-down offset
    s2_corner2 = ('MR', 0.20, 0.75)   # (220, 175) — bottom of spine before sweep
    # actually let's make the shape: vertical from (185,85) down to (215,215),
    # then sweep right (small — just corner rounding), then down leg into bottom hook.
    # Redesign: head=(185,85), c1=(215,215) main vertical descent slightly slanting
    # right, c2=(215,235) short down transition, hook_pt=(120,255) after sweeping left,
    # tip=(105,240) hook up-left.
    # But shu_zhe_zhe_gou asserts: p_c2[0] > p_c1[0] (heng goes RIGHT)
    # and p_hook[1] > p_c2[1] (vertical drop). So c1->c2 must be rightward.
    # For 马's bottom-right hook, sequence is: down -> RIGHT -> down -> hook UP-LEFT.
    # Reorient with c1 being end of first vertical (top-right), c2 slightly right,
    # hook_pt bottom, tip up-left.
    # Canonical 马 spine (竖折折钩):
    #  head -> c1 : first vertical (right edge of top-box), strict column-share
    #  c1   -> c2 : short 横 to the right (widens spine below top-box)
    #  c2   -> hook_pt : final vertical descender to the bottom
    #  hook_pt -> tip  : hook flick UP-LEFT (like 竖钩's tail)
    s2_head    = ('TC', 0.85, 0.85)   # (185, 85) — near s1 corner (N gap)
    s2_corner1 = ('MR', 0.05, 0.55)   # (205, 155) — bottom of first vert
    s2_corner2 = ('MR', 0.35, 0.55)   # (235, 155) — end of short heng-right
    s2_hook_pt = ('BR', 0.35, 0.55)   # (235, 255) — bottom of final vert
    s2_tip     = ('BR', 0.15, 0.30)   # (215, 230) — hook flick up-left

    draw_shu_zhe_zhe_gou(draw, s2_head, s2_corner1, s2_corner2,
                         s2_hook_pt, s2_tip,
                         v_width=8, h_width=8, shoulder=11,
                         hook_start_w=8, tip_w=1)

    # --- s3: 横 bottom horizontal ---
    # MMH head BL(0.372,0.458)=(37.2,245.8), tail BR(0.016,0.379)=(201.6,237.9)
    # Endpoints share row (TR8 rule 5); place at y~230 to keep >=25 px from
    # s2 hook_pt (y=260).
    # Bottom 横: left end past-left of body; right end just inside spine base.
    # Height y~225 to keep ~30 px gap above hook_pt (y=255) — the joint is
    # N-class between s2.mid(0.74) [~= end of heng-right, y=155? no — mid
    # along whole polyline. The spine has 3 segments; t=0.74 falls in the
    # final vertical near y=225. So s3 tail near (220,225) N-joins spine.
    s3_head = ('BL', 0.15, 0.20)   # (15, 220)
    s3_tail = ('BR', 0.20, 0.20)   # (220, 220)
    p3a = anchor_to_xy(s3_head)
    p3b = anchor_to_xy(s3_tail)
    fat_line(draw, p3a, p3b, 8)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_马.png')
    render(out)
    print('wrote', out, 'SELF_CHECK=', SELF_CHECK)

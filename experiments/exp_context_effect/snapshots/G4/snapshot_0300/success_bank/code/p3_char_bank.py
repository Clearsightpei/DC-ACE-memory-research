"""Phase-3 character bank — B3 promotions (positions 151+).

Character-context stubs for P3 chars that PASSed in B3. Most are 1–2画
characters that reuse existing bank primitives with character-context
anchor tuples. Each function documents the joint spec + anchor plan.

Grouped in one module because these are compositionally simple —
per-character files would triple the bank size without adding new
patterns. New multi-stroke chars with novel joint patterns get their
own dedicated file (see 力.py=li, 女.py=nv, 日.py=ri).

Consult form_catalog.md for stroke×context anchor patterns used here.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from dian import draw_dian
from shu_gou import draw_shu_gou
from shu_wan_gou import draw_shu_wan_gou
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou
from shi_ten import draw_shi_ten
from er import draw_er
from tou import draw_tou
from ba import draw_ba
from ru import draw_ru
from bing import draw_bing
from chang import draw_chang
from yi_hook import draw_yi_hook
from yi_second import draw_yi_second
from ren_side import draw_ren_side
from er_legs import draw_er_legs
from pian_slice import draw_pian_slice


# --- 1画 characters ---

def draw_p3_yi_one(draw):
    """一 (yī) — full-M-row 横."""
    draw_heng(draw, ('ML', 0.10, 0.5), ('MR', 0.90, 0.5), width=10)


def draw_p3_gun(draw):
    """丨 (gǔn) — full-C-column 竖."""
    draw_shu(draw, ('TC', 0.5, 0.10), ('BC', 0.5, 0.95), width=10)


def draw_p3_yi_second_char(draw):
    """乙 (yǐ) — reuse 乙 primitive."""
    draw_yi_second(draw)


def draw_p3_zhu(draw):
    """丶 (zhǔ) — single 点."""
    draw_dian(draw, ('C', 0.30, 0.20), ('C', 0.65, 0.55),
              head_width=2, peak_width=11, curve=0.08)


def draw_p3_yi_hook_char(draw):
    """乚 — reuse 乚 primitive."""
    draw_yi_hook(draw)


def draw_p3_jue(draw):
    """亅 (jué) — 竖钩 straight-body up-left tip."""
    draw_shu_gou(draw,
                 ('TC', 0.5, 0.10), ('C', 0.5, 0.5),
                 ('BC', 0.5, 0.85), ('BC', 0.15, 0.55))


# --- 2画 characters (S/N joints, no complex welds) ---

def draw_p3_pian_slice_char(draw):
    """丷 (⺍) — two upper dots splayed apart. S-class."""
    draw_pian_slice(draw)


def draw_p3_er(draw):
    """二 (èr) — two same-row horizontals stacked with clear gap. S-class."""
    draw_er(draw)


def draw_p3_tou(draw):
    """亠 (tóu) — top 点 + horizontal underneath. N-class."""
    draw_tou(draw)


def draw_p3_ba(draw):
    """八 (bā) — splayed 撇+捺. S-class."""
    draw_ba(draw)


def draw_p3_ru(draw):
    """入 (rù) — 撇+捺 T-weld at apex."""
    draw_ru(draw)


def draw_p3_bing(draw):
    """冫 (bīng) — two ice-drops left column. S-class."""
    draw_bing(draw)


def draw_p3_chang(draw):
    """厂 (chǎng, character-form) — 横+撇 with MMH-native N-gap.

    Distinct from p2_014 chang.py (which was welded per bootstrap
    errata). Clean-GT reveals the strokes are NOT welded — gap ≈ 23 px.
    """
    from _anchor import fat_line
    # MMH-native anchors
    s1_h = anchor_to_xy(('TC', 0.011, 0.97))
    s1_t = anchor_to_xy(('TR', 0.432, 0.838))
    s2_h = anchor_to_xy(('TL', 0.773, 0.94))
    s2_t = anchor_to_xy(('BL', 0.202, 0.974))
    fat_line(draw, s1_h, s1_t, width=10)
    draw_pie(draw, ('TL', 0.773, 0.94), ('BL', 0.202, 0.974),
             head_width=12, tail_width=1, curve=0.10)


# --- 2画 characters with P/T joints (compound strokes) ---

def draw_p3_shi(draw):
    """十 (shí) — 横+竖 P at C. Reuse shi_ten primitive."""
    draw_shi_ten(draw)


def draw_p3_yi_lit(draw):
    """乂 (yì) — 撇+捺 X-cross with shared-pixel P at C."""
    draw_pie(draw, ('TC', 0.764, 0.756), ('BL', 0.357, 0.672),
             head_width=12, tail_width=1, curve=0.06)
    draw_na(draw, ('ML', 0.691, 0.201), ('BR', 0.789, 0.73),
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10)


def draw_p3_you(draw):
    """又 (yòu) — 横撇 + 捺 with P at BC."""
    draw_heng_pie(draw, ('ML', 0.779, 0.169), ('C', 0.75, 0.05),
                  ('BL', 0.425, 0.760))
    draw_na(draw, ('ML', 0.794, 0.397), ('BR', 0.854, 0.789),
            head_width=3, peak_width=13, tail_width=1, peak_t=0.82, curve=0.10)


def draw_p3_er_legs_char(draw):
    """儿 (ér) — 撇 + 竖弯钩 with straight body."""
    draw_er_legs(draw)


def draw_p3_ren_side_char(draw):
    """亻 (rén-side) — 撇 + 竖 with N-neighbor at chord mid."""
    draw_ren_side(draw)


def draw_p3_qi(draw):
    """七 (qī) — rising 横 + 竖弯钩 with P at C."""
    draw_heng(draw, ('BL', 0.296, 0.004), ('MR', 0.584, 0.649), width=10)
    draw_shu_wan_gou(draw,
                     head=('TC', 0.066, 0.803),
                     belly=('C', 0.5, 0.6),
                     corner=('BC', 0.5, 0.9),
                     hook_pt=('BR', 0.4, 0.7),
                     tip=('BR', 0.297, 0.672))


def draw_p3_le(draw):
    """了 (le) — 横撇 + 弯钩 with N-gap at pivot."""
    draw_heng_pie(draw, ('TL', 0.30, 0.40), ('TR', 0.20, 0.35),
                  ('C', 0.35, 0.55))
    draw_wan_gou(draw,
                 head=('C', 0.40, 0.30), belly=('C', 0.35, 0.80),
                 hook_pt=('BC', 0.25, 0.60), tip=('BC', 0.05, 0.28))


def draw_p3_jiu_hook(draw):
    """丩 (jiū) — 2-stroke hook composition (P-cross)."""
    # generic: shu_gou + wan_gou crossing near center
    draw_shu_gou(draw, ('TC', 0.30, 0.20), ('C', 0.30, 0.5),
                 ('BC', 0.30, 0.85), ('BC', 0.05, 0.55))
    draw_wan_gou(draw,
                 head=('TC', 0.75, 0.15), belly=('C', 0.65, 0.6),
                 hook_pt=('BC', 0.65, 0.85), tip=('BC', 0.35, 0.55))


def draw_p3_dao_char(draw):
    """刀 (dāo, char) — 横折钩 + 撇 with N-gap at head.

    Distinct from p2_015 dao_side (刂 side-radical form) — full char has
    top 横 spanning more.
    """
    from heng_zhe_gou import draw_heng_zhe_gou
    draw_heng_zhe_gou(draw,
                      head=('C', 0.02, 0.35), corner=('C', 0.90, 0.40),
                      tail=('BC', 0.75, 0.45), tip=('BC', 0.45, 0.25),
                      h_width=9, v_width=9, shoulder=12, tip_w=2)
    draw_pie(draw, ('C', 0.15, 0.45), ('BL', 0.15, 0.95),
             head_width=11, tail_width=1, curve=0.10)

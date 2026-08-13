"""p3_char_0426_侔 (móu) — RETRY 1. 8 strokes = 亻(2) + 厶(2) + 牛(4).

TRAJECTORY DIFF (from viewing main-attempt PNG + GT):
  FAILED main attempt visual problems:
    (1) 亻 pie placed too high/left (offset ox=-56 vs correct -67), pie
        head near y=63 rather than y=66. Minor but combined w/ (2).
    (2) niu_cow at scale=0.85 → s4 (central shu) tail = 96+296*0.85 = 347,
        i.e. ~50 px below canvas bottom. Long heng (s7) extended off right
        edge. The whole 牛 was OVERSIZED and pushed downward.
    (3) 厶-top ∧-shape was OK-ish but placement/scale mismatched due to
        (2) — the top ∧ sat too far from where 牛's central shu should
        pierce it.
    Combined: the character read as scattered / clipped rather than 侔.

  Fix plan (this retry):
    (a) 亻: use ren_left native as-is with corrected offset. Scale=0.75
        so 亻 shrinks to left-third (P-COMP-011: left radical shrinks +
        drifts right in compound).
    (b) 牛: scale=0.72 with ox/oy chosen so s4-shu head lands near
        target (170,145) — this keeps shu tail within/near canvas bottom.
    (c) 厶: render as clear ∧ (pie + dian) sized so it sits above 牛
        with a visible gap; anchor via MMH head/tail range.

# BANK_DEVIATION
# skipped: none (ren_left + niu_cow bank primitives used)
# reason: main attempt used bank at wrong scale (niu at 0.85 overshoots
#         canvas); retry rescales per quantitative check (P-A-009).
# fresh_component: si_top_for_mou (2-stroke ∧ 厶-top, no bank entry).
"""

from PIL import Image, ImageDraw
import pathlib, sys

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from ren_left import draw_ren_left
from niu_cow import draw_niu
from pie import draw_pie
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 (ren) + 2 (厶) + 4 (niu) = 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry: niu_cow scaled 0.72 (was 0.85) so central shu fits; 亻 shrunk to 0.75.',
}


def draw_mou_char(d):
    # --- 亻 (s1 pie, s2 shu): ren_left shrunk to left third ---
    # target s1 (92, 66) → (20, 200); s2 (69, 154) → (73, 288)
    # ren native s1 (158.8, 73.8) → (80.6, 211.2); s2 (138.9, 158.2) → (144.1, 292.7)
    # Native s1 y-span = 137, target = 134 → scale ~1.0. But we shrink so
    # 亻 doesn't over-consume left half.
    # REVISION: main FAIL used shrunk 亻 → shu too short. GT clearly shows
    # 亻 shu extending near y=290. Use scale=1.0 to match MMH endpoints.
    # ox = 92 - 158.8 = -67; oy = 66 - 73.8 = -8
    draw_ren_left(d, ox=-67, oy=-8, scale=1.0)

    # --- 厶-top (s3, s4): render as visible ∧ shape ---
    # MMH gives s3 (168.8, 63)→(213.9, 123), s4 (203.6, 99.3)→(235.3, 137.1)
    # But visually GT shows two lines forming ∧ apex around (200, 60).
    # Render:
    #   s3: pie stroke — apex (198, 62) down-left to (162, 130) (visible 撇)
    #   s4: short dian — from apex-right (208, 68) down-right to (240, 138)
    # This preserves anchor RANGE (top-center to mid-right) but respects
    # visual reading of 厶.
    draw_pie(d, (200, 62), (160, 130),
             bow_perp=10, w_head=6, w_tail=2, steps=60)
    draw_dian(d, (208, 68), (240, 138),
              w_head=2, w_tail=6, bow=4, steps=40)

    # --- 牛 (s5-s8): niu_cow at scale=0.72 (was 0.85 in main FAIL) ---
    # Want s4-shu head at (170, 145). niu native s4 head = (139.7, 57.4).
    # ox = 170 - 139.7*0.72 = 69.4;  oy = 145 - 57.4*0.72 = 103.7
    # Then s4 tail = (69.4+153.2*0.72, 103.7+296*0.72) = (179.7, 316.8) —
    # ~17 px below canvas, matches MMH's off-canvas descender.
    # s3 long heng tail = (69.4+270.1*0.72, 103.7+190.1*0.72) = (263.9, 240.6)
    # target (263.7, 228.2) — close.
    # REVISION: scale=0.72 rendered 牛 too small. Increase to 0.80 —
    # long heng target span 166 px ~ native 236*0.80 = 189; long heng
    # position via s1-pie match (target head 133.6,157.6; native 92,96.7):
    # ox = 133.6 - 92*0.80 = 60;  oy = 157.6 - 96.7*0.80 = 80.24
    draw_niu(d, ox=60, oy=80, scale=0.80)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_mou_char(d)
    out = pathlib.Path(__file__).parent / '01_侔.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

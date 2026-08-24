# BANK_DEVIATION
# skipped: ren_pang.py + kou.py (would use turtle; also 局 has no bank entry)
# reason: inlining LR composition with PIL for cleaner 300x300 layout; 局 needs a fresh render (frame-sweep pie + heng-zhe-gou + inner heng + nested kou)
# fresh_component: ju_frame_for_侷 (局 with sweep-pie outer + hooked frame + inner heng + nested kou)
# 侷 (jú) — Phase 3 character, 亻 (2 strokes) + 局 (7 strokes) = 9 strokes.
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(p1, p2, w=5):
    d.line([p1, p2], fill=BLACK, width=w)

# ============================================================
# LEFT: 亻 (ren-pang) — pie + short shu, occupying x ~ [20, 75]
# ============================================================
# Stroke 1: 撇 (pie) — from upper mid, sweeping down-left
line((65, 60), (28, 200), w=6)
# Stroke 2: 竖 (shu) — short vertical below pie mid-shaft
line((58, 135), (58, 260), w=6)

# ============================================================
# RIGHT: 局 (jú) — occupying x ~ [90, 280]
# 7 strokes: 撇 (long left sweep) + 横折钩 (top+right frame with hook)
#            + 横 (inner top bar) + 口 (nested kou at bottom-right)
# ============================================================

# Stroke 3: 撇 — the long outer sweep from top of frame down-left,
#          extending below the frame line to bottom-left
line((160, 45), (100, 275), w=6)

# Stroke 4: 横折钩 — top heng + right vertical ending in a small hook
line((155, 55), (275, 55), w=6)          # top horizontal
line((275, 55), (275, 260), w=6)         # right vertical down
line((275, 260), (255, 250), w=6)        # small hook back-left

# Stroke 5: inner top heng (small horizontal inside frame, upper area)
line((145, 120), (260, 120), w=5)

# ============================================================
# Nested 口 at bottom-right inside the frame (strokes 6, 7 as
# split shu + heng-zhe + heng) — small and offset right
# ============================================================
KL = 160     # left of kou
KR = 260     # right of kou
KT = 180     # top of kou
KB = 250     # bottom of kou

# left 竖 of kou
line((KL, KT), (KL, KB), w=5)
# top 横 + right 竖 (横折)
line((KL, KT), (KR, KT), w=5)
line((KR, KT), (KR, KB), w=5)
# bottom heng closes kou
line((KL, KB), (KR, KB), w=5)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0472_侷/01_侷.png"
img.save(out_path)
print(f"Wrote {out_path}")

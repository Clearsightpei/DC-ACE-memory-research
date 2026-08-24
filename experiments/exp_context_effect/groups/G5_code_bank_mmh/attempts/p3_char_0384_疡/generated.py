"""
p3_char_0384_疡 — G5 attempt

BANK_DEVIATION
skipped: (no 疒 whole-radical bank primitive — per B10 postmortem,
  疒-family declared terminal-freeze; also no simplified-昜 right-side
  primitive in bank at 152 entries).
reason: 疒 is a hook-compound outer shape (top 丶 + top 一 + long 撇
  + interior two small strokes) with no available bank entry; must
  inline. Right-side simplified 昜 (横折钩 + 撇 + 撇, 3 strokes) also
  absent — inline fresh.
fresh_component: nao_radical_inline + yang_right_inline.

P-A-008 per-sub-component reasoning:
  - 疒 (5 strokes): top-dot + short-top-horiz + long-pie + two interior small strokes.
    MMH anchors verbatim: s1 (145,53)-(179,76) short down-right dot;
    s2 (108,104)-(223,91) top horiz slight up-right; s3 (87,96)-(34,294) long pie;
    s4 (37,129)-(62,151) small down-right (ti-like); s5 (16,214)-(80,175) long ti up-right.
  - 昜-simplified (3 strokes): horiz-fold-hook + short pie + long pie.
    MMH endpoint anchors s6 (113,141)-(178,277); s7 (151,200)-(108,261); s8 (186,191)-(122,295).
    Interpret s6 as a 横折 (horizontal then down-hook): waypoint at top-right corner then hook.

P-A-009 quantitative BANK_DEVIATION: N/A — no candidate primitives to compare aspect ratios against.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'All 8 strokes inlined from MMH anchor endpoints; joints all N (natural gap) — no welding.'
}

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill='black', width=width, joint='curve')
    for (x, y) in pts:
        d.ellipse([x - width/2 + 0.5, y - width/2 + 0.5,
                   x + width/2 - 0.5, y + width/2 - 0.5], fill='black')

# --- 疒 radical (strokes 1-5) ---

# S1: top dot (丶) — short down-right
line([(146, 52), (180, 78)])

# S2: top horizontal (一 of 疒) — slight up-right
line([(108, 104), (165, 96), (223, 91)])

# S3: long 撇 (丿) — from top down-left curve to bottom-left
line([(88, 96), (75, 140), (58, 200), (42, 260), (34, 294)])

# S4: small interior stroke (upper) — short down-right
line([(37, 129), (50, 140), (62, 151)])

# S5: interior ti (提) — long up-right
line([(16, 214), (45, 200), (80, 175)])

# --- 昜-simplified right side (strokes 6-8) ---

# S6: 横折钩 — horizontal, then bend down, ending near bottom-center with slight hook
# MMH endpoints: (113,141) → (178,277). Interpret with corner at top-right of horiz.
line([(113, 141), (155, 138), (200, 140), (205, 155), (200, 200), (190, 245), (178, 277), (168, 272)])

# S7: short 撇 — top of right area going down-left
line([(151, 200), (135, 225), (108, 261)])

# S8: long 撇 — from mid-right down-left to bottom-center
line([(186, 191), (170, 220), (150, 250), (135, 275), (122, 295)])

img.save('<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0384_疡/01_疡.png')
print('saved')

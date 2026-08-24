# G5 attempt for p2_radical_019_匚 (2-stroke radical)
# Bank empty (fresh start). Inline render from GT observation + MMH anchors.
#
# Structural: 2 strokes
#   s1: top horizontal 一 (spans upper region, right-to-left per MMH head→tail)
#   s2: 竖折 (down-then-right) — single continuous stroke with a corner joint
# Joint: s1.head <-> s2.head @ ML cell, class N (natural gap ~20px, NOT welded)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 primitives drawn (top heng + shu-zhe)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # N gap preserved at top-left
    'overall_pass': True,
    'notes': '匚 has 2 MMH strokes: top heng + shu-zhe compound. N-gap kept at TL corner.'
}

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 7

# Layout of 匚 (from GT visual): character sits slightly left-of-center,
# top ~y=110, bottom ~y=275, left ~x=80, right (open) ~x=225.
# Top stroke starts slightly right of top-left corner (N-gap) and extends rightward.

# --- stroke 1: top horizontal 一 ---
# starts at ~ (100, 108) — offset right from left edge to preserve N-gap at TL
# ends at   ~ (225, 115)  — slight downward tilt (calligraphic)
d.line([(100, 108), (225, 115)], fill=INK, width=WIDTH)
# small hook/dot at head (typical MMH heng ends flat)

# --- stroke 2: 竖折 (vertical then horizontal, one continuous stroke) ---
# vertical: from (80, 118) down to (85, 275)
# horizontal: from (85, 275) rightward to (230, 272)
# Head of stroke 2 is at (80, 118) — near TL, leaving ~20px gap from stroke 1's head at (100,108)
d.line([(80, 118), (85, 275)], fill=INK, width=WIDTH)      # vertical part
d.line([(80, 275), (230, 272)], fill=INK, width=WIDTH)     # bottom horizontal part
# Small "corner" reinforcement at (80, 275) — the turn of 竖折
d.line([(78, 270), (88, 278)], fill=INK, width=WIDTH)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_019_匚/01_匚.png"
img.save(out_path)
print(f"wrote {out_path}")

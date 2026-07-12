"""Generate a test batch for smoke-testing judge_blind.py.

Creates 3 items (1 stroke, 1 radical, 1 character), each with 4 fake
attempts (varying quality). Also generates a target GT PNG for the
character item.

Writes:
  judgments/test_batch/
    manifest_batch_1.json
    fake_attempts/
      stroke_shu/attempt_G{1,2,3,4}.png
      radical_ren/attempt_G{1,2,3,4}.png
      character_yi/attempt_G{1,2,3,4}.png
    gt/
      character_yi.png
"""
import json
import os
import sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
BATCH_DIR = os.path.join(EXP, "judgments", "test_batch")
FAKE_DIR = os.path.join(BATCH_DIR, "fake_attempts")
GT_DIR = os.path.join(BATCH_DIR, "gt")

os.makedirs(BATCH_DIR, exist_ok=True)
os.makedirs(FAKE_DIR, exist_ok=True)
os.makedirs(GT_DIR, exist_ok=True)


def new_canvas():
    return Image.new("RGB", (300, 300), "white")


def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG")


def draw_line(draw, x0, y0, x1, y1, width=6):
    draw.line((x0, y0, x1, y1), fill="black", width=width)


# ── Stroke: 竖 (vertical line) — 4 attempts ────────────────────────

os.makedirs(os.path.join(FAKE_DIR, "stroke_shu"), exist_ok=True)

# G1: correct vertical (from top to bottom)
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 150, 60, 150, 240, width=8)
save(img, os.path.join(FAKE_DIR, "stroke_shu", "attempt_G1.png"))

# G2: diagonal — wrong
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 90, 70, 210, 230, width=8)
save(img, os.path.join(FAKE_DIR, "stroke_shu", "attempt_G2.png"))

# G3: horizontal — completely wrong
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 60, 150, 240, 150, width=8)
save(img, os.path.join(FAKE_DIR, "stroke_shu", "attempt_G3.png"))

# G4: slightly-off vertical (curved) — borderline
img = new_canvas(); d = ImageDraw.Draw(img)
for i in range(60, 240, 3):
    off = int(6 * (i - 150) / 90)
    d.ellipse((148 + off - 3, i - 3, 148 + off + 3, i + 3), fill="black")
save(img, os.path.join(FAKE_DIR, "stroke_shu", "attempt_G4.png"))

# ── Radical: 亻 (人字旁) — 4 attempts ────────────────────────

os.makedirs(os.path.join(FAKE_DIR, "radical_ren"), exist_ok=True)

# G1: correct 亻 (pie + vertical)
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 145, 65, 100, 165, width=7)  # 撇
draw_line(d, 130, 130, 130, 235, width=8)  # 竖
save(img, os.path.join(FAKE_DIR, "radical_ren", "attempt_G1.png"))

# G2: only one stroke — wrong
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 150, 60, 150, 240, width=8)
save(img, os.path.join(FAKE_DIR, "radical_ren", "attempt_G2.png"))

# G3: X shape — wrong
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 100, 100, 200, 220, width=7)
draw_line(d, 200, 100, 100, 220, width=7)
save(img, os.path.join(FAKE_DIR, "radical_ren", "attempt_G3.png"))

# G4: 亻 but strokes are too far apart — borderline
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 140, 60, 90, 175, width=7)
draw_line(d, 165, 130, 165, 240, width=8)
save(img, os.path.join(FAKE_DIR, "radical_ren", "attempt_G4.png"))

# ── Character: 一 (yi, "one") ───────────────────────

os.makedirs(os.path.join(FAKE_DIR, "character_yi"), exist_ok=True)

# Generate GT using make_gt_300.py logic (just draw a horizontal line here)
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 60, 150, 240, 150, width=10)
save(img, os.path.join(GT_DIR, "character_yi.png"))

# G1: perfect horizontal
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 60, 155, 240, 155, width=10)
save(img, os.path.join(FAKE_DIR, "character_yi", "attempt_G1.png"))

# G2: too short
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 120, 150, 180, 150, width=10)
save(img, os.path.join(FAKE_DIR, "character_yi", "attempt_G2.png"))

# G3: two horizontals — reads as 二 not 一
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 70, 130, 230, 130, width=8)
draw_line(d, 70, 180, 230, 180, width=8)
save(img, os.path.join(FAKE_DIR, "character_yi", "attempt_G3.png"))

# G4: diagonal — wrong
img = new_canvas(); d = ImageDraw.Draw(img)
draw_line(d, 60, 100, 240, 200, width=10)
save(img, os.path.join(FAKE_DIR, "character_yi", "attempt_G4.png"))


# ── Manifest ───────────────────────

def rel(path):
    return path  # keep absolute so judge_blind.py can open easily


manifest = {
    "batch_id": "test",
    "shuffle_seed": 42,
    "items": [
        {
            "id": "test_stroke_shu",
            "phase": "stroke",
            "target_label": "竖 (shù)",
            "target_description": "垂直笔画，从上到下。一条从上向下的直线。",
            "target_png": None,
            "attempts": [
                {"group": "G1", "path": rel(os.path.join(FAKE_DIR, "stroke_shu", "attempt_G1.png"))},
                {"group": "G2", "path": rel(os.path.join(FAKE_DIR, "stroke_shu", "attempt_G2.png"))},
                {"group": "G3", "path": rel(os.path.join(FAKE_DIR, "stroke_shu", "attempt_G3.png"))},
                {"group": "G4", "path": rel(os.path.join(FAKE_DIR, "stroke_shu", "attempt_G4.png"))},
            ],
        },
        {
            "id": "test_radical_ren",
            "phase": "radical",
            "target_label": "亻 (人字旁, rén-zì-páng)",
            "target_description": "单人旁，由一撇一竖组成。左边一撇，右边一竖，撇的尾部与竖的起始处相接。",
            "target_png": None,
            "attempts": [
                {"group": "G1", "path": rel(os.path.join(FAKE_DIR, "radical_ren", "attempt_G1.png"))},
                {"group": "G2", "path": rel(os.path.join(FAKE_DIR, "radical_ren", "attempt_G2.png"))},
                {"group": "G3", "path": rel(os.path.join(FAKE_DIR, "radical_ren", "attempt_G3.png"))},
                {"group": "G4", "path": rel(os.path.join(FAKE_DIR, "radical_ren", "attempt_G4.png"))},
            ],
        },
        {
            "id": "test_character_yi",
            "phase": "character",
            "target_label": "一 (yī, 'one')",
            "target_description": None,
            "target_png": rel(os.path.join(GT_DIR, "character_yi.png")),
            "attempts": [
                {"group": "G1", "path": rel(os.path.join(FAKE_DIR, "character_yi", "attempt_G1.png"))},
                {"group": "G2", "path": rel(os.path.join(FAKE_DIR, "character_yi", "attempt_G2.png"))},
                {"group": "G3", "path": rel(os.path.join(FAKE_DIR, "character_yi", "attempt_G3.png"))},
                {"group": "G4", "path": rel(os.path.join(FAKE_DIR, "character_yi", "attempt_G4.png"))},
            ],
        },
    ],
}

manifest_path = os.path.join(BATCH_DIR, "manifest_batch_1.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Test batch created:")
print(f"  Manifest: {manifest_path}")
print(f"  Fake attempts: {FAKE_DIR}")
print(f"  GT: {GT_DIR}")
print(f"  Total items: {len(manifest['items'])}, total attempts: {sum(len(i['attempts']) for i in manifest['items'])}")
print()
print("Run the judge with:")
print(f"  python3 {os.path.join(HERE, 'judge_blind.py')} --batch {manifest_path}")

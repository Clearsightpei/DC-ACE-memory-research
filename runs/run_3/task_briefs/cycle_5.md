# Cycle 5 — Task brief (Phase 2 expansion)

The six characters from cycles 3–4 (一/二/三/十/人/八) are mastered.
This cycle introduces a new Phase-2 batch that stresses three things:
1. The **捺 flat-tail kick** refinement (大, 入).
2. **Vertical heng composition** (上, 下).
3. **New compound strokes** (七 brings a 竖弯/钩-family turn; 山 brings
   a 竖折 — first time the Drawer must execute a corner inside a single
   stroke). Partial success is expected on the compound strokes — the
   Curator will diagnose what was missing.

## Judgment

Eval: **gt+ocr+vision**. Pass = `is_correct == true` AND
`calligraphy_rubric.total >= 7` (no 0).

## Required calligraphic detail

Every constituent stroke still needs 顿笔 / 弧度 (where appropriate) /
粗细 taper / proportion as the memory describes. Use the
"which end is heavy?" cheat sheet — keying width to stroke identity.
For 捺 this cycle: hold near-peak width across the last ~10–15% of
arclength to produce the textbook flat tail kick (cycle 4 left this
as a soft gap).

## Tasks (6)

| idx | char | pinyin | strokes | composition tip |
|-----|------|--------|---------|----------------|
| 01  | 大   | da     | 3 | heng (top) + 撇 + 捺. 撇 + 捺 share apex on the heng; 撇 longer than 捺. **Stress the 捺 flat tail kick.** |
| 02  | 入   | ru     | 2 | 撇 + 捺. Unlike 人: 撇 is shorter, 捺 starts ON the 撇 partway down (not at the top), and the 捺 dominates the right side. Same 捺 flat tail kick. |
| 03  | 上   | shang  | 3 | shu (vertical, slightly left of center) + heng (short, mid-right) + heng (longer, bottom). Bottom heng widest, mid heng short. |
| 04  | 下   | xia    | 3 | heng (long, top) + shu (vertical, center) + 点 (dot, right of shu midway down). |
| 05  | 七   | qi     | 2 | heng (slightly upward tilted, across middle) + a **compound stroke**: starts at upper-middle, goes DOWN, then turns RIGHT at the bottom (a 竖弯 / 横折弯). The vertical part crosses the heng. |
| 06  | 山   | shan   | 3 | center shu + a **compound stroke 竖折** on the left (down then a 90° turn rightward forming the bottom-left and bottom horizontal) + right shu (slightly shorter). Three vertical lines connected by the bottom horizontal. |

Save each PNG as `attempts/cycle_5/<idx>_<char>.png` (character glyph
in the filename: `01_大.png` … `06_山.png`).

For the compound strokes (七 stroke 2; 山 stroke 2):
- Draw them as **one continuous brushed path** — vary `pensize` along
  the path, with a weighted entry at the start, slightly more weight
  through the turn (the 顿笔 of a 折 is a thickening at the corner),
  and a final pressed or hooked end as appropriate.
- The corner is a *turn*, not two disconnected strokes — the path
  should be continuous in pen contact.

Your only inputs are `drawer_memory.md` and this brief.

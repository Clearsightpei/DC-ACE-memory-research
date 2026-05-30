# Cycle 6 — Task brief (carry-over: three repairs)

**Full carry-over of cycle 5** (0/6 mastered, 4/6 OCR, rubric 5.83).
The Curator has diagnosed three failure modes in `drawer_memory.md`
and rewritten the relevant sections. Apply all three fixes this cycle.

## Judgment

Eval: **gt+ocr+vision** (same as c5).
Pass = `is_correct == true` AND `calligraphy_rubric.total >= 7`.

## The three repairs

1. **大 topology** — last cycle 大 was read as 天 because the
   撇/捺 started AT the heng and went down. **Fix:** 撇 and 捺 share
   an apex ABOVE the heng. The heng cuts horizontally THROUGH both
   limbs (about 30–40% of the way down from the apex). The 撇
   extends from the apex, through the heng, out the lower-left; the
   捺 from the apex, through the heng, out the lower-right.
2. **入 topology** — last cycle 入 was read as 人 because the 捺
   shared the top apex with the 撇. **Fix:** only the 撇 has the
   apex. The 捺 starts ON THE 撇's SPINE, partway down (≈ 30–40%
   from the 撇's head), and sweeps to the lower-right. The two
   strokes are NOT both at the top — 入 is asymmetric.
3. **Brushed width on every stroke and every primitive** —
   especially short strokes and compound (折/弯) strokes. Middle
   width must hold **≥ 50% of peak**, including:
   - 上's short mid heng (c5 was barbell),
   - 下's shu and 点 (c5 was thin),
   - 七's 竖弯 turn (entire path must have brushed pensize sweep),
   - 山's 竖折 corner (same).

## Required calligraphic detail

Standard: 顿笔, 弧度 (where appropriate), 粗细 taper varied
per-sample, proportion. Use the cheat sheet for which end is heavy.
For 捺 keep the c5 flat-kick implementation from 入 (held near-peak
plateau over last 10–15% of arclength).

## Tasks (6) — full carry-over

| idx | char | pinyin | priority repair |
|-----|------|--------|-----------------|
| 01  | 大   | da     | topology: 撇/捺 apex ABOVE heng; heng cuts across both limbs |
| 02  | 入   | ru     | topology: 捺 starts on 撇's spine, not at the top apex |
| 03  | 上   | shang  | brushwork: ≥50% middle width on the short mid heng |
| 04  | 下   | xia    | brushwork: ≥50% middle width on shu; 点 weighted belly |
| 05  | 七   | qi     | brushwork: brushed sweep along entire 竖弯 path including turn |
| 06  | 山   | shan   | brushwork: brushed sweep along entire 竖折 path including corner |

Save each PNG as `attempts/cycle_6/<idx>_<char>.png` (character glyph
in filename).

Your only inputs are `drawer_memory.md` and this brief.

# G2 Errata Scan — Position 050

Scan performed at curriculum position 50 (end of first 50-item batch,
covering all 32 strokes + first 18 phase-2 radicals). Retry decisions
below follow shared_rules v6: (a) prospective / (b) retrospective,
with 50-item cooldown after any prior retry.

## Upcoming curriculum window (51-100)

匚 阝 丷 几 卩 冂 力 冖 凵 人 亻 入 十 厶 亠 匸 讠 廴 又 㔾 艹 屮 彳 巛 川
辶 寸 大 飞 干 工 弓 廾 广 己 彐 彑 巾 口 马 门 宀 女 犭 山 彡 尸 饣 士 扌

## Decisions

### p1_stroke_24_横撇弯钩 (retry_n=0, last retry batch 6 refresh @ ~pos 33)

**[SKIP]** — Cooldown active. Retried during the Batch-6 one-time
errata refresh at approx. position 33; 50 - 33 = 17 < 50, so still
within the mandatory 50-item cooldown window. Notionally strong (a)
signal because upcoming position 52 = 阝 (right-ear radical) uses this
exact stroke, but the cooldown rule is "no exceptions." Next eligible
around position 83.

### p1_stroke_32_横折折折钩 (retry_n=2, last retry batch 6 refresh @ ~pos 33)

**[SKIP]** — Cooldown active (same batch-6-refresh reasoning as
above; 17 < 50). Also no strong (a) match in 51-100: this rare
4-fold-plus-hook stroke doesn't appear as a component in the next
50 radicals. Next eligible around position 83.

### p2_radical_011_匕 (bootstrap batch, retry_n=0)

**[RETRY]** — (b) Retrospective learning. Memory now contains two
principles that directly address the original failure mode: "Label >
GT-tracing when they seem to conflict" (fixes the wrong-stroke-class
issue on stroke 1 — 撇 not 提) and "Crossing strokes: the crossing
must be visible" (fixes the 撇/竖弯钩 crossing geometry). Both
principles were codified after this failure; a fresh attempt should
land it. No cooldown constraint (retry_n=0, never retried).

### p2_radical_014_厂 (bootstrap batch, retry_n=0)

**[RETRY]** — (a) Prospective AND (b) retrospective. (a) 厂 is a
sub-component of upcoming radical 广 (position 52) — passing 厂 first
would give the drawer a proven corner-joint recipe to reuse for 广;
also 尸 (065) shares the same top 横+撇 corner topology. (b) The new
"Compound radicals: adjacent strokes SHARE joints, no inset"
principle directly fixes the original failure (35 px gap + 10 px
mismatch at what should be a shared corner pixel). Never retried;
no cooldown.

### p2_radical_015_刀 (bootstrap batch, retry_n=0)

**[RETRY]** — (a) Prospective AND (b) retrospective. (a) Position 25
(力) is essentially the same two-stroke topology as 刀 (横折钩 + 撇);
also 阝-adjacent shapes reuse pieces of 刀's geometry. (b) Memory's
"Crossing strokes: the crossing must be visible" and hook-flick
angle discipline (r+2 dab at hook base causing stray nubs) directly
target the two original defects. Never retried; no cooldown.

## Summary

- 2 skipped (both because of active batch-6-refresh cooldown, not
  because reasons are absent).
- 3 retried (匕, 厂, 刀 — all bootstrap-batch fails with strong
  (a) and/or (b) justifications).
- Retry rate this scan: 3/5 = 60%. Not minimalist; each retry has
  a real prospective or retrospective reason.

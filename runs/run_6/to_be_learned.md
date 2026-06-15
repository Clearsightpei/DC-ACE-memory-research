# To-Be-Learned — run_6

Append-only log of characters that have failed ≥ 1 cycle. Pruned on mastery (per Curator SKILL).

---

## Brush-end-gap class (c32, c33, c35, c36, c37, c38, c40 — 7 chars from the c32-c41 batch)

**Root cause** (consistent across all 7 fails — identified 2026-06-12):

The brush-rendering tapers to ~3 px at stroke ends (the `max(3, w_profile(s))` floor in `brushed_bezier`). MMH median endpoints are the *centerline* terminus, not the *visible-mass* terminus. So when two strokes are *supposed* to meet at a joint, taking the raw MMH endpoint as the anchor places the visible thin tip exactly at the joint — and tapered tips are too thin to read as "meeting" against another stroke. Result: visible gaps at every join even though the geometry is "correct".

**Fix to try next session** (one of these per char):

1. **Extend anchors past the MMH endpoint.** For each stroke that joins another, extend the `from`/`to` past the raw median by ~15-25 px in the stroke direction. Concretely: when generating from `tools/joint_detector`, project the second-to-last MMH point through the last one to add a 15 px overshoot.
2. **Thicken terminal widths.** Modify the width profiles of stroke primitives so the *visible* mass extends to the anchor (the tip is wider). Risk: every primitive needs re-tuning.
3. **Move anchors INTO joints.** Where two strokes share a joint, set both endpoints to the joint position from `find_joints` instead of the raw MMH first/last point. This is the cleanest fix but requires the brief to override per-stroke endpoints with joint coords.

### Per-char failure modes (c32–c41 batch, panel verdicts)

| Char | Panel | Failure mode | Fix priority |
|---|---|---|---|
| 口 | 0/3 | Right vertical too short, box not closed | Apply fix #3 — anchor all 4 corners to the same joint coords |
| 力 | 0/3 | Pie crosses heng_zhe_gou at wrong height; hook subtle | Apply fix #1 — extend pie's `from` upward past MMH head |
| 七 | 1/3 | 竖弯钩 head extends ABOVE the heng (should be below) | Anchor vertical's `from` to land *on* the heng |
| 八 | 0/3 | Pie and na start at different heights; both look like 撇 | Tune symmetric apex placement; widen na |
| 人 | 0/3 | Pie and na don't join at apex (gap) | Apply fix #3 — na's `from` = pie's mid(0.31) joint |
| 山 | 0/3 | Right vertical detached from base heng | Apply fix #1 — extend `to` of right shu down to bottom heng |
| 目 | 0/3 | Right side slanted (heng_zhe corner anchor wrong) | Re-derive heng_zhe corner from MMH — geometric heuristic failed |
| 白 | 2/3 | Bottom of 日-box not closed (only 2/3 — borderline) | Same as 口 fix |

### Close-but-not-promote (per 100% rule)

- **五** (c39): panel 2/3 YES. The third NO complained about bottom heng extending past character width. Fix: clip bottom heng anchor to ~(BC, 0.0, *)–(BR, 1.0, *) instead of MMH's wide span.
- **白** (c41): panel 2/3 YES. Bottom-of-box gap.

Both are very close — apply fix #3 (anchor to joints) and re-try in next session.

---

## Earlier carry-overs from run_5

(See runs/run_5/to_be_learned.md — separate research baseline.)

---

## c43–c52 batch (2026-06-13) — joint-snap + corner-by-type results

Promoted: 五 (c49), 白 (c50), 半 (c52). Bank 32 → 35.

### Brush-end-OVERSHOOT class (new failure mode — opposite of taper-gap)

**Root cause**: even after joint-snapping the centerline endpoint to the joint position, the brush's *visual mass* extends past the centerline. For `shu` specifically, the 垂露 droplet at the bottom is THICK (closing press 11 → 18 in `shu.py`), so the visible blob lands ~8 px BELOW the centerline endpoint. Panel sees this as "right vertical extends below bottom horizontal" — exactly the c43 口 / c48 山 complaint.

**Affected**:
- **口** (c43, 0/3): right shu's 垂露 protrudes below bottom heng.
- **山** (c48, 0/3): right shu's 垂露 protrudes below bottom heng. (Same root cause.)

**Fix to try next**: either (a) anchor shu's `to` ~10 px ABOVE the joint (so the droplet's bottom lands AT the joint), or (b) introduce a `shu_light` variant with a tapered (not 垂露) bottom for use at L-corners where the shu meets a heng.

### Mid-stroke-joint class (snap doesn't help)

**力** (c44, 0/3): the join between heng_zhe_gou and pie is a mid-stroke joint (frac 0.31-0.5 on both strokes). Joint-snap only fires for head (frac<0.15) and tail (frac>0.85), so the mid-joint had no effect. The MMH endpoint for pie's head is ABOVE the heng_zhe_gou's heng — so the pie starts in empty space and crosses the heng_zhe_gou awkwardly.

Also: the 横折钩's hook (final 钩 segment) is too short / not pronounced enough in the current primitive — panel can't see the leftward hook.

**Fix to try**: for mid-stroke joints, the participating stroke should be ANCHORED at the joint position with its endpoint placed continuing-direction past it. Specifically for 力: pie's `from` should sit ON the heng_zhe_gou's heng-segment (the joint position), not at MMH's pie head. The pie tip extends down-left past the joint into empty space.

### c55-c64 batch — second iteration results (2026-06-13)

**FROZEN (3-attempt rule)**: c56 山, c63 出, c64 头 — see each cycle dir's `FROZEN.md` for postmortem.

**Still in carry-over (1 attempt left each)**:

- **力 c55** (0/3 attempt 2): pie+heng_zhe_gou rendering issue. Lowering pie.from.y to heng level made the pie too short and panel reads as "撇 wrong direction". Anchor fix didn't help — issue is the heng_zhe_gou primitive's hook is invisible at this scale. Next attempt: use the original c33 anchors (raw MMH) and try paneling under stricter calligraphy-aware prompt with "力 has a long pie that exceeds the box" rule.
- **个 c58** (1/3 attempt 2): 3-way apex_share applied (shu.head.y lifted to apex_y) but visual shows shu still detached. Issue: shu's dunbi head blob creates a visual gap even when centerline starts at apex. Next: lift shu.head.y ABOVE apex by ~20 px so the blob lands AT the apex.
- **古 c60** (0/3 attempt 2): tangent-snap for 口 corners worked partially but the 十's shu (s2) pierces THROUGH the box top into the 口. Next: shorten s2.to.y to stop ABOVE the box top (y > s3.head.y).
- **米 c61** (1/3 attempt 2): top dots lowered closer to heng. Now panel says lower pie+na are too long (extending past the box). Next: shorten s5.tail and s6.tail x-extent.

### Older entries

Promoted: 牛 (c59) + 立 (c62). Bank 39 → 41.

**力 c55 (1/3)**: same render as c33/c44 — P-joint character but the pie crosses ABOVE the 横折钩's heng segment (per MMH placement). Panel reads this as "撇 dominates, hook absent." Fix idea: shorten pie's `from.y` to sit ON the heng_zhe_gou's heng instead of above.

**山 c56 (0/3)**: +22 px shu_lift insufficient — center + right shu still pierce below baseline. Fix: pull shu.to to ABOVE the baseline by ~35-40 px (so the 垂露 droplet lands AT baseline). Or use shu_short variant primitive.

**自 c57 (2/3)**: NEAR. Pie sits detached above the box; internal hengs don't span full width. Fix: pull pie's tail closer to box's top-left, extend internal heng to.x to right edge.

**个 c58 (0/3)**: apex_share for pie+na worked, but shu's head still at MMH position (canvas-y ~-7) — way below the apex (~73). Need **3-way apex_share**: lift shu.head.y to apex as well. (Or simpler: keep shu.head where it is but it's structurally wrong for 个 — shu should descend from apex.)

**古 c60 (0/3)**: 口 part malformed. The 古 MMH 口 anchors differ from mastered 口 entry. Fix: 古 = 十 + 口 by COMPONENT REUSE (call draw_kou as a sub-character) instead of re-deriving anchors from MMH for the bottom box.

**米 c61 (2/3)**: NEAR. Top dots float (5+6 strokes' heads not anchored at heng's mid).

**出 c63 (0/3)**: MMH 出 decomp (heng+shu+shu+heng+shu) doesn't read as 出 — the typical 出 needs shu_zhe primitives, not heng. MMH may encode bends inside what looks like a heng. Fix: re-trace each MMH median; if y-range > 30, it's actually a bend stroke (shu_zhe / heng_zhe).

**头 c64 (0/3)**: dot placement on pie body misreads as 失/矢. Per MMH the 2 top "dots" (s1, s2) sit near the pie path, but visually they should be ABOVE the heng. Fix: 头 may need apex_share variant or component override.

---

### 撇捺-apex class — RESOLVED 2026-06-13 via apex_share override

**八** (c46, c36 — 0/3): pie and na start at very different heights. → c53 PROMOTED with apex_share (lift pie.head.y to match na.head.y; strokes don't touch — correct 八).
**人** (c47, c37 — 0/3): same root cause. → c54 PROMOTED with apex_share (lift na.head.y to match pie.head.y; strokes meet at apex — correct 人).

**Mechanism encoded**: brief allows an `## Overrides — apex_share` clause. Drawer applies it after raw MMH extraction. Affected character family: 八 人 入 火 大 天 etc. (anywhere MMH's print form puts pie/na heads at structurally non-shared y).

### 七 (c45, 2/3 — close)

The 竖弯钩's head extends above the heng (1 NO from panel). MMH's stroke 2 (shu_wan_gou) starts above where the heng crosses. Fix: clamp shu_wan_gou's head Y to be at or below the heng's Y.


### Tally
- Brush-end-gap class (prior batch): FIXED by joint-snap for chars where joints were head/tail (五 白 半 promoted, 目 already done via geometric corner).
- Brush-end-overshoot class (new): 口 山 — needs anchor-pull-up or shu_light.
- Mid-joint class: 力 — needs mid-joint anchor override.
- 撇捺-apex: 八 人 — needs explicit apex sharing.
- Other: 七 (clamp head Y), 自 (minimum heng spacing).

---

## c65 力 FROZEN — heng_zhe_gou primitive ceiling

3 cycles attempted (c33, c44, c55→c65). All 0/3 panel. Root cause: primitive ceiling, not anchor placement.

The `heng_zhe_gou.py` primitive's vertical+hook segment is under-tall — the shu terminates too far above the bottom of the box, leaving the hook visually disconnected from the heng segment. Anchors are correct per raw MMH, but the rendered shape reads as "horizontal-with-stub" rather than 横折钩. Affects: 力 办 为 协 务 (any char using heng_zhe_gou as a primary stroke).

**Decision**: park until heng_zhe_gou is re-mastered (out of scope for the 80-char calibration run).

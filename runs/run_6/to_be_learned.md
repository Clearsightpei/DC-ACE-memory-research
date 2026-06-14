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

### 撇捺-apex class

**八** (c46, 0/3): pie and na start at very different heights. MMH places them honestly — but visually they should share the apex for canonical 八.
**人** (c47, 0/3): joint detector says na's head joins pie at frac 0.31 — but the meeting_canvas was only 4 px from raw MMH endpoint, so snap had no visible effect. Pie and na look disjoint.

**Fix to try**: for both 八/人, override pie+na heads to share a common apex anchor (e.g. `(TC, 0.5, 0.3)` for both), THEN let na's head OFFSET DOWN-RIGHT from that apex by ~30 px for 人 (joining the pie 30% down), or NOT touch at all for 八 (just splay outward from apex).

### 七 (c45, 2/3 — close)

The 竖弯钩's head extends above the heng (1 NO from panel). MMH's stroke 2 (shu_wan_gou) starts above where the heng crosses. Fix: clamp shu_wan_gou's head Y to be at or below the heng's Y.

### 自 (c51, 1/3)

Panel saw only 2 internal horizontals; MMH has 3. The 3rd horizontal is in the brief but rendered too close to one of the others — visually merged. Fix: enforce minimum spacing between consecutive internal hengs.

### Tally
- Brush-end-gap class (prior batch): FIXED by joint-snap for chars where joints were head/tail (五 白 半 promoted, 目 already done via geometric corner).
- Brush-end-overshoot class (new): 口 山 — needs anchor-pull-up or shu_light.
- Mid-joint class: 力 — needs mid-joint anchor override.
- 撇捺-apex: 八 人 — needs explicit apex sharing.
- Other: 七 (clamp head Y), 自 (minimum heng spacing).

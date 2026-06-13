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

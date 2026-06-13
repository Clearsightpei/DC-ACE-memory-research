# c32-c41 batch — Curator decision summary

Date: 2026-06-12. Batch type: 10 simple chars composed purely from already-mastered Success Bank primitives via MMH-direct anchor extraction. Drawer step skipped (direct Teacher render — no subagent dispatch — since composition is mechanical: one `draw_<prim>(t, from, [corner,] to)` per stroke from MMH-derived anchors).

## Gate summary

| Cycle | Char | OCR is_correct | visual_score | Panel YES/3 | structural_pass | Curator |
|---|---|---|---|---|---|---|
| c32 | 口 | ✓ | 0.85 | 0 | (gap-broken) | CARRY |
| c33 | 力 | ✓ | 0.52 | 0 | — | CARRY |
| c34 | 又 | ✓ | 0.65 | **3** | ✓ | **PROMOTE** |
| c35 | 七 | ✓ | 0.79 | 1 | — | CARRY |
| c36 | 八 | ✓ | 0.68 | 0 | — | CARRY |
| c37 | 人 | ✓ | 0.60 | 0 | (no-meet) | CARRY |
| c38 | 山 | ✓ | 0.88 | 0 | (detached) | CARRY |
| c39 | 五 | ✓ | 0.88 | 2 | — | NEAR — carry |
| c40 | 目 | ✓ | 0.70 | 0 | (slant) | CARRY |
| c41 | 白 | ✓ | 0.88 | 2 | — | NEAR — carry |

## Outcome
- **Promoted**: 1 (又, c34). Bank size 30 → 31.
- **Carry-over**: 9. All logged in `to_be_learned.md` under "Brush-end-gap class".

## Root cause analysis
All 9 carry-overs share one fix-class: **MMH-median endpoints + brush taper = visible gaps at joins**.

The MMH skeleton stops at the centerline endpoint. Brushed strokes taper to 3 px at that endpoint. So when two strokes are supposed to meet, their visible thin tips don't overlap — every joint shows a gap. Panel skeptics consistently flagged this as "not closed", "detached", "no meet", "malformed corner".

## Recommended fix (next session)

Move from anchoring at MMH stroke-endpoints to anchoring at MMH-derived **joints** (already computed by `tools/joint_detector.find_joints`). For every stroke that participates in a joint, override its endpoint with the joint's `meeting_canvas` coords. Strokes that don't join keep their MMH endpoints.

This is structurally cleaner anyway — the memory says "strokes meet at this joint" rather than "stroke ends here, AND another stroke ends nearby, and the brush hopefully overlaps".

## Lesson encoded to teaching_log
Add: "When composing a character from MMH medians, always project endpoints to find_joints' meeting points — never use raw median first/last point as a join anchor."

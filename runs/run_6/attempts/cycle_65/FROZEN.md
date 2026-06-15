# FROZEN — cycle 65 力 (3-attempt rule)

3rd attempt of 力 across c33 / c44 / c55 → c65. Panel 0/3 YES. Per the 3-attempt freeze rule, the cycle directory is preserved as evidence and no further attempts will be made for 力 (until/unless a fundamentally new primitive arrives).

## Attempt history

| Cycle | Strategy | Panel | Failure mode |
|---|---|---|---|
| c33 | Raw MMH anchors | 0/3 | Pie dominates; hook invisible at brush scale |
| c44 | Joint-snap fix | 0/3 | Mid-joint snap didn't fire (head/tail-only); same as c33 |
| c55 | Lift pie head down to heng level | 0/3 | Pie too short → reads as 撇 wrong direction |
| c65 | Revert to raw MMH + calligraphy-aware panel | 0/3 | Heng_zhe_gou's vertical+hook segment too short/disconnected from the bend; panel reads as malformed |

## Root cause (consensus across panel)

The `heng_zhe_gou.py` primitive's vertical+hook segment is too short relative to canonical 力. Pie length is fine (raw MMH is canonically long), but the heng_zhe_gou's downward shu segment terminates too high above the bottom of the box, leaving the hook visually disconnected. This is a PRIMITIVE issue, not an anchor placement issue — the anchors are correct per MMH.

## Renderer ceiling note

Logged to `to_be_learned.md` as "heng_zhe_gou primitive: shu+hook segment under-tall — affects 力 family chars (力 办 为 协 务)". Re-mastering this primitive would unblock a family of carry-overs but is out-of-scope for this 80-char calibration run.

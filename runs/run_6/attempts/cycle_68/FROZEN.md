# FROZEN — cycle 68 古 (3-attempt rule)

Attempts: c33-or-similar, c60, c68. All 0/3 panel or OCR-misread.

c68 strategy was shu_lift_above_box (correct — fixed the piercing). But the box-portion anchors derived from MMH (s3 heng_zhe, s4 shu, s5 heng) trace an X/diagonal shape rather than a closed 口. OCR reads as 女.

## Root cause
MMH's 古 decomposition gives box anchors that, when transcribed by cell_relative_for_xy + literal anchor_to_xy, produce an X-cross rather than a rectangle. Component reuse (calling draw_kou from success_bank) is the right fix but requires a different brief format that the Teacher SKILL doesn't currently support cleanly.

Parked: park 古 until brief format supports `call_subcharacter("kou", ...)` syntax for component reuse.

# Sandbox — run_6

## c71 明 — carry-over diagnosis

Brief had heng_zhe corner anchor at ("BC", 0.976, 0.756) — wrong cell, dropped 日 right wall to bottom. Drawer rendered faithfully and produced a malformed 日. OCR returned empty.

**Fix for c72**: corrected heng_zhe corner should be in same cell as head (TL) at the head's y_frac and tail's x_frac. s2 corner1 = ("TL", 0.976, 0.756). Re-derive entire brief with this principle: heng_zhe corner = same row as head (same cell y) + same column as tail (same cell x).

Next focus: 明 (retry, c72).

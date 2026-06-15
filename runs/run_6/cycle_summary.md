# Batch summary c71-c80 (run_6 continuation, 2-attempt rule)

PROMOTED (2): 京 c72 (re-verified after demotion), 果 c74.
FROZEN (8): 明 c71, 国 c73, 金 c75, 法 c76, 朋 c77, 美 c78, 思 c79, 看 c80.
Bank: 42→44.

Common failure modes:
- 月-containing chars (明, 朋): MMH-derived top doesn't close cleanly → OCR misreads as 用/眸.
- Multi-component chars with 王 inside (金): 人 tent + 王 don't fit cleanly together.
- 心 + 田 (思): MMH stroke decomposition produces unclear render.
- 手 component (看): pies don't cleanly form 手 radical.

Successes are 田-based (果) and stack-with-下点 (京). Pattern: characters where MMH's stroke decomposition matches canonical brush stroke set succeed; characters needing structural overrides (apex_share, top-closure for 月, internal-tighten for 王) fail.

Total calibration PNGs added: 10. Plus 11 cycle_71/72/73/75/76/77 attempt-2 variants.

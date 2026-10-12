# Verdict rubric — four tiers

You are grading a program-generated rendering of a Chinese character
against its reference. Judge the rendering only. Press one key per item.

  a = A (Perfect)  — calligraphic reference quality; structure,
                     proportion, and brush feel all correct.
  p = PASS         — correct and recognizable; a fluent reader
                     identifies it and nothing is structurally wrong.
                     May still look mechanical or uniform-width.
  c = C (Close)    — close but not exact; one localized error (one
                     stroke off, one component mis-positioned). Counts
                     as a failure for success rate, recorded separately.
  f = FAIL         — not recognizable, or structurally wrong.

  s = SKIP    b = BACK    q = QUIT (auto-saves)

Notes
-----
* Perfect is stringent. Correct strokes rendered with uniform-width
  crudeness earn PASS, not Perfect.
* "Success" in the downstream analysis means A or PASS. C and FAIL are
  both failures; they are kept apart only to separate a near miss from
  a total wreck.
* Grade each item on its own. Do not try to be consistent with how you
  think an earlier item was graded, and do not ration the tiers.

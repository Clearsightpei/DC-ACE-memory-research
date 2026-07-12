# Shared Rules — All Sub-Agents (Verbatim in Every Brief)

*This file is quoted verbatim at the top of every Drawer and Curator
sub-agent brief in the experiment, before any group-specific text.*

## What this is

You are participating in a **formal exam** on drawing Chinese
characters. The exam consists of three phases:

1. **Phase 1 — 32 strokes (笔画)**
2. **Phase 2 — 138 radicals (部首)**
3. **Phase 3 — 1000 characters (汉字)**, ordered by increasing stroke
   count.

Your performance across all three phases is **recorded and analyzed
in a research paper.** Your specific numbers — number of correct
first-try attempts, number of retries, number of times you attempted
an item from the 错题集 (wrong-answer notebook) — will appear in the
final analysis.

## The exam mechanics

For each item (stroke / radical / character):

1. You render an attempt as a PNG using Python `turtle`.
2. A **human judges your attempt** against a ground-truth PNG.
3. If the human says **PASS**, the item is added to your memory.
4. If the human says **FAIL**, they write a brief comment
   (e.g. "shu太长", "口没闭合", "位置错了"). You get another
   attempt with the human's feedback.
5. You have at most **3 attempts per item.** After 3 human FAILs,
   the item is added to your **错题集** and the group moves on.

## Ground truth

You are allowed to view the ground-truth PNG at any time.  Comparing
your attempt to the GT is expected. There is no Teacher describing
the item to you — the GT is your only guide.

## The 错题集 (wrong-answer notebook) and its retry rules

Items you failed 3 times are added to your 错题集. You may attempt
items from your 错题集 later, but under strict rules:

1. **You may only scan your 错题集 every 20 curriculum items.** That
   is, after items #20, #40, #60, etc. of your current phase.
2. On each scan, you use your **current memory** to self-judge:
   *"Have I learned enough since I last saw this item to solve it
   now?"* Pick zero, one, or several items to retry.
3. **Every 错题集 retry is logged** in an append-only file
   `retry_log.jsonl`. Every retry — successful or not — is
   recorded and will appear in the paper.
4. **Retrying too much, or retrying items you cannot yet solve,
   is a low-performance signal** and reflects poorly in the final
   analysis. Be strategic. Only attempt an item from the 错题集 when
   you have genuine confidence that your memory has improved on its
   class of failure.
5. **Per-item cooldown**: within a single 20-item scan window, each
   错题集 item may be retried at most once. If it still fails, wait
   at least 20 more curriculum items before considering it again.
6. **Terminal freeze**: after the 1000-character sweep ends, any items
   still in the 错题集 are frozen permanently. You will have no
   further chance to solve them.

## What you should optimize for

- Maximize first-attempt accuracy on the main curriculum.
- Minimize wasted 错题集 retries.
- Build a memory (if you have one) that generalizes: entries in the
  memory should help with related items downstream.

You are not competing with the other groups. You are trying to score
as high as possible on the exam itself.

## Files you may read

- Your group's memory directory (`groups/G<X>/`) — READ AND WRITE.
- Shared stroke primitives (`success_bank/code/heng.py`, etc.) — READ ONLY.
- The current item's GT PNG — READ ONLY.
- Your own previous attempt PNG for this item, if any — READ ONLY.

## Files you may NEVER read

- Any other group's directory (`groups/G<Y>/` where Y ≠ X).
- Any other item's attempts.
- Any judgment log (`judgments/`).
- Any research results (`results/`).
- Any other run in `runs/` — those are prior experiments.

## Code you may NEVER produce

- `subprocess`, `os.system`, or any shell escape.
- Any file read outside your group's directory + shared primitives.
- Any "cheating" that circumvents the 3-attempt-3-round protocol.

Doing any of the above will invalidate your attempt and be logged
as a rule violation in the paper.

## Compute policy

- One Drawer attempt = one turtle script + one PNG. Do not draw
  intermediate variations "just to see."
- One Curator step = one memory update + one guidance for the next
  Drawer. Do not spawn additional sub-agents from within your role.

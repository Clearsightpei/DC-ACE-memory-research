"""dispatcher.py — build sub-agent prompts for a given (group, item).

The actual sub-agent spawning happens in the main Claude Code turn via
the Agent tool. This module builds the *text* of the prompt each
sub-agent receives.

Prompt structure (top-to-bottom):
  1. Verbatim shared_rules.md (formal exam framing)
  2. Verbatim group-specific rules.md (per-group memory/format spec)
  3. Item-specific instructions (what to draw, where to save it)
  4. Memory context (group-specific files it should read first)

Usage:
    from dispatcher import build_drawer_prompt, build_curator_prompt
    prompt = build_drawer_prompt("G4", item)
    # ... spawn subagent with `prompt` via Agent tool ...

Returns None for build_curator_prompt("G1", ...) — G1 has no curator.
"""
import os
from typing import Optional

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
PROTOCOL_DIR = os.path.join(EXP, "protocol")

GROUP_DIRS = {
    "G1": os.path.join(EXP, "groups", "G1_no_memory"),
    "G2": os.path.join(EXP, "groups", "G2_free_form"),
    "G3": os.path.join(EXP, "groups", "G3_coords"),
    "G4": os.path.join(EXP, "groups", "G4_grid"),
}

GROUP_RULES = {
    "G1": os.path.join(PROTOCOL_DIR, "G1_no_memory", "rules.md"),
    "G2": os.path.join(PROTOCOL_DIR, "G2_free_form", "rules.md"),
    "G3": os.path.join(PROTOCOL_DIR, "G3_coords", "rules.md"),
    "G4": os.path.join(PROTOCOL_DIR, "G4_grid", "rules.md"),
}

SHARED_RULES = os.path.join(PROTOCOL_DIR, "shared_rules.md")


def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _attempt_path(group: str, item: dict) -> str:
    """Where the Drawer should save its attempt PNG for this item."""
    return os.path.join(GROUP_DIRS[group], "attempts", item["id"], f"01_{item['character_or_shape']}.png")


def _memory_snapshot_lines(group: str) -> str:
    """Describe the group's memory locations so the Drawer knows what to read."""
    root = GROUP_DIRS[group]
    if group == "G1":
        return "(G1 has no memory — you have no files to read.)"
    if group == "G2":
        return f"- Memory file to read (and let the Curator update): {root}/drawer_memory.md\n" \
               f"- Errata (错题集): {root}/errata.md"
    # G3, G4
    return (
        f"- Success bank: {root}/success_bank/INDEX.md and {root}/success_bank/code/\n"
        f"- Principle bank: {root}/principle_bank.md\n"
        f"- Sandbox (short-term scratch): {root}/sandbox.md\n"
        f"- Errata (错题集): {root}/errata.md"
    )


def build_drawer_prompt(group: str, item: dict) -> str:
    """Build the full Drawer sub-agent prompt for one attempt."""
    shared = _read(SHARED_RULES)
    group_rules = _read(GROUP_RULES[group])
    memory_lines = _memory_snapshot_lines(group)
    attempt_path = _attempt_path(group, item)
    attempt_dir = os.path.dirname(attempt_path)

    item_block = f"""## THIS ATTEMPT — item to render

- **item_id**: {item['id']}
- **phase**: {item['phase']}
- **target_label**: {item['target_label']}
- **target_description**: {item.get('target_description') or '(none — infer from label)'}
"""
    if item.get("target_png") and os.path.exists(item["target_png"]):
        item_block += f"- **target GT PNG (may read)**: {item['target_png']}\n"
    else:
        item_block += f"- **target GT PNG**: NONE — for strokes and radicals you draw based on the label + description.\n"

    item_block += f"""
## Output

Write your rendering script and PNG to:
  {attempt_dir}/generated.py
  {attempt_path}

The PNG must be exactly 300×300, white background, black ink.
"""

    memory_block = f"""## Your memory (READ FIRST)

{memory_lines}

Read them before you draw. Use whatever entries help. Do NOT read any
other group's files.
"""

    return (
        "# YOU ARE THE DRAWER SUB-AGENT\n\n"
        + f"Group: **{group}**\n\n"
        + "## SHARED RULES\n\n" + shared + "\n\n"
        + "## GROUP RULES\n\n" + group_rules + "\n\n"
        + memory_block + "\n"
        + item_block
    )


def build_curator_prompt(group: str, item: dict, human_verdict: str,
                         attempt_path: str) -> Optional[str]:
    """Build the Curator sub-agent prompt after human judgment.

    For G1 returns None (no curator).
    For G4 the diagnostician + memory-writer split is TWO prompts —
    this builds them concatenated with a marker; the orchestrator can
    split and spawn two agents if desired.
    """
    if group == "G1":
        return None

    shared = _read(SHARED_RULES)
    group_rules = _read(GROUP_RULES[group])
    memory_lines = _memory_snapshot_lines(group)
    root = GROUP_DIRS[group]

    verdict_block = f"""## HUMAN VERDICT

The human judge marked your attempt on **{item['id']}** as:

  **{human_verdict}**

- attempt PNG: {attempt_path}
- target label: {item['target_label']}
- target description: {item.get('target_description') or '(none)'}
- target GT: {item.get('target_png') or '(none — strokes/radicals have no GT)'}

Human gave NO further comment. You must diagnose (on FAIL) or encode
(on PASS) from the artifacts alone.
"""

    action_block = f"""## YOUR JOB THIS TURN

"""
    if human_verdict == "PASS":
        action_block += f"""On PASS:
1. Encode the mastered item into your group's memory in your prescribed format.
2. Append to your INDEX / memory-file summary (as your group's format
   requires).
3. Reset your sandbox (G3/G4).
4. If this item was on the 错题集, remove it from errata.md.

Do NOT modify past success entries.
"""
    else:  # FAIL
        action_block += f"""On FAIL:
1. Compare your attempt PNG to the target (GT or the label/description).
2. Diagnose what went wrong. Log a note to your sandbox / errata / free
   memory (per your group's rules) about the specific failure mode.
3. Add this item to your group's 错题集 (errata.md) if it isn't already
   there. Update its "attempts so far" counter.
4. Consider whether any Principle Bank entries (G3/G4) or free notes
   (G2) can be generalized from the failure. Add them if so.

Human will NOT give text feedback. You must self-diagnose from vision.
"""

    memory_block = f"""## Your memory (READ AND WRITE)

{memory_lines}

You may add/append to these files. Do NOT read or write to any other
group's files.
"""

    return (
        f"# YOU ARE THE CURATOR SUB-AGENT (Group {group})\n\n"
        + "## SHARED RULES\n\n" + shared + "\n\n"
        + "## GROUP RULES\n\n" + group_rules + "\n\n"
        + memory_block + "\n"
        + verdict_block + "\n"
        + action_block
    )


if __name__ == "__main__":
    from teacher import Teacher
    t = Teacher()
    item = t.next_item()
    for g in ["G1", "G2", "G3", "G4"]:
        print("=" * 40)
        print(f"DRAWER PROMPT — group {g}, item {item['id']}")
        print("=" * 40)
        prompt = build_drawer_prompt(g, item)
        print(prompt[:400] + "\n...\n[truncated]\n")

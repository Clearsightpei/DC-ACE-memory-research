# Success Bank (Part A of memory)

This directory is the run's **immutable library of working code**.

## Layout

```
success_bank/
├── INDEX.md              ← queryable list of entries with component tags
├── README.md             ← this file
├── code/
│   ├── <char>.py         ← exact code that produced a mastered render
│   ├── <char>.md         ← natural-language description + tags
│   └── ...
└── visual/
    └── visual_index.png  ← Curator-assembled grid of past wins
```

## Code file convention

Each `code/<char>.py` is a **self-contained drawing function** that
takes a turtle, an origin offset, and optionally a scale. The Drawer
imports it and calls it to compose a complex character from parts.

```python
# code/木.py — mastered c?? in run_4
# Tags: tag:character tag:heng tag:shu tag:撇捺-symmetric
# Component-of: 林, 森, 本, 杏, 杉
# Description: 木 — a centered heng, a centered shu crossing it,
#   a 撇 from the heng-shu intersection sweeping down-left, a 捺
#   from the same intersection sweeping down-right. Mastered at
#   10/10 in cycle ??.
def draw(t, ox=0, oy=0, scale=1.0):
    # ... exact mastered code, parameters intact ...
```

## Description file convention

Each `code/<char>.md` has:

- **Tags** — `tag:atomic-stroke`, `tag:character`, `tag:heng`,
  `tag:component-of(<char1>,<char2>)`, ...
- **Description** — what this entry produces, when to use it, what
  to substitute when reusing.
- **Original cycle** — the cycle where this was first mastered.
- **Permanent rubric score** (for the audit trail).

## Rules

- **Curator-owned**: only the Curator writes here.
- **Immutable parameters**: once an entry passes mastery and is
  added, its code is frozen. Bug fixes are done by adding a NEW
  entry that supersedes; the old one stays for the audit trail.
- **No half-mastered code**: if an entry didn't cross the mastery
  gate, it does not go in the bank. The Sandbox is for in-progress
  attempts.

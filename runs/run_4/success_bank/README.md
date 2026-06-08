# Success Bank (Part A of memory)

This directory is the run's **immutable library of working code**.

## Layout

```
success_bank/
├── INDEX.md                ← queryable list of entries with component tags
├── README.md               ← this file
├── build_visual_index.py   ← helper script the Curator runs after each new entry
├── code/
│   └── <char>.py           ← code + docstring (tags, mastered-cycle, rubric, reuse)
└── visual/
    └── visual_index.png    ← Curator-assembled grid of past wins
```

**One file per entry.** The entry's metadata (tags, description,
mastered cycle, rubric score) lives in the **module docstring at the
top of `<char>.py`**, NOT a separate `.md` file. INDEX.md is the
queryable surface; the .py docstring is the human-readable spec
right next to the code.

For project-wide first principles (Bézier helper rules, translate/
scale interface, contrastive rules, etc.), see the central
`../principle_bank.md` instead — those apply across all entries.

## Code file convention

Each `code/<char>.py` is a **self-contained drawing function** that
takes a turtle, an origin offset, and optionally a scale. The Drawer
imports it and calls it to compose a complex character from parts.

```python
"""
<char> (<pinyin>) — <one-line description>.

Tags: tag:<...> tag:<...>
Component-of: <chars that contain this as a part, or "(to fill)">
Mastered: run_<R> cycle <N>, rubric <X>/10 (dunbi=<>, hudu=<>, taper=<>, proportion=<>, overall=<>)

<one-paragraph description of what this entry produces and why it matters>

Reuse interface:
    from <name> import draw as draw_<name>
    draw_<name>(t)
    draw_<name>(t, ox=..., oy=..., scale=...)

<any caveats — e.g. "preserves all mastered parameters verbatim — DO NOT modify">
"""

def draw(t, ox=0, oy=0, scale=1.0):
    # ... exact mastered code, parameters intact ...
```

## Rules

- **Curator-owned**: only the Curator writes here.
- **Immutable parameters**: once an entry passes mastery and is
  added, its code is frozen. Bug fixes are done by adding a NEW
  entry that supersedes; the old one stays for the audit trail.
- **No half-mastered code**: if an entry didn't cross the mastery
  gate, it does not go in the bank. The Sandbox is for in-progress
  attempts.
- **No per-entry .md files**: docstring + INDEX.md row is enough.

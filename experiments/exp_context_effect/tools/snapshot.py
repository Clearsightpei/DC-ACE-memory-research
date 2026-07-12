"""snapshot.py — freeze memory state for retrospective analysis.

At snapshot milestones (position 50, then every 100), each group's
memory + errata + retry_log gets copied to snapshots/G<X>/snapshot_<pos>/.

This lets us later ask: "did memory_at_500 solve items that memory_at_100
couldn't?" — a retrospective validation experiment.

Usage:
    from snapshot import take_snapshot
    take_snapshot(position=50)          # snapshots all 4 groups at pos 50

    from snapshot import list_snapshots
    print(list_snapshots("G4"))
"""
import json
import os
import shutil
from typing import List

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
SNAP_ROOT = os.path.join(EXP, "snapshots")

GROUP_DIRS = {
    "G1": os.path.join(EXP, "groups", "G1_no_memory"),
    "G2": os.path.join(EXP, "groups", "G2_free_form"),
    "G3": os.path.join(EXP, "groups", "G3_coords"),
    "G4": os.path.join(EXP, "groups", "G4_grid"),
}

# Files/dirs to include in a snapshot per group. Attempts folder is NOT
# snapshotted (too much data + attempts don't need retrospective replay
# for the transfer question). Snapshot memory-relevant artifacts only.
SNAPSHOT_INCLUDES = {
    "G1": [],  # G1 has no memory to snapshot
    "G2": ["drawer_memory.md", "errata.md", "retry_log.jsonl"],
    "G3": ["success_bank", "principle_bank.md", "sandbox.md",
           "errata.md", "retry_log.jsonl"],
    "G4": ["success_bank", "principle_bank.md", "sandbox.md",
           "errata.md", "retry_log.jsonl"],
}


def take_snapshot(position: int, groups: List[str] = None) -> dict:
    """Copy each group's memory-relevant artifacts into
    snapshots/G<X>/snapshot_<position>/.

    Returns dict of {group: snapshot_dir_path} for the snapshots created.
    """
    if groups is None:
        groups = ["G1", "G2", "G3", "G4"]
    made = {}
    for g in groups:
        src = GROUP_DIRS[g]
        dst = os.path.join(SNAP_ROOT, g, f"snapshot_{position:04d}")
        if os.path.exists(dst):
            print(f"  {g}: snapshot {position} already exists at {dst} — skipping")
            continue
        os.makedirs(dst, exist_ok=True)
        for name in SNAPSHOT_INCLUDES[g]:
            s = os.path.join(src, name)
            d = os.path.join(dst, name)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            elif os.path.isfile(s):
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)
        # write a manifest so future readers know when this was frozen
        with open(os.path.join(dst, "_snapshot_meta.json"), "w") as f:
            json.dump({
                "position": position,
                "group": g,
                "files": SNAPSHOT_INCLUDES[g],
            }, f, indent=2)
        made[g] = dst
        print(f"  {g}: snapshot {position} → {dst}")
    return made


def list_snapshots(group: str) -> List[int]:
    """List snapshot positions available for a group."""
    d = os.path.join(SNAP_ROOT, group)
    if not os.path.exists(d):
        return []
    out = []
    for name in os.listdir(d):
        if name.startswith("snapshot_"):
            try:
                out.append(int(name[len("snapshot_"):]))
            except ValueError:
                pass
    return sorted(out)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--position", type=int, required=True,
                   help="Curriculum position at which to snapshot.")
    p.add_argument("--groups", nargs="+", default=None,
                   help="Which groups to snapshot (default all).")
    args = p.parse_args()
    made = take_snapshot(args.position, args.groups)
    print(f"\nCreated {len(made)} snapshots.")

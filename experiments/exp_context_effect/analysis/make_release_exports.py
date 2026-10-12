#!/usr/bin/env python3
"""make_release_exports.py — build the derived exports the paper cites.

Produces, under export/:
  memory_checkpoints.csv    paper Table 2 (observed memory checkpoints)
  mmh_joint_table.csv       derived per-character structural supervision,
                            the "derived per-character joint tables" named in
                            Data availability. Contains only our derived
                            abstraction (stroke count, endpoint anchors, joint
                            classes); it does NOT redistribute MakeMeAHanzi's
                            underlying stroke-median database.

Run from the experiment root:
    python3 analysis/make_release_exports.py
"""
import csv, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
EXPORT = os.path.join(ROOT, "export")
sys.path.insert(0, ROOT)

# ---------------------------------------------------------------- Table 2
# Observed memory checkpoints, recomputed under the operational-memory
# definition (curator-authored files available to support drawing; excludes
# auto-generated pass_index.md and process records evolution.md + scans/).
CHECKPOINTS = [
    # position, commit, G2 lines, G3 primitives, G4 primitives
    (0,   "b502d0ed", 0,     0,   0),
    (150, "9ae9ffde", 1011,  67,  78),
    (400, "685bde5d", 3707,  184, 140),
    (668, "6b761109", 5111,  251, 130),
]

def write_checkpoints():
    out = os.path.join(EXPORT, "memory_checkpoints.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        f.write("# Observed memory checkpoints (paper Table 2).\n")
        f.write("# G2 unit: lines of curator-authored operational memory --\n")
        f.write("#   all curator-authored .md available to support drawing,\n")
        f.write("#   EXCLUDING auto-generated pass_index.md and process records\n")
        f.write("#   (evolution.md, scans/). At position 668 this is 5,111 lines:\n")
        f.write("#   2,556 in errata.md + 2,555 across seven other files.\n")
        f.write("# G3/G4 unit: count of promoted bank primitives (.py in\n")
        f.write("#   success_bank/code/). G4's decrease at 668 reflects pruning.\n")
        f.write("# Units are architecture-specific and are NOT comparable\n")
        f.write("#   information quantities across conditions.\n")
        f.write("# Values are the four observed git checkpoints; intermediate\n")
        f.write("#   per-batch values were NOT recorded and are not interpolated here.\n")
        f.write("# G5 is absent: it was created post-B11 and has no checkpoint series;\n")
        f.write("#   its per-batch bank counts are in groups/G5_code_bank_mmh/evolution.md.\n")
        f.write("# Supersedes the earlier memory_growth_full.csv, which used a\n")
        f.write("#   different G2 counting definition (6,694) and linear interpolation.\n")
        w = csv.writer(f)
        w.writerow(["curriculum_position", "git_commit",
                    "g2_operational_memory_lines", "g3_bank_primitives",
                    "g4_bank_primitives"])
        for row in CHECKPOINTS:
            w.writerow(row)
    print(f"wrote {out}")

# ------------------------------------------------- derived joint table
def write_joint_table():
    """Per-character derived structural supervision for the Phase-3 curriculum."""
    try:
        from tools.mmh_joints import expected_joints
    except Exception as e:
        print(f"SKIP joint table: cannot import tools.mmh_joints ({e})")
        print("     (requires draw_character/graphics.txt from upstream MakeMeAHanzi)")
        return

    curric = os.path.join(ROOT, "curriculum", "chars_1000.json")
    if not os.path.exists(curric):
        print(f"SKIP joint table: {curric} not found")
        return
    data = json.load(open(curric, encoding="utf-8"))
    items = data if isinstance(data, list) else data.get("items", data.get("chars", []))

    out = os.path.join(EXPORT, "mmh_joint_table.csv")
    n_ok = n_fail = 0
    with open(out, "w", newline="", encoding="utf-8") as f:
        f.write("# Derived per-character structural supervision, as injected into\n")
        f.write("# G4/G5 drawer prompts (paper 2.4, Appendix B).\n")
        f.write("# DERIVED ABSTRACTION ONLY. This does not redistribute\n")
        f.write("# MakeMeAHanzi's stroke-median database; obtain it upstream at\n")
        f.write("# commit 618dbab8 (Arphic Public License lineage) and regenerate\n")
        f.write("# with analysis/make_release_exports.py.\n")
        f.write("# joints: semicolon-separated 'sA.labelA-sB.labelB@cell:CLASS:gap_px'\n")
        f.write("# CLASS: P=piercing/welded  T=tangent  N=neighbour (natural gap)\n")
        w = csv.writer(f)
        w.writerow(["char", "stroke_count", "endpoints", "joints"])
        for it in items[:533]:   # Phase-3 curriculum actually dispatched
            ch = (it.get("character") or it.get("char")) if isinstance(it, dict) else it
            if not ch:
                continue
            try:
                e = expected_joints(ch)
            except Exception:
                n_fail += 1
                continue
            eps = ";".join(
                f"s{p['stroke']}:{p['head_anchor']}->{p['tail_anchor']}"
                for p in e["endpoints"])
            jts = ";".join(
                f"s{j['stroke_a']}.{j['label_a']}-s{j['stroke_b']}.{j['label_b']}"
                f"@{j['cell']}:{j['class']}:{j.get('expected_gap_px','')}"
                for j in e["joints"])
            w.writerow([ch, e["stroke_count"], eps, jts])
            n_ok += 1
    print(f"wrote {out}  ({n_ok} characters, {n_fail} unavailable upstream)")

if __name__ == "__main__":
    os.makedirs(EXPORT, exist_ok=True)
    write_checkpoints()
    write_joint_table()

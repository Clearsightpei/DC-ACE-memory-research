"""Classify a joint emitted by `joint_detector.find_joints` into one of
four topology classes derived directly from MMH (no hand-coding).

Classes (validated against 半 口 人 八 中 七 又 五 白 力 — see
~/.claude/plans/should-i-install-rapid-lexical-lantern.md taxonomy table):

  P  Piercing.  dist_mmh < 5 AND both labels are mid(...).
                Two strokes cross THROUGH each other; brush sampling on
                the raw polylines welds the crossing naturally.
                Drawer: use raw MMH endpoints, no override.
                Examples: 半 s3⇆s5 (d=0), 中 s2⇆s4 (d=0), 七 s1⇆s2 (d=0).

  T  Tangent.   dist_mmh < 10 AND at least one label is head or tail.
                One stroke's TIP touches another stroke.
                Drawer: snap that tip to meeting_canvas.
                Rare — most head/tail joints fall into class N.

  N  Neighbor.  10 <= dist_mmh < eps_mmh (=90 by detector default).
                Stroke tips end NEAR each other; the natural small gap
                (canvas px = dist_mmh * 0.4) IS correct calligraphy.
                Drawer: use raw MMH endpoints — DO NOT snap.
                Examples: 口 3 non-welded corners (d=32-38), 人 apex (d=51).

  S  Same-stroke internal corner (NOT from find_joints — from find_corners).
                Compound stroke's internal bend (横折 etc.). Handled
                inside the primitive code. Listed here for completeness;
                this module does not emit S — that comes from find_corners.

If dist >= eps_mmh, find_joints doesn't return the joint at all (-> "no joint").
"""

# Thresholds (canvas-coord behaviour derives from these via the *0.4 scale).
TAU_PIERCE = 5.0   # MMH-coord dist; < this and both-mid -> P
TAU_TANGENT = 10.0 # MMH-coord dist; < this with head/tail involvement -> T


def is_tip(label: str) -> bool:
    """True if the label denotes a stroke endpoint (head or tail)."""
    return label == "head" or label == "tail"


def is_mid(label: str) -> bool:
    """True if the label is a mid(frac) marker."""
    return label.startswith("mid(")


def classify(joint: dict) -> str:
    """Return 'P' | 'T' | 'N' for a joint dict from find_joints.

    The dict must have keys: dist_mmh, label_a, label_b.
    Joints with dist_mmh >= eps_mmh aren't emitted by find_joints, so
    this function does not need to return a 'no joint' class.
    """
    d = joint["dist_mmh"]
    la, lb = joint["label_a"], joint["label_b"]

    if d < TAU_PIERCE and is_mid(la) and is_mid(lb):
        return "P"
    if d < TAU_TANGENT and (is_tip(la) or is_tip(lb)):
        return "T"
    return "N"


def gap_canvas_px(joint: dict) -> float:
    """Expected visual gap in canvas pixels for an N-class joint.

    The MMH -> canvas transform is *0.4. P/T joints should render as
    welded (0 px) regardless of this number; the canvas-px gap is only
    meaningful for class N.
    """
    return joint["dist_mmh"] * 0.4


# ─── Self-test ──────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from joint_detector import find_joints

    # Expected classifications per-character (eyeball-validated).
    EXPECT = {
        "半": ["P", "P"],
        "口": ["N", "N", "N"],
        "人": ["N"],          # d=51 -> N
        "中": ["N", "N", "N", "P", "P"],
        "七": ["P"],
        "又": ["P"],
        "五": None,           # check empirically (mixed)
        "白": ["N", "N", "N", "N", "N"],  # all d>=29
        "力": ["P"],
    }

    print("classify_joints self-test:")
    for char, expected in EXPECT.items():
        joints = find_joints(char)
        actual = [classify(j) for j in joints]
        ok = "✓" if expected is None or actual == expected else "✗"
        exp_str = "(any)" if expected is None else "".join(expected)
        print(f"  {char}: classes={''.join(actual)}  expected={exp_str}  {ok}")
        for j, c in zip(joints, actual):
            extra = f" gap={gap_canvas_px(j):.1f}px" if c == "N" else ""
            print(f"     s{j['stroke_a']}.{j['label_a']:<11}⇆"
                  f" s{j['stroke_b']}.{j['label_b']:<11}@{j['cell']:<3}"
                  f" d={j['dist_mmh']:.1f}  -> {c}{extra}")

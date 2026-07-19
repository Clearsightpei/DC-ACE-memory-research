"""teacher.py — curriculum position tracker and batch manager.

The "Teacher" is NOT pedagogical. It doesn't teach content or evaluate
correctness. It's purely a state machine:

  - knows what item comes next
  - tracks position across the 3 phases (strokes → radicals → characters)
  - detects 20-item scan boundaries for 错题集 sweeps
  - builds batch manifests for judgment

Usage (from Claude Code orchestrator turn):

    from teacher import Teacher
    t = Teacher()
    for _ in range(20):
        item = t.next_item()
        if item is None:
            break                     # curriculum exhausted
        # ... dispatch 4 drawer sub-agents in parallel to render this item ...
        # ... collect the 4 attempt PNG paths ...
        t.mark_dispatched(item, attempt_paths_by_group)
    t.save()
    manifest_path = t.build_batch_manifest()
    # ... human judges via judge_blind.py ...
    t.process_labels(manifest_path)   # promotes / errata-adds based on verdicts
    if t.should_scan_errata():
        # dispatch errata retries; see errata.py
        pass

State file: state/teacher_state.json
"""
import json
import os
from dataclasses import dataclass, field, asdict
from typing import Optional

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
STATE_DIR = os.path.join(EXP, "state")
os.makedirs(STATE_DIR, exist_ok=True)
STATE_FILE = os.path.join(STATE_DIR, "teacher_state.json")

CURRICULUM_DIR = os.path.join(EXP, "curriculum")
STROKES_MD = os.path.join(CURRICULUM_DIR, "strokes_32.md")
RADICALS_MD = os.path.join(CURRICULUM_DIR, "radicals.md")
CHARS_JSON = os.path.join(CURRICULUM_DIR, "chars_1000.json")

GROUPS = ["G1", "G2", "G3", "G4"]
GROUP_DIRS = {
    "G1": os.path.join(EXP, "groups", "G1_no_memory"),
    "G2": os.path.join(EXP, "groups", "G2_free_form"),
    "G3": os.path.join(EXP, "groups", "G3_coords"),
    "G4": os.path.join(EXP, "groups", "G4_grid"),
}

# ── Curriculum loading ─────────────────────────────────────────────────

# The strokes list — order matches strokes_32.md exactly.
STROKES_ORDER = [
    ("横",  "水平笔画，从左到右"),
    ("竖",  "垂直笔画，从上到下"),
    ("撇",  "撇画，从右上向左下"),
    ("捺",  "捺画，从左上向右下"),
    ("点",  "点画，短小的斜点"),
    ("提",  "提画，从左下向右上"),
    ("弯钩", "弯钩，弧线加末尾的钩"),
    ("卧钩", "卧钩，横躺的弯钩"),
    ("横撇", "横然后转向左下"),
    ("横钩", "横然后末尾勾一下"),
    ("横折", "横然后转90°向下"),
    ("竖提", "竖然后向右上提起"),
    ("竖弯", "竖然后向右横"),
    ("竖钩", "竖然后末尾勾一下"),
    ("竖折", "竖然后转向右"),
    ("斜钩", "从左上向右下带钩"),
    ("撇点", "撇然后转向右下点"),
    ("撇折", "撇然后转向右横"),
    ("横斜钩", "横加斜加钩"),
    ("橫折提", "横折加提"),
    ("横折弯", "横折加弯"),
    ("横折钩", "横折加钩"),
    ("竖弯钩", "竖弯加钩"),
    ("横撇弯钩", "横加撇加弯加钩"),
    ("横折弯钩", "横折加弯加钩"),
    ("横折折", "横折加横折"),
    ("竖折撇", "竖折加撇"),
    ("竖折折", "竖折加折"),
    ("横折折撇", "横折折加撇"),
    ("横折折折", "横折折折"),
    ("竖折折钩", "竖折折加钩"),
    ("横折折折钩", "横折折折加钩"),
]

# Radicals grouped by 画数 (from radicals.md)
RADICALS_BY_STROKES = {
    1: list("丨亅丿乛一乙乚丶"),
    2: list("八勹匕冫卜厂刀刂儿二匚阝丷几卩冂力冖凵人亻入十厶亠匸讠廴又㔾"),
    3: list("艹屮彳巛川辶寸大飞干工弓廾广己彐彑巾口马门宀女犭山彡尸饣士扌氵纟巳土囗兀夕小忄幺弋尢夂子丬夊"),
    4: list("贝比灬长车歹斗厄方风父戈户火旡见斤耂毛木肀牛爿片攴攵气欠犬日氏礻手殳水瓦尣王韦文毋心牙爻曰月爫支止爪无"),
}


def load_curriculum():
    """Returns (strokes_items, radical_items, char_items) — each list of dicts.

    Each dict:
      - id: str, globally unique
      - phase: "stroke" | "radical" | "character"
      - target_label: str, shown in judgment UI header
      - target_description: str or None
      - target_png: str or None (for characters)
      - character_or_shape: str, what to render (for strokes/radicals we
        pass the primitive character to the renderer)
    """
    strokes = []
    for i, (name, desc) in enumerate(STROKES_ORDER):
        strokes.append({
            "id": f"p1_stroke_{i+1:02d}_{name}",
            "phase": "stroke",
            "target_label": name,
            "target_description": desc,
            "target_png": None,   # strokes have no PNG target (per design)
            "character_or_shape": name,
        })

    radicals = []
    rn = 1
    for sc in sorted(RADICALS_BY_STROKES):
        for ch in RADICALS_BY_STROKES[sc]:
            gt_png = os.path.join(EXP, "gt", "phase2", f"{ch}.png")
            radicals.append({
                "id": f"p2_radical_{rn:03d}_{ch}",
                "phase": "radical",
                "target_label": f"{ch} ({sc}画)",
                "target_description": f"{sc}画部首",
                # v6 (Phase-2 restart): radicals now have GT PNGs like characters,
                # from MMH graphics.txt via tools/render_all_radical_gt.py.
                # File exists on disk for all 135 curriculum radicals.
                "target_png": gt_png if os.path.exists(gt_png) else None,
                "character_or_shape": ch,
            })
            rn += 1

    characters = []
    with open(CHARS_JSON, "r", encoding="utf-8") as f:
        char_data = json.load(f)
    for entry in char_data:
        ch = entry["character"]
        characters.append({
            "id": f"p3_char_{entry['idx']:04d}_{ch}",
            "phase": "character",
            "target_label": ch,
            "target_description": None,
            "target_png": os.path.join(EXP, "gt", "phase3", f"{ch}.png"),
            "character_or_shape": ch,
            "strokes": entry["strokes"],
            "tier": entry["tier"],
        })

    return strokes, radicals, characters


# ── Teacher state ─────────────────────────────────────────────────────

@dataclass
class TeacherState:
    global_position: int = 0            # 0-indexed into the concatenated curriculum
    phase: str = "stroke"               # "stroke", "radical", "character", "done"
    phase_position: int = 0             # 0-indexed within the current phase
    last_errata_scan_position: int = 0  # global position at which we last scanned
    batches_created: int = 0
    total_items: int = 0                # populated after load_curriculum

    @classmethod
    def load(cls):
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE) as f:
                return cls(**json.load(f))
        return cls()

    def save(self):
        with open(STATE_FILE, "w") as f:
            json.dump(asdict(self), f, indent=2)


class Teacher:
    def __init__(self):
        self.state = TeacherState.load()
        strokes, radicals, characters = load_curriculum()
        self.strokes = strokes
        self.radicals = radicals
        self.characters = characters
        self.all_items = strokes + radicals + characters
        self.state.total_items = len(self.all_items)

    def next_item(self):
        """Return next curriculum item, or None if exhausted."""
        if self.state.global_position >= len(self.all_items):
            self.state.phase = "done"
            return None
        item = self.all_items[self.state.global_position]
        self.state.phase = item["phase"]
        return item

    def advance(self):
        """Called after an item's attempts have been dispatched."""
        self.state.global_position += 1

    def should_scan_errata(self) -> bool:
        """True on 25-item boundaries (v6): after items 25, 50, 75, 100, ...

        This produces TWO errata scans per 50-item batch:
        - Scan A at the START of the batch (last cycle's boundary, e.g. pos 50 → scan before dispatching 51-100)
        - Scan B at the MIDDLE of the batch (e.g. pos 75 → scan between items 51-75 and 76-100)

        Per-item cooldown enforced separately: an item retried once must
        wait 50 more curriculum items before another retry.
        """
        pos = self.state.global_position
        if pos == 0 or pos == self.state.last_errata_scan_position:
            return False
        return pos % 25 == 0

    def mark_errata_scanned(self):
        self.state.last_errata_scan_position = self.state.global_position

    def build_batch_manifest(self, items_and_attempts, batch_dir):
        """items_and_attempts = list of (item, {group: attempt_path}) tuples.

        Writes batch_dir/manifest.json. Returns the manifest path.
        """
        os.makedirs(batch_dir, exist_ok=True)
        entries = []
        for item, group_paths in items_and_attempts:
            entries.append({
                "id": item["id"],
                "phase": item["phase"],
                "target_label": item["target_label"],
                "target_description": item.get("target_description"),
                "target_png": item.get("target_png"),
                "attempts": [
                    {"group": g, "path": group_paths[g]}
                    for g in GROUPS if g in group_paths
                ],
            })
        self.state.batches_created += 1
        manifest = {
            "batch_id": self.state.batches_created,
            "shuffle_seed": 42 + self.state.batches_created,
            "items": entries,
        }
        path = os.path.join(batch_dir, "manifest.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        return path

    def save(self):
        self.state.save()

    @property
    def position(self):
        return self.state.global_position

    @property
    def phase(self):
        return self.state.phase

    def snapshot_due(self) -> Optional[int]:
        """Returns the milestone number if a snapshot should be taken, else None.

        Cadence: at position 50, then every 100 thereafter.
        """
        pos = self.state.global_position
        if pos == 50:
            return 50
        if pos > 50 and (pos - 50) % 100 == 0:
            return pos
        return None


if __name__ == "__main__":
    t = Teacher()
    print(f"Curriculum: {len(t.strokes)} strokes + {len(t.radicals)} radicals + {len(t.characters)} chars = {len(t.all_items)} total")
    print(f"Current position: {t.state.global_position} / {len(t.all_items)}")
    print(f"Current phase: {t.state.phase}")
    print(f"Next item: {t.next_item()}")

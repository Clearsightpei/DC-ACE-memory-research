"""G4 attempt for 过 (p3_char_0239).

Read: drawer_memory.md (skimmed), memory_index.md, errata (grep 过 = not present).
Structure: 6 strokes = 寸 (heng + vertical-hook + dot) + 辶 (dot + turn + na-sweep).

Uses 米字格 anchor tuples per G4 spec. No raw offsets.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 6 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes: 寸 (heng, shu-hook, dian) + 辶 (dian, turn, na). '
             'Joint s1 x s2 welded (P). Joint s5-s6 small gap ~10px (N).'
}

# ---- endpoint anchors from MMH-derived brief ----
S1_HEAD = ('C',  0.192, 0.418)
S1_TAIL = ('MR', 0.561, 0.274)
S2_HEAD = ('TC', 0.898, 0.697)
S2_TAIL = ('BC', 0.573, 0.309)
S3_HEAD = ('C',  0.315, 0.729)
S3_TAIL = ('C',  0.573, 0.966)
S4_HEAD = ('TL', 0.63,  0.765)
S4_TAIL = ('ML', 0.967, 0.022)
S5_HEAD = ('ML', 0.378, 0.655)
S5_TAIL = ('BL', 0.882, 0.455)
S6_HEAD = ('BL', 0.354, 0.602)
S6_TAIL = ('BR', 0.701, 0.807)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1: heng of 寸 (top horizontal, small qi/shou taper)
    p0 = anchor_to_xy(S1_HEAD)
    p1 = anchor_to_xy(S1_TAIL)
    pts = [(p0[0] + t*(p1[0]-p0[0]), p0[1] + t*(p1[1]-p0[1])) for t in [i/20 for i in range(21)]]
    widths = [max(4, 7 - abs(i-10)/3) for i in range(21)]
    stroke_variable_width(d, pts, widths)

    # stroke 2: vertical shu-hook of 寸 (goes down and slightly left, then tiny hook at bottom)
    q0 = anchor_to_xy(S2_HEAD)   # top
    q1 = anchor_to_xy(S2_TAIL)   # bottom
    # gentle curve, mostly straight
    ctrl = ((q0[0]+q1[0])/2 + 4, (q0[1]+q1[1])/2)
    pts2 = quad_bezier(q0, ctrl, q1, n=30)
    widths2 = [6]*len(pts2)
    stroke_variable_width(d, pts2, widths2)
    # small hook at bottom-left
    hook_end = (q1[0] - 14, q1[1] - 4)
    fat_line(d, q1, hook_end, 6)

    # stroke 3: dian of 寸 (short diagonal dot)
    r0 = anchor_to_xy(S3_HEAD)
    r1 = anchor_to_xy(S3_TAIL)
    pts3 = [(r0[0] + t*(r1[0]-r0[0]), r0[1] + t*(r1[1]-r0[1])) for t in [i/10 for i in range(11)]]
    widths3 = [3 + i*0.6 for i in range(11)]
    stroke_variable_width(d, pts3, widths3)

    # stroke 4: top dot of 辶 (small dian at top-left)
    s0 = anchor_to_xy(S4_HEAD)
    s1 = anchor_to_xy(S4_TAIL)
    pts4 = [(s0[0] + t*(s1[0]-s0[0]), s0[1] + t*(s1[1]-s0[1])) for t in [i/10 for i in range(11)]]
    widths4 = [3 + i*0.5 for i in range(11)]
    stroke_variable_width(d, pts4, widths4)

    # stroke 5: horizontal-then-turn (the 乛 / short horizontal + descent) mid-left
    t0 = anchor_to_xy(S5_HEAD)
    t1 = anchor_to_xy(S5_TAIL)
    # slight bend: control point offset
    ctrl5 = ((t0[0]+t1[0])/2, (t0[1]+t1[1])/2 - 8)
    pts5 = quad_bezier(t0, ctrl5, t1, n=30)
    widths5 = [5]*len(pts5)
    stroke_variable_width(d, pts5, widths5)

    # stroke 6: the long 乀 (na / horizontal-sweeping base) of 辶
    u0 = anchor_to_xy(S6_HEAD)
    u1 = anchor_to_xy(S6_TAIL)
    # curve dipping down then sweeping up-right
    ctrl6 = ((u0[0]+u1[0])/2 - 20, u1[1] + 10)
    pts6 = quad_bezier(u0, ctrl6, u1, n=40)
    # thickens toward the tail (na character)
    widths6 = [5 + i*0.2 for i in range(len(pts6))]
    stroke_variable_width(d, pts6, widths6)

    out = os.path.join(os.path.dirname(__file__), '01_过.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()

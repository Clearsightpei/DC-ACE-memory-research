# ba_dot.py — 丷 (bā, top-radical dot pair), 2 strokes.
# GRADUATED at p2_radical_021_丷__retry_4 (B5, retry_4 PASS).
# Recipe: asymmetric hand-render per GT — LEFT tiny 点 (short arc slanting
# down-right) + RIGHT short 撇 (thin diagonal slash), both ~3-5 px per P12.
# LESSON: prior retries force-fit mirror_dian_pair helper (symmetric); GT
# is asymmetric. This entry explicitly REJECTS mirror_dian_pair and
# renders per GT observation.
from _shared_helpers import variant_pie, variant_dian


def draw_ba_dot(t, ox=0, oy=0, scale=1.0):
    """丷 — asymmetric top-radical dot pair (LEFT 点 + RIGHT 撇)."""
    def _sh(x, y):
        return (ox + x * scale, oy + y * scale)

    # LEFT 点: small short curved dot, slanting down-right.
    variant_dian(
        t,
        head=_sh(-35.0, -5.0),
        tail=_sh(-22.0, -25.0),
        w_head=3.0,
        w_tail=5.0,
        bow_perp=-2.0,
    )

    # RIGHT 撇 (short pie): thin diagonal from upper-right to lower-left.
    variant_pie(
        t,
        head=_sh(30.0, 0.0),
        tail=_sh(5.0, -50.0),
        w_head=5.0,
        w_tail=2.5,
        bow_perp=-3.0,
    )

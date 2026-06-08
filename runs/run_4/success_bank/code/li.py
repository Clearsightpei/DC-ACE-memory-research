"""
力 (li) — power. 横折钩 frame + 撇 cutting through heng.

Tags: tag:character tag:2-strokes tag:hook+pie tag:component-of(办,加,助)
Mastered: run_4 cycle 23, rubric 10/10 (OCR 力, visual 0.39)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng_zhe_gou import draw as draw_heng_zhe_gou
from pie import draw as draw_pie

def draw(t, ox=0.0, oy=0.0, scale=1.0):
    draw_heng_zhe_gou(t, ox=ox-15*scale, oy=oy-25*scale, scale=0.95*scale)
    draw_pie(t, ox=ox-90*scale, oy=oy-10*scale, scale=0.6*scale)

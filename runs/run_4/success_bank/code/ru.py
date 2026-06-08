"""
入 (ru) — enter. 捺 dominant + 撇 attached partway down 捺's upper portion.

Tags: tag:character tag:2-strokes tag:捺-dominant tag:asymmetric
Mastered: run_4 cycle 20, rubric 10/10 (OCR 入, visual 0.58)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pie import draw as draw_pie
from na import draw as draw_na

def draw(t, ox=0.0, oy=0.0, scale=1.0):
    draw_na(t, ox=ox+97*scale, oy=oy+0*scale, scale=0.65*scale)
    draw_pie(t, ox=ox-52*scale, oy=oy+30*scale, scale=0.45*scale)

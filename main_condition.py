from manim import *
from pathlib import Path
import os
# ----------- FLAGS
FLAGS = f"-pqm"
SCENE = "MyScene1" # <-- Here goes the Scene name


class MyScene1(Scene):
    def construct(self):
        self.play(GrowFromCenter(Circle()))
        
class MyScene2(Scene):
    def construct(self):
        self.play(Create(Square()))
        
if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {SCENE} {FLAGS}")
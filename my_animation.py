from manim import *

class MyScene(Scene):
    def construct(self):
        # Define Mobjects
        circle = Circle()
        self.play(GrowFromCenter(circle))
        self.wait()
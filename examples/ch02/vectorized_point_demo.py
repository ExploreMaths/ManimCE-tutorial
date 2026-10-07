from manim import *


class VectorizedPointDemo(Scene):
    def construct(self):
        dot = Dot(color=RED)
        self.play(FadeIn(dot))
        anchor = VectorizedPoint(2 * RIGHT)
        box = Square().next_to(anchor, RIGHT)
        self.play(FadeIn(box))
        self.play(dot.animate.move_to(anchor))
        self.wait(0.5)

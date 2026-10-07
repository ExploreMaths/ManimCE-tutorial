from manim import *


class DotsDemo(Scene):
    def construct(self):
        dot = Dot(LEFT * 2, color=RED)
        label_dot = LabeledDot(Text("A"), color=BLUE)
        label_dot.next_to(dot, RIGHT, buff=1.2)
        self.play(FadeIn(dot), FadeIn(label_dot))
        self.play(dot.animate.move_to(ORIGIN))
        self.wait(0.5)

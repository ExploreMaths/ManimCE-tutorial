"""CircleIntro: a Circle with a FadeIn entrance and a text label."""

from manim import *


class CircleIntro(Scene):
    def construct(self):
        circle = Circle(radius=1.5)
        circle.set_fill(BLUE_E, opacity=0.6)
        circle.set_stroke(BLUE, width=4)

        label = Text("Circle", font_size=36)
        label.next_to(circle, DOWN)

        self.play(FadeIn(circle))
        self.play(Write(label))
        self.wait(2)

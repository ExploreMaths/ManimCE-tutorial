from manim import *


class CircleEllipseDemo(Scene):
    def construct(self):
        circle = Circle(radius=1.2)
        ellipse = Ellipse(width=3.0, height=1.4, color=YELLOW)
        group = VGroup(circle, ellipse).arrange(RIGHT, buff=0.8)
        self.play(FadeIn(group))
        self.play(ellipse.animate.set_fill(YELLOW, 0.3))
        self.wait(0.5)

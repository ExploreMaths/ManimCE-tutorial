"""CreationFamily: Create / DrawBorderThenFill / Uncreate."""

from manim import *


class CreationFamily(Scene):
    def construct(self):
        shapes = VGroup(
            Square().set_fill(RED, opacity=0.5),
            Circle().set_fill(GREEN, opacity=0.5),
            Triangle().set_fill(BLUE, opacity=0.5),
        ).arrange(RIGHT, buff=1.2)

        self.play(Create(shapes[0]), run_time=0.9)
        self.play(DrawBorderThenFill(shapes[1]), run_time=1.2)
        self.add(shapes[2])
        self.wait(0.3)
        self.play(Uncreate(shapes[0]), run_time=0.8)
        self.play(Uncreate(shapes[1]), run_time=0.8)
        self.wait(0.3)

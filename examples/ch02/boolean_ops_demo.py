"""BooleanOpsDemo: Union / Intersection / Difference / Exclusion."""

from manim import *


class BooleanOpsDemo(Scene):
    def construct(self):
        sq = Square(side_length=1.8, fill_opacity=1, color=BLUE).shift(LEFT * 0.6)
        ci = Circle(radius=1.1, fill_opacity=1, color=RED).shift(RIGHT * 0.6)
        self.play(FadeIn(sq), FadeIn(ci))
        self.wait(0.5)

        union = Union(sq, ci, fill_opacity=1, color=GREEN).shift(DOWN * 2.2 + LEFT * 4)
        inter = Intersection(sq, ci, fill_opacity=1, color=YELLOW).shift(DOWN * 2.2 + LEFT * 1.3)
        diff = Difference(sq, ci, fill_opacity=1, color=ORANGE).shift(DOWN * 2.2 + RIGHT * 1.3)
        excl = Exclusion(sq, ci, fill_opacity=1, color=PURPLE).shift(DOWN * 2.2 + RIGHT * 4)

        self.play(FadeOut(sq), FadeOut(ci))
        self.play(
            FadeIn(union),
            FadeIn(inter),
            FadeIn(diff),
            FadeIn(excl),
        )
        self.wait(1)

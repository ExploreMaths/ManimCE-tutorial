"""ColorsDemo: ManimColor interpolation, lighter/darker, gradient and palettes."""

from manim import *


class ColorsDemo(Scene):
    def construct(self):
        base = ManimColor.from_hex("#58C4DD")
        colors = [
            base,
            base.lighter(0.5),
            base.darker(0.5),
            base.interpolate(PURE_RED, 0.6),
            base.opacity(0.35),
        ]
        squares = VGroup(
            *[
                Square(side_length=1.1, fill_opacity=1, stroke_width=0, color=c)
                for c in colors
            ]
        ).arrange(RIGHT, buff=0.25)
        self.play(FadeIn(squares))
        self.wait(0.5)

        gradient = color_gradient([BLUE_E, GREEN, YELLOW], 12)
        dots = VGroup(
            *[
                Dot(radius=0.18, color=c)
                for c in gradient
            ]
        ).arrange(RIGHT, buff=0.12).shift(DOWN * 1.5)
        self.play(FadeIn(dots))

        rcg = RandomColorGenerator(seed=7)
        random_squares = VGroup(
            *[
                Square(side_length=0.6, fill_opacity=1, stroke_width=0, color=rcg.next())
                for _ in range(5)
            ]
        ).arrange(RIGHT, buff=0.25).shift(DOWN * 3)
        self.play(FadeIn(random_squares))
        self.wait(1)

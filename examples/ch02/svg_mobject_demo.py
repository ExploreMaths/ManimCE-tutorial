"""SvgMobjectDemo: load examples/_shared/assets/sample.svg and restyle it."""

from manim import *


class SvgMobjectDemo(Scene):
    def construct(self):
        star = SVGMobject("examples/_shared/assets/sample.svg", height=3)
        self.play(DrawBorderThenFill(star))
        self.wait(0.5)

        star_colored = SVGMobject(
            "examples/_shared/assets/sample.svg",
            height=3,
            fill_color=YELLOW,
            stroke_color=RED,
            stroke_width=6,
        ).shift(RIGHT * 0.2)
        self.play(Transform(star, star_colored))
        self.play(star.animate.shift(LEFT * 2).scale(0.6))
        self.wait(0.5)

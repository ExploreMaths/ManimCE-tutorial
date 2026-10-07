"""LinesArrowsDemo: Line / DashedLine / Arrow / DoubleArrow / Vector."""

from manim import *


class LinesArrowsDemo(Scene):
    def construct(self):
        line = Line(LEFT * 5 + DOWN, LEFT * 3 + UP, color=BLUE)
        dashed = DashedLine(LEFT * 2.5 + UP * 2, RIGHT * 2.5 + UP * 2, dash_length=0.2)

        arrow = Arrow(LEFT * 4, LEFT * 4 + 2 * UP + RIGHT, buff=0, color=GREEN)
        stealth = Arrow(
            LEFT * 1.5 + DOWN * 2,
            RIGHT * 1.5 + DOWN * 0.5,
            buff=0,
            tip_shape=StealthTip,
            color=YELLOW,
        )
        double = DoubleArrow(RIGHT * 2 + DOWN * 2, RIGHT * 5 + DOWN * 0.5, buff=0, color=RED)

        vector = Vector(RIGHT * 1.5 + UP, color=MAROON).shift(LEFT * 0.5 + UP * 0.5)

        self.play(Create(line), Create(dashed))
        self.play(GrowArrow(arrow), GrowArrow(stealth), GrowArrow(double))
        self.play(GrowArrow(vector))
        self.wait(1)

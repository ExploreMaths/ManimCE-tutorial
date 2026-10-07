"""GrowVariants: GrowFromPoint / GrowFromCenter / GrowFromEdge / GrowArrow / SpinInFromNothing."""

from manim import *


class GrowVariants(Scene):
    def construct(self):
        p1 = Square(0.7).set_fill(RED, opacity=0.5).shift(LEFT * 3.5 + UP * 1.5)
        p2 = Circle(0.4).set_fill(GREEN, opacity=0.5).shift(LEFT * 1.2 + UP * 1.5)
        p3 = Triangle().set_fill(BLUE, opacity=0.5).shift(RIGHT * 1.2 + UP * 1.5).scale(0.6)
        arrow = Arrow(ORIGIN, RIGHT * 1.5).shift(LEFT * 0.7 + DOWN * 1.2)
        star = Star().set_fill(YELLOW, opacity=0.6).shift(RIGHT * 2.8 + UP * 1.5).scale(0.7)

        self.play(GrowFromPoint(p1, point=LEFT * 5 + UP * 2.5), run_time=0.8)
        self.play(GrowFromCenter(p2), run_time=0.8)
        self.play(GrowFromEdge(p3, edge=RIGHT), run_time=0.8)
        self.play(GrowArrow(arrow), run_time=0.8)
        self.play(SpinInFromNothing(star), run_time=0.8)
        self.wait(0.5)

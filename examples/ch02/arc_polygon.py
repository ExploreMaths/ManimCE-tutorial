from manim import *


class ArcPolygonDemo(Scene):
    def construct(self):
        straight = Polygon(LEFT * 2, RIGHT * 2, UP * 2, DOWN * 2)
        curved = ArcPolygon(LEFT * 2, RIGHT * 2, UP * 2, DOWN * 2, angle=45 * DEGREES)
        straight.shift(LEFT * 2.5)
        curved.shift(RIGHT * 2.5)
        self.play(Create(straight), run_time=1)
        self.play(Create(curved), run_time=1.5)
        self.wait()

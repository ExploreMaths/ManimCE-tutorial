from manim import *


class PolygonDemo(Scene):
    def construct(self):
        poly = Polygon([-1.5, -1, 0], [0, 1.2, 0], [1.5, -1, 0], color=BLUE)
        reg = RegularPolygon(n=6, color=GREEN)
        tri = Triangle(color=YELLOW)
        group = VGroup(poly, reg, tri).arrange(RIGHT, buff=0.7)
        self.play(FadeIn(group))
        self.play(poly.animate.set_fill(BLUE, 0.4))
        self.wait(0.5)

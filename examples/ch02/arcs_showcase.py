"""ArcsShowcase: Arc / ArcBetweenPoints / Sector / AnnularSector / Annulus / CubicBezier / CurvedArrow / CurvedDoubleArrow."""

from manim import *


class ArcsShowcase(Scene):
    def construct(self):
        arc = Arc(radius=1.2, start_angle=PI / 6, angle=PI * 0.75, color=BLUE)
        sector = Sector(radius=1.0, angle=PI / 3, color=GREEN).shift(LEFT * 3.5 + DOWN * 0.5)
        annular = AnnularSector(inner_radius=0.6, outer_radius=1.1, angle=PI * 0.9, color=YELLOW)
        annular.shift(RIGHT * 3.5 + DOWN * 0.5)
        annulus = Annulus(inner_radius=0.5, outer_radius=0.9, color=RED).shift(RIGHT * 0.2 + UP * 0.3)

        self.play(Create(arc), Create(sector), Create(annular), FadeIn(annulus))

        bez = CubicBezier(
            LEFT * 5 + DOWN * 2.5,
            LEFT * 3.5 + DOWN * 0.5,
            LEFT * 2 + DOWN * 3.5,
            LEFT * 0.5 + DOWN * 2,
            color=PURPLE,
        )
        curved = CurvedArrow(ORIGIN + DOWN * 2.5, RIGHT * 2.5 + DOWN * 2.5, color=ORANGE)
        dcurved = CurvedDoubleArrow(RIGHT * 3 + DOWN * 3, RIGHT * 5.5 + DOWN * 1.5, color=PINK)

        self.play(Create(bez), Create(curved), Create(dcurved))
        self.wait(1)

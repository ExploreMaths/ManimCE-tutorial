from manim import *


class HullCutoutDemo(Scene):
    def construct(self):
        dots_pos = [
            LEFT * 1.4 + UP,
            RIGHT * 1.4 + UP * 0.9,
            RIGHT + DOWN,
            LEFT * 1.2 + DOWN * 1.1,
        ]
        dots = VGroup(*[Dot(p, radius=0.06, color=YELLOW) for p in dots_pos])
        hull = ConvexHull(*dots_pos, color=BLUE)
        self.play(FadeIn(dots), Create(hull))
        self.play(hull.animate.set_fill(BLUE, 0.2))
        cut = Cutout(
            Square(side_length=2.6),
            Circle(radius=0.7).shift(0.4 * RIGHT),
            color=RED,
            fill_opacity=0.6,
        )
        cut.next_to(VGroup(dots, hull), DOWN, buff=0.6)
        self.play(FadeIn(cut))
        self.wait(0.5)

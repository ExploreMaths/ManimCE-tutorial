from manim import *


class RectFamilyDemo(Scene):
    def construct(self):
        square = Square(side_length=1.8, color=BLUE)
        rect = Rectangle(width=3.2, height=1.6, color=GREEN)
        rounded = RoundedRectangle(
            corner_radius=0.4, width=3.2, height=1.6, color=RED
        )
        group = VGroup(square, rect, rounded).arrange(RIGHT, buff=0.5)
        self.play(FadeIn(group))
        grid = Rectangle(width=3.2, height=1.6, grid_xstep=0.8, grid_ystep=0.8)
        grid.next_to(group, DOWN, buff=0.5)
        self.play(FadeIn(grid))
        self.wait(0.5)

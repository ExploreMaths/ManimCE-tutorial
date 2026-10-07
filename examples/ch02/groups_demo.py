from manim import *


class GroupsDemo(Scene):
    def construct(self):
        shapes = VGroup(Square(), Circle(), Triangle()).arrange(RIGHT, buff=0.4)
        self.play(FadeIn(shapes))
        self.play(shapes.animate.scale(0.7).rotate(PI / 8))
        squares = VGroup(*[Square(side_length=0.5) for _ in range(4)]).arrange(RIGHT)
        squares.to_edge(DOWN)
        self.play(FadeIn(squares))
        self.play(squares[1].animate.set_fill(YELLOW, 0.8))
        self.wait(0.5)

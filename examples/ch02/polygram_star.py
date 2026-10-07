from manim import *


class PolygramDemo(Scene):
    def construct(self):
        bowtie = Polygram(
            [[-1.2, 0, 0], [-0.4, 0.8, 0], [0.4, -0.8, 0]],
            [[-0.4, -0.8, 0], [0.4, 0.8, 0], [1.2, 0, 0]],
            color=BLUE,
        )
        hexagram = RegularPolygram(num_vertices=6, density=2, color=GREEN)
        star = Star(n=5, color=YELLOW, fill_opacity=0.5)
        group = VGroup(bowtie, hexagram, star).arrange(RIGHT, buff=0.8)
        self.play(FadeIn(group))
        self.play(star.animate.rotate(PI))
        self.wait(0.5)

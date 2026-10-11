from manim import *


class GraphDemo(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4), (1, 3)]
        g = Graph(vertices, edges, layout="circular", labels=True)
        self.play(Create(g), run_time=2)
        dg = DiGraph(vertices, edges, layout="circular", labels=True)
        dg.shift(RIGHT * 4.5)
        self.play(g.animate.shift(LEFT * 2.5), FadeIn(dg, shift=RIGHT), run_time=1.5)
        self.wait()

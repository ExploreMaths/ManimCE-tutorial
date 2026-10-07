"""NumberPlaneDemo: NumberPlane 背景网格与淡化线。"""

from manim import *


class NumberPlaneDemo(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.5,
            },
            faded_line_style={"stroke_opacity": 0.15},
            faded_line_ratio=2,
        )
        self.add(plane)

        dot = Dot(plane.coords_to_point(1.5, 1), color=YELLOW)
        self.play(FadeIn(dot, scale=2), run_time=0.8)
        self.play(dot.animate.move_to(plane.coords_to_point(-2, -1)), run_time=1.2)
        self.wait(0.5)

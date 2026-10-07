"""ThreeDAxesDemo: 在普通 2D Scene 中创建 ThreeDAxes（斜投影）。"""

from manim import *


class ThreeDAxesDemo(Scene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-3, 3, 1),
            y_range=(-3, 3, 1),
            z_range=(-2, 2, 1),
            z_axis_config={"stroke_color": BLUE},
        )
        self.play(Create(axes), run_time=2.0)

        # coords_to_point 接受三个坐标（普通 Scene 中为斜投影效果）
        dot = Dot3D(axes.coords_to_point(1, 1, 1), color=RED)
        self.play(FadeIn(dot), run_time=0.8)
        self.wait(0.5)

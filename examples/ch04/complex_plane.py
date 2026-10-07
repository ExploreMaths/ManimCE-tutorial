"""ComplexPlaneDemo: ComplexPlane 上复数与点的互转。"""

from manim import *


class ComplexPlaneDemo(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
        )
        self.add(plane)

        # number_to_point 接受复数（或实数），返回场景坐标
        z = 2 + 1j
        dot = Dot(plane.number_to_point(z), color=RED)
        v_line = DashedLine(
            plane.number_to_point(2), plane.number_to_point(z), color=RED
        )
        h_line = DashedLine(
            plane.number_to_point(1j), plane.number_to_point(z), color=RED
        )
        label = Text("2 + i", font_size=30).next_to(dot, UR, buff=0.1)

        self.play(FadeIn(h_line), FadeIn(v_line), FadeIn(dot), run_time=1.0)
        self.play(Write(label), run_time=0.8)

        # point_to_number 返回复数
        back = plane.point_to_number(dot.get_center())
        self.wait(0.5)

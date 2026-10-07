"""PolarPlaneDemo: PolarPlane 极坐标网格与极坐标曲线。"""

from manim import *


class PolarPlaneDemo(Scene):
    def construct(self):
        # 默认 azimuth_units="PI radians"，角度标签以 PI 的倍数表示
        plane = PolarPlane(
            radius_max=4,
            azimuth_units="PI radians",
            background_line_style={"stroke_opacity": 0.3},
        )
        self.add(plane)

        # 三瓣玫瑰线 r = 1.5 + cos(3t)
        graph = plane.plot_polar_graph(
            lambda t: 1.5 + np.cos(3 * t),
            theta_range=(0, 2 * PI),
            color=YELLOW,
        )
        self.play(Create(graph), run_time=2.0)
        self.wait(0.5)

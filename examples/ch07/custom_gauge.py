import numpy as np

from manim import *


class Gauge(VMobject):
    """半圆形仪表盘：外弧 + 9 根刻度，全部在 generate_points 中绘制。"""

    def __init__(self, radius=1.8, num_ticks=9, **kwargs):
        self.radius = radius
        self.num_ticks = num_ticks
        super().__init__(**kwargs)

    def generate_points(self):
        # 外弧：用 60 段折线近似半圆
        steps = 60
        self.start_new_path(self.radius * RIGHT)
        for k in range(1, steps + 1):
            angle = PI * k / steps
            self.add_line_to(self.radius * np.array([np.cos(angle), np.sin(angle), 0]))
        # 刻度：从内圈指向外圈的短线，每根都是独立子路径
        for k in range(self.num_ticks):
            angle = PI * k / (self.num_ticks - 1)
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            self.start_new_path(0.78 * self.radius * direction)
            self.add_line_to(0.94 * self.radius * direction)


class CustomGauge(Scene):
    def construct(self):
        gauge = Gauge().set_stroke(YELLOW, width=5)
        needle = VGroup(
            Line(ORIGIN, 1.2 * RIGHT).set_stroke(RED, width=8),
            Dot().scale(1.2),
        )
        self.play(Create(gauge), run_time=1.5)
        self.play(FadeIn(needle), run_time=0.5)
        self.play(Rotate(needle, angle=PI, about_point=ORIGIN), run_time=2.0)
        self.wait(0.5)

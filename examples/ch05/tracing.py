"""TracingAndBoundary: TracedPath 拖尾轨迹，AnimatedBoundary 流动边界。"""

from manim import *


class TracingAndBoundary(Scene):
    def construct(self):
        dot = Dot(LEFT * 2)
        self.add(dot)
        self.add(
            TracedPath(
                dot.get_center,
                stroke_color=YELLOW,
                stroke_width=4,
                dissipating_time=2,  # 2 秒前的轨迹逐渐消散
            )
        )
        self.play(MoveAlongPath(dot, Circle(radius=2)), run_time=2.5)

        square = Square().shift(RIGHT * 3.2)
        self.add(square, AnimatedBoundary(square))
        self.wait(1.5)

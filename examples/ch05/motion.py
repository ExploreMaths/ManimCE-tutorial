"""MotionAndHomotopy: MoveAlongPath 沿路径运动，Homotopy 自定义形变。"""

from manim import *


class MotionAndHomotopy(Scene):
    def construct(self):
        dot = Dot(LEFT * 2.5)
        self.add(dot)
        self.play(
            MoveAlongPath(
                dot,
                ArcBetweenPoints(LEFT * 2.5, RIGHT * 2.5, angle=-PI / 2),
            ),
            run_time=2,
        )

        # homotopy: 对空间中的每个点 (x, y, z)，按时间 t 映射到新位置
        def squash(x, y, z, t):
            return (x, y * (1 - t) + t * 0.3 * np.sin(3 * PI * x), z)

        square = Square().shift(LEFT * 2.5)
        self.add(square)
        self.play(Homotopy(squash, square, run_time=2))
        self.wait(0.5)

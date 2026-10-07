"""RotateVsRotating: Rotate（Transform 系，默认 smooth、PI）与
Rotating（Animation 系，默认 linear、TAU）对比。"""

from manim import *


class RotateVsRotating(Scene):
    def construct(self):
        left_sq = Square().shift(LEFT * 2.5)
        right_sq = Square().shift(RIGHT * 2.5)
        self.add(left_sq, right_sq)

        # Rotate：Transform 子类，默认 angle=PI、rate_func=smooth
        self.play(Rotate(left_sq, angle=PI / 2), run_time=1.5)

        # Rotating：Animation 子类，默认 rate_func=linear，每帧从起始快照重算
        self.play(Rotating(right_sq, angle=PI / 2), run_time=1.5)
        self.wait(1)

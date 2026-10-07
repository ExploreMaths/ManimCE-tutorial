"""ChangeSpeedDemo: speedinfo 在动画进度的关键节点上改变播放速度。"""

from manim import *


class ChangeSpeedDemo(Scene):
    def construct(self):
        dot = Dot(LEFT * 3)
        self.add(dot)

        # 键是内层动画进度（0~1 的比例），值是速度倍率；
        # 0.5~0.7 段以 0.15 倍慢速播放，实际时长会被拉长
        self.play(
            ChangeSpeed(
                dot.animate.shift(RIGHT * 6),
                speedinfo={0: 1, 0.5: 1, 0.7: 0.15, 1: 0.15},
                rate_func=linear,
            )
        )

"""DecimalNumberDemo: 用 ValueTracker 驱动小数滚动。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class DecimalNumberDemo(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        num = DecimalNumber(
            0,
            num_decimal_places=3,
            show_ellipsis=True,
        )
        num.add_updater(lambda m: m.set_value(PI * tracker.get_value()))

        self.add(num)
        self.play(tracker.animate.set_value(1), run_time=2)
        self.wait(0.5)

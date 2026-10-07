"""UpdaterHelpers: always_redraw 重绘、always_rotate 自转、cycle_animation 循环动画。"""

from manim import *


class UpdaterHelpers(Scene):
    def construct(self):
        t = ValueTracker(0)
        sine = always_redraw(
            lambda: FunctionGraph(
                lambda x: 0.8 * np.sin(x + t.get_value()),
                x_range=[-3, 3],
                color=BLUE,
            )
        )
        self.add(sine)
        self.play(t.animate.set_value(PI), run_time=2.5)

        square = always_rotate(Square(), rate=1.2)  # 弧度/秒
        square.shift(RIGHT * 2.5 + UP * 1.5)
        self.add(square)

        # 把一个一次性动画变成循环 updater，物体先 add 再 wait
        circle = Circle(radius=0.4).shift(LEFT * 2.5 + UP * 1.5)
        cycle_animation(Rotate(circle, TAU, run_time=2, rate_func=linear))
        self.add(circle)
        self.wait(2)

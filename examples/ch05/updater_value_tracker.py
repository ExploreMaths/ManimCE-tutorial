"""UpdaterValueTracker: ValueTracker 驱动 DecimalNumber 与 Dot，suspend/resume 对比。"""

from manim import *


class UpdaterValueTracker(Scene):
    def construct(self):
        tracker = ValueTracker(0)

        # mob_class=Text：默认的 MathTex 需要 LaTeX，本机未安装
        number = DecimalNumber(0, num_decimal_places=1, mob_class=Text).to_edge(UP)
        number.add_updater(lambda n: n.set_value(tracker.get_value()))

        dot = Dot(color=YELLOW)
        dot.add_updater(lambda d: d.move_to(RIGHT * tracker.get_value() + DOWN))

        self.add(number, dot)
        self.play(tracker.animate.set_value(2), run_time=2)

        # 圆点暂停跟随 tracker，但数字的 updater 仍在运行
        dot.suspend_updating()
        self.play(tracker.animate.set_value(-2), run_time=1.5)

        dot.resume_updating()
        self.play(tracker.animate.set_value(0), run_time=1)

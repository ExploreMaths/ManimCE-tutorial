"""NumberAnimations: ChangingDecimal 按函数计数，ChangeDecimalToValue 直达目标值。"""

from manim import *


class NumberAnimations(Scene):
    def construct(self):
        # mob_class=Text：默认的 MathTex 需要 LaTeX，本机未安装
        number = DecimalNumber(0, num_decimal_places=0, font_size=72, mob_class=Text)
        self.add(number)

        # 更新函数接收动画进度 alpha（0→1），返回此刻应显示的数值
        self.play(ChangingDecimal(number, lambda alpha: 10 * alpha), run_time=1.5)

        # 从当前值平滑数到目标值 42
        self.play(ChangeDecimalToValue(number, 42), run_time=1.5)
        self.wait(0.5)

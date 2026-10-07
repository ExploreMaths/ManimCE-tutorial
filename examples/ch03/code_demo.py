"""CodeDemo: Code 默认 Pygments 配色与窗口背景。"""

from manim import *


class CodeDemo(Scene):
    def construct(self):
        code = Code(
            code_string="def greet(name):\n    return f'你好, {name}'",
            language="python",
            background="window",
        )
        self.play(FadeIn(code))
        self.wait(0.5)

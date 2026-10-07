"""CodeFormatterStyle: 用 Pygments Style 子类自定义 Code 配色。"""

from manim import *
from pygments.style import Style
from pygments.token import Keyword, Name, String


class NordLike(Style):
    background_color = "#2E3440"

    styles = {
        Keyword: "#81A1C1",
        Name.Function: "#88C0D0",
        String: "#A3BE8C",
    }


class CodeFormatterStyle(Scene):
    def construct(self):
        code = Code(
            code_string="def double(x):\n    return x * 2",
            language="python",
            formatter_style=NordLike,
        )
        self.play(FadeIn(code))
        self.wait(0.5)

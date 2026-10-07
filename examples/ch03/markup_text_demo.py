"""MarkupTextDemo: Pango 标记语言的常用标签。"""

from manim import *


class MarkupTextDemo(Scene):
    def construct(self):
        title = MarkupText('<span foreground="#FFFF00" size="x-large">Pango 标记语言</span>')
        body = MarkupText(
            '上下标：x<sup>2</sup> + y<sub>i</sub>，<b>粗体</b> 与 <i>斜体</i>',
            font_size=32,
        )
        body.next_to(title, DOWN, buff=0.6)

        self.play(FadeIn(title))
        self.play(FadeIn(body, shift=UP))
        self.wait(0.5)

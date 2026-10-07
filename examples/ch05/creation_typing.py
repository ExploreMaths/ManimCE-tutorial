"""CreationTyping: TypeWithCursor / UntypeWithCursor."""

from manim import *


class CreationTyping(Scene):
    def construct(self):
        text = Text("typewriter", font_size=44)
        cursor = Rectangle(
            height=0.55, width=0.32, stroke_width=2
        ).set_fill(opacity=0)

        # 光标贴着文字打字
        self.play(TypeWithCursor(text, cursor), run_time=2.0)
        self.wait(0.3)
        # UntypeWithCursor 的 cursor 默认是 None，不显式传会在 begin() 崩溃
        self.play(UntypeWithCursor(text, cursor), run_time=1.5)
        self.wait(0.3)

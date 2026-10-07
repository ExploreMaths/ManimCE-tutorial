"""LogScaleDemo: LinearBase 与 LogBase 两种缩放基的对照。"""

from manim import *


class LogScaleDemo(Scene):
    def construct(self):
        linear = NumberLine(
            x_range=[0, 8, 1],
            length=8,
            scaling=LinearBase(),
        ).shift(UP * 1.5)
        linear_title = Text("LinearBase", font_size=30).next_to(linear, UP)

        # LogBase(base=2)：x_range 是指数标签 0..3，对应真值 1..8；
        # number_to_point / add_labels 都使用真值（内部自动取 log）
        log = NumberLine(
            x_range=[0, 3, 1],
            length=8,
            scaling=LogBase(base=2, custom_labels=False),
        ).shift(DOWN * 1.5)
        log.add_labels(
            {
                1: Text("1", font_size=30),
                2: Text("2", font_size=30),
                4: Text("4", font_size=30),
                8: Text("8", font_size=30),
            }
        )
        log_title = Text("LogBase(base=2)", font_size=30).next_to(log, DOWN)

        self.play(Create(linear), Create(log), run_time=1.5)
        self.play(
            FadeIn(linear_title),
            FadeIn(log_title),
            # 注意：add_labels 的标签存在 line.labels 属性里，
            # v0.21.0 的 get_labels() 返回的是刻度数字而非这些标签
            FadeIn(log.labels),
            run_time=1.0,
        )
        self.wait(0.5)

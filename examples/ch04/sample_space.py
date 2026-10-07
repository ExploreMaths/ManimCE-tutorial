"""SampleSpaceDemo: SampleSpace 的划分与花括号标签。

注意：v0.21.0 中 SampleSpace.get_subdivision_braces_and_labels 会把
min_num_quads 传给 Brace 而 Brace 不接受该参数，调用必崩；
这里用手工 Brace + Text 的组合代替。
"""

from manim import *


class SampleSpaceDemo(Scene):
    def construct(self):
        space = SampleSpace(height=3, width=6)
        # 注意：第一个位置参数是“比例列表”，不是可变参数；
        # 省略余量会自动补齐（1 - sum(parts)）
        # divide_vertically 按宽度切成竖条，divide_horizontally 按高度切成横条
        space.divide_vertically([0.5, 0.3, 0.2])

        self.play(FadeIn(space), run_time=1.0)

        # 动态属性：divide 之后才有 vertical_parts / horizontal_parts
        parts = space.vertical_parts
        braces = VGroup(*[Brace(p, UP, buff=0.15) for p in parts])
        labels = VGroup(
            *[
                Text(s, font_size=24).next_to(b, UP, buff=0.1)
                for b, s in zip(braces, ["0.5", "0.3", "0.2"])
            ]
        )
        self.play(FadeIn(braces), FadeIn(labels), run_time=1.0)
        self.wait(0.5)

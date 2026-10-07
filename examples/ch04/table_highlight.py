"""TableHighlightDemo: 普通 Table（字符串单元格）与单元格高亮。"""

from manim import *


class TableHighlightDemo(Scene):
    def construct(self):
        # 字符串单元格默认由 Paragraph 渲染，不依赖 LaTeX
        table = Table(
            [["apple", "red"], ["banana", "yellow"], ["grape", "purple"]],
            row_labels=[Text("a", font_size=30), Text("b", font_size=30), Text("c", font_size=30)],
            include_outer_lines=True,
        )
        self.play(Create(table), run_time=1.5)

        # get_highlighted_cell 返回一个背景矩形，add 到对应单元格后面
        highlight = table.get_highlighted_cell((1, 2), color=RED, fill_opacity=0.4)
        self.add(highlight)
        self.wait(0.5)

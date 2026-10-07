"""BarChartDemo: BarChart 柱状图、数值标签与动态改值。"""

from manim import *


class BarChartDemo(Scene):
    def construct(self):
        chart = BarChart(
            values=[3, 5, 2, 4, 6],
            bar_names=["A", "B", "C", "D", "E"],
            y_range=[0, 7, 1],
            y_length=5,
        )
        self.play(Create(chart), run_time=1.5)

        # change_bar_values 只瞬时更新柱高，不播放动画
        chart.change_bar_values([5, 2, 6, 3, 4])

        # get_bar_labels 按当前柱高生成标签（改值后调用才是新值）
        labels = chart.get_bar_labels(font_size=24)
        self.play(FadeIn(labels), run_time=1.0)
        self.wait(0.5)

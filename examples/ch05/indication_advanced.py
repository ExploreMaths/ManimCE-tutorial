"""IndicationAdvanced: ShowPassingFlash 家族 / ApplyWave / Wiggle / Blink / Broadcast。"""

from manim import *


class IndicationAdvanced(Scene):
    def construct(self):
        line = Line(LEFT * 3, RIGHT * 3, color=BLUE)
        square = Square().shift(LEFT * 2.5 + DOWN)
        dot = Dot(RIGHT * 2.5 + DOWN)
        self.add(line, square, dot)

        # 一道亮光沿线条扫过
        self.play(ShowPassingFlash(line.copy(), time_width=0.3), run_time=1)
        # 扫光且笔画逐渐变细，动画结束自动移除
        self.play(ShowPassingFlashWithThinningStrokeWidth(line.copy()), run_time=1)
        # 波浪沿竖直方向滚过线条
        self.play(ApplyWave(line), run_time=1.2)
        # 左右物体分别扭动与闪烁
        self.play(Wiggle(square), run_time=0.8)
        self.play(Blink(dot), run_time=0.6)
        self.play(Broadcast(dot), run_time=1.4)

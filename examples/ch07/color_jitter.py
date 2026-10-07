import numpy as np

from manim import *


class ColorJitter(Animation):
    """自定义动画：颜色向目标色渐变，同时叠加先增后减的随机抖动。"""

    def __init__(self, mobject, target_color=YELLOW, amplitude=0.12, **kwargs):
        self.target_color = target_color
        self.amplitude = amplitude
        super().__init__(mobject, **kwargs)

    def begin(self):
        # 在 super().begin() 之前预生成随机位移：
        # 基类 begin 会立即调用 interpolate(0)，噪声必须先就绪
        rng = np.random.default_rng(0)
        self.noise = rng.uniform(-1, 1, self.mobject.points.shape)
        super().begin()

    def interpolate_mobject(self, alpha):
        mobject = self.mobject
        start = self.starting_mobject
        mobject.set_color(interpolate_color(start.get_color(), self.target_color, alpha))
        # 4 * alpha * (1 - alpha)：两端为 0，中间最大，抖动随动画结束自然归位
        weight = 4 * alpha * (1 - alpha)
        mobject.points = start.points + self.amplitude * weight * self.noise


class CustomAnimationDemo(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=0.6).set_stroke(WHITE, width=4)
        self.play(FadeIn(square), run_time=0.5)
        self.play(ColorJitter(square, target_color=RED, run_time=2.0))
        self.play(ColorJitter(square, target_color=GREEN, amplitude=0.2, run_time=1.5))
        self.wait(0.5)

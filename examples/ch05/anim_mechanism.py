"""AnimMechanism: run_time / rate_func / lag_ratio / Add / Wait."""

from manim import *


class AnimMechanism(Scene):
    def construct(self):
        square = Square().set_fill(BLUE_E, opacity=0.6)

        # run_time 与 rate_func 控制单个动画的时长与节奏
        self.play(DrawBorderThenFill(square), run_time=1.2, rate_func=double_smooth)

        # lag_ratio 让同一 play 里的多个动画错峰开始
        dot_l = Dot(LEFT * 2 + DOWN)
        dot_r = Dot(RIGHT * 2 + DOWN)
        self.play(FadeIn(dot_l), FadeIn(dot_r), lag_ratio=0.5, run_time=1.5)

        # Add 也是动画：默认 run_time=0，单独播放会报错，
        # 必须显式给一个正的 run_time（相当于“出现后再静止这么久”）
        self.play(Add(Text("Add 瞬间出现", font_size=32).next_to(square, UP)), run_time=0.5)

        # Wait 让画面静止
        self.wait(0.5)

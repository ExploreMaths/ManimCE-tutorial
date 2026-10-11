from manim import *


class BannerDemo(Scene):
    def construct(self):
        banner = ManimBanner()
        banner.shift(UP * 0.5)
        self.play(banner.create(), run_time=1.5)
        self.play(banner.expand(), run_time=1.5)
        self.wait()

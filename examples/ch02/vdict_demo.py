from manim import *


class VDictDemo(Scene):
    def construct(self):
        d = VDict({"sq": Square(), "ci": Circle()})
        d.arrange(RIGHT, buff=0.5)
        self.play(FadeIn(d))
        self.play(d["sq"].animate.set_fill(BLUE, 0.7))
        d["tri"] = Triangle().next_to(d["ci"], RIGHT)
        self.play(FadeIn(d["tri"]))
        self.wait(0.5)

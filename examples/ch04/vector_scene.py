"""VectorSceneDemo: VectorScene 的加向量与向量标注。"""

from manim import *


class VectorSceneDemo(VectorScene):
    def construct(self):
        # add_vector 默认播放动画并返回 Arrow
        v = self.add_vector([3, 1.5], color=YELLOW)
        self.label_vector(v, Text("v", font_size=36))
        self.wait(0.5)

        w = self.add_vector([-1.5, 2.25], color=BLUE)
        self.label_vector(w, Text("w", font_size=36))
        self.wait(0.5)

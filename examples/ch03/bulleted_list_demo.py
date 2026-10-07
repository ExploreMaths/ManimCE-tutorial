"""BulletedListDemo: BulletedList 默认样式与 dot_buff。（需要 LaTeX，由 CI 渲染）"""

from manim import *


class BulletedListDemo(Scene):
    def construct(self):
        bl = BulletedList("第一条要点", "第二条要点", "第三条要点", buff=0.5)

        self.play(FadeIn(bl))
        self.play(bl.fade_all_but("第二条要点", opacity=0.3))
        self.wait(0.5)

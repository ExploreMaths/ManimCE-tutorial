"""TexTemplateCtex: 用 ctex 模板排版中文 TeX。（需要 XeLaTeX，由 CI 渲染）"""

from manim import *


class TexTemplateCtex(Scene):
    def construct(self):
        text = Tex(
            r"勾股定理：$a^2 + b^2 = c^2$",
            tex_template=TexTemplateLibrary.ctex,
        )
        self.play(Write(text))
        self.wait(0.5)

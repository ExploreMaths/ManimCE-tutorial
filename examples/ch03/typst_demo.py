"""TypstDemo: 用 Typst 排版一段图文内容。"""

from textwrap import dedent

from manim import *


class TypstDemo(Scene):
    def construct(self):
        doc = Typst(
            dedent(
                r"""
                #set text(size: 20pt)
                #set heading(numbering: "1.")

                = Typst 排版

                由 Rust 原生编译为 SVG，_无需安装 TeX_ 系统。
                """
            )
        )
        self.play(FadeIn(doc))
        self.wait(0.5)

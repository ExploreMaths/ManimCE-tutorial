"""MatchingTexDemo: TransformMatchingTex 与 key_map。需要本机 LaTeX，CI 渲染。"""

from manim import *


class MatchingTexDemo(Scene):
    def construct(self):
        # 按 tex_string 匹配：相同的符号原地保留，不同的符号交叉变换
        eq1 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq2 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")
        self.add(eq1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.0)
        self.wait(0.3)

        # key_map：源子对象的 key → 目标子对象的 key，强行把不匹配的两部分当作一对
        # 注意 v0.21.0 中 "{{x}}^2" 会拆成 "x" 与 "^2" 两个部分，key 是不含花括号的 "x"
        eq3 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        self.play(
            TransformMatchingTex(
                eq3,
                eq2,
                key_map={"x": "a", "y": "b", "z": "c"},
            ),
            run_time=1.2,
        )
        self.wait(0.3)

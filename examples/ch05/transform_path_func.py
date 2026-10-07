"""TransformPathFunc: ApplyMethod / ApplyFunction / ApplyMatrix / CyclicReplace / Swap."""

from manim import *


class TransformPathFunc(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=0.5).shift(UP * 1.5)
        dot = Dot().shift(LEFT * 3 + DOWN * 1.5)
        tri = Triangle().set_fill(GREEN, opacity=0.5).shift(RIGHT * 3 + DOWN * 1.5)
        self.add(square, dot, tri)

        # ApplyMethod：以“方法名 + 参数”的形式播放方法动画
        self.play(ApplyMethod(square.shift, DOWN * 0.8), run_time=0.5)
        self.wait(0.2)

        # ApplyFunction：对物体每个点施加同一个函数
        self.play(
            ApplyFunction(lambda m: m.scale(1.6).set_color(YELLOW), dot),
            run_time=0.5,
        )
        self.wait(0.2)

        # ApplyMatrix：左乘一个矩阵（这里是 90° 旋转矩阵）
        rot = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        self.play(ApplyMatrix(rot, tri), run_time=0.6)
        self.wait(0.2)

        # Swap / CyclicReplace：多个物体沿弧线交换位置
        a = Circle(radius=0.3).set_fill(TEAL, opacity=0.6).shift(LEFT * 1.2 + DOWN * 0.5)
        b = Square(0.6).set_fill(PURPLE, opacity=0.6).shift(RIGHT * 1.2 + DOWN * 0.5)
        self.add(a, b)
        self.play(Swap(a, b), run_time=0.7)
        self.wait(0.2)

        c = Star().set_fill(GOLD, opacity=0.6).shift(RIGHT * 1.2 + UP * 1.2)
        self.add(c)
        self.play(CyclicReplace(a, b, c), run_time=0.8)
        self.wait(0.3)

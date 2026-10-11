from manim import *


class VectorFieldDemo(Scene):
    def construct(self):
        def field(p):
            return np.array([-p[1], p[0], 0]) / 4

        vf = ArrowVectorField(field, x_range=[-5, 5, 1], y_range=[-2.5, 2.5, 1])
        self.play(Create(vf), run_time=1.5)
        sl = StreamLines(field, x_range=[-2.5, 2.5, 0.6], y_range=[-2.5, 2.5, 0.6],
                         noise_factor=0.2)
        self.add(sl)
        self.play(Create(sl), run_time=3)
        self.wait()

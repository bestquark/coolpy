from manim import *

class TikTokVideo(Scene):
    def construct(self):
        title = Text(
            "Learn how to do\nmath animations\nusing python",
            t2c={"python": YELLOW},
            disable_ligatures=True
        ).move_to(UP * 2)
        equation = MathTex("f(x)", " = ", "x^2 + 1").move_to(
            UP * 2
        )
        self.play(Write(title))
        self.play(ReplacementTransform(title, equation))

        framebox1 = SurroundingRectangle(
            equation[0], buff=0.1
        )
        framebox2 = SurroundingRectangle(
            equation[2], buff=0.1
        )
        self.play(
            Create(framebox1)
        )
        self.wait()

        ax = Axes(x_range=[-2,2], y_range=[-5,20],
                    x_length=6, y_legnth=8)
        labels = ax.get_axis_labels(
            x_labels="x", ylabel="f(x)"
        )
        def fun(x):
            return (2*x) ** 2 + 1
        
        graph = ax.plot(fun, color=MAROON)
        g = Group(ax, labels, graph).scale(0.5).move_to(DOWN)
        self.play(AnimationGroup(
            ReplacementTransform(framebox1, framebox2),
            FadeIn(g, shift=UP * 1.5)
        ))
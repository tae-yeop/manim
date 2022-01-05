# https://www.youtube.com/watch?v=KHGoFDB-raE
from manim import *

# class Pith(Scene):
#     def construct(self):
#         sq = Square(side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75)

#         self.play(Create(sq), run_times=3)
#         self.wait()

# class Testing(Scene):
#     def construct(self):
#         name = Text("Test").to_edge(UL, buff=0.5)
#         sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.75).shift(LEFT * 3)
#         tri = Triangle().scale(0.6).to_edge(DR)

#         self.play(Write(name))
#         self.play(DrawBorderThenFill(sq))
#         self.play(Create(tri))
#         self.wait()

#         self.play(name.animate.to_edge(UR), run_time = 2)
#         self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
#         self.wait()

# class Errors(Scene):
#     def construct(self):

#         c = Circle(radius= 2)
#         self.play(Write(c))

# from manim import *

# class Library(Scene):
#     def construct(self):
#         ax = Axes()

# https://pythonawesome.com/animations-made-using-manim-ce-the-code-turned-out-to-be-a-bit-complicated/
# from manim import *

# class Getters(Scene):
#     def construct(self):
#         rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
#         circ = Circle().to_edge(DOWN)
#         arrow = Line(start= rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip()

#         self.play(Create(VGroup(rect, circ, arrow)))
#         self.wait()
#         self.play(rect.animate.to_edge(UR)) # 여기까지만 하면 rect만 오른쪽으로 움직임

# from manim import *

# class Getters(Scene):
#     def construct(self):
#         rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)
#         circ = Circle().to_edge(DOWN)
#         arrow = always_redraw( # 이걸 해야 arrow 위치가 업데이트
#             lambda : Line(
#                 start= rect.get_bottom(), end=circ.get_top(), buff=0.2).add_tip()
#                 )

#         self.play(Create(VGroup(rect, circ, arrow)))
#         self.wait()
#         self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)  # 다 같이 움직이기

# from manim import *

# class Updaters(Scene):
#     def construct(self):

#         num = MathTex("ln(2)")
#         box = SurroundingRectangle(num, color = BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5)
#         name = Tex("Ty").next_to(box, DOWN, buff=0.25)

#         self.play(Create(VGroup(num, box, name)))
#         self.play(num.animate.shift(RIGHT*2), run_time=2) # 이렇게만 하면 이름만 오른쪽으로
#         self.wait()

# from manim import *

# class Updaters(Scene):
#     def construct(self):

#         num = MathTex("ln(2)")
#         # always_redraw를 사용하자
#         box = always_redraw(
#             lambda: SurroundingRectangle(num, color = BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5)
#         )
#         name = always_redraw(
#             lambda: Tex("Ty").next_to(box, DOWN, buff=0.25)
#         )
        
#         self.play(Create(VGroup(num, box, name)))
#         self.play(num.animate.shift(RIGHT*2), run_time=2) # 이렇게만 하면 이름만 오른쪽으로
#         self.wait()

# from manim import *

# class ValueTrackers(Scene):
#     def construct(self):
#         k = ValueTracker(5)

#         num = always_redraw(lambda:DecimalNumber().set_value(k.get_value()))

#         self.play(FadeIn(num))
#         self.wait()
#         self.play(k.animate.set_value(0), run_time=5, rate_func=linear) #smooth

# from manim import *

# class Graphing(Scene):
#     def construct(self):
#         plane = NumberPlane(
#             x_range=[-4,4,2], x_length=7,
#             y_range=[0,16,4], y_length=8).to_edge(DOWN).add_coordinates()

#         labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

#         parab = plane.get_graph(lambda x: x**2, x_range=[-4,4], color=GREEN)

#         area = plane.get_riemann_rectangles(graph=parab, x_range=[-2,3], dx=0.2, stroke_width=0.1,
#         stroke_color=WHITE)
#         func_label = (MathTex("f(x)={x}^{2}").scale(0.6).next_to(parab).set_color(GREEN))
        
#         num = MathTex("ln(2)")
#         self.play(DrawBorderThenFill(plane))
#         self.play(Create(VGroup(num, labels, parab, func_label)))
#         self.wait()
#         self.play(Create(area))
#         self.wait()

# from manim import *

# class UpdaterGraphing(Scene):
#     def construct(self):

#         k = ValueTracker(-4)
#         ax = (Axes(x_range=[-4,4,1], y_range=[-2,16,2], x_length=10, y_length=6)
#         .to_edge(DOWN)
#         .add_coordinates()).set_color(WHITE)
#         func = ax.get_graph(lambda x: x**2, x_range=[-4,4], color=BLUE)
#         # slope = ax.get_secant_slope_group(
#         #     x=3, graph=func, dx=0.01, secant_line_color=GREEN,secant_line_length=3)

#         slope = always_redraw(lambda: ax.get_secant_slope_group(
#             x=k.get_value(),
#             graph=func,
#             dx=0.01,
#             secant_line_color=GREEN,
#             secant_line_length=3
#         ))

#         pt = always_redraw(lambda: 
#         Dot().move_to(ax.c2p(k.get_value(), func.underlying_function(k.get_value()))))

#         self.add(ax, func, slope, pt)
#         self.wait()
#         self.play(k.animate.set_value(4), run_time=3)

from manim import *

HOME = "D:\\"

class SVGs(Scene):
    def construct(self):
        icon = SVGMobject(f"{HOME}\\1638578518.svg")
        im = ImageMobject(f"{HOME}\\1638578518.png").scale(0.5).to_edge(DL)
        # self.play(DrawBorderThenFill(icon))
        self.play(FadeIn(im))


class Text(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0,10,2],
            y_range=[0,10,2],
            x_length=7,
            y_length=7,
            axis_config={
                "include_numbers":True,
                "font_size":30,
                "include_top":True,
                "numbers_to_exclude":[0],
                "numbers_with_elongated_ticks":[0,2]
            }
        )

        self.add(ax)
        self.wait()
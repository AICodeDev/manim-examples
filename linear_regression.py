from manim import *
import numpy as np


class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 10], axis_config={"include_tip": False}
        )
        labels_x = ax.get_axis_labels(x_label="Weight", y_label="")
        labels_y = ax.get_axis_labels(x_label="", y_label="Height")


        eq1 = MathTex("y = ","a","\\cdot x + ","b").shift(UP*3)

        framebox1 = SurroundingRectangle(eq1[1], buff = .1)
        framebox2 = SurroundingRectangle(eq1[3], buff = .1)

        
        def linear1(x):
            return 0.3*x + 4
        def linear2(x):
            return 3*x - 4
        def linear3(x):
            return 1.1*x - 2
        def linear4(x):
            return 1.1*x + 0.2
        def linear5(x):
            return 1.005*x + 0.01

        def linear_a_high(x):
            return 3*x + 0.01
        def linear_a_low(x):
            return -3*x + 0.01
        def linear_b_high(x):
            return 1.005*x + 5
        def linear_b_low(x):
            return 1.005*x + -5

        def linear_pre_train(x):
            return 0.3*x + 0.01


        linear1 = ax.get_graph(linear1, color=BLUE)
        linear2 = ax.get_graph(linear2, color=BLUE)
        linear3 = ax.get_graph(linear3, color=BLUE)
        linear4 = ax.get_graph(linear4, color=BLUE)
        linear5 = ax.get_graph(linear5, color=BLUE)

        linear_a_high = ax.get_graph(linear_a_high, color=BLUE)
        linear_a_low = ax.get_graph(linear_a_low, color=BLUE)
        linear_b_high = ax.get_graph(linear_b_high, color=BLUE)
        linear_b_low = ax.get_graph(linear_b_low, color=BLUE)

        linear_pre_train = ax.get_graph(linear_pre_train, color=BLUE)

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(9, linear5), color=YELLOW)
        
        
        
        dot1 = Dot(point = LEFT*4, radius=0.08).shift(DOWN*2)
        dot2 = Dot(point = LEFT*3, radius=0.08).shift(DOWN*1.5)
        dot3 = Dot(point = LEFT*2, radius=0.08).shift(DOWN*1)
        dot4 = Dot(point = LEFT*1, radius=0.08).shift(DOWN*0.5)
        dot5 = Dot(point = ORIGIN, radius=0.08)
        dot6 = Dot(point = RIGHT*1, radius=0.08).shift(UP*0.5)
        dot7 = Dot(point = RIGHT*2, radius=0.08).shift(UP*1)
        dot8 = Dot(point = RIGHT*3, radius=0.08).shift(UP*1.5)
        dot_predict = Dot(point = RIGHT*4.8, radius=0.08).shift(UP*2.4)

        
        dc1 = Dot(point = LEFT*4, radius=0.08).shift(DOWN*2.7)
        dc2 = Dot(point = LEFT*3, radius=0.08).shift(DOWN*2.55)
        dc3 = Dot(point = LEFT*2, radius=0.08).shift(DOWN*2.4)
        dc4 = Dot(point = LEFT*1, radius=0.08).shift(DOWN*2.25)
        dc5 = Dot(point = ORIGIN, radius=0.08).shift(DOWN*2.1)
        dc6 = Dot(point = RIGHT*1, radius=0.08).shift(DOWN*1.95)
        dc7 = Dot(point = RIGHT*2, radius=0.08).shift(DOWN*1.8)
        dc8 = Dot(point = RIGHT*3, radius=0.08).shift(DOWN*1.65)
        cost_line1 = Line(dot1.get_center(), dc1.get_center(), color=RED)
        cost_line2 = Line(dot2.get_center(), dc2.get_center(), color=RED)
        cost_line3 = Line(dot3.get_center(), dc3.get_center(), color=RED)
        cost_line4 = Line(dot4.get_center(), dc4.get_center(), color=RED)
        cost_line5 = Line(dot5.get_center(), dc5.get_center(), color=RED)
        cost_line6 = Line(dot6.get_center(), dc6.get_center(), color=RED)
        cost_line7 = Line(dot7.get_center(), dc7.get_center(), color=RED)
        cost_line8 = Line(dot8.get_center(), dc8.get_center(), color=RED)


        
        dot_y = Tex("y").shift(RIGHT*3).shift(DOWN*2)
        dot_t = Tex("t").shift(RIGHT*3).shift(UP*2)


        b1 = Brace(cost_line8, direction=cost_line8.copy().rotate(90*DEGREES).get_unit_vector())
        b1_text = b1.get_text("Loss")


        mse_1 = MathTex("y-t").shift(UP*3)
        mse_2 = MathTex("(y-t)^2").shift(UP*3)
        mse_3 = MathTex("\\sum_{i=1}^{n} (y_i-t_i)^2").shift(UP*3)
        mse_4 = MathTex("\\frac{1}{2} \\sum_{i=1}^{n} (y_i-t_i)^2").shift(UP*3)
        mse_5 = MathTex("Error = \\frac{1}{2} \\sum_{i=1}^{n} (y_i-t_i)^2").shift(UP*3)
        

        self.play(Create(ax, run_time=2))  
        self.play(Create(labels_x, run_time=2)) 
        self.play(Create(labels_y, run_time=2))     

        self.wait(10)

        self.play(Create(dot1))
        self.play(Create(dot2))
        self.play(Create(dot3))
        self.play(Create(dot4))
        self.play(Create(dot5))
        self.play(Create(dot6))
        self.play(Create(dot7))
        self.play(Create(dot8))

        self.wait(20)
        
        self.play(Create(linear1, run_time=3))   

        self.wait(2)

        self.play(Transform(linear1, linear2), run_time=1)

        self.wait(2)

        self.play(Transform(linear1, linear3), run_time=1)

        self.wait(2)

        self.play(Transform(linear1, linear4), run_time=1)

        self.wait(2)

        self.play(Transform(linear1, linear5), run_time=1)

        self.wait(20)

        self.play(Write(eq1))

        self.wait(15)

        self.play(Write(framebox1))
        self.play(Transform(linear1, linear_a_high), run_time=1)
        self.play(Transform(linear1, linear_a_low), run_time=2)
        self.play(Transform(linear1, linear5), run_time=2)

        self.wait(10)

        self.play(Transform(framebox1, framebox2))
        self.play(Transform(linear1, linear_b_high), run_time=1)
        self.play(Transform(linear1, linear_b_low), run_time=1)
        self.play(Transform(linear1, linear5), run_time=1)
        self.wait(1)
        self.remove(framebox1)

        self.wait(10)

        self.play(Create(line_1, run_time=1))
        self.play(Create(dot_predict))

        self.wait(15)

        self.remove(dot_predict, eq1, line_1)
        self.play(Transform(linear1, linear_pre_train))

        self.wait(20)

        self.play(Create(cost_line1))
        self.play(Create(cost_line2))
        self.play(Create(cost_line3))
        self.play(Create(cost_line4))
        self.play(Create(cost_line5))
        self.play(Create(cost_line6))
        self.play(Create(cost_line7))
        self.play(Create(cost_line8))

        self.wait(20)

        self.play(Create(b1))
        self.play(Create(b1_text))

        self.wait(10)

        self.remove(b1, b1_text)
        self.play(Create(dc8))
        self.play(Write(dot_y))
        self.play(Write(dot_t))

        self.wait(20)
        
        self.play(Write(mse_1))

        self.wait(10)
        
        self.play(Transform(mse_1, mse_2))

        self.wait(10)
        
        self.play(Transform(mse_1, mse_3))

        self.wait(10)
        
        self.play(Transform(mse_1, mse_4))

        self.wait(10)
        
        self.play(Transform(mse_1, mse_5))

        self.wait(20)

        
        
        

        

        

        

        self.wait(10)

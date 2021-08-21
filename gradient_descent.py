from manim import *

class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="Weight", y_label="Loss")

        t = ValueTracker(1.5)
        t_2 = ValueTracker(8.5)

        def func(x):
            return 8 * (x - 5)**2 + 10


            
        
        graph = ax.get_graph(func, color=WHITE)

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(6.5, graph), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.input_to_graph_point(3.5, graph), color=YELLOW)

        def linear(x):
            return 25*x - 135

    

        def linear2(x):
            return -25*x + 115
        linear_graph = ax.get_graph(linear, color=BLUE)
        linear_graph2 = ax.get_graph(linear2, color=BLUE)




        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        point_2 = [ax.coords_to_point(t_2.get_value(), func(t_2.get_value()))]
        dot = Dot(point=initial_point, color=RED)
        dot2 = Dot(point=point_2)


        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()
        



        



        self.add(ax, labels, graph)
        self.play(Create(graph, run_time=3))
        self.add(dot)

        self.play(t.animate.set_value(x_space[minimum_index] + 3.5), run_time=5)
        self.play(t.animate.set_value(x_space[minimum_index] - 3.5), run_time=5)
        self.play(t.animate.set_value(x_space[minimum_index] + 3.5), run_time=5)
        self.play(t.animate.set_value(x_space[minimum_index] - 3.5), run_time=5)
        self.play(t.animate.set_value(x_space[minimum_index] + 1.5), run_time=5)


        

        self.play(Create(line_1, run_time=1))
        self.play(Create(linear_graph, run_time=2))
        self.wait(20)
        self.play(t.animate.set_value(x_space[minimum_index]), run_time=1)
        self.wait(10)



        self.play(t.animate.set_value(x_space[minimum_index] - 1.5), run_time=5)
        self.play(Create(line_2, run_time=1))
        self.play(Create(linear_graph2, run_time=2))
        self.wait(20)
        self.play(t.animate.set_value(x_space[minimum_index]), run_time=1)
        self.wait(10)







        

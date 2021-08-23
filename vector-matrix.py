from manim import *

class MatrixExamples(Scene):
    def construct(self):
        
        vec1 = Matrix([[2, 1, -1]])
        vec2 = Matrix([[2, 4, 8]])
        vec3 = Matrix([[1], [2], [3]])
        vec4 = Matrix([[2], [3], [4]])

 
        g1 = Group(vec1).arrange_in_grid(buff=2)
        g2 = Group(vec2).arrange_in_grid(buff=2)
        g3 = Group(vec3).arrange_in_grid(buff=2)
        g4 = Group(vec4).arrange_in_grid(buff=2)
        

        self.play(g1.animate().shift(UP*0.5))
        self.play(g2.animate().shift(DOWN*0.5))
        self.play(g3.animate().shift(RIGHT*3))
        self.play(g4.animate().shift(RIGHT*4.2))


        self.add(g1)
        self.add(g2)
        self.add(g3)
        self.add(g4)
        
        self.wait(7)

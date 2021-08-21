from manim import *

class MatrixExamples(Scene):
    def construct(self):
        
        mat1 = Matrix([[2, 0.5, -1], [1, 0.3, 1.4]])

        
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=",
            "f(x)\\frac{d}{dx}g(x)",
            "+",
            "g(x)\\frac{d}{dx}f(x)"
        )

        framebox1 = SurroundingRectangle(text[0], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        



        
        surr_col_1 = SurroundingRectangle(mat1.get_columns()[0])   # 행, 열 박스 초기화
        surr_col_2 = SurroundingRectangle(mat1.get_columns()[1])
        surr_col_3 = SurroundingRectangle(mat1.get_columns()[2])
        surr_row_1 = SurroundingRectangle(mat1.get_rows()[0])
        surr_row_2 = SurroundingRectangle(mat1.get_rows()[1])
        




        g = Group(mat1).arrange_in_grid(buff=2)   # 행렬 그리기
        self.add(g) 
        self.wait(7)



        self.play(Write(surr_row_1), run_time=3)   # 행 박스 그리기
        self.wait(10)
        self.play(ReplacementTransform(surr_row_1,surr_row_2), run_time=2)
        self.wait(7)




        self.remove(surr_row_1, surr_row_2)   # 행 박스 지우기




        self.wait(7)   # 열 박스 그리기
        self.play(Write(surr_col_1), run_time=3)
        self.wait(10)
        self.play(ReplacementTransform(surr_col_1,surr_col_2), run_time=2)
        self.wait(7)
        self.play(ReplacementTransform(surr_col_2,surr_col_3), run_time=2)
        self.wait(7)


        

        self.remove(surr_col_1, surr_col_2, surr_col_3)   # 열 박스 지우기




        surr_col_1 = SurroundingRectangle(mat1.get_columns()[0])   # 행, 열 박스 초기화
        surr_col_2 = SurroundingRectangle(mat1.get_columns()[1])
        surr_col_3 = SurroundingRectangle(mat1.get_columns()[2])
        surr_row_1 = SurroundingRectangle(mat1.get_rows()[0])
        surr_row_2 = SurroundingRectangle(mat1.get_rows()[1])
        self.wait(7)


        
        self.play(Write(surr_row_1), run_time=3)   # 행, 열 박스 그리기
        self.play(Write(surr_col_1), run_time=3)
        self.wait(7)
        self.play(ReplacementTransform(surr_col_1,surr_col_2), run_time=2)
        self.wait(7)
        self.play(ReplacementTransform(surr_col_2,surr_col_3), run_time=2)
        self.wait(7)
        self.play(ReplacementTransform(surr_row_1,surr_row_2), run_time=2)



        surr_col_1 = SurroundingRectangle(mat1.get_columns()[0])   # 행, 열 박스 초기화
        surr_col_2 = SurroundingRectangle(mat1.get_columns()[1])
        surr_col_3 = SurroundingRectangle(mat1.get_columns()[2])
        surr_row_1 = SurroundingRectangle(mat1.get_rows()[0])
        surr_row_2 = SurroundingRectangle(mat1.get_rows()[1])
        self.wait(7)



        self.play(ReplacementTransform(surr_col_3,surr_col_1), run_time=2)   # 행, 열 박스 그리기
        self.wait(7)
        self.play(ReplacementTransform(surr_col_1,surr_col_2), run_time=2)
        self.wait(7)
        self.play(ReplacementTransform(surr_col_2,surr_col_3), run_time=2)
        self.wait(7)
        
        

        '''
        self.play(Write(text))
        self.play(Write(framebox1), run_time=3)
        self.wait(1)
        self.play(ReplacementTransform(framebox1,framebox2), run_time=3)
        '''

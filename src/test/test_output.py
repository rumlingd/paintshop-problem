import unittest
from src.format_input import *
from src.paintshop_solver import *


class OutputTestCase(unittest.TestCase):

    def test_file_1(self):
        path = 'text-files/example1.txt'
        input_obj = FormatInput(str(path))
        solver_obj = PaintShopSolver(input_obj.custs, input_obj.num_of_colours)
        solution = solver_obj.get_best_solution(solver_obj.get_viable_solutions())
        self.assertTrue(solution == ['G', 'G', 'G', 'G', 'M'])

    def test_file_2(self):
        path = 'text-files/example2.txt'
        input_obj = FormatInput(str(path))
        solver_obj = PaintShopSolver(input_obj.custs, input_obj.num_of_colours)
        solution = solver_obj.get_best_solution(solver_obj.get_viable_solutions())
        self.assertTrue(solution == 'No solution exists')

    def test_file_3(self):
        path = 'text-files/example3.txt'
        input_obj = FormatInput(str(path))
        solver_obj = PaintShopSolver(input_obj.custs, input_obj.num_of_colours)
        solution = solver_obj.get_best_solution(solver_obj.get_viable_solutions())
        self.assertTrue(solution == ['G', 'M', 'G', 'M', 'G'])

    def test_file_4(self):
        path = 'text-files/example4.txt'
        input_obj = FormatInput(str(path))
        solver_obj = PaintShopSolver(input_obj.custs, input_obj.num_of_colours)
        solution = solver_obj.get_best_solution(solver_obj.get_viable_solutions())
        self.assertTrue(solution == ['M', 'M'])

    if __name__ == '__main__':
        unittest.main()

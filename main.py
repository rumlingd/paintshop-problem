from src.format_input import *
from src.paintshop_solver import *
import sys


def display_solution():
    """Method which returns a solution by taking in a command
       line argument and passing it back out

        Returns:
            self.solution: list containing solution

        Example:
            ['M','G','M']

        """
    path1 = sys.argv[1]
    input_obj = FormatInput(str(path1))
    solver_obj = PaintShopSolver(input_obj.custs, input_obj.num_of_colours)
    solution = solver_obj.get_best_solution(solver_obj.get_viable_solutions())
    if type(solution) is list:
        print(" ".join(map(str, solution)))

    else:
        print(solution)


if __name__ == "__main__":
    display_solution()

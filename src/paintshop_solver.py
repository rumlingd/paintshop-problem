#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:53:11 2018

@author: d
"""
from itertools import product
from itertools import groupby


class PaintShopSolver(object):
    """Class which takes a correctly format and solves the paintshop problem

    """

    def __init__(self, customers, number_of_colours):
        """Method which initialises a Solver Object

        Args:
            customers(list): List with customer prefs
            number_of_colours(int):Number of colours in text file

        """
        self.custs = customers
        self.num_of_colours = number_of_colours

        self.picky_custs = self.find_picky_customers()
        self.picky_custs = flatten(self.picky_custs)
        self.candidates = self.get_candidates()

    def find_picky_customers(self):
        """Method which finds picky customers who must satisfied
           i.e picky customers only choose one colour

        Returns:
            unique_picky_custs(list): lists of list e.g [[5:'M']]

        """
        picky = []
        for idx, cust in enumerate(self.custs):
            if len(cust) is 1:
                picky.append(cust)

        unique_picky_custs = get_unique_elements(picky)
        return unique_picky_custs

    def get_candidates(self):
        """Method which uses itertools product to calculate possible candidate
           solutions based on customer preferences contained in input file.

        Returns:
            candidates(list): list of lists e.g [[[5:'M'],[2:'G']],
                                                [[1:'M'],[3:'G']]]

        """
        candidates = []
        for prod in product(*self.custs):
            prod = list(prod)
            for picky_cust in self.picky_custs:
                prod.append(picky_cust)
                candidates.append(prod)

        return candidates

    def get_viable_solutions(self):
        """Method calculates possible solutions by filling in zeroes for unobserved
           colours in candidate solutions

        Returns:
            possible_sols(list): list of lists e.g [[0,'G',0,0,'M'],
                                                    ['M','G',0,'G',0]

        """
        possible_sols = []
        for candidate in self.candidates:
            solution_list = [0] * self.num_of_colours
            possible_sols.append(solution_list)
            for can in candidate:
                index = can[0] - 1

                solution_list[index] = can[1]

        return self.fill_in_zeros_with_g(possible_sols)

    def fill_in_zeros_with_g(self, possible_sols):
        """Method which replaces possible solutions entries
           of 0 by replacing with 'G' for gloss colour

        Returns:
            filled_in_sols(list): list of lists e.g [['G,'G','G,'G,'M'],
                                                     ['M','G','G,'G','G']

        """
        for sol in possible_sols:
            for idx, entry in enumerate(sol):
                if entry is 0:
                    sol[idx] = 'G'

        return possible_sols

    def check_solution(self, solution):
        """Method which checks if a solution satisfies all customers preferences

        Args:
            solution(list): solution to verify['G,'G','G,'G,'M']

        Returns:
            solution(list): list e.g['G,'G','G,'G,'M'] i.e sol that was passed
                            string: 'No solution exists'

        """
        satisfied_custs = []
        for idx, cust in enumerate(self.custs):
            for index, sol in enumerate(solution):
                current_check = [index + 1, sol]
                if current_check in cust:
                    satisfied_custs.append(1)
                    break

                else:
                    pass

        if sum(satisfied_custs) is len(self.custs):
            return solution

        else:
            return 'No solution exists'
            pass

    def get_best_solution(self, solutions):
        """Method which returns the best solution,if not all solutions
           are "No solution exists", the highest index(best) is returned

        Args:
            solutions(list): solutions to verify[['G,'G'],['G','M']

        Returns:
            final_sol(list): list e.g['G,'G'] i.e sol that was passed

        """
        no_sol_string = 'No solution exists'
        valid_sols = []
        for sol in solutions:
            valid_sol = self.check_solution(sol)
            valid_sols.append(valid_sol)

        if valid_sols.count(no_sol_string) != len(solutions):
            valid_sols[:] = [x for x in valid_sols if x != no_sol_string]
            final_sol = valid_sols[0]
        else:
            final_sol = valid_sols[0]

        return final_sol


def flatten(lst):
    """Method which flattens a list of lists

    Args:
    lst(list of lists): list of lists to flatten

    Returns:
        (list): list.g [[5:'M'], [2:'G']]

    """
    return [item for sublist in lst for item in sublist]


def get_unique_elements(lst):
    """Method which returns the unique elements in a list

    Returns:
           unique_list: e.g [[5,'M'], [2,'G']]

    Example:
    [[5,'M'], [2,'G'], [[5,'M'], [2,'G']]] becomes [[5,'M'], [2,'G']]

    """
    lst.sort()
    unique_lst = list(lst for lst, _ in groupby(lst))
    return unique_lst

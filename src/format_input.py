#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Feb  15 16:19:09 2017

@author: d
"""


class FormatInput(object):
    """Class which takes input from a text file and parses into customers

    """

    def __init__(self, file_path):
        """Method which initialises an Input File and formats it

        Args:
            file_path(string): path to the file you wish to import

        """
        self.input_file = open(file_path, "r")
        self.lines = self.input_file.read().strip().split("\n")
        self.num_of_colours = int(self.lines[0])
        self.custs = self.get_customers_pref()
        self.custs = self.sort_customers()

    def get_customers_pref(self):
        """Method which returns each customers preferences in the correct format

        Returns:
            formatted_prefs(lists): lists of lists e.g [[2,'M'] [2,'G']


        """
        formatted_prefs = []
        for i in range(1, len(self.lines)):
            current_cust = self.lines[i].split()
            customer_prefs = []
            formatted_prefs.append(customer_prefs)
            for j in range(1, len(current_cust), 2):
                customer_pref = current_cust[j]
                colour = int(current_cust[j-1])
                customer_prefs.append([colour, customer_pref])

        return formatted_prefs

    def sort_customers(self):
        """Method which sorts customer prefs alphabetically then numerically

        Returns:
            sorted_custs(list): lists of lists e.g [[2,'G'] [1:'M']]


        """
        sorted_custs = []
        for cust in self.custs:
            cust.sort(key=lambda x: x[1])
            sorted_custs.append(cust)

        return sorted_custs

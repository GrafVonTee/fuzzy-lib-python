"""Accumulation Module

Some accumulation classes and functions here
"""
from typing import Dict, List, Union
from fuzzy_lib.term import *


class Accumulation:
    @staticmethod
    def compute(term_list: List[Term]) -> Term:
        return None


class MaxAccumulation(Accumulation):
    @staticmethod
    def compute(term_list: List[Term]) -> Term:
        if len(term_list) == 0:
            return None

        max_term = term_list[0].copy()
        max_term.name = "Accumulated"

        for i in range(max_term.lower_bound, max_term.upper_bound + 1):
            for term in term_list:
                if max_term.membership(i) < term.membership(i):
                    max_term.set_value_in_range(i, term.membership(x))

        return max_term

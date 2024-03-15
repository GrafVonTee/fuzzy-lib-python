"""Defuzzification Module

Some defuzzification classes and functions here
"""
from typing import Dict, List, Union
from fuzzy_lib.term import *


class Defuzzification:
    @staticmethod
    def defuzzify(term: Term) -> int:
        return term.lower_bound


class LargeMaxDefuzzification(Defuzzification):
    @staticmethod
    def defuzzify(term: Term) -> int:
        max_x: int = term.lower_bound
        max_value: float = term.membership(max_x)

        for i in range(term.lower_bound, term.upper_bound + 1):
            if max_value <= term.membership(i):
                max_value = term.membership(i)
                max_x = i

        return max_x


class CentroidDefuzzification(Defuzzification):
    @staticmethod
    def defuzzify(term: Term) -> int:
        output_value: float = 0
        overall_value: float = 0

        for i in range(term.lower_bound, term.upper_bound + 1):
            output_value += term.membership(i) * i
            overall_value += term.membership(i)

        output_value /= overall_value

        return int(output_value)

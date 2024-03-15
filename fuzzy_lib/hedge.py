"""Hedge Module

Some hedge classes and functions here
"""
from typing import Dict, List, Union
from fuzzy_lib.term import *


class Hedge:
    @staticmethod
    def compute(term: Term) -> Term:
        return term.copy()


class HedgeNot(Hedge):
    @staticmethod
    def compute(term: Term) -> Term:

        def not_func(x):
            return 1 - x

        new_term = super().compute(term)
        new_term.name = "Not" + new_term.name
        new_value_range = not_func(new_term.get_value_range())
        new_term.set_value_range(new_value_range)
        return new_term


class HedgeApprox(Hedge):
    @staticmethod
    def compute(term: Term) -> Term:

        def approx_func(x):
            return x**(1/2)

        new_term = super().compute(term)
        new_term.name = "Approx" + new_term.name
        new_value_range = approx_func(new_term.get_value_range())
        new_term.set_value_range(new_value_range)
        return new_term


class HedgeVery(Hedge):
    @staticmethod
    def compute(term: Term) -> Term:

        def very_func(x):
            return x**2

        new_term = super().compute(term)
        new_term.name = "Very" + new_term.name
        new_value_range = very_func(new_term.get_value_range())
        new_term.set_value_range(new_value_range)
        return new_term

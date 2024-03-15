"""Variable Module

Some variable classes and functions here
"""
from typing import Dict, List, Union
from fuzzy_lib.term import *
import operator
import random


class VariableReceiver:
    @staticmethod
    def receive(values: Dict[str, float]) -> str:
        return ""


class MaxReceiver(VariableReceiver):
    @staticmethod
    def receive(values: Dict[str, float]) -> str:
        return max(values.iteritems(), key=operator.itemgetter(1))[0]


class AuctionReceiver(VariableReceiver):
    @staticmethod
    def receive(values: Dict[str, float]) -> str:
        auction_float: List[float] = []
        auction_names: List[str] = []
        max_value: float = 0

        for elem in values:
            auction_float.append(max_value)
            auction_names.append(elem[0])
            max_value += elem[1]

        rand_value: float = random.uniform(0, max_value)

        for name_value, float_value in zip(auction_names, auction_float)[::-1]:
            if float_value < rand_value:
                return name_value

        return ""


class Variable:
    def __init__(self, name: str, lower_bound: int, upper_bound: int, receiver: VariableReceiver):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self._receiver = receiver

        self._terms: Dict[str, Term] = {}

    def add_term(self, term_name: str, new_term: Term):
        self._terms[term_name] = new_term

    def clear_terms(self):
        self._terms.clear()

    def get_terms(self) -> List[Term]:
        return list(self._terms.values())

    def membership(self, x: int) -> Dict[str, float]:
        return {elem: self._terms[elem].membership(x) for elem in self._terms.keys()}

    def get_term_name_in_value(self, x: int) -> str:
        return self._receiver.receive(self.membership(x))

    def get_term_by_name(self, term_name: str) -> Term:
        return self._terms[term_name]

    def get_x_from_degree(self, degree: float):
        x_dict: Dict[str, int] = {}
        for elem in self._terms.keys():
            elem_val = self._terms[elem]
            most_similar_value: int = elem_val.lower_bound
            smallest_error: float = (degree - elem_val.membership(most_similar_value))**2

            for val in range(elem_val.lower_bound, elem_val.upper_bound + 1):
                new_error: float = (degree - elem_val.membership(val))**2
                if new_error < smallest_error:
                    smallest_error = new_error
                    most_similar_value = val

            x_dict[elem] = most_similar_value
        return x_dict

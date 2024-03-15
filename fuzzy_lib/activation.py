"""Activation Module

Some activation classes and functions here
"""
from typing import Dict, List, Union
from fuzzy_lib.term import *


class Activation:
    @staticmethod
    def activate(activation_coeff: float, original_term: Term) -> Term:
        return original_term.copy()


class ProdActivation(Activation):
    @staticmethod
    def activate(activation_coeff: float, original_term: Term) -> Term:
        new_term = super().activate(activation_coeff, original_term)
        new_term.name = "Activated"

        for i in range(len(new_term)):
            new_term.set_value_in_range(i, activation_coeff * new_term.get_value_range()[i])

        return new_term

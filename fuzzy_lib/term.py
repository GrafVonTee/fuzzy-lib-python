"""Term Module

Some Terms classes and functions here
"""
import numpy as np


class Term:
    """Just a basic term class"""
    def __init__(self, name: str, lower_bound: int, upper_bound: int):
        self.name = name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.value_range = np.zeros(upper_bound - lower_bound + 1)

    def MakeRange(self):
        pass


class Gaussian(Term):
    pass

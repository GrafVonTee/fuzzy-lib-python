"""Term Module

Some Terms classes and functions here
"""
import numpy as np
import math


class Term:
    """Just a basic term class"""
    def __init__(self, name: str, lower_bound: int, upper_bound: int):
        self.name: str = name
        self.lower_bound: int = lower_bound
        self.upper_bound: int = upper_bound
        self.value_range = np.zeros(0)

    """Initialize value_range with defaults"""
    def make_range(self):
        self.value_range = np.zeros(self.upper_bound - self.lower_bound + 1)

    """
    """
    def get_value_range(self):
        return self.value_range

    """
    """
    def get_degree_of_membership(self, x: int) -> float:
        if x < self.lower_bound or x > self.upper_bound:
            return 0.0

        return self.value_range[x - self.lower_bound]


class Gaussian(Term):
    """Gaussian Term class"""
    def __init__(self,
                 name: str,
                 lower_bound: int,
                 upper_bound: int,
                 mean: int,
                 variance: float):
        super().__init__(name, lower_bound, upper_bound)
        self.mean = mean
        self.variance = variance

    def make_range(self):
        super().make_range()

        max_value: float = 0
        temp_mean = self.mean - self.lower_bound

        for i, x in np.ndenumerate(self.value_range):
            self.value_range[i] = math.exp(
                -1 * math.pow(i[0] - temp_mean, 2)
                / (2 * math.pow(self.variance, 2))
            )

            if max_value < self.value_range[i]:
                max_value = self.value_range[i]

        self.value_range /= max_value

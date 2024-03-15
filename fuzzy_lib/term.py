"""Term Module

Some Terms classes and functions here
"""
from typing import Dict, List, Union
import numpy as np
import math
import copy


class Term:
    """Just a basic term class"""
    def __init__(self, name: str, lower_bound: int, upper_bound: int):
        self.name: str = name
        self.lower_bound: int = lower_bound
        self.upper_bound: int = upper_bound
        self._value_range = np.zeros(0)
        self.__make_range()

    """Initialize value_range with defaults"""
    def _make_range(self):
        self._value_range = np.zeros(self.upper_bound - self.lower_bound + 1)

    """Copy of the _make_range() function"""
    __make_range = _make_range

    """
    """
    def __len__(self):
        return len(self._value_range)

    """
    """
    def get_value_range(self):
        return self._value_range

    """
    """
    def set_value_range(self, new_value_range: List[float]):
        self._value_range = new_value_range

    """
    """
    def set_value_in_range(self, pos: int, value: float):
        self._value_range[pos] = value

    """
    """
    def membership(self, x: int) -> float:
        if x < self.lower_bound or x > self.upper_bound:
            return 0.0

        return self._value_range[x - self.lower_bound]

    """
    """
    def copy(self):
        return copy.deepcopy(self)


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
        self._make_range()

    def _make_range(self):
        max_value: float = 0
        temp_mean = self.mean - self.lower_bound

        for i, x in np.ndenumerate(self._value_range):
            self._value_range[i] = math.exp(
                -1 * math.pow(i[0] - temp_mean, 2)
                / (2 * math.pow(self.variance, 2))
            )

            if max_value < self._value_range[i]:
                max_value = self._value_range[i]

        self._value_range /= max_value


class Linear(Term):
    """Linear term class"""
    def __init__(self,
                 name: str,
                 lower_bound: int,
                 upper_bound: int,
                 begin: int,
                 end: float):
        super().__init__(name, lower_bound, upper_bound)
        self.begin = begin
        self.end = end
        self._make_range()

    def _make_range(self):
        temp_begin = self.begin - self.lower_bound
        temp_end = self.end - self.lower_bound

        for i, x in np.ndenumerate(self._value_range):
            if i[0] < temp_begin or i[0] > temp_end:
                self._value_range[i] = 0
            else:
                self._value_range[i] = (i[0] - temp_begin) / (temp_end - temp_begin)


class Triangular(Term):
    """Triangular term class"""
    def __init__(self,
                 name: str,
                 lower_bound: int,
                 upper_bound: int,
                 point_begin: int,
                 point_peek: int,
                 point_end: int):
        super().__init__(name, lower_bound, upper_bound)
        self.point_begin = point_begin
        self.point_peek = point_peek
        self.point_end = point_end
        self._make_range()

    def _make_range(self):
        temp_a = self.point_begin - self.lower_bound
        temp_b = self.point_peek - self.lower_bound
        temp_c = self.point_end - self.lower_bound

        for i, x in np.ndenumerate(self._value_range):
            if i[0] < temp_a or i[0] > temp_c:
                self._value_range[i] = 0
            elif i[0] < temp_b:
                self._value_range[i] = (i[0] - temp_a) / (temp_b - temp_a)
            elif i[0] == temp_b:
                self._value_range[i] = 1
            else:
                self._value_range[i] = (temp_c - i[0]) / (temp_c - temp_b)


class Trapezoid(Term):
    """Trapezoid term class"""
    def __init__(self,
                 name: str,
                 lower_bound: int,
                 upper_bound: int,
                 point_a: int,
                 point_b: int,
                 point_c: int,
                 point_d: int):
        super().__init__(name, lower_bound, upper_bound)
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d
        self._make_range()

    def _make_range(self):
        temp_a = self.point_a - self.lower_bound
        temp_b = self.point_b - self.lower_bound
        temp_c = self.point_c - self.lower_bound
        temp_d = self.point_d - self.lower_bound

        for i, x in np.ndenumerate(self._value_range):
            if i[0] < temp_a or i[0] > temp_d:
                self._value_range[i] = 0
            elif i[0] < temp_b:
                self._value_range[i] = (i[0] - temp_a) / (temp_b - temp_a)
            elif i[0] <= temp_c:
                self._value_range[i] = 1
            else:
                self._value_range[i] = (temp_d - i[0]) / (temp_d - temp_c)


class SquareRoot(Term):
    """Gaussian Term class"""
    def __init__(self,
                 name: str,
                 lower_bound: int,
                 upper_bound: int,
                 begin: int,
                 end: int):
        super().__init__(name, lower_bound, upper_bound)
        self.begin = begin
        self.end = end
        self._make_range()

    def _make_range(self):
        temp_begin = self.begin - self.lower_bound
        temp_end = self.end - self.lower_bound

        for i, x in np.ndenumerate(self._value_range):
            if i[0] < temp_begin or i[0] > temp_end:
                self._value_range[i] = 0
            else:
                self._value_range[i] = ((i[0] - temp_begin) / (temp_end - temp_begin))**(1/2)

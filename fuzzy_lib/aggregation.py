"""Aggregation Module

Some aggregation classes and functions here
"""
from typing import Dict, List, Union


class Aggregation:
    @staticmethod
    def compute(values_list: List[float]) -> float:
        return 0


class MinAggregation(Aggregation):
    @staticmethod
    def compute(values_list: List[float]) -> float:
        return min(*values_list)

from fuzzy_lib.term import *
from fuzzy_lib.hedge import *
from fuzzy_lib.variable import *
from fuzzy_lib.activation import *
from fuzzy_lib.aggregation import *
from fuzzy_lib.accumulation import *
from fuzzy_lib.defuzzification import *

import numpy as np
import matplotlib.pyplot as plt


def get_thurst_variable() -> Variable:
    thurst = Variable("thurst", 0, 300, MaxReceiver())

    thurst_low = Gaussian("low", 0, 300, 0, 65)
    thurst.add_term(thurst_low.name, thurst_low)

    thurst_mid = Gaussian("mid", 0, 300, 150, 65)
    thurst.add_term(thurst_mid.name, thurst_mid)

    thurst_high = Gaussian("high", 0, 300, 300, 65)
    thurst.add_term(thurst_high.name, thurst_high)

    return thurst


def print_term(term: Term):
    plt.figure(figsize=(6, 4))
    plt.title(f"{term.name}")

    x_array = np.arange(term.upper_bound - term.lower_bound + 1)
    plt.plot(x_array, term.get_value_range(), label=term.name)

    plt.legend()
    plt.show()


def print_variable(var: Variable):
    plt.figure(figsize=(6, 4))
    plt.title(f"{var.name} terms")

    x_array = np.arange(var.upper_bound - var.lower_bound + 1)
    for term in var.get_terms():
        plt.plot(x_array, term.get_value_range(), label=term.name)

    plt.legend()
    plt.show()


def print_membership(x: int, var: Variable):
    membership = var.membership(x)

    plt.figure(figsize=(6, 4))
    plt.title(f"Membership of {var.name} in value {x}")

    x_array = np.arange(var.upper_bound - var.lower_bound + 1)

    plt.axvline(x=x)
    for i, term in enumerate(var.get_terms()):
        plt.plot(x_array, term.get_value_range(), label=term.name)
        plt.plot(x, membership[term.name], 'ro')

    plt.legend()
    plt.show()


def print_activation(activated_term: Term, original_term: Term):
    plt.figure(figsize=(6, 4))
    plt.title(f"{original_term.name}")

    x_array = np.arange(original_term.upper_bound - original_term.lower_bound + 1)
    plt.plot(x_array, original_term.get_value_range(), label=original_term.name)
    plt.plot(x_array, activated_term.get_value_range(), label=activated_term.name)

    plt.legend()
    plt.show()


def get_values_from_rule(rule: Dict[Term, int]):
    values: List[float] = []
    for elem in rule:
        values.append(elem[0].membership(elem[1]))
    return values


print_membership(35, get_thurst_variable())

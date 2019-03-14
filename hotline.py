##
## EPITECH PROJECT, 2019
## 203hotline_2018
## File description:
## hotline
##

from binomial import binomial_coefficient, binomial_law
from poisson import poisson_law

def hotline_two(data: [int]):
    """Hotline function with 2 args."""
    print('{:g}-combination of a {:g} set:' .format(data[1], data[0]))
    print('{:d}' .format(binomial_coefficient(data[0], data[1])))

def hotline_one(data: int):
    """Hotline function with 1 arg."""
    binomial_law(data)
    print('')
    poisson_law(data)

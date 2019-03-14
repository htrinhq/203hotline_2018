##
## EPITECH PROJECT, 2019
## 203hotline_2018
## File description:
## poisson
##

from time import time
from math import factorial, exp
from binomial import sep_selector

def poisson_law(data: int):
    """Get the Poisson law expectations from 0 to 50."""
    print('Poisson distribution:')
    overload = 0
    x = 1
    start = time()
    over_time = 3500 * (data / (3600 * 8))
    for i in range(0, 51):
        result = exp(-over_time) * pow(over_time, i) / factorial(i)
        if i > 25:
            overload += result
        print('{:d} -> {:.03f}' .format(i, result), end='')
        x = sep_selector(x, i)
    end = time()
    print('overload: {:.01f}%' .format(overload * 100),
          'computation time: {:.02f} ms' .format((end - start) * 1000),
          sep='\n')

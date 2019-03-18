##
## EPITECH PROJECT, 2019
## 203hotline_2018
## File description:
## binomial
##

from math import factorial
from time import time
from sys import stderr

def error(str: str):
    """Error message, on error output, then exits."""
    stderr.write(str)
    exit(84)

def binomial_coefficient(n: int, k: int):
    """Get the binomial coefficient of 2 values."""
    a = factorial(n)
    b = factorial(k)
    c = factorial(n - k)
    return a // (b * c)

def sep_selector(x: int, i: int) -> int:
    """Select separator between tab en end line."""
    if x == 6 or i == 50:
            print('')
            return 1
    else:
        print('', end='\t')
        return x + 1

def binomial_law(data: int):
    """Get the binomial law from 0 to 50."""
    print('Binomial distribution:')
    start = time()
    n = 3500
    x = 1
    overload = 0
    for i in range(0, 51):
        over_time = data / (3600 * 8)
        result = (binomial_coefficient(n, i) *
            (over_time ** i) * ((1 - over_time) ** (n - i)))
        if i > 25:
            overload += result
        print('{:d} -> {:.03f}' .format(i, result), end='')
        x = sep_selector(x, i)
    end = time()
    print('overload: {:.01f}%' .format((overload * 100) if data < 303 else 100),
          'computation time: {:.02f} ms' .format((end - start) * 1000),
          sep='\n')

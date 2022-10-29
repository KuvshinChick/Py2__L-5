#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    a = (-x**2)/16
    S = 0
    k = 1

    # Найти сумму членов ряда.
    while math.fabs(a) > EPS:
        a *= ((-x**2) / 4)/(k + 1)**2
        S += a
        k += 1

    # Вывести значение функции.
    print("Sum: ", S)

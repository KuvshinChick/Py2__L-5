#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Input variables
    n = int(input("Введите разряд чисел n: "))
    k = int(input("Введите делитель k: "))
    i = (10 ** n) - 1
    s = 0
    f = 10 ** (n-1)

    # Divisibility check cycle
    while i >= f:
        if i % k == 0:
            s += i
        i -= 1
    print("Сумма всех чисел кратных k:")
    print(s)

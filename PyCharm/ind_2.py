#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import math module
import math

if __name__ == "__main__":
    # coefficients input
    print("Enter the coefficients for the equation")
    print("ax^2 + bx + c = 0:")
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    # calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    print("Discriminant = %.2f" % discriminant)

    # solution of the equation
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discriminant == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print('x1 = ', round(- b /(2 * a), 2), ' + ', round(math.sqrt(abs(discriminant))/(2 * a), 2), 'i')
        print('x2 = ', round(- b /(2 * a), 2), ' - ', round(math.sqrt(abs(discriminant))/(2 * a), 2), 'i')
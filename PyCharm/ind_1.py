#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # List of months & 31_days_lict
    days31_list = [1, 3, 5, 7, 8, 10, 12]
    month_list = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    # Input number of month
    month_num = int(input("Enter month number: "))

    # Output from the array check
    if month_num < 1 or month_num > 12:
        print("Please, enter the right number.")
    else:
        # Month output
        if month_num in days31_list:
            print(f'{month_list[month_num-1]}: 31 days')
        elif month_num == 2:
            print(f'{month_list[month_num - 1]}: 28/29 days')
        else:
            print(f'{month_list[month_num - 1]}: 30 days')

"""
Ask for two numbers and print:
a > b
a == b
a != b
(all boolean results)
"""

import sys


def main():
    try:
        number_a = int(input("Enter a number a:"))
        number_b = int(input("Enter a number b:"))
    except ValueError:
        print("Wrong input.Enter a valid number")
        return 1

    print("a > b", number_a > number_b)
    print("a == b", number_a == number_b)
    print("a != b", number_a != number_b)

    return 0


if __name__ == '__main__':
    sys.exit(main())

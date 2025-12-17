""""
Ask the user for a number.

Convert to int.

Then reassign the variable to None.

Print both states and explain (in comments) why a variable can change type.

"""

import sys
from enum import nonmember


def main():
    try:
        number = (input("Enter a number: "))
        print(number, type(number))

        number2 = int(number)
        print(number, type(number2))

        number = None
        print(number, type(number))
    except ValueError:
        print("Invalid input")

    return 0


if __name__ == '__main__':
    sys.exit(main())

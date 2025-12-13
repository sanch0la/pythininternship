"""
Create a variable x = None. Print it.
Ask the user to then assign a value to x via input. Print the new value.
"""

import sys


def main():
    x = None
    print(x)

    x = int(input("Enter a number: "))
    print(f"x is equal to {x}.")

    return 0


if __name__ == '__main__':
    sys.exit(main())

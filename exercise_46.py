""""
Ask the user for a number.

Create a boolean variable is_even.

If is_even is True, print "Even number", else print "Odd number".
"""
import sys


def main():
    try:

        number = int(input("Enter a number: "))
        is_even = number % 2 == 0
        if is_even:
            print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Not an integer")
    return 0


if __name__ == '__main__':
    sys.exit(main())

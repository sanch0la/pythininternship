""""
Ask the user for an integer.

If the number is greater than 10, print "Large number".
"""
import sys


def main():
    try:
        number = int(input("Enter an integer: "))
        if number > 10:
            print("Large number")
    except ValueError:
        print("Not an integer")
    return 0


if __name__ == '__main__':
    sys.exit(main())

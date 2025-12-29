""""
Ask the user for a number.
Print:
"Negative" if the number is less than 0
"Zero" if the number is 0
"Positive" otherwise
"""
import sys


def main():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Negative")
        elif number > 0:
            print("Positive")
        else:
            print("Zero")
    except ValueError:
        print("Not an integer")
    return 0


if __name__ == '__main__':
    sys.exit(main())

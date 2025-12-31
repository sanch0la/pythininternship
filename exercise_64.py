""""
Given a list of integers, print only the positive numbers.
This will require the use of the 'continue' keyword.
"""
import sys


def main():
    numbers = [1, 3, 5, 6, -3, 5, -6, 77]
    for number in numbers:
        if number > 0:
            print(number)

        else:
            continue

    return 0


if __name__ == '__main__':
    sys.exit(main())

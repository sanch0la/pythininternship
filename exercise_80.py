"""
Define a function double_number(n) that:
assigns n * 2 to a local variable
prints the result
Call it with a number from input.
"""
import sys


def main():
    def double_number():
        n = int(input("Enter a number: "))
        x = n * 2
        print(f"The double of {n} is {x}")

    double_number()
    return 0


if __name__ == '__main__':
    sys.exit(main())

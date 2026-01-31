""""
Use the return value of one function as the argument to another
"""
import sys


def main():
    def add(a, b):
        c = a + b
        print(f"The sum of a and b is {c}")
        return c

    def square_number(c):
        result = c * c
        print(f"The square of c is {result}")
        return c

    sum_result = add(1, 2)
    square_number(sum_result)

    return 0


if __name__ == '__main__':
    sys.exit(main())
